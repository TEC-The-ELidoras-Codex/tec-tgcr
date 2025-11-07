# CODEX Structure Overview (Nov 2025)

## Why This Exists

The repository now centers on the CODEX cards and TGCR guidance. This overview locates the current sources of truth, the automation surfaces, and the historical material that has been archived.

---

## Entry Points

| Track | File | Purpose |
|-------|------|---------|
| 15 min import | `research/CODEX/QUICK_START_GPT.md` | Fastest way to stand up a CODEX-aware GPT |
| Full plan | `research/CODEX/GPT_IMPORT_ACTION_PLAN.md` | Copy cards, configure GPTs, log refinements |
| Deep guide | `research/CODEX/GPT_IMPORT_GUIDE.md` | All platforms + local workflows |
| ChatGPT instructions | `config/CODEX_INSTRUCTIONS_COMPACT.txt` | Paste into Custom Instructions |
| GPT Actions | `config/gpt-actions-research.json` | CODEX Knowledge API (cards, manifest, refinements) |
| Canonical map | `data/knowledge_map.yml` | Index of CODEX files and supporting assets |

Legacy FOLD documents are preserved in `docs/archive/` and `config/archive/`.

---

## Repository Layout (Current)

```
README.md                     # CODEX overview + navigation
STRUCTURE_OVERVIEW.md         # (this file) entry points + topology
config/
├── CODEX_INSTRUCTIONS_COMPACT.txt  # ChatGPT compact instructions
├── gpt-actions-research.json       # CODEX Knowledge API (OpenAPI 3.1)
└── archive/                        # FOLD instructions & API notes (historical)
data/
└── knowledge_map.yml               # Canonical index (update when files move)
research/
├── CODEX/                          # Core cards, guides, refinements
│   ├── core_theory/                # Chronosphere, Pac-Man Universe
│   ├── nodes/                      # Synthetic Introspection, Gut-Brain φᵗ
│   ├── clusters/                   # Sleep Token Rain, TDWP
│   ├── QUICK_START_GPT.md          # Quick import steps
│   ├── GPT_IMPORT_ACTION_PLAN.md   # Detailed rollout plan
│   └── GPT_IMPORT_GUIDE.md         # Exhaustive guide
└── ALBUM_ANALYSIS/                 # Motif data backing the cards
docs/
├── CODEX_BOOTUP_CHECKLIST.md       # Operational readiness
├── DEVELOPMENT_NODE.md             # Active development rituals
├── archive/                        # Archived FOLD docs
└── ...                             # Additional maps, lexicons, workflows
```

---

## Maintaining Alignment

- **Additions**: New instructions or quick starts should live beside the CODEX counterparts, not in archive directories.
- **Knowledge map**: Update `data/knowledge_map.yml` whenever files move or new cards are created.
- **Refinements**: Store GPT learnings in `research/CODEX/_refinements/` using the dated template.
- **API surface**: Extend the OpenAPI spec when adding endpoints; document auth in `config/`.

---

## Archive Policy

- Anything purely FOLD-era (ritual pipelines, old ChatGPT instructions, API auth guides) moves to:
  - `docs/archive/`
  - `config/archive/`
- References in README, quick starts, or STRUCTURE_OVERVIEW should only point to live CODEX material.
- When reviving an archived file, migrate it back into the active structure and note the change in `data/knowledge_map.yml`.

Keep CODEX first, keep provenance clear, and surface the cards everywhere the user enters the repo.
