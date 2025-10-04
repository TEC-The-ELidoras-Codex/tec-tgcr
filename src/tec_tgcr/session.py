"""Conversation session orchestration."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .agents.base import AgentProtocol
from .memory.memory import ConversationMemory


@dataclass
class ConversationSession:
    """Manages the lifecycle of a dialogue with an agent."""

    agent: AgentProtocol
    memory: ConversationMemory = field(default_factory=ConversationMemory)

    def process_user_message(self, message: str) -> str:
        """Route a user message through memory and agent reasoning."""
        self.memory.record_user(message)
        context = self.memory.recall()
        agent_response = self.agent.respond(message, context)
        self.memory.record_agent(agent_response)
        return agent_response

    def transcript(self) -> List[tuple[str, str]]:
        """Return the conversation transcript as a list of tuples."""
        return self.memory.as_pairs()
