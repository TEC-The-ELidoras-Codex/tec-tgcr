# Repository Organization Guide — TGCR Agent Stack

**Purpose**: Define where files live in the TEC/TGCR repository based on type, purpose, and TGCR philosophy.

**Principle**: *Contextual coherence* — every file location strengthens the resonance field between intention and discovery.

---

## Directory Structure & Conventions

### `/` (Root Level)

**Purpose**: Entry points, configuration, top-level manifests.

**What belongs here**:

- `README.md` — Repository overview (φ: attention gateway)
- `LICENSE` — Legal foundation
- `pyproject.toml` — Python package manifest (dependencies, metadata, build config)
- `tec_agent_runner.py` — CLI entry point (legacy; prefer `python -m tec_tgcr.cli`)
- `.gitignore`, `.gitattributes` — Git configuration
- `CHECKSUMS.md` — SHA256 fingerprint manifest (code integrity)

**What does NOT belong here**:

- Source code (`src/`)
- Documentation (`docs/`)
- Data files (`data/`)
- Scripts (`scripts/`)
- Build artifacts (`exports/`)

---

### `/src/tec_tgcr/`

**Purpose**: Core Python package — runtime modules, agent orchestration, tool wrappers, CLI.

**Structure**:

```
src/tec_tgcr/
├── __init__.py          # Package root, version export
├── cli.py               # Typer CLI commands (chat, export, analyze)
├── session.py           # Agent session management
├── tools/               # Tool wrappers (SharePoint, Blender, resonance evaluator)
│   ├── __init__.py
│   ├── sharepoint.py
│   └── resonance_evaluator.py
└── agents/              # Agent-specific modules (future: airth/, arcadia/, ely/)
```

**What belongs here**:

- Python modules imported by CLI or other packages
- Agent orchestration logic (session, context management)
- Tool wrappers with retry/caching/typed responses
- Reusable functions (not scripts)

**What does NOT belong here**:

- Standalone scripts (use `scripts/`)
- Documentation (use `docs/`)
- Configuration files (use `config/`)
- Notebooks (use `ai-workflow/`)

---

### `/scripts/`

**Purpose**: Runnable automation — PowerShell/Python scripts for build, deploy, analysis, export.

**Categories**:

1. **Build & Package**:
   - `pack_wp_plugin.ps1` — WordPress plugin ZIP with build-info.json
   - `pack_support_bundle.ps1` — Support bundle for audits
   - `bootstrap.ps1` — Environment setup (.venv, dependencies)

2. **Export & Generation**:
   - `export_compendium.py` — Generate TEC_TGCR_COMPENDIUM.docx
   - `export_readme_docx.py` — Convert README to DOCX
   - `generate_prompts.py` — Batch-generate AI prompts for consistency tests

3. **Azure & Cloud**:
   - `query_azure_resources.ps1` — Azure resource inventory with error handling
   - `start_sd_api.ps1` — Stable Diffusion API (local GPU)

4. **Blender & 3D**:
   - `blender_headless_idle.py` — Headless Blender idle animation script
   - `run_blender_idle.ps1` — PowerShell wrapper for Blender execution

5. **Utilities**:
   - `verify_checksums.ps1` — Verify CHECKSUMS.md against actual files
   - `sanitize_spotify_url.ps1` / `.py` — Clean Spotify embed URLs
   - `search_models.py` — Search Hugging Face models

**Naming conventions**:

- Use snake_case for Python: `export_compendium.py`
- Use PascalCase for PowerShell verbs: `Pack-WpPlugin.ps1` or lowercase with underscores `pack_wp_plugin.ps1` (prefer consistency)
- Prefix with action verb: `generate_`, `export_`, `pack_`, `verify_`, `run_`

**What does NOT belong here**:

- Reusable library code (use `src/tec_tgcr/`)
- Documentation (use `docs/`)
- Data files (use `data/`)

---

### `/docs/`

**Purpose**: Human-readable documentation — TGCR theory, brand doctrine, setup guides, operational runbooks.

**Categories**:

1. **Core Philosophy**:
   - `MACHINE_GODDESS.md` — Mythic foundation, TGCR cosmology
   - `LuminAI.md` — LuminAI character definition, personality, cadence
   - `ARCADIA.md` — Arcadia Clone agent specification
   - `FAERHEE.md` — Faerhee persona (future)

2. **Agent System**:
   - `AGENT_OVERVIEW.md` — Multi-agent architecture, responsibilities, handoff protocol
   - `PERSONAS.md` — All agent personas in one file
   - `agent-data-integration.md` — Knowledge map, manifest system

3. **Technical Setup**:
   - `GITHUB_SECRETS_SETUP.md` — GitHub Actions secrets configuration
   - `QUICK_SECRETS_FILL.md` — Pre-filled values for WordPress.com deployment
   - `LOCAL_SECRETS.md` — Local secrets handling (.env.local, .secrets/)
   - `M365_INTEGRATION.md` — Microsoft 365, Graph API, Dataverse, Fabric setup
   - `PHP-WPCLI-SETUP.md` — PHP/WP-CLI installation for local WordPress testing

4. **Operations & Deployment**:
   - `WORDPRESS-DEPLOYMENT-CHECKLIST.md` — Pre-flight checks for WP deployment
   - `WPCOM-DEPLOYMENT-FIX.md` — Troubleshooting WordPress.com deploy
   - `3D-PIPELINE.md` — Blender → GLB → WordPress embed workflow
   - `CROSS-DEVICE-UNITY.md` — Multi-device development setup

5. **Audits & Reviews**:
   - `COMPREHENSIVE_READINESS_AUDIT.md` — Full system audit (2025-10-15)
   - `REPOSITORY-AUDIT-2025-10-15.md` — Repository structure audit
   - `SIX_DIMENSION_VALIDATION_SUMMARY.md` — TGCR validation framework

6. **Examples & Templates**:
   - `examples/spinning_svg.html` — Interactive SVG with TGCR mapping
   - `templates/` — Document templates (future)

7. **Exports** (generated):
   - `exports/TEC_TGCR_COMPENDIUM.docx` — Master exportable doc

**Naming conventions**:

- Use CAPS-WITH-DASHES for major docs: `AGENT_OVERVIEW.md`
- Use lowercase-with-dashes for operational guides: `agent-data-integration.md`
- Prefix audits with date: `REPOSITORY-AUDIT-2025-10-15.md`
- Keep examples separate: `examples/`, `templates/`

**What does NOT belong here**:

- Source code (use `src/`)
- Scripts (use `scripts/`)
- Notebooks (use `ai-workflow/`)
- Raw data (use `data/`)

---

### `/data/`

**Purpose**: Structured data, knowledge maps, evidence, financial records, digital assets.

**Structure**:

```
data/
├── knowledge_map.yml          # TGCR knowledge pillars, doc references
├── digital_assets/            # Brand assets (logos, glyphs, 3D models)
│   └── (GLB, PNG, SVG files)
├── evidence/                  # Experimental results, citations
│   └── (CSV, JSON from tests)
├── financial/                 # Billing data, cost analysis
│   ├── cost-analysis.csv
│   └── m365-cost-analysis-2025-10-15.md
└── azure-inventory-*/         # Azure resource snapshots (timestamped)
    ├── resource-groups.json
    ├── all-resources.json
    └── cost-analysis.json
```

**Categories**:

1. **Configuration**:
   - `knowledge_map.yml` — Central knowledge graph for agents
   - Future: `brand_palette.yml`, `tgcr_constants.yml`

2. **Assets**:
   - `digital_assets/` — GLB models, SVG glyphs, PNG logos
   - Keep original sources (Blender .blend files, Illustrator .ai)

3. **Evidence**:
   - `evidence/` — Experimental data supporting TGCR claims
   - CSV/JSON from tests, measurements, resonance field analyses

4. **Financial**:
   - `financial/` — Billing disputes, cost analysis, subscription records
   - Sensitive files should be `.gitignore`d if they contain account numbers

5. **Azure Snapshots**:
   - `azure-inventory-{timestamp}/` — Timestamped resource inventories
   - Keep for audit trails, refund disputes, cost tracking

**What does NOT belong here**:

- Documentation (use `docs/`)
- Scripts (use `scripts/`)
- Secrets (use `.secrets/` and `.gitignore`)

---

### `/exports/`

**Purpose**: Generated artifacts for distribution — plugin ZIPs, support bundles, compendium docs.

**Structure**:

```
exports/
├── wp-plugin/                 # WordPress plugin ZIP artifacts
│   └── tec-tgcr-1.0.1.zip
└── support/                   # Support bundles (logs, evidence, billing disputes)
    └── YQAT-E6IU-BG7-PGB/
        ├── MICROSOFT-SUPPORT-BILLING-DISPUTE-YQAT-E6IU-BG7-PGB.md
        └── (attached evidence files)
```

**Categories**:

1. **WordPress Plugin**:
   - `wp-plugin/tec-tgcr-{version}.zip` — Packaged plugin with build-info.json
   - Version should match `tec-tgcr.php` header

2. **Support Bundles**:
   - `support/{ticket-id}/` — Organized by support request ID
   - Include narrative, evidence, screenshots, logs

3. **Documentation Exports**:
   - `docs/exports/TEC_TGCR_COMPENDIUM.docx` — Master doc (lives in docs/exports/ not root exports/)

**What does NOT belong here**:

- Source code (use `src/`)
- Raw data (use `data/`)
- Logs from local dev (use `.gitignore`d logs/ directory)

---

### `/apps/`

**Purpose**: Application frontends — WordPress plugin, React shells, SharePoint widgets, Blender addons.

**Structure**:

```
apps/
├── wordpress/
│   └── tec-tgcr/              # WordPress plugin source (deployed to WP.com)
│       ├── tec-tgcr.php
│       ├── includes/
│       ├── assets/
│       └── build-info.json    (generated by pack script)
├── luminai-interface/         # React/Next.js interface for LuminAI chat
├── resonance-player/          # Audio player with TGCR visualization
├── voice-imprint-studio/      # Voice profile capture tool
└── widgets-sharepoint/        # SharePoint web parts
```

**Categories**:

1. **WordPress Plugin**:
   - `wordpress/tec-tgcr/` — PHP plugin deployed to WordPress.com
   - Keep shortcodes, REST API, admin pages here

2. **React/Next.js Apps**:
   - `luminai-interface/` — Standalone Next.js app for LuminAI chat
   - `resonance-player/` — Audio player with interactive viz

3. **Specialized Tools**:
   - `voice-imprint-studio/` — Voice capture + analysis
   - `widgets-sharepoint/` — SharePoint Framework (SPFx) widgets

**What does NOT belong here**:

- Python scripts (use `scripts/`)
- Documentation (use `docs/`)
- Core TGCR logic (use `src/tec_tgcr/`)

---

### `/agents/`

**Purpose**: Agent-specific manifests, memory, tool loadouts.

**Structure**:

```
agents/
└── manifests/
    ├── airth_research_guard.json   # Airth agent manifest
    ├── arcadia_clone.json          # Arcadia agent manifest (future)
    └── ely_ops.json                # Ely agent manifest (future)
```

**What belongs here**:

- Agent manifests (JSON) with capabilities, tools, knowledge refs
- Agent memory files (YAML) if needed
- Agent-specific tool configs

**What does NOT belong here**:

- Agent *implementation* (use `src/tec_tgcr/agents/`)
- Global config (use `config/`)

---

### `/config/`

**Purpose**: Global runtime configuration — agent defaults, credentials schema, TGCR constants.

**Structure**:

```
config/
├── agent.yml                  # Default agent config (tone, knowledge refs)
└── tec-verified-credential.json   # Verifiable credential schema (future)
```

**What belongs here**:

- YAML/JSON config files loaded by `src/tec_tgcr/` at runtime
- Schema definitions, constants, default settings

**What does NOT belong here**:

- Secrets (use `.secrets/` and `.gitignore`)
- Agent manifests (use `agents/manifests/`)
- Data files (use `data/`)

---

### `/ai-workflow/`

**Purpose**: Jupyter notebooks, prompt stacks, experimental workflows, output snapshots.

**Structure**:

```
ai-workflow/
├── lumina_cr_assistant.ipynb  # LuminAI character refinement notebook
├── prompt_templates.py        # Python module for prompt generation
├── README.md                  # Notebook usage guide
└── output/                    # Generated outputs (prompts, samples)
    ├── all_prompts.json
    ├── luminai_blushing_1.txt
    └── ...
```

**What belongs here**:

- `.ipynb` notebooks for experiments, prompt testing, data analysis
- Python modules used BY notebooks (e.g., `prompt_templates.py`)
- `output/` for generated artifacts (snapshots, not version-controlled)

**What does NOT belong here**:

- Production code (use `src/`)
- Documentation (use `docs/`)
- Scripts meant to run standalone (use `scripts/`)

---

### `/tests/`

**Purpose**: pytest tests — unit tests, integration tests, conversational regression.

**Structure**:

```
tests/
├── test_agent.py              # Agent session tests
├── test_resonance_evaluator.py  # Resonance strength tests
└── test_spotify_url.py        # Utility function tests
```

**What belongs here**:

- `test_*.py` files with pytest fixtures
- Conversational regression fixtures (JSON snapshots)
- Mock data for tests

**What does NOT belong here**:

- Source code (use `src/`)
- Scripts (use `scripts/`)

---

### `/todo/`

**Purpose**: Task tracking, project management, manual todo lists.

**Structure**:

```
todo/
├── tasks.json                 # Structured task list (future: integrate with CLI)
├── todo.json                  # Legacy JSON todo
├── todo.md                    # Human-readable markdown
└── todo.txt                   # Plain text
```

**What belongs here**:

- Task lists in various formats
- Project milestones, sprint plans

**What does NOT belong here**:

- Code (use `src/`)
- Documentation (use `docs/`)

---

## File Movement Recommendations

### Misplaced Files (Current State)

1. **Root-level docs → `/docs/`**:
   - `LUMINAI-API-SETUP-GUIDE.md` → `docs/LUMINAI-API-SETUP-GUIDE.md`
   - `LuminAI-Character-Perfection-Plan.md` → `docs/LuminAI-Character-Perfection-Plan.md`
   - `LuminAI-Test-Plan.md` → `docs/LuminAI-Test-Plan.md`
   - `LUMINAI-VISUAL-WORKFLOW.md` → `docs/LUMINAI-VISUAL-WORKFLOW.md`

2. **Root-level YAML configs → `/config/`**:
   - `github-luminai-api.yaml` → `config/github-luminai-api.yaml`
   - `sharepoint-luminai-api.yaml` → `config/sharepoint-luminai-api.yaml`

3. **Support bundles → `/exports/support/`**:
   - Already correct: `exports/support/YQAT-E6IU-BG7-PGB/...`

4. **Data files**:
   - If any `.csv`, `.json` data files are in root, move to `data/`

5. **Scripts**:
   - All `.ps1`, `.py` scripts should be in `scripts/` (currently correct)

---

## Git Best Practices

### Use `git mv` for Tracked Files

When moving tracked files, use `git mv` to preserve history:

```powershell
git mv LUMINAI-API-SETUP-GUIDE.md docs/LUMINAI-API-SETUP-GUIDE.md
git mv github-luminai-api.yaml config/github-luminai-api.yaml
```

### Update References

After moving files, search for references and update:

```powershell
# Find references to old path
grep -r "LUMINAI-API-SETUP-GUIDE.md" . --exclude-dir=.git

# Update imports, links, paths in:
# - README.md
# - docs/*.md
# - data/knowledge_map.yml
# - config/agent.yml
```

### Commit Strategy

Group related moves in single commit:

```powershell
git mv LUMINAI-API-SETUP-GUIDE.md docs/
git mv LuminAI-Character-Perfection-Plan.md docs/
git mv LuminAI-Test-Plan.md docs/
git mv LUMINAI-VISUAL-WORKFLOW.md docs/
git commit -m "docs: Move LuminAI docs from root to docs/ (TGCR file org)"
```

---

## Automated Reorganization Script

See `scripts/reorganize_repo.ps1` (to be created) for automated file movement with:

- Confirmation prompts
- Reference updating
- Git history preservation
- Rollback support

---

## Summary: Where Files Live

| **File Type** | **Location** | **Example** |
|---------------|--------------|-------------|
| Python package source | `src/tec_tgcr/` | `cli.py`, `session.py` |
| Runnable scripts | `scripts/` | `export_compendium.py` |
| Documentation | `docs/` | `AGENT_OVERVIEW.md` |
| Data files | `data/` | `knowledge_map.yml`, `cost-analysis.csv` |
| Build artifacts | `exports/` | `wp-plugin/tec-tgcr-1.0.1.zip` |
| App frontends | `apps/` | `wordpress/tec-tgcr/` |
| Agent manifests | `agents/manifests/` | `airth_research_guard.json` |
| Config files | `config/` | `agent.yml` |
| Notebooks | `ai-workflow/` | `lumina_cr_assistant.ipynb` |
| Tests | `tests/` | `test_agent.py` |
| Task tracking | `todo/` | `tasks.json` |

---

**Resonance Principle**: *Every file location is a contextual anchor. When placement is intentional, discovery becomes inevitable.*

---

*Last updated: 2025-10-18 by TGCR Agent Stack*
