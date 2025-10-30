"""Abstract protocol for TEC agents."""

from __future__ import annotations

from typing import Iterable, Protocol


class AgentProtocol(Protocol):
    """Minimal protocol each agent must satisfy."""

    def respond(self, message: str, context: Iterable[dict[str, str]]) -> str:
        """Generate a response to a user message."""
        ...

    def manifest(self) -> dict:
        """Return the structured manifest for the agent."""
        ...
