"""
Web Research Tool for TEC Agents

Provides pluggable web research using providers like Bing Web Search
or Azure Cognitive Search. Controlled via tool_settings.research.
"""
from __future__ import annotations

import os
from typing import Optional, Dict, Any, List

import httpx


class ResearchTool:
    name = "web_research"
    description = "Perform web research and return cited findings from reputable sources."

    def __init__(
        self,
        provider: str = "bing",
        endpoint: Optional[str] = None,
        api_key: Optional[str] = None,
        max_results: int = 5,
        market: str = "en-US",
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        self.provider = (provider or "bing").lower()
        self.endpoint = endpoint or self._default_endpoint(self.provider)
        self.api_key = api_key or os.getenv("BING_SEARCH_KEY")
        self.max_results = max_results
        self.market = market
        self._client = http_client

    @property
    def available(self) -> bool:
        return bool(self.endpoint and self.api_key)

    def run(self, query: str) -> str:
        if not self.available:
            return (
                "Research offline — configure tool_settings.research (endpoint, api_key) "
                "or set BING_SEARCH_KEY to enable web research."
            )

        if self.provider == "bing":
            return self._run_bing(query)
        # Future: add more providers here (azure-search, serpapi, etc.)
        return "Provider not supported yet."

    # === Provider implementations ===
    def _run_bing(self, query: str) -> str:
        client = self._ensure_client()
        params = {"q": query, "mkt": self.market, "count": self.max_results, "responseFilter": "Webpages"}
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        try:
            endpoint = str(self.endpoint)
            key = str(self.api_key)
            resp = client.get(endpoint, params=params, headers={"Ocp-Apim-Subscription-Key": key}, timeout=20.0)
            resp.raise_for_status()
            data = resp.json()
            return self._format_bing_results(data)
        except Exception as exc:  # pragma: no cover - network errors handled uniformly
            return f"Research request failed: {exc}"

    def _format_bing_results(self, data: Dict[str, Any]) -> str:
        web = data.get("webPages", {})
        results = web.get("value", [])[: self.max_results]
        if not results:
            return "No web results found."
        lines: List[str] = ["Top findings:"]
        for i, item in enumerate(results, start=1):
            name = item.get("name", "Untitled")
            url = item.get("url", "")
            snippet = item.get("snippet", "")
            lines.append(f"{i}. {name}\n   {url}\n   {snippet}")
        return "\n".join(lines)

    def _default_endpoint(self, provider: str) -> Optional[str]:
        if provider == "bing":
            return "https://api.bing.microsoft.com/v7.0/search"
        return None

    def _ensure_client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client()
        return self._client
