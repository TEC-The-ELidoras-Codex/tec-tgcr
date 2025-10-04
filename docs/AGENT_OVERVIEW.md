# Airth Research Guard — Architecture Overview

## Purpose
The Airth Research Guard is the first operational agent in the TEC Agent Suite. It synthesizes
research, branding, and operational cadence information to support the Theory of General
Contextual Resonance (TGCR) initiatives.

## Core Components

- **Configuration (`config/agent.yml`)** — Declares persona, objectives, memory limits, and
  the linked knowledge base file.
- **Knowledge Map (`data/knowledge_map.yml`)** — Structured YAML containing the TEC
  knowledge pillars, branding assets, and operational references.
- **Agent Runtime (`src/tec_tgcr/agents/airth.py`)** — Implements heuristics, tool routing,
  and manifest generation for the agent.
- **Tools (`src/tec_tgcr/tools/`)**
  - `knowledge_lookup` performs keyword search across the knowledge map.
  - `schedule_planner` summarizes build sessions and confirmed shifts.
- **Memory (`src/tec_tgcr/memory/memory.py`)** — Maintains a rolling history of the
  conversation for contextual responses.
- **CLI (`src/tec_tgcr/cli.py`)** — Typer-based interface exposing `chat` and `manifest`
  commands.

## Conversation Flow

1. User message enters the `ConversationSession` and is recorded by memory.
2. The agent inspects keywords to determine whether to trigger the schedule tool or the
   knowledge lookup tool.
3. If no specific keywords are detected, the agent provides a strategic hint grounded in TEC
   lore and appends knowledge highlights.
4. Memory echoes from the past four turns are appended to maintain continuity.

## Manifest

Running `tec-agent manifest` emits the JSON description of the agent, including tools,
objectives, and linked knowledge sources. This manifest can be consumed by higher-level
orchestration platforms or Azure-based agent hosts.

## Next Steps

- Wire additional tools (SharePoint deployment, Spotify resonance pipeline).
- Integrate OpenAI/Anthropic connectors for generative augmentation.
- Expand tests covering tool routing edge cases.
