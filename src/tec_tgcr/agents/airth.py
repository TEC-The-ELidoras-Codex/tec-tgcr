"""Implementation of the Airth Research Guard agent."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional

from ..config import AgentConfig
from ..tools.base import Tool
from ..tools.knowledge_lookup import KnowledgeLookupTool
from ..tools.llm import LLMResponder
from ..tools.schedule import ScheduleTool
from ..tools.sharepoint import SharePointPublisherTool
from ..tools.spotify_resonance import SpotifyResonanceTool
from ..tools.research import ResearchTool

DEFAULT_SESSIONS = [
    {"label": "Mon–Fri", "window": "10:00–12:00 Eastern — TEC Agent build sprints"},
]

DEFAULT_SHIFTS = [
    {"label": "Sun Oct 5", "window": "22:00–06:00"},
    {"label": "Mon Oct 6", "window": "22:00–06:00"},
    {"label": "Tue Oct 7", "window": "12:00–19:00"},
    {"label": "Wed Oct 8", "window": "11:00–19:00"},
]


class AirthResearchGuard:
    """Primary TEC agent orchestrating tool routing and lore guidance."""

    def __init__(self, config: Optional[AgentConfig] = None) -> None:
        self.config = config or AgentConfig.load()

        knowledge_path = Path(self.config.knowledge_base)
        if not knowledge_path.is_absolute():
            knowledge_path = Path.cwd() / knowledge_path

        self.knowledge_tool = KnowledgeLookupTool(knowledge_path)
        self.schedule_tool = self._init_schedule_tool()
        self.sharepoint_tool = self._init_sharepoint_tool()
        self.spotify_tool = self._init_spotify_tool()
        self.llm_tool = self._init_llm_tool()
        self.research_tool: Optional[Tool] = self._init_research_tool()

        self._tools: List[object] = [self.knowledge_tool, self.schedule_tool]
        for tool in (self.sharepoint_tool, self.spotify_tool, self.llm_tool, self.research_tool):
            if tool is not None:
                self._tools.append(tool)

        # Cache knowledge pillars for manifest metadata.
        self._knowledge_cache = self.knowledge_tool.data

    # === Public interface ===
    def respond(self, message: str, context: Iterable[dict[str, str]]) -> str:
        """Generate a structured response routed through the available tools."""
        message_lower = message.lower()
        sections: List[str] = []

        if any(keyword in message_lower for keyword in ("schedule", "shift", "planner", "711", "calendar")):
            sections.append(self.schedule_tool.run(message))

        if any(keyword in message_lower for keyword in ("knowledge", "branding", "map", "tgcr", "pillar")):
            sections.append(self.knowledge_tool.run(message))

        if self.sharepoint_tool and any(keyword in message_lower for keyword in ("sharepoint", "publish", "siteassets", "deploy")):
            sections.append(self.sharepoint_tool.run(message))

        if self.spotify_tool and ("spotify" in message_lower or "resonance" in message_lower):
            sections.append(self.spotify_tool.run(message))

        if self.llm_tool and any(keyword in message_lower for keyword in ("analysis", "deep", "synthesis", "llm")):
            system_hint = (
                f"You are {self.config.name}, {self.config.persona}. Provide TGCR-aligned synthesis."
            )
            llm_response = self.llm_tool.run(message, system=system_hint)
            if llm_response:
                sections.append(f"LLM Synthesis:\n{llm_response}")

        # Research routing
        research_settings = self.config.tool_settings.get("research", {})
        research_keywords = research_settings.get("keywords", ["research", "search", "web", "sources", "citations"])
        if self.research_tool and any(keyword in message_lower for keyword in research_keywords):
            research_result = self.research_tool.run(message)
            if research_result:
                sections.append(f"Research Findings:\n{research_result}")

        if not sections:
            sections.append(self._craft_lore_hint(message_lower))
            sections.append(self.knowledge_tool.run(message))

        if context:
            sections.append(self._context_echo(context))

        return "\n\n".join(section for section in sections if section)

    def manifest(self) -> dict:
        """Return the manifest description consumed by orchestration layers."""
        manifest_tools = [
            {
                "name": self.knowledge_tool.name,
                "description": self.knowledge_tool.description,
            },
            {
                "name": self.schedule_tool.name,
                "description": self.schedule_tool.description,
            },
        ]

        manifest_tools.append(self._manifest_entry(self.sharepoint_tool, "sharepoint_publish", "Publish static assets to SharePoint using the Microsoft 365 CLI."))
        manifest_tools.append(self._manifest_entry(self.spotify_tool, "spotify_resonance", "Project Spotify audio features into OXY/DOP/ADR resonance scores."))
        manifest_tools.append(self._manifest_entry(self.llm_tool, "llm_responder", "Summon an LLM insight block when deeper synthesis is requested."))
        manifest_tools.append(self._manifest_entry(self.research_tool, "web_research", "Perform web research and return cited findings from reputable sources."))

        knowledge_overview = self._knowledge_cache.get("overview", {}) if isinstance(self._knowledge_cache, dict) else {}
        pillars = knowledge_overview.get("pillars", [])

        return {
            "agent_spec_version": "1.0",
            "name": self.config.name,
            "persona": self.config.persona,
            "objectives": self.config.objectives,
            "tools": manifest_tools,
            "memory": {
                "max_turns": self.config.memory.max_turns,
                "summary_after": self.config.memory.summary_after,
            },
            "knowledge": {
                "source": str(self.config.knowledge_base),
                "pillars": pillars,
            },
        }

    # === Internal helpers ===
    def _manifest_entry(self, tool: Optional[object], fallback_name: str, fallback_description: str) -> dict:
        payload = {
            "name": getattr(tool, "name", fallback_name),
            "description": getattr(tool, "description", fallback_description),
        }
        if hasattr(tool, "available"):
            payload["available"] = getattr(tool, "available")
        return payload

    def _context_echo(self, context: Iterable[dict[str, str]]) -> str:
        tail = list(context)[-4:]
        if not tail:
            return ""
        lines = ["Recent memory echo:"]
        for item in tail:
            role = item.get("role", "?")
            content = item.get("content", "")
            lines.append(f"  - {role}: {content}")
        return "\n".join(lines)

    def _craft_lore_hint(self, message_lower: str) -> str:
        if "music" in message_lower or "spotify" in message_lower:
            return (
                "Resonance Insight: Route track IDs through the Spotify resonance tool, then log the findings "
                "inside the Development › Pipelines pillar."
            )
        if "avatar" in message_lower or "sharepoint" in message_lower:
            return (
                "Visual Directive: Update the SharePoint landing glyphs using the branded palette before publishing."
            )
        return (
            "Strategic Pulse: Anchor your next action to one of the five TEC pillars and consult the knowledge map "
            "for supporting lore."
        )

    def _init_schedule_tool(self) -> ScheduleTool:
        settings = self.config.tool_settings.get("schedule_planner", {})
        sessions = settings.get("sessions", DEFAULT_SESSIONS)
        shifts = settings.get("shifts", DEFAULT_SHIFTS)
        ics_name = settings.get("ics_name", "tec_schedule")
        planner_bucket = settings.get("planner_bucket", "Operations")
        return ScheduleTool(sessions=sessions, shifts=shifts, ics_name=ics_name, planner_bucket=planner_bucket)

    def _init_sharepoint_tool(self) -> Optional[SharePointPublisherTool]:
        settings = self.config.tool_settings.get("sharepoint_publish", {})
        site_url = settings.get("site_url")
        target_folder = settings.get("target_folder")
        files = settings.get("files")
        if not (site_url and target_folder and files):
            return None
        dry_run = settings.get("dry_run", True)
        return SharePointPublisherTool(site_url=site_url, target_folder=target_folder, files=files, dry_run=dry_run)

    def _init_spotify_tool(self) -> Optional[SpotifyResonanceTool]:
        settings = self.config.tool_settings.get("spotify_resonance", {})
        references = settings.get("library_refs")
        client_id = settings.get("client_id")
        client_secret = settings.get("client_secret")
        return SpotifyResonanceTool(client_id=client_id, client_secret=client_secret, references=references)

    def _init_llm_tool(self) -> Optional[LLMResponder]:
        settings = self.config.tool_settings.get("llm", {})
        if not settings:
            return None
        return LLMResponder(
            provider=settings.get("provider", "openai"),
            model=settings.get("model", "gpt-4o-mini"),
            max_tokens=settings.get("max_tokens", 600),
            temperature=settings.get("temperature", 0.4),
            api_key=settings.get("api_key"),
            endpoint=settings.get("endpoint"),
        )

    def _init_research_tool(self) -> Optional[ResearchTool]:
        settings = self.config.tool_settings.get("research", {})
        if not settings:
            return None
        return ResearchTool(
            provider=settings.get("provider", "bing"),
            endpoint=settings.get("endpoint"),
            api_key=settings.get("api_key"),
            max_results=settings.get("max_results", 5),
            market=settings.get("market", "en-US"),
        )
