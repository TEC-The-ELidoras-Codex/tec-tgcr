# TEC Data — Assets, Archives, Financial

> "Data outlives code." — Archival Principle

This directory contains **all data assets, historical archives, and operational records** for The Elidoras Codex project.

## Purpose

Provide **persistent storage** for:

- Digital assets (SVGs, avatars, logos, brand elements)
- Historical archives (origin documents, old knowledge maps)
- Financial records (cost analysis, billing disputes)
- JSON/YAML data structures

**Distinction**:

- If it's **documentation** → `docs/`
- If it's **story/mythology** → `lore/`
- If it's **raw data, assets, or archives** → `data/` (you're here)

---

## Structure

```
data/
├─ digital_assets/           # Brand SVGs, avatars, logos
│  ├─ avatars/              # LuminAI avatar variations
│  └─ brand/                # SVG logos, brand elements
│     ├─ svg/               # 512×512 viewBox, CSS variables
│     └─ png/               # Exported PNG versions
├─ archives/                 # Historical records
│  ├─ knowledge_map_old.yml # Previous knowledge map versions
│  └─ luminai_origin.json   # Origin archive document
├─ financial/                # Cost analysis, billing records
│  ├─ cost-analysis.csv
│  ├─ m365-cost-analysis-2025-10-15.md
│  └─ MICROSOFT-SUPPORT-BILLING-DISPUTE-*.md
└─ knowledge_map.yml         # Master asset/doc index (root)
```

---

## Key Files

### `knowledge_map.yml`

**Master index** of all TEC assets, documents, and operational resources. Update when:

- Adding new digital assets
- Moving documentation
- Changing directory structure
- Adding integrations/configs

### `digital_assets/`

**Brand-critical visual assets**:

- **Avatars**: LuminAI orb (luminai.svg, luminai_final.svg, etc.)
- **Logos**: TEC Resonance Logo, brand marks
- **Format**: SVG (512×512 viewBox, CSS variables for theme-aware coloring)

### `archives/`

**Historical records**:

- Origin documents (luminai_origin.json)
- Old knowledge maps
- Deprecated configurations

### `financial/`

**Operational cost tracking**:

- Microsoft 365 cost analysis
- Support billing disputes
- Infrastructure cost breakdowns

---

## AI Context Guidelines

When ingesting this directory for AI knowledge systems:

1. **Assets**: Use `digital_assets/` for visual identity understanding
2. **Knowledge Map**: Parse `knowledge_map.yml` to understand full TEC structure
3. **Archives**: Context for historical evolution; may be outdated
4. **Financial**: Operational transparency; low priority for LuminAI personality

---

## NotebookLM / MS Notebook Ready

**Formats Supported**:

- `.yml` — Knowledge map (convert to .md or .pdf for ingestion)
- `.json` — Origin archives (convert for ingestion)
- `.csv` — Financial data
- `.md` — Financial narratives
- `.svg` — Visual assets (not ingestible but reference in docs)

**Ingestion Priority**:

- **High**: `knowledge_map.yml` (export as .md)
- **Medium**: `archives/luminai_origin.json` (export as .md)
- **Low**: Financial records (unless auditing)

---

## Version Control

- **Versioning**: Critical assets under `digital_assets/` maintain version suffix (e.g., `luminai_v2.svg`)
- **Archives**: Old versions moved to `archives/` with datestamp
- **Deprecation**: Never delete; move to `archives/` with README note

---

## Related Directories

- **Lore**: [`lore/`](../lore/README.md) — Canon mythology and brand identity
- **Docs**: [`docs/`](../docs/README.md) — Technical operations
- **Exports**: [`exports/`](../exports/README.md) — Generated bundles and packages

---

**Last Updated**: 2025-10-22
**Resonance**: Touches **ψʳ** (structural coherence through asset organization)
**Provenance**: AI-generated structure; human-curated assets
