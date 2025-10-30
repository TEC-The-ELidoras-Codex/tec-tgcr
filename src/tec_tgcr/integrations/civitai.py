from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import httpx

from ..env import env_str


class CivitaiClient:
    """Minimal Civitai API client for model search and downloads.

    Docs: https://github.com/civitai/civitai/wiki/REST-API-Reference
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        client: Optional[httpx.Client] = None,
    ) -> None:
        self.api_key = api_key or env_str("CIVITAI_API_KEY")
        self.api_base = (
            api_base or env_str("CIVITAI_API_BASE", "https://civitai.com/api/v1")
        ).rstrip("/")
        self._client = client

    @property
    def available(self) -> bool:
        return bool(self.api_key)

    def _ensure_client(self) -> httpx.Client:
        if self._client is None:
            headers = {"User-Agent": "TEC-TGCR/1.0 (LuminAI)"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            self._client = httpx.Client(timeout=60.0, headers=headers)
        return self._client

    def _get(self, path: str, **params: Any) -> httpx.Response:
        url = f"{self.api_base}{path}"
        return self._ensure_client().get(url, params=params or None)

    def get_model(self, model_id: int) -> Dict[str, Any]:
        r = self._get(f"/models/{model_id}")
        r.raise_for_status()
        return r.json()

    def search_models(self, query: str, limit: int = 20) -> Dict[str, Any]:
        r = self._get("/models", query=query, limit=limit)
        r.raise_for_status()
        return r.json()

    def get_model_version(self, version_id: int) -> Dict[str, Any]:
        r = self._get(f"/model-versions/{version_id}")
        r.raise_for_status()
        return r.json()

    def download_file(self, url: str, dest: Path) -> Path:
        dest.parent.mkdir(parents=True, exist_ok=True)
        with self._ensure_client().stream("GET", url) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_bytes():
                    f.write(chunk)
        return dest


__all__ = ["CivitaiClient"]
