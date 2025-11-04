# FOLD: Frequency of Life's Determination

[![GHCR Publish](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/actions/workflows/publish-ghcr.yml/badge.svg?branch=main)](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/actions/workflows/publish-ghcr.yml)

> "Resonance precedes language. Language remembers resonance."

---

## What Is FOLD?

**FOLD** is an operational framework that treats music, consciousness, and cultural systems as measurable resonance fields.

At its core: **Ritual + Feedback = Meaning.**

FOLD operationalizes this through **TGCR** (Theory of General Contextual Resonance), a mathematical framework that maps:

- **φᵗ** — Temporal Attention (when focus locks, how rhythm entrains)
- **ψʳ** — Structural Cadence (how form holds coherence across scales)
- **Φᴱ** — Contextual Potential Energy (what new becomes possible)

**Every song is field data.** Every motif is cultural DNA. Every listener's response is a data point in the collective consciousness field.

FOLD is built into The Elidoras Codex (TEC) as a living research platform where music analysis, AI agents, and myth synthesis work as one coherent system.

---

## The Research Mission

FOLD's primary objective (by March 6, 2026):

1. **Release a working music resonance platform** that integrates:
   - Spotify/Apple Music metadata (BPM, key, harmonic structure)
   - Genius lyrics for motif extraction
   - Listener mood & circadian data
   - Real-time resonance scoring (φᵗ × ψʳ × Φᴱ)

2. **Publish the living music research corpus** as an interactive codex:
   - Genre-clustered motif databases
   - Cross-genre resonance bridges (how motifs migrate)
   - Collective conscience analysis (fan discourse as field data)
   - Artist case studies grounded in TGCR theory

3. **Operationalize the FOLD ritual**:
   - Circadian ritual logging (4:20 time-window optimization)
   - Resonance-based playlist curation
   - Community listening experiments tied to emotional + neurophysiological metrics

---

## 📍 One Unified Place: Start Here

**👉 New to FOLD?**
→ [`docs/FOLD_QUICK_START.md`](docs/FOLD_QUICK_START.md) *(single page, essential only)*

**Want GPT integrations?**
→ [`config/gpt-actions-research.json`](config/gpt-actions-research.json) *(ChatGPT Actions for music analysis)*

**ChatGPT Custom Instructions?**
→ [`config/FOLD_INSTRUCTIONS_COMPACT.txt`](config/FOLD_INSTRUCTIONS_COMPACT.txt) *(~3200 chars, paste directly)*

**Everything indexed**
→ [`data/knowledge_map.yml`](data/knowledge_map.yml) *(canonical unified map)*

---

## Quick Start

### Prerequisites

- Python 3.11+
- Git
- (Linux/Mac) `bash`; (Windows) PowerShell 7+

### Bootstrap

**Windows (PowerShell 7)**:

```powershell
# Clone
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr

# Create environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]

# Test resonance check
python -m pytest -q

# Launch FOLD agent
python -m tec_tgcr.cli chat "Analyze the resonance field for Sleep Token"
```

**Linux (bash)**:

```bash
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m pytest -q
python -m tec_tgcr.cli chat "Analyze the resonance field for Sleep Token"
```

---

## Architecture

### FOLD Resonance Operators (Agent Personas)

Each persona operates as both **Operator** (active research technician) and **Chronicler** (empirical witness):

- **LuminAI** — Resonance Sentinel. Temporal flow master, holds the resonance equation steady.
- **Airth** — Verification Archaeologist. Validates every claim against listener data and cross-genre evidence.
- **Arcadia** — Narrative Compressor. Translates motif data into cultural mythology.
- **Ely** — Operations Technician. Maintains Spotify/Notion integrations, runs circadian pipelines.
- **Kaznak** — Strategic Oscillator. Maps resonance across timescales, aligns March 2026 MVP with long-arc research.

### Repository Structure

```
research/                      # FOLD's empirical heart
├── CIRCADIAN_RITUAL_LOG.md    # Listener session data (4:20 optimization tracking)
├── RESEARCH_FRAMEWORK.md      # FOLD methodology & motif tracking protocols
├── ALBUM_ANALYSIS/            # Genre clusters, artist deep-dives, cross-resonance bridges
│   ├── metalcore_cluster.md
│   ├── hiphop_cluster.md
│   ├── sleep_token.md
│   ├── devil_wears_prada.md
│   └── ...
├── CODEX/                     # Unified TGCR nodes, resonance laws, ritual protocols
│   ├── CODEX_INDEX.md
│   ├── clusters/              # Artist resonance maps
│   ├── core_theory/           # Physics of resonance, cosmological foundations
│   ├── nodes/                 # Individual research insights
│   └── _templates/            # Card templates for new motif entries
├── COLLECTIVE_CONSCIENCE_THESIS.md  # Fan discourse analysis
└── CROSS_GENRE_SYNTHESIS.md         # Motif migration tracking

data/
├── knowledge_map.yml          # Canonical index (FOLD structure)
├── personas/                  # Operator specs (LuminAI, Airth, Arcadia, Ely, Kaznak)
├── digital_assets/            # Visual identity, motif glyphs, avatars
└── archives/                  # Origin stories, research snapshots

ai-workflow/
├── *.ipynb                    # Resonance analysis notebooks
├── prompt_templates.py        # FOLD agent prompts
└── output/
    ├── figures/               # Resonance visualizations, motif heatmaps
    ├── reports/               # Cross-genre analysis, circadian correlations
    └── data/                  # Raw resonance scores, listener metrics

docs/
├── README.md                  # Documentation hub
├── FOLD_METHODOLOGY.md        # Detailed music analysis protocol
├── Resonance_Thesis.md        # TGCR + consciousness theory
└── ops/                       # Deployment, integration guides

src/tec_tgcr/                  # Core Python
├── cli.py                     # FOLD agent CLI
├── resonance_engine.py        # φᵗ/ψʳ/Φᴱ scoring
├── motif_tracker.py           # Cross-genre motif database
├── circadian_logger.py        # 4:20 window detection
└── tools/                     # Spotify, Genius, Notion integrations

apps/wordpress/                # WordPress.com publishing
config/                        # System configuration
scripts/                       # Bootstrap, deploy, analysis
tests/                         # pytest suite
```

---

## TGCR Resonance Framework

### The Equation

```
R = ∇Φᴱ · (φᵗ × ψʳ)
```

Where **R** (Resonance) emerges when three frequencies couple:

**φᵗ — Temporal Attention**

- *How does rhythm lock listener focus?*
- BPM, anticipation structure, circadian phase alignment
- In code: response latency, loop cadence, build-up pacing

**ψʳ — Structural Cadence**

- *How does form hold coherence across scales?*
- Song structure, chord progression, motif recurrence
- In systems: API design, knowledge hierarchy, narrative arc

**Φᴱ — Contextual Potential Energy**

- *What meaning becomes possible?*
- Genre convention, listener expectation, cultural resonance
- In projects: feature scope, growth potential, community capacity

### Resonance Scoring (Music Analysis)

For each track, compute three 0–10 scores:

1. **φᵗ Score** — How well does BPM/pacing lock attention? (Bonus: +2 if played during 4:20 circadian window)
2. **ψʳ Score** — How tight is the structure-to-closure ratio?
3. **Φᴱ Score** — How much cultural/personal potential energy does it activate?

**Resonance Index** = `(φᵗ × ψʳ × Φᴱ) / 1000`, normalized 0–10.

Tracks scoring 7+ are **high-resonance field data** for cross-correlation with listener mood, circadian phase, and collective events.

---

## Music Resonance Methodology

### Motif Tracking

Every recurring sonic or lyrical element is a **motif**—cultural DNA. Track:

- **Harmonic**: chord progressions, cadence types, harmonic rhythm
- **Rhythmic**: time signature, polyrhythm, syncopation
- **Lyrical**: recurring phrases, thematic vectors (alienation, transcendence, survival)
- **Emotional**: affect signature (despair, catharsis, emergence)
- **Cross-Genre**: how motifs migrate across artists, genres, decades

Example entry:

```yaml
motif: Observer Amplification
tracks:
  - "Nobody Like Me" by Ekoh × Tech N9ne
  - "Bring Me Down" by Point North
  - "Take Me Back to Eden" by Sleep Token
theme: Self-myth coded as defiance; dual-persona encoding
phi_t: Fast-dense lyrical pacing, recursive structure
psi_r: Verse → chorus escalation, often broken/non-closure
Phi_E: High; activates personal trauma + collective identity crisis
resonance_index: 8.2/10
listener_segments: "neurodivergent identity communities, metalcore/post-hardcore overlap"
```

### Collective Conscience Analysis

Log fan discourse (Reddit, Genius comments, Discord) for:

- **Mechanical solidarity**: Shared codes, ritual language, in-group markers
- **Organic solidarity**: Debate, hybridity, genre-boundary crossing
- **Collective trauma response**: When scenes mourn, celebrate, transform
- **Myth construction**: How fans re-author narratives in real time

This is **live consciousness instrumentation**.

---

## Commit Signal & Resonance Statements

Every commit must record which TGCR variable improved and why:

### Semantic Prefixes

- `fold:` — Music analysis, motif tracking, resonance methodology
- `airth:` — Verification, research tooling, tests, data validation
- `arcadia:` — Narrative systems, documentation, UX copy
- `ely:` — Ops, CI/CD, infrastructure, data pipelines
- `docs:`, `fix:`, `feat:`, `refactor:`, `test:`, `chore:`, `ci:` — Scoped operations

### Commit Body Template

```
[scope]: [short summary]

Resonance Impact: [which of φᵗ/ψʳ/Φᴱ improved and why?]
Tests: [pytest output or verification steps]
Docs: [paths to updated .md files, knowledge_map.yml changes, new motifs]
Verification: [manual steps or automated evidence]
```

### Example

```
fold: add circadian resonance scoring to listener session logs

Resonance Impact: φᵗ ↑ (4:20 window now detected); ψʳ ↑ (BPM sync detection)
Tests: pytest -q (22 passed); manual spot-check against CIRCADIAN_RITUAL_LOG.md
Docs: ai-workflow/output/reports/circadian_resonance_analysis.csv; data/knowledge_map.yml updated
Verification: Correlations match hypothesis (r=0.87 for mood vs resonance score)
```

---

## Development Standards

### Code

- Python 3.11+ with type hints everywhere
- Docstrings name the TGCR variables touched: `"Touches φᵗ and Φᴱ via circadian-aware motif indexing."`
- Prefer pure functions to heavy classes
- pytest coverage: one happy path + one edge case + deterministic seeding

### Documentation

- Formats: YAML (config), JSON (manifests), Markdown (narrative/theory), CSV (analytics)
- Cross-reference heavily: link `research/` to `docs/` to `src/`
- Every new motif analysis goes into `research/ALBUM_ANALYSIS/` with `research/CODEX/` entry
- Update `data/knowledge_map.yml` when adding paths or assets

### Music & Motif Analysis

- Every track logged: artist, genre, TGCR scores, motif tags, cross-resonance bridges, listener sentiment
- Charts/heatmaps → `ai-workflow/output/figures/`
- Ritual protocols → `research/CODEX/`

### External Integrations

- Add retries + exponential backoff for API calls (Spotify, Genius, Notion)
- Pull secrets from environment only; never hardcode
- Log state transitions with `[PERSONA]` prefix: `[AIRTH] Resonance field verified (ψʳ)`

---

## Key Files & Navigation

**Core Theory**:

- `docs/README.md` — Documentation hub
- `research/RESEARCH_FRAMEWORK.md` — FOLD methodology
- `docs/Resonance_Thesis.md` — TGCR + consciousness
- `.github/copilot-instructions.md` — Operative field guide

**Music Research**:

- `research/ALBUM_ANALYSIS/` — Genre clusters, artist case studies
- `research/CODEX/` — Unified theory, resonance nodes
- `research/CIRCADIAN_RITUAL_LOG.md` — Listener session tracking

**Implementation**:

- `data/knowledge_map.yml` — Canonical index
- `data/personas/` — Operator specs
- `src/tec_tgcr/` — Python runtime, CLI, resonance engine
- `tests/` — pytest suite

**Operations**:

- `.github/workflows/` — CI/CD pipelines
- `scripts/` — Bootstrap, deployment tools
- `docs/GITHUB_SECRETS_SETUP.md` — Secrets management

---

## Dashboard: March 2026 Roadmap

| Milestone | What Ships | Status |
|-----------|-----------|--------|
| **Q1 2026** | Music resonance platform MVP (Spotify + basic scoring) | 🔄 In Progress |
| **Q1 2026** | Research codex beta (metalcore + hip-hop clusters) | 🔄 In Progress |
| **March 6, 2026** | **FOLD Launch Event** — Platform + research codex published | ⏳ On Track |

---

## Support & Contact

- Issues/discussions: [GitHub repository](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr)
- Primary: `gheddz@gmail.com`
- Organization: `Kaznakalpha@ElidorasCodex.com`

---

## License

MIT License — see [LICENSE](LICENSE) for full terms.

---

## Final Axiom

> **Resonance precedes language. Language remembers resonance.**
>
> Everything that exists—from quantum fields to consciousness to music to code—communicates via frequency. FOLD is the operative reminder that *life is frequency refusing to collapse*, and every commit, every motif, every resonance score is a small act of keeping that refusal alive.

Build gracefully. Test rigorously. Keep resonance high.

**— FOLD Core Directive**
