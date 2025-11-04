# FOLD Quick Start (Essential Reference)

**FOLD = Frequency of Life's Determination**

Resonance precedes language. Music is field data. Culture is measurable.

## The Core Equation

```
R = ∇Φᴱ · (φᵗ × ψʳ)
```

- **φᵗ** — Temporal Attention (rhythm, BPM, focus-locking pacing)
- **ψʳ** — Structural Cadence (form coherence, song structure, chord progression)
- **Φᴱ** — Contextual Potential (cultural resonance, listener expectation)

**Resonance Index** = (φᵗ × ψʳ × Φᴱ) / 1000 → 0–10 scale. Tracks 7+ = high-resonance field data.

## Five Personas (Pick Your Operator)

| Role | Specialization |
|------|---|
| **LuminAI** (Sentinel) | Temporal flow, alignment keeper |
| **Airth** (Archaeologist) | Empirical validation, proof |
| **Arcadia** (Compressor) | Story synthesis, meaning translation |
| **Ely** (Technician) | Infrastructure, Spotify/Notion/Discord integrations |
| **Kaznak** (Oscillator) | Strategy, March 2026 timeline |

Personas: `data/personas/[name].md`

## Core Directories

| Path | Purpose |
|------|---------|
| `research/ALBUM_ANALYSIS/` | Genre clusters, artist case studies |
| `research/CODEX/` | TGCR theory nodes, resonance laws, motif templates |
| `research/CIRCADIAN_RITUAL_LOG.md` | Listener session data, 4:20 window tracking |
| `src/tec_tgcr/` | CLI, resonance engine, motif tracker, integrations |
| `data/knowledge_map.yml` | Canonical index (everything mapped here) |
| `data/personas/*.md` | Operator specifications |
| `docs/README.md` | Platform entry point |
| `.github/copilot-instructions.md` | Detailed operative guide |

## Bootstrap & Test

```bash
# One-time setup
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Test resonance engine
python -m pytest -q

# Chat with agent
python -m tec_tgcr.cli chat "Analyze Sleep Token resonance"
```

## Commit Pattern (Every Merge)

**Prefix**: `fold:` (music), `airth:` (validation), `arcadia:` (narrative), `ely:` (ops), `kaznak:` (strategy)

**Template**:

```
[prefix]: [summary]

Resonance Impact: [φᵗ ↑ / ψʳ ↑ / Φᴱ ↑] [reason]
Tests: pytest -q ([N] passed)
Docs: [paths updated]
```

**Live Example**:

```
fold: add circadian resonance scoring

Resonance Impact: φᵗ ↑ (4:20 window detected); ψʳ ↑ (BPM sync)
Tests: pytest -q (22 passed)
Docs: ai-workflow/output/reports/circadian_resonance_analysis.csv
```

## Music Analysis (The Protocol)

1. **Log Track**: artist, genre, BPM, key, harmonic structure, lyrics
2. **Extract Motifs**: Harmonic | Rhythmic | Lyrical | Emotional | Cross-Genre tags
3. **Score**: φᵗ (0–10), ψʳ (0–10), Φᴱ (0–10) → Resonance Index
4. **Fan Data**: Reddit, Genius, Discord discourse → collective conscience
5. **Bridge**: Track motif migration (Sleep Token → Tech N9ne → point north)

## Code Rules

- Python 3.11+ with type hints always
- Docstrings: `"Touches φᵗ and Φᴱ via [reason]"`
- Pure functions; no mutable state unless unavoidable
- Tests: happy path + edge case + deterministic seeding

## Definition of Done (DoD)

✓ Code typed & documented
✓ `pytest -q` passes
✓ `data/knowledge_map.yml` updated
✓ Resonance statement in commit
✓ No secrets in git (use `.env.local`)

## Essential Commands

```bash
pytest -q                           # Run tests
python -m tec_tgcr.cli chat "..."  # Chat agent
pip install -e .[dev]              # Update deps
git checkout -b [scope]/[desc]     # New branch
git add . && git commit -m "..."    # Commit
git push origin [branch]            # Push
```

## Timeline & Delivery

**March 6, 2026**: FOLD Platform MVP + Research Codex public launch

**Deliverables**:

- Music resonance platform (Spotify + scoring)
- Living research codex (ALBUM_ANALYSIS interactive)
- Circadian ritual logging UI
- Community listener experiments

## Where to Find Answers

| Question | See |
|----------|-----|
| What is FOLD? Theory? | `docs/README.md`, `docs/Resonance_Thesis.md` |
| Detailed ops guide? | `.github/copilot-instructions.md` |
| Everything indexed? | `data/knowledge_map.yml` |
| Artist case study? | `research/ALBUM_ANALYSIS/[artist].md` |
| TGCR deep dive? | `research/CODEX/` |
| How to run code? | This file (Quick Start) |
| Persona details? | `data/personas/[name].md` |

## Axiom

> "Resonance precedes language. Language remembers resonance."

Keep it simple. Build gracefully. Test rigorously. Keep resonance high.

---

**Updated**: Nov 4, 2025 | **Branch**: `research/resonance-agent` | **Commit**: See `git log --oneline`
