from __future__ import annotations

from pathlib import Path

NEW_README = """# The Elidoras Codex — TGCR Agent Stack

> TEC weaves myth, machine, and meaning into a living open-source cosmology.

## Overview
The TGCR agent stack packages the first operational sentinel, **Airth Research Guard**, alongside the scaffolding required to expand into a full suite of resonance-aware helpers. The repository delivers a Typer-based CLI, knowledge-map loaders, memory buffers, and specialized tools for knowledge search, scheduling, SharePoint publishing, and Spotify resonance analysis.

## Quick start

```pwsh
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -e .[dev]
python -m tec_tgcr.cli chat "Help me plan a TEC build sprint"
```

## CLI commands
- `tec-agent chat` — open the interactive console experience.
- `tec-agent manifest` — emit the Airth Research Guard manifest JSON.
- `pytest` — execute regression coverage.

## Repository map
- `config/agent.yml` — persona, objectives, and memory tuning for Airth.
- `data/knowledge_map.yml` — structured knowledge pillars, branding cues, and cadence data.
- `agents/manifests/airth_research_guard.json` — exportable manifest for orchestration layers.
- `docs/AGENT_OVERVIEW.md` — runtime architecture notes.
- `docs/archive/planning_scratchpad.md` — legacy planning canvas preserved for context.
- `src/tec_tgcr/` — Python package (agents, tools, memory, CLI, configuration helpers).
- `tests/` — conversational regression scenarios.

## Agent snapshot
- **Name:** Airth Research Guard
- **Purpose:** Safeguard TGCR research threads, synthesize cross-domain insight, and uphold the TEC brand system.
- **Tools:**
  - `knowledge_lookup` — keyword search across the TEC knowledge map.
  - `schedule_planner` — formatted summaries of TEC build sessions and confirmed shifts.
  - `sharepoint_publish` — preview or deploy SharePoint Site Assets via the Microsoft 365 CLI.
  - `spotify_resonance` — translate Spotify audio features into OXY/DOP/ADR resonance metrics.
  - `llm_responder` — optional deep-synthesis bridge when model credentials are available.
- **Knowledge pillars:** Research & Theory · Development & Pipelines · Branding & Media · Community & Outreach · Professional Growth.

## Schedules at a glance
- **TEC build sessions:** Monday–Friday, 10:00–12:00 Eastern.
- **7-Eleven shifts:** Sun Oct 5 (22:00–06:00), Mon Oct 6 (22:00–06:00), Tue Oct 7 (12:00–19:00), Wed Oct 8 (11:00–19:00).
- Prompt the agent with "schedule", "planner", or "711" for rapid summaries. Ask for "calendar" to receive an `.ics` export or "planner csv" for Microsoft Planner scaffolding.

## Roadmap
- Automate SharePoint deployments via GitHub Actions once credentials can be stored securely.
- Persist Spotify-derived resonance scores into the knowledge map for analytics review.
- Expand regression coverage with stubs for the LLM endpoint and Spotify API.

---
Looking for the original planning mural? Check `docs/archive/planning_scratchpad.md` for the full preserved canvas, SharePoint publishing flow, and Spotify pipeline sketches.
"""


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    readme_path = repo_root / "README.md"
    archive_path = repo_root / "docs" / "archive" / "planning_scratchpad.md"

    original = readme_path.read_text(encoding="utf-8")

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_path.write_text(original, encoding="utf-8")

    readme_path.write_text(NEW_README, encoding="utf-8")

    print(f"Archived legacy README to {archive_path.relative_to(repo_root)}")
    print("README.md refreshed with concise overview")


if __name__ == "__main__":
    main()
