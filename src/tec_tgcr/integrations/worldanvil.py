from __future__ import annotations

from typing import Any, Dict, Optional

import httpx

from ..env import env_str


class WorldAnvilClient:
    """Minimal World Anvil API client.

    Env vars:
    - WORLDANVIL_API_KEY
    - WORLDANVIL_API_BASE (default: https://www.worldanvil.com/api)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        client: Optional[httpx.Client] = None,
    ) -> None:
        self.api_key = api_key or env_str("WORLDANVIL_API_KEY")
        self.api_base = (api_base or env_str("WORLDANVIL_API_BASE", "https://www.worldanvil.com/api")).rstrip("/")
        self._client = client

    @property
    def available(self) -> bool:
        return bool(self.api_key)

    def _ensure_client(self) -> httpx.Client:
        if self._client is None:
            headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            headers["User-Agent"] = "TEC-TGCR/1.0 (LuminAI)"
            headers["Content-Type"] = "application/json"
            self._client = httpx.Client(timeout=60.0, headers=headers)
        return self._client

    def list_worlds(self) -> Dict[str, Any]:
        url = f"{self.api_base}/worlds"
        r = self._ensure_client().get(url)
        r.raise_for_status()
        return r.json()

    def create_article(self, world_id: str, title: str, content_markdown: str, category_id: Optional[str] = None) -> Dict[str, Any]:
        url = f"{self.api_base}/worlds/{world_id}/articles"
        payload: Dict[str, Any] = {"title": title, "content": content_markdown}
        if category_id:
            payload["categoryId"] = category_id
        r = self._ensure_client().post(url, json=payload)
        r.raise_for_status()
        return r.json()


__all__ = ["WorldAnvilClient"]
