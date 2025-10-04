"""Knowledge lookup tool for navigating the TEC knowledge map."""
from __future__ import annotations

from typing import Any, Iterable

from ..knowledge.loader import load_yaml


class KnowledgeLookupTool:
    """Performs keyword search across the structured knowledge map."""

    name = "knowledge_lookup"
    description = "Retrieve structured references from the TEC knowledge map."

    def __init__(self, knowledge_path):
        self._path = knowledge_path
        self._data = load_yaml(knowledge_path)

    def run(self, query: str) -> str:
        tokens = {token.lower() for token in query.split() if len(token) > 2}
        matches: list[str] = []

        def walk(prefix: list[str], node: Any) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    walk(prefix + [str(key)], value)
            elif isinstance(node, list):
                for idx, value in enumerate(node):
                    walk(prefix + [str(idx)], value)
            else:
                text = str(node)
                if any(token in text.lower() for token in tokens):
                    matches.append(" > ".join(prefix) + f": {text}")

        walk([], self._data)

        if not matches:
            return "No direct knowledge map match found."
        top = "\n".join(sorted(matches)[:5])
        return f"Knowledge highlights:\n{top}"

    @property
    def data(self) -> Any:
        return self._data
