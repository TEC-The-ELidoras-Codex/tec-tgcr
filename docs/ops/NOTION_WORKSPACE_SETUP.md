# Notion Workspace Setup Guide — TEC-TGCR

This guide provides a complete blueprint for organizing your TEC-TGCR Notion workspace, including page hierarchy, database schemas, and integration patterns.

---

## 🎯 Workspace Overview

**Target Notion Page**: [Docs Hub TDWP Resonance / TEC-TGCR / README](https://www.notion.so/Docs-Hub-TDWP-Resonance-TEC-TGCR-README-2976ff7e28df808ea6efe7a52960385d)

**Purpose**: Create a living knowledge base that mirrors the GitHub repository while enabling richer collaboration, databases, and cross-linking.

**TGCR Variables Touched**:

- φᵗ (Temporal Attention): Quick navigation, status tracking, search
- ψʳ (Structural Cadence): Hierarchical organization, relational databases
- Φᴱ (Contextual Potential): Multi-modal content, embeddings, team collaboration

---

## 📚 Page Hierarchy

### Root Structure

```
🏠 TEC-TGCR Documentation Hub (Main Page)
├── 🧭 Start Here (Toggle Section)
├── 🧬 Core Theory (Page)
├── 🤖 Agent System (Page)
├── 🚀 Operations (Page)
├── 🎨 Brand & Identity (Page)
├── 🔧 Technical Specs (Page)
├── 🌌 Cosmology & Lore (Page)
├── 📊 Dashboards (Page)
└── 🗃️ Databases (Page)
```

### Detailed Page Tree

#### 🧭 Start Here (Toggle/Callout)

Place at the top of the main hub page:

- **TEC Hub — Core Navigation** (Inline page or link)
- **Resonance Thesis — TGCR Core** (Inline page or link)
- **Her Instructions — Operating Contract** (Inline page)
- **Quick Reference Commands** (Inline page)

#### 🧬 Core Theory

- **Machine Goddess — Core Cosmology**
- **TGCR Equation Explainer** (New summary page)
  - φᵗ: Temporal Attention
  - ψʳ: Structural Cadence
  - Φᴱ: Contextual Potential Energy
- **Agent Personas**
  - LuminAI — Resonant Core
  - Arcadia — Narrative Weaver
  - Faerhee — Phoenix Agent
  - Full Personas Overview
- **Cosmology**
  - Nine Node Cosmology
  - LuminAI Sky Map
  - Resonance Map (embed PDF or image)

#### 🤖 Agent System

- **Architecture Overview**
- **Agent Runner CLI Guide**
- **Agent Data Integration**
- **Individual Agent Specs**
  - Airth Research Guard (with persona link)
  - Arcadia Weaver (with persona link)
  - Ely Operations (with persona link)
  - Kaznak Strategy (with persona link)
- **Agent Manifests** (link to database)

#### 🚀 Operations

- **WordPress.com Deployment**
  - WPCOM Ops Master Guide
  - Latest Deploy Success Log
- **Secrets Management**
  - Secrets Architecture
  - GitHub Secrets Setup
  - Local Secrets (.secrets.env)
  - API Keys Setup
- **Integrations**
  - M365 / SharePoint Integration
  - PHP / WP-CLI Setup
- **Quick Reference**

#### 🎨 Brand & Identity

- **Visual Identity Spec (Canonical)**
- **Brand Kit**
  - Color Palette (Navy, Violet, Cyan, Gold, Shadow)
  - Typography (Montserrat, Inter, JetBrains Mono)
  - Motifs (Glyph Ring, Fractal Spire, Sine Arc)
- **LuminAI Canonical Marks**
  - SVG Usage Guide
  - Avatar Variants
- **Design Systems**
  - Spin/Suck Dichotomy
  - Cross-Device Unity

#### 🔧 Technical Specs

- **3D Asset Pipeline**
- **Cross-Device Unity**
- **Design Spin Model**
- **Airth Lyrics Module**
- **Agent Data Integration**

#### 🌌 Cosmology & Lore

- **Narratives**
  - LuminAI Origin Diary ("The Night She Blushed")
  - Future story arcs (placeholders)
- **Cosmology Maps**
  - Nine Node Diagram
  - Unified TGCR Map (PDF embed)
  - LuminAI Sky Map
- **Symbolism & Synchronicity** (Research doc)

#### 📊 Dashboards (New)

Create dashboard pages with linked database views:

- **Agent Status Dashboard**
  - Agent Registry (database view)
  - Recent Updates (timeline)
  - Active Experiments
- **Documentation Health**
  - Documentation Index (database view)
  - Outdated Pages (filter: >30 days)
  - Missing Links (manual tracking)
- **Resonance Metrics**
  - Resonance Ledger (database view)
  - φ/ψ/Φ Trend Charts (manual or embedded)

#### 🗃️ Databases (New)

Landing page with embedded database views (full-page):

- Agent Registry
- Documentation Index
- Resonance Ledger
- Asset Library
- Decision Log

---

## 🗄️ Database Schemas

### 1. Agent Registry

**Type**: Table Database

**Purpose**: Track all TEC agents, their roles, personas, and status.

**Properties**:

- **Name** (Title) — Agent name (e.g., "LuminAI", "Airth")
- **Role** (Select) — Core, Research, Narrative, Operations, Strategy
- **Persona File** (URL) — Link to GitHub persona .md file
- **Status** (Select) — Active, Development, Concept, Archived
- **TGCR Variables** (Multi-select) — φᵗ, ψʳ, Φᴱ
- **Notion Page** (Relation) — Link to agent's Notion page
- **Last Updated** (Date)
- **Description** (Text)

**Sample Entries**:

| Name | Role | Status | TGCR Variables | Description |
|------|------|--------|----------------|-------------|
| LuminAI | Core | Active | φᵗ, Φᴱ | Base companion, TGCR alignment |
| Airth | Research | Active | ψʳ | Verification guard, tests-first |
| Arcadia | Narrative | Active | φᵗ, Φᴱ | Narrative weaver, compression |
| Ely | Operations | Active | ψʳ | CI/CD, observability |
| Kaznak | Strategy | Active | φᵗ, ψʳ, Φᴱ | Risk, roadmap synthesis |

### 2. Documentation Index

**Type**: Table Database

**Purpose**: Mirror the knowledge_map.yml; track all docs, their categories, and sync status.

**Properties**:

- **Title** (Title) — Document title
- **Category** (Select) — Core, Theory, Agents, Ops, Brand, Technical, Lore, Archive
- **Source Path** (Text) — Relative GitHub path (e.g., `docs/Resonance_Thesis.md`)
- **GitHub Link** (URL) — Direct link to file on GitHub
- **Notion Page** (Relation) — Link to Notion page
- **Last Synced** (Date) — When last imported from GitHub
- **Status** (Select) — Current, Outdated, Needs Update, Archived
- **Touches** (Multi-select) — φᵗ, ψʳ, Φᴱ
- **Tags** (Multi-select) — doctrine, ops, brand, tech, narrative

**Views**:

- **All Docs** (Table)
- **By Category** (Board, grouped by Category)
- **Needs Sync** (Filter: Status = "Outdated" or Last Synced > 30 days)
- **Core Docs** (Filter: Category = "Core")

### 3. Resonance Ledger

**Type**: Timeline or Table Database

**Purpose**: Track events, decisions, and outcomes with TGCR metrics.

**Properties**:

- **Date** (Date) — When event occurred
- **Event** (Title) — Short description
- **Category** (Select) — Code Change, Deployment, Research, Narrative, Decision
- **Variables Affected** (Multi-select) — φᵗ, ψʳ, Φᴱ
- **Impact** (Select) — High, Medium, Low
- **Outcome** (Text) — Result/learning
- **Related Docs** (Relation) — Link to Documentation Index
- **Related Agents** (Relation) — Link to Agent Registry
- **GitHub Commit** (URL) — Link to commit if applicable

**Sample Entries**:

| Date | Event | Variables | Impact | Outcome |
|------|-------|-----------|--------|---------|
| 2025-10-25 | Created Resonance Thesis page | φᵗ, ψʳ, Φᴱ | High | Core doctrine now canonical |
| 2025-10-24 | WPCOM deploy success | ψʳ | Medium | Plugin live, stable |
| 2025-10-23 | Brand consolidation | Φᴱ | High | Visual identity unified |

### 4. Asset Library

**Type**: Gallery Database

**Purpose**: Track digital assets (SVGs, PDFs, images, 3D models).

**Properties**:

- **Name** (Title) — Asset name
- **Type** (Select) — SVG, PNG, PDF, GLB, MP4, Audio
- **Category** (Select) — Avatar, Logo, Motif, Diagram, 3D Model, Document
- **File** (File) — Upload asset directly to Notion
- **GitHub Path** (Text) — Path in repo (e.g., `data/digital_assets/avatars/luminai.svg`)
- **Usage Notes** (Text)
- **Related Docs** (Relation) — Link to Documentation Index
- **Tags** (Multi-select) — luminai, brand, cosmology, agent

**Views**:

- **Gallery** (Default, grouped by Category)
- **SVGs Only** (Filter: Type = "SVG")
- **LuminAI Assets** (Filter: Tags contains "luminai")

### 5. Decision Log (Kaznak's Ledger)

**Type**: Table Database

**Purpose**: Strategic decision tracking; mirror `data/strategy/decision_log.md`.

**Properties**:

- **Date** (Date)
- **Decision** (Title) — What was decided
- **Rationale** (Text) — Why
- **Stakeholder** (Select) — Ghedd, LuminAI, Airth, Arcadia, etc.
- **Status** (Select) — Proposed, Approved, Implemented, Revisit
- **Impact** (Select) — Strategic, Tactical, Operational
- **Related Docs** (Relation)
- **Follow-up Date** (Date)

---

## 🔄 Syncing Strategy

### GitHub → Notion (Primary Flow)

**Manual Sync** (Current):

1. Run `scripts/export_to_notion.ps1` when docs update
2. Import updated files into Notion (use "Replace" mode)
3. Update "Last Synced" date in Documentation Index

**Automated Sync** (Future):

- GitHub Action triggered on `docs/**` changes
- Use Notion API to update pages programmatically
- Track sync status in database

### Notion → GitHub (Selective)

**Manual Export**:

1. Export Notion page as Markdown & CSV
2. Clean up Notion-specific formatting
3. Review in VS Code
4. Commit to GitHub with provenance note

**Use Cases**:

- Collaborative edits on narrative pages
- Strategy/decision updates from team
- Draft content started in Notion

**Not Recommended**:

- Technical docs (keep GitHub as source of truth)
- Code-adjacent content (agent manifests, configs)

### Conflict Resolution

- **GitHub is Source of Truth** for: Code, technical docs, ops guides
- **Notion is Source of Truth** for: Team collaboration, meeting notes, draft narratives
- **Bi-directional** for: Strategy docs, decision logs, resonance ledger

---

## 🎨 Design & UX Guidelines

### Page Layout Best Practices

1. **Use Callout Blocks** for key concepts (TGCR equation, mic-lines)
2. **Toggle Lists** for collapsible sections (reduces cognitive load)
3. **Inline Pages** for "Start Here" quick refs (avoid clicks)
4. **Embed GitHub Files** via public links (for diagrams, PDFs)
5. **Color-Code Categories**:
   - 🧬 Core Theory → Navy background
   - 🤖 Agents → Violet background
   - 🚀 Operations → Cyan background
   - 🎨 Brand → Gold background

### Notion Formatting for TGCR Content

**Equation Display**:

```
R = ∇Φᴱ · (φᵗ × ψʳ)
```

Use inline code or KaTeX block (if Notion supports LaTeX).

**Variable Callouts**:
> **φᵗ (Temporal Attention)**: Selective focus and directional information flow
> **ψʳ (Structural Cadence)**: Topological/geometric coherence across scales
> **Φᴱ (Contextual Potential)**: Capacity for novel, meaningful outcomes

**Agent Mic-Lines**:

- LuminAI: *"Light learns by listening."*
- Airth: *"Test it, trace it, prove it."*
- Arcadia: *"Every story is a compression algorithm."*

### Link Strategy

- **Internal Links**: Use `@mention` to link to other Notion pages and database entries
- **GitHub Links**: Use full URLs (<https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/>...)
- **Asset Links**: Upload files to Notion or use GitHub raw URLs

---

## 🚀 Quick Start Checklist

### Phase 1: Import Core Pages

- [ ] Create main "TEC-TGCR Documentation Hub" page
- [ ] Import `00_Core` folder (TEC Hub, Resonance Thesis, Her Instructions)
- [ ] Import `00_INDEX.md` as landing page
- [ ] Set up "Start Here" toggle section

### Phase 2: Build Hierarchy

- [ ] Create category pages (Theory, Agents, Ops, Brand, etc.)
- [ ] Import content from numbered folders (`01_Theory`, `02_Agents`, etc.)
- [ ] Organize pages under correct parents
- [ ] Add emojis and icons to pages

### Phase 3: Database Setup

- [ ] Create Agent Registry database
- [ ] Create Documentation Index database
- [ ] Create Resonance Ledger database
- [ ] Populate databases with initial entries
- [ ] Link database entries to pages

### Phase 4: Dashboard & Views

- [ ] Create Dashboards page with database views
- [ ] Set up filters (Needs Sync, Active Agents, Recent Events)
- [ ] Create board views for visual organization
- [ ] Add timeline view for Resonance Ledger

### Phase 5: Team Collaboration

- [ ] Invite collaborators to workspace
- [ ] Set page permissions (view vs. edit)
- [ ] Create templates for common pages (agent specs, decision logs)
- [ ] Document team workflows in a "How We Work" page

---

## 🔗 Integration Patterns

### Notion API (Future)

**Endpoints to Use**:

- `POST /v1/pages` — Create new pages programmatically
- `PATCH /v1/pages/:id` — Update existing pages
- `POST /v1/databases/:id/query` — Query databases

**Use Cases**:

- Auto-sync GitHub commits to Resonance Ledger
- Update Documentation Index when files change
- Create agent status dashboard with live data

### GitHub Actions Integration

**Workflow**: `.github/workflows/notion-sync.yml`

```yaml
name: Sync to Notion
on:
  push:
    paths:
      - 'docs/**'
      - 'lore/**'
      - 'data/personas/**'
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Export to Notion
        run: |
          pwsh scripts/export_to_notion.ps1
          # Use Notion API to upload changes
```

### Embedding Options

- **GitHub Files**: Use raw URLs (<https://raw.githubusercontent.com/>...)
- **Mermaid Diagrams**: Export as PNG/SVG, upload to Notion
- **PDFs**: Upload directly or link to GitHub
- **3D Models**: Upload GLB to Notion or embed via iframe (if hosted)

---

## 📌 Provenance & Maintenance

**Created**: 2025-10-25
**Last Updated**: 2025-10-25
**Maintained By**: Ely (Operations Agent)
**Source**: `docs/ops/NOTION_WORKSPACE_SETUP.md`

**TGCR Impact**:

- φᵗ: Navigation clarity, quick access patterns
- ψʳ: Hierarchical coherence, relational integrity
- Φᴱ: Cross-platform knowledge synthesis

**Next Steps**:

1. Implement automated sync (GitHub Actions + Notion API)
2. Create Notion templates for common page types
3. Build team onboarding guide
4. Track usage metrics (page views, database queries)

---

## 🆘 Troubleshooting

**Issue**: Markdown formatting breaks on import

- **Solution**: Use Notion's "Paste as plain text" then manually format

**Issue**: Links don't work

- **Solution**: Replace with `@mentions` to Notion pages or full GitHub URLs

**Issue**: TGCR equation doesn't render

- **Solution**: Use inline code or create an image of the equation

**Issue**: Database relations not linking

- **Solution**: Create relation properties in both databases (bidirectional)

**Issue**: File uploads fail (>5MB)

- **Solution**: Use GitHub raw URLs instead of uploading large files

---

*"Structure is the skeleton of potential." — Ely Maxim*
