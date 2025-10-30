from __future__ import annotations


import httpx


class ArxivSearch:
    """Simple arXiv API wrapper for search and metadata.

    For bulk PDFs/SRC on S3 requester pays, use AWS SDK (not included here).
    """

    def __init__(self):
        self._client = httpx.Client(base_url="https://export.arxiv.org/api/", timeout=30, headers={
            "User-Agent": "TEC-TGCR/1.0"
        })

    def search(self, query: str, start: int = 0, max_results: int = 25) -> str:
        # arXiv uses Atom XML; return raw text to be parsed upstream as needed
        params = {"search_query": query, "start": start, "max_results": max_results}
        r = self._client.get("query", params=params)
        r.raise_for_status()
        return r.text

__all__ = ["ArxivSearch"]
