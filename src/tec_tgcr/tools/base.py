"""Tool abstractions for TEC agents."""
from __future__ import annotations

from typing import Protocol


class Tool(Protocol):
    """Basic protocol for callable agent tools."""

    name: str
    description: str

    def run(self, query: str) -> str:
        """Execute the tool against a query and return structured text."""
        ...
