from pathlib import Path

from tec_tgcr.agents.airth import AirthResearchGuard
from tec_tgcr.config import AgentConfig

class DummyResearchTool:
    name = "web_research"
    description = "Dummy"
    def __init__(self, text: str = ""):
        self._text = text or "Top findings:\n1. Example Result\n   https://example.com\n   Example snippet"
    @property
    def available(self):
        return True
    def run(self, query: str) -> str:
        return self._text


def test_agent_schedule_response(tmp_path: Path):
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    response = agent.respond("What's on my schedule tonight?", [])
    assert "7-Eleven" in response
    assert "Generated" in response


def test_agent_knowledge_response():
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    response = agent.respond("Guide me through the branding knowledge map", [])
    assert "Knowledge highlights" in response


def test_agent_sharepoint_preview():
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    response = agent.respond("SharePoint publish preview", [])
    assert "DRY RUN" in response
    assert "Preview mode" in response


def test_agent_spotify_credential_notice():
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    response = agent.respond("Spotify resonance 0VjIjW4GlUZAMYd2vXMi3b", [])
    assert "Spotify credentials missing" in response


def test_agent_llm_offline_message():
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    response = agent.respond("Need deep analysis on TGCR pillars", [])
    assert "LLM Synthesis" in response
    assert "LLM offline" in response


def test_agent_research_routing(monkeypatch):
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    # Inject dummy research tool
    agent.research_tool = DummyResearchTool()
    response = agent.respond("Please research sources for quantum mythic patterns", [])
    assert "Research Findings:" in response
    assert "Top findings:" in response


def test_existing_paths_still_work():
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    # Schedule path unaffected
    response = agent.respond("show my schedule", [])
    assert "Generated" in response
    # Knowledge path unaffected
    response2 = agent.respond("knowledge branding pillars", [])
    assert "Knowledge highlights" in response2


def test_manifest_structure():
    config = AgentConfig()
    agent = AirthResearchGuard(config)
    manifest = agent.manifest()
    assert manifest["name"] == config.name
    tool_names = {tool["name"] for tool in manifest["tools"]}
    assert {"knowledge_lookup", "schedule_planner", "sharepoint_publish", "spotify_resonance", "llm_responder", "web_research"}.issubset(tool_names)
