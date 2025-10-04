"""Lightweight conversation memory."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class ConversationMemory:
    """Maintains rolling context for agent conversations."""

    max_turns: int = 12
    _history: List[dict[str, str]] = field(default_factory=list)

    def record_user(self, message: str) -> None:
        self._history.append({"role": "user", "content": message})
        self._trim()

    def record_agent(self, message: str) -> None:
        self._history.append({"role": "agent", "content": message})
        self._trim()

    def recall(self) -> List[dict[str, str]]:
        return list(self._history)

    def as_pairs(self) -> List[tuple[str, str]]:
        pairs: List[tuple[str, str]] = []
        user_message: str | None = None
        for item in self._history:
            if item["role"] == "user":
                user_message = item["content"]
            elif item["role"] == "agent" and user_message is not None:
                pairs.append((user_message, item["content"]))
                user_message = None
        return pairs

    def _trim(self) -> None:
        overflow = len(self._history) - (self.max_turns * 2)
        if overflow > 0:
            del self._history[:overflow]
