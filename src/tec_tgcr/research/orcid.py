from __future__ import annotations

import os
from typing import Dict, Any

import httpx


class ORCIDClient:
    """Minimal public ORCID profile fetcher (public API).

    Uses ORCID_ID from environment if not provided.
    """

    def __init__(self, orcid_id: str | None = None):
        self.orcid_id = orcid_id or os.getenv("ORCID_ID")
        if not self.orcid_id:
            raise RuntimeError("ORCID_ID not set")
        self._client = httpx.Client(
            base_url="https://pub.orcid.org/v3.0/",
            headers={"Accept": "application/json", "User-Agent": "TEC-TGCR/1.0"},
        )

    def summary(self) -> Dict[str, Any]:
        r = self._client.get(f"{self.orcid_id}/summary")
        r.raise_for_status()
        return r.json()


__all__ = ["ORCIDClient"]
