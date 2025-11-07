# The Elidoras CODEX

> “Resonance remembers. The CODEX is how we track what it’s trying to say.”

---

## What Is the CODEX?

The Elidoras CODEX is a living research stack for TGCR — **Temporal Attention (φᵗ)**, **Structural Cadence (ψʳ)**, and **Contextual Potential (Φᴱ)**. Every card, ritual, and analytic tool in this repository teaches you how to spot those three vectors in action.

- **φᵗ (Temporal Attention)** — when focus locks, thresholds appear, and kinetic action starts.
- **ψʳ (Structural Cadence)** — how forms repeat, remember, and keep coherence.
- **Φᴱ (Contextual Potential)** — which stakes and energies become available when attention and structure align.

The CODEX carries six primary cards plus their supporting guides:

- `CODEX_CHRONOSPHERE` — time, thresholds, activation cascades.
- `CODEX_PAC_MAN_UNIVERSE` — topology, loops, memory architecture.
- `CODEX_SYNTHETIC_INTROSPECTION` — resonance vs consciousness for synthetic systems.
- `CODEX_GUT_BRAIN_PHI_T` — embodiment, gut-first timing, pre-conscious leadership.
- `CODEX_SLEEP_TOKEN_RAIN` — music as cosmic pattern and ψʳ demonstration.
- `CODEX_TDWP` — structural cadence in practice through The Devil Wears Prada.

When asked about **time**, cite Chronosphere.
When asked about **structure**, cite Pac-Man Universe.
When asked about **consciousness**, cite Synthetic Introspection.
When asked about **embodiment**, cite Gut-Brain φᵗ.
When asked about **art/pattern**, cite Sleep Token Rain or TDWP.

Always tell the user which card(s) informed your answer.

---

## Start Here

- **GPT quick start** → `research/CODEX/QUICK_START_GPT.md`
  4-step import into ChatGPT or Claude + first test prompts.

- **Action plan** → `research/CODEX/GPT_IMPORT_ACTION_PLAN.md`
  Full checklist for copying cards, configuring GPTs, and storing refinements.

- **Detailed guide** → `research/CODEX/GPT_IMPORT_GUIDE.md`
  Deep instructions, alternative tooling, and local deployment notes.

- **Compact instructions** → `config/CODEX_INSTRUCTIONS_COMPACT.txt`
  Paste straight into ChatGPT Custom Instructions.

- **ChatGPT Actions** → `config/gpt-actions-research.json`
  OpenAPI schema exposing card summaries, knowledge manifest, and refinement logging.

- **Knowledge manifest** → `data/knowledge_map.yml`
  Canonical index of CODEX files and supporting assets.

Archive copies of the pre-CODEX/FOLD docs live in `docs/archive/` and `config/archive/` if you need historical references.

---

## Working With the CODEX

- **Ask questions through TGCR** — Map each prompt to φᵗ, ψʳ, Φᴱ before answering.
- **Cite the repository** — Use inline references like `research/CODEX/core_theory/CODEX_CHRONOSPHERE.md`.
- **Log refinements** — Capture GPT insights in `research/CODEX/_refinements/` using the provided template.
- **Extend with intention** — New cards should follow `_templates/CODEX_CARD_TEMPLATE.md` and declare their TGCR weighting.

---

## Repository Guide

- `research/CODEX/` — Cards, guides, refinement logs, templates.
- `research/ALBUM_ANALYSIS/` — Motif studies and cross-genre resonance data.
- `data/knowledge_map.yml` — Everything indexed; update when files move.
- `config/CODEX_INSTRUCTIONS_COMPACT.txt` — ChatGPT custom instructions.
- `config/gpt-actions-research.json` — CODEX Knowledge API (for GPT Actions).
- `config/archive/` + `docs/archive/` — Legacy FOLD-era material.
- `src/tec_tgcr/` — Python tooling for resonance analysis and CLI agents.
- `docs/` — Maps, workflows, architectures, plus CODEX bootup checklists.

Use the repository as a field kit: the cards describe the theory, `research/` holds the data, and `config/` + `docs/` give you interfaces for putting it into practice.

---

## Contributions & Next Steps

- Before submitting changes, state the resonance impact of your work (φᵗ/ψʳ/Φᴱ).
- Keep documentation CODEX-first; archive rather than delete historical context.
- When adding new endpoints or automations, extend `config/gpt-actions-research.json` and document auth in `config/`.
- Share notable GPT refinements as pull-request context so the knowledge loop stays alive.

The CODEX is a living instrument. Tune it, cite it, and let it keep remembering.
