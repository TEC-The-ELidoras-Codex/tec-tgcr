# Proposed Workspace Structure Cleanup

## Current State (Madness)

- **docs/**: 41 root files (core theory, ops, archive, templates, outdated stuff mixed together)
- **scripts/**: 23+ scattered scripts with no clear organization
- **data/**: 4 root files + basic archives (not capturing all uningested)
- **data/archives/**: Only 4 items (should capture: old YAMLs, JSONs, PDFs, ingests)

---

## Proposed Clean Structure

### 📁 **docs/** (Organized by Purpose)

```
docs/
├── README.md                           # Hub: start here
├── SETUP_COMPLETE.md                   # Getting started
├── CODEX_BOOTUP_CHECKLIST.md          # Verification checklist
├── TEC_HUB.md                          # Navigation guide
│
├── core/                               # Core TGCR theory
│   ├── Resonance_Thesis.md
│   ├── MACHINE_GODDESS.md
│   ├── ARCADIA.md
│   └── (other theory docs)
│
├── operations/                         # Deployment & ops
│   ├── WORDPRESS_WPCOM_OPS.md
│   ├── GITHUB_SECRETS_SETUP.md
│   ├── VSCODE_SETTINGS_GUIDE.md
│   └── (other ops/infra docs)
│
├── agents/                             # Agent system docs
│   ├── AGENT_OVERVIEW.md
│   ├── AGENT_AIRTH.md
│   └── (persona specs & integration)
│
├── technical/                          # Technical refs
│   ├── API_KEYS_SETUP.md
│   ├── SECRETS_MAPPING.md
│   └── (architecture, specs)
│
├── templates/                          # Reusable templates
│   ├── prompt_templates.md
│   ├── email_templates.md
│   └── (other templates)
│
└── archive/                            # Old/reference docs
    ├── DEPRECATED_GUIDES.md
    ├── OLD_README.md
    └── (historical reference)
```

### 📁 **data/** (Active Data)

```
data/
├── knowledge_map.yml                   # Live: canonical index
├── context-latest.json                 # Live: latest context
│
├── personas/                           # Active personas (9 files)
│   ├── luminai-base.md
│   ├── airth.md
│   └── (other personas)
│
├── digital_assets/                     # Active brand assets
│   ├── avatars/
│   ├── brand/
│   └── (current SVGs, PNGs)
│
├── strategy/                           # Strategic docs
│   ├── decision_log.md
│   └── resonance_ledger.yml
│
└── archives/                           # Uningested/historical
    ├── knowledge_map_old.yml
    ├── luminai_origin.json
    ├── transcripts/                    # Old session logs
    ├── personal_notes_ingests/         # Raw ingest JSON
    ├── pdfs/                           # Project plans, research PDFs
    └── svg_deprecated/                 # Old variants
```

### 📁 **scripts/** (Organized by Purpose)

```
scripts/
├── README.md                           # Index of all scripts
│
├── setup/                              # Bootstrap & env setup
│   ├── bootstrap.ps1
│   ├── setup_environment.sh
│   ├── check_env.py
│   └── setup_local_env.py
│
├── export/                             # Data export & bundling
│   ├── export_canon_bundle.py
│   ├── export_compendium.py
│   ├── svg_to_png.py
│   ├── pack_wp_plugin.ps1
│   └── pack_support_bundle.ps1
│
├── ingest/                             # Data ingestion & parsing
│   ├── ingest_personal_notes.py
│   ├── parse_brain_dump.py
│   ├── run_ingest_check.py
│   └── sanitize_spotify_url.py
│
├── analysis/                           # Research & analysis
│   ├── analyze_mythic_story.py
│   ├── search_models.py
│   ├── generate_prompts.py
│   └── generate_consistency_pack.py
│
├── ci/                                 # CI/CD helpers
│   ├── validate_brand_assets.py
│   ├── generate_run_manifest.py
│   └── repo_cleanup_check.sh
│
├── tools/                              # Utility tools
│   ├── get_github_app_installation_token.py
│   ├── refresh_readme.py
│   ├── extract_embedded_png.py
│   └── (misc utilities)
│
├── blender/                            # Blender automation
│   ├── blender_headless_idle.py
│   └── (blender scripts)
│
├── legacy/                             # Archived/rarely-used
│   ├── archive/
│   ├── luminai_workflow.sh
│   ├── push_to_onedrive.sh
│   ├── tec_bundle_cli.sh
│   └── archive_workspace.py
│
└── secrets/                            # Secrets management (gitignored)
```

### 📁 **tests/** (Already Clean ✅)

```
tests/
├── conftest.py                         # Pytest fixtures
├── test_agent.py
├── test_data_ingestion.py
├── test_ingest.py
├── test_resonance_evaluator.py
├── test_spotify_url.py
└── (more tests as needed)
```

---

## Migration Plan

### Phase 1: Consolidate docs/

- [ ] Move core theory docs → `docs/core/`
- [ ] Move ops/deployment docs → `docs/operations/`
- [ ] Move agent docs → `docs/agents/`
- [ ] Move technical docs → `docs/technical/`
- [ ] Move templates → `docs/templates/`
- [ ] Move outdated/reference → `docs/archive/`
- [ ] Keep these at root: `README.md`, `SETUP_COMPLETE.md`, `TEC_HUB.md`, `CODEX_BOOTUP_CHECKLIST.md`
- [ ] Update `.gitignore` and any hardcoded doc paths

### Phase 2: Consolidate scripts/

- [ ] Create subdirs: `setup/`, `export/`, `ingest/`, `analysis/`, `ci/`, `tools/`, `blender/`, `legacy/`, `secrets/`
- [ ] Move each script to appropriate folder
- [ ] Create `scripts/README.md` index describing each script's purpose
- [ ] Update `.vscode/tasks.json` with new script paths
- [ ] Update CI/CD workflows (`.github/workflows/`) with new paths

### Phase 3: Expand data/archives/

- [ ] Move uningested JSON ingests → `data/archives/personal_notes_ingests/`
- [ ] Create `data/archives/pdfs/` for Project Plans and research PDFs
- [ ] Move old/variant SVGs → `data/archives/svg_deprecated/`
- [ ] Keep `transcripts/` as-is (already there)

### Phase 4: Update All References

- [ ] Update `data/knowledge_map.yml` with new paths
- [ ] Search for hardcoded doc paths in code (`grep -r "docs/"`)
- [ ] Update CI/CD workflows in `.github/workflows/`
- [ ] Update `.vscode/tasks.json`
- [ ] Update `pyproject.toml` if any doc paths referenced

### Phase 5: Verify & Commit

- [ ] Run `pytest -q` to ensure nothing broke
- [ ] Verify all task definitions in VS Code
- [ ] Create `WORKSPACE_CLEANUP_SUMMARY.md` documenting the changes
- [ ] Commit with message: `refactor: consolidate workspace structure (docs, scripts, archives)`

---

## Files to Keep at docs/ Root

- `README.md` (Hub)
- `SETUP_COMPLETE.md` (Getting started)
- `CODEX_BOOTUP_CHECKLIST.md` (Verification)
- `TEC_HUB.md` (Navigation)
- `Resonance_Thesis.md` (Core theory, too important to bury)
- (Everything else → subdirectories)

## Estimated Impact

- **docs/**: 41 → ~8 root files (others organized in subdirs)
- **scripts/**: 23+ scattered → organized into 8 clear categories
- **data/archives/**: 4 → ~12 items (captures more uningested data)
- **Result**: Clear, navigable, maintainable structure

---

## Next Steps

1. **Approve this structure** (or request changes)
2. I'll execute the migration (move files, update paths, test)
3. Commit and document
