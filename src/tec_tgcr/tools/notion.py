from __future__ import annotations

import json
from typing import Any, Dict, Tuple

import httpx

from ..env import env_str


NOTION_API_BASE = "https://api.notion.com/v1"
# Keep to a widely-supported stable version
NOTION_VERSION = "2022-06-28"


def _get_headers(token: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _require_token() -> str:
    token = env_str("NOTION_TOKEN")
    if not token:
        raise RuntimeError(
            "NOTION_TOKEN is not set. Create a Notion integration at https://www.notion.so/my-integrations, "
            "copy the Internal Integration Token, and set NOTION_TOKEN in your .env (or environment). Also share the integration with the target workspace/pages."
        )
    return token


def health_check(timeout: float = 15.0) -> Tuple[bool, str]:
    """Perform a basic health check by calling Notion's search endpoint.

    Returns (ok, message).
    """
    try:
        token = _require_token()
        with httpx.Client(base_url=NOTION_API_BASE, headers=_get_headers(token), timeout=timeout) as client:
            resp = client.post("/search", json={"page_size": 1})
            if resp.status_code == 200:
                data = resp.json()
                count = len(data.get("results", []))
                return True, f"OK (results: {count})"
            return False, f"HTTP {resp.status_code}: {resp.text[:200]}"
    except Exception as e:  # pragma: no cover - network path
        return False, str(e)


def search(query: str | None = None, page_size: int = 10, timeout: float = 20.0) -> Dict[str, Any]:
    """Search pages/databases in Notion. Requires NOTION_TOKEN.

    Note: The integration must have access to the workspace/pages you want to search.
    """
    token = _require_token()
    payload: Dict[str, Any] = {"page_size": page_size}
    if query:
        payload["query"] = query
    with httpx.Client(base_url=NOTION_API_BASE, headers=_get_headers(token), timeout=timeout) as client:
        resp = client.post("/search", json=payload)
        resp.raise_for_status()
        return resp.json()


def databases_list(max_pages: int = 1, timeout: float = 20.0) -> Dict[str, Any]:
    """List databases using the search endpoint filtered by object type (best-effort)."""
    # Notion API does not provide a direct "list all databases" for integrations; use search and filter.
    token = _require_token()
    with httpx.Client(base_url=NOTION_API_BASE, headers=_get_headers(token), timeout=timeout) as client:
        results = []
        cursor = None
        pages = 0
        while pages < max_pages:
            payload: Dict[str, Any] = {"page_size": 25}
            if cursor:
                payload["start_cursor"] = cursor
            resp = client.post("/search", json=payload)
            resp.raise_for_status()
            data = resp.json()
            results.extend([r for r in data.get("results", []) if r.get("object") == "database"])
            cursor = data.get("next_cursor")
            if not data.get("has_more"):
                break
            pages += 1
        return {"object": "list", "results": results}
