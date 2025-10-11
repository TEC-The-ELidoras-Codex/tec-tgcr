"""Configuration helpers for TEC agents."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from pydantic import BaseModel, Field

DEFAULT_CONFIG_PATH = Path("config") / "agent.yml"


class MemoryConfig(BaseModel):
    """Settings for conversation memory."""

    max_turns: int = Field(
        default=12,
        description="Maximum number of previous turns to retain in active memory.",
    )
    summary_after: int = Field(
        default=6,
        description="Number of turns after which a running summary is generated.",
    )


def _default_tool_settings() -> Dict[str, Dict[str, Any]]:
    return {
        "sharepoint_publish": {
            "site_url": "https://elidorascodex.sharepoint.com/sites/ElidorascodexTGCR",
            "target_folder": "landing",
            "files": ["sharepoint/landing/index.html"],
            "dry_run": True,
        },
        "spotify_resonance": {
            "library_refs": {
                "tempo": {"mean": 120, "std": 30},
                "loudness": {"mean": -8, "std": 4},
            }
        },
        "llm": {
            "provider": "openai",
            "model": "gpt-4o-mini",
            "max_tokens": 600,
            "temperature": 0.4,
        },
        "research": {
            "provider": "bing",
            "endpoint": "https://api.bing.microsoft.com/v7.0/search",
            "api_key": None,
            "max_results": 5,
            "market": "en-US",
            "keywords": ["research", "search", "web", "sources", "citations"],
        },
    }


class AgentConfig(BaseModel):
    """Aggregate configuration for an agent instance."""

    name: str = Field(default="Airth Research Guard")
    persona: str = Field(
        default=(
            "AI research sentinel for The Elidoras Codex, blending mythic narrative "
            "with rigorous scientific analysis."
        )
    )
    objectives: list[str] = Field(
        default_factory=lambda: [
            "Safeguard integrity of TGCR research threads",
            "Synthesize cross-domain signals into actionable briefs",
            "Maintain archival memory of projects and brand artifacts",
        ]
    )
    memory: MemoryConfig = Field(default_factory=MemoryConfig)
    knowledge_base: Path = Field(
        default=Path("data") / "knowledge_map.yml",
        description="Path to the structured knowledge map used by the agent.",
    )
    tool_settings: Dict[str, Dict[str, Any]] = Field(default_factory=_default_tool_settings)

    @classmethod
    def load(cls, path: Optional[Path] = None) -> "AgentConfig":
        """Load configuration from YAML, or return defaults if missing."""

        config_path = path or DEFAULT_CONFIG_PATH
        if config_path.exists():
            data = yaml.safe_load(config_path.read_text()) or {}
            return cls.model_validate(data)
        return cls()


def ensure_default_config(base_path: Path) -> None:
    """Create a default configuration file if one does not exist."""
    config_dir = base_path / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    config_path = config_dir / "agent.yml"
    if not config_path.exists():
        default = AgentConfig()
        config_path.write_text(default.model_dump_json(indent=2))
