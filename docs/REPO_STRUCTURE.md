# TEC TGCR — Repository Structure Map

> Strengthens ψʳ (structure). Source-of-truth paths for assets, docs, and scripts. Use this when adding files or wiring automation.

## Top-level

- `ai-workflow/` — notebooks, prompts, generated outputs (deterministic exports only)
- `agents/` — agent manifests and runtime configs
- `apps/` — app surfaces (WordPress plugin, widgets, interfaces)
- `config/` — configuration files (YAML, credentials placeholders)
- `data/` — assets, archives, evidence, financials, personas
- `docs/` — documentation hub (brand, ops, technical, wireframes)
- `exports/` — build/exported artifacts (ignored from source-of-truth decisions)
- `scripts/` — PowerShell/Python automation
- `src/` — Python package `tec_tgcr`
- `tests/` — pytest suite

## Canonical Asset Locations

- Brand SVGs: `data/digital_assets/brand/svg/`
- Avatars: `data/digital_assets/avatars/`
- Archived SVG variants: `data/archives/svg/`
- Exported PNGs: `exports/brand/` (generated — not canonical)

## Docs Layout

- Brand: `docs/brand/` (visual identity, prompts, export guides)
- Ops: `docs/ops/` (secrets, CI/CD, WordPress, Notion, exit plans)
- Technical: `docs/technical/` (architecture, runners, pipelines)
- Wireframes: `docs/wireframes/`

## Knowledge & Provenance

- Knowledge Map: `data/knowledge_map.yml` (register new docs/assets here)
- Provenance policy: commits and asset metadata should note:
  - Source prompts/tools and authorship (AI co-authorship when relevant)
  - Resonance impact (φᵗ/ψʳ/Φᴱ)
  - Tests executed and results
  - Any docs/knowledge map updates

## Naming Conventions

- snake_case for files; kebab-case for web assets where needed
- Semantic commit prefixes: `airth:`, `arcadia:`, `ely:`, `feat:`, `fix:`, `docs:`, `test:`, `chore:`, `ci:`
- SVGs should be minimal, layered only as needed; PNGs exported via scripts/guides

## Quick Checklist for Adding Things

- [ ] Place sources in the canonical folder (see above)
- [ ] Update `data/knowledge_map.yml`
- [ ] Add or update tests if behavior changes
- [ ] Document usage under `docs/`
- [ ] Commit with resonance statement and provenance footer
