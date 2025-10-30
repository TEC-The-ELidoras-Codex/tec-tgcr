"""LLM-backed reasoning helper."""

from __future__ import annotations

import json
import os
from typing import Optional

import httpx


class LLMResponder:
    """Lightweight wrapper around hosted LLM providers."""

    name = "llm_responder"
    description = "Summon an LLM insight block when deeper synthesis is requested."

    def __init__(
        self,
        provider: str,
        model: str,
        max_tokens: int,
        temperature: float,
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        http_client: Optional[httpx.Client] = None,
        use_env_api_key: bool = False,
    ) -> None:
        self.provider = provider
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        # Prefer explicit configuration; optionally fall back to environment if enabled.
        self.api_key = api_key or (
            os.getenv("OPENAI_API_KEY") if use_env_api_key else None
        )
        self.endpoint = endpoint or self._default_endpoint(provider)
        self._client = http_client

    @property
    def available(self) -> bool:
        return bool(self.api_key and self.endpoint)

    def run(self, prompt: str, system: Optional[str] = None) -> str:
        if not self.available:
            return "LLM offline — set OPENAI_API_KEY or configure tool_settings.llm to enable synthesis."

        client = self._ensure_client()
        payload = self._build_payload(prompt, system)
        headers = self._headers()

        try:
            # At this point, availability has been checked; endpoint must be non-None.
            assert self.endpoint is not None
            response = client.post(
                self.endpoint, json=payload, headers=headers, timeout=30.0
            )
            response.raise_for_status()
            return self._parse_response(response)
        except Exception as exc:  # pragma: no cover - network errors handled uniformly
            return f"LLM request failed: {exc}"

    # === Provider plumbing ===
    def _ensure_client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(timeout=30.0)
        return self._client

    def _default_endpoint(self, provider: str) -> Optional[str]:
        if provider.lower() == "openai":
            return "https://api.openai.com/v1/chat/completions"
        if provider.lower() == "azure-openai":
            base = os.getenv("AZURE_OPENAI_ENDPOINT")
            deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
            if base and deployment:
                return f"{base}/openai/deployments/{deployment}/chat/completions?api-version=2024-02-15-preview"
        return None

    def _headers(self) -> dict[str, str]:
        if self.provider.lower() == "azure-openai":
            key = self.api_key or os.getenv("AZURE_OPENAI_KEY", "")
            return {
                "api-key": key,
                "Content-Type": "application/json",
            }
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _build_payload(self, prompt: str, system: Optional[str]) -> dict:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "messages": messages,
        }

    def _parse_response(self, response: httpx.Response) -> str:
        data = response.json()
        choices = data.get("choices", [])
        if not choices:
            return json.dumps(data, indent=2)
        message = choices[0].get("message") or {}
        content = message.get("content")
        if content:
            return content.strip()
        return json.dumps(data, indent=2)
