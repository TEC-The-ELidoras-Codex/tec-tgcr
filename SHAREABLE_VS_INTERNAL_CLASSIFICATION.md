# Shareable vs. Internal — File Classification System

**Purpose**: Clearly mark which files are meant to be shared (team, GPT KB, public) vs. internal-only (backend, secrets, local dev).

---

## 🟢 SHAREABLE (Safe to Push, Upload to GPT, Share with Team)

### Category: Personas & Routing

- ✅ `data/personas/*.md` — All 9 persona definitions (canonical source)
- ✅ `PERSONAS_CANONICAL_MANIFEST.md` — Reference guide for personas
- ✅ `PERSONA_QUICK_REFERENCE.md` — Concise persona summary
- ✅ `PERSONAS_CONSOLIDATION_COMPLETE.md` — Provenance & registry
- ✅ `.github/copilot-instructions.md` — Master routing table

### Category: GPT Builder & Deployment

- ✅ `GPT_SYSTEM_PROMPT_READY.txt` — Copy-paste template for GPT instructions
- ✅ `GPT_ATTACHMENT_CHEAT_SHEET.md` — Quick reference for uploads
- ✅ `GPT_PERSONAS_ATTACHMENT_DECISION.md` — Which personas attach
- ✅ `GPT_DEPLOYMENT_READY.md` — Step-by-step deployment guide

### Category: Documentation & Theory

- ✅ `README.md` — Project entry point
- ✅ `docs/` folder (entire) — Public documentation, theory, guides
- ✅ `lore/narratives/` — Canonical lore & origin stories
- ✅ `research/CODEX/` — Research framework & theory

### Category: Code & Config (Backend-Safe)

- ✅ `src/tec_tgcr/` — Core Python code (no secrets embedded)
- ✅ `src/resonance_notebook/` — Notebook ingestion code
- ✅ `tests/` — Test suite (no hardcoded credentials)
- ✅ `pyproject.toml` — Dependencies & build config
- ✅ `Dockerfile`, `docker-compose.yml` — Container definitions

### Category: Brand & Visual Assets

- ✅ `data/digital_assets/` — Logos, glyphs, SVGs, public images
- ✅ `lore/brand/` — Brand guidelines, color palette
- ✅ `ai-workflow/output/figures/` — Published charts & visualizations

---

## 🔴 INTERNAL-ONLY (DO NOT Push, DO NOT Share, DO NOT Upload to GPT)

### Category: Secrets & Credentials

- ❌ `.env` — Local environment variables (API keys, tokens)
- ❌ `.env.local` — Personal overrides for .env
- ❌ `secrets-local/` — All local secret files
- ❌ `secrets/mapping.example.json` — Credential mapping templates
- ❌ Any file containing: `api_key`, `secret`, `token`, `password`, `credential`

### Category: Personal Notes & Brainstorms

- ❌ `ai-workflow/` notebooks (unless published/sanitized)
- ❌ `BRAIN_DUMP_*.md` — Raw personal notes
- ❌ `TODO_PERSONAL.md` — Personal task lists
- ❌ `scripts/blender/` — Local Blender automation (personal rig work)

### Category: Local Development Only

- ❌ `.venv/` — Local Python virtual environment
- ❌ `build/` — Local build artifacts
- ❌ `dist/` — Local distribution packages
- ❌ `__pycache__/`, `*.pyc` — Python bytecode
- ❌ `.pytest_cache/` — Pytest artifacts
- ❌ `.DS_Store`, `Thumbs.db` — OS artifacts

### Category: External/Third-Party Data

- ❌ `sources/external/` — External links, archives (reference only; don't commit raw data)
- ❌ `artifacts/luminai-archive/` — Archived versions (keep local, don't share)
- ❌ `specs/resonance_bundle_schema.json` — Internal spec (OK to share if sanitized; currently internal)

### Category: Deployment & Infrastructure (Backend)

- ❌ `scripts/blender/rig_lumina.py` — Local Blender work (personal)
- ❌ `scripts/secrets/` — Secret generation scripts
- ❌ `config/CODEX_API_SETUP.md` — API setup instructions (reference only)
- ❌ `config/API_KEYS_NEEDED.md` — List of required keys (reference only)

### Category: Archived / Deprecated

- ❌ Files with `_ARCHIVE`, `_OLD`, `_DEPRECATED`, `_BACKUP` in name
- ❌ `scripts/archive/` — Old deployment scripts

---

## 🟡 CONDITIONAL (Depends on Sanitization)

### Needs Sanitization Before Sharing

- ⚠️ `ai-workflow/TEC_Copilot365_Notebook.ipynb` — Check for embedded API keys before sharing
- ⚠️ `ai-workflow/lumina_cr_assistant.ipynb` — Sanitize before upload
- ⚠️ `scripts/generate_env_from_bitwarden.sh` — Shows structure; verify no secrets embedded
- ⚠️ `config/gpt-actions-research.json` — Verify no embedded keys
- ⚠️ `apps/wordpress/` — Check plugin code for hardcoded credentials
- ⚠️ `apps/resonance-player/` — Verify no API keys in React code

**Before uploading**: Run search for `api_key`, `secret`, `token`, `password` in code.

---

## 📋 File Naming Convention (Quick Visual Check)

Use these prefixes to make classification instant:

- **`SHAREABLE_*`** or **`PUBLIC_*`** — Explicitly shareable (e.g., `SHAREABLE_PROMPT.txt`)
- **`INTERNAL_*`** or **`BACKEND_*`** or **`LOCAL_*`** — Explicitly internal (e.g., `INTERNAL_API_SETUP.md`)
- **`DRAFT_*`** or **`TEMP_*`** — Temporary; review before sharing
- **`TEMPLATE_*`** — Example templates; check for embedded credentials
- **`ARCHIVE_*`** or **`_OLD`** — Deprecated; don't share

Examples already in repo:

- ✅ `GPT_SYSTEM_PROMPT_READY.txt` — "READY" signals shareable
- ✅ `PERSONAS_CANONICAL_MANIFEST.md` — Canonical = shareable
- ✅ `.env.example` — "example" signals it's a template, not real secrets
- ❌ `.env` — No prefix; naturally internal (in .gitignore)

---

## 📂 Folder-Level Rules

### ALWAYS SHAREABLE

```
data/personas/
docs/
lore/narratives/
research/CODEX/
research/ALBUM_ANALYSIS/
data/digital_assets/
```

### ALWAYS INTERNAL

```
secrets-local/
.venv/
__pycache__/
build/
dist/
.pytest_cache/
```

### CONDITIONAL (Review Before Sharing)

```
ai-workflow/
config/
apps/
scripts/
```

---

## 🚀 Pull & Build Workflow

### What to Pull (From GitHub)

```bash
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr
```

**Gets you**:

- ✅ All persona files (`data/personas/`)
- ✅ All documentation (`docs/`, `README.md`)
- ✅ All code (`src/`, `tests/`)
- ✅ GPT deployment guides (all `GPT_*.md` files)
- ✅ Lore & research (`lore/`, `research/`)

**Does NOT get you**:

- ❌ Secrets (`.env`, `secrets-local/`) — intentionally ignored by `.gitignore`
- ❌ Virtual environment (`.venv/`) — you'll rebuild
- ❌ Build artifacts (`build/`, `dist/`) — you'll regenerate

### What to Set Up Locally (First Time)

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows

# 2. Install dependencies
pip install -e .[dev]

# 3. Create local secrets (DO NOT commit)
cp .env.example .env.local
# Edit .env.local with your actual API keys (never push this)

# 4. Run tests
python -m pytest tests/ -q
```

### What Never Gets Pushed (Blocked by .gitignore)

```
.env
.env.local
secrets-local/
.venv/
__pycache__/
*.pyc
.pytest_cache/
build/
dist/
```

---

## ✅ Pre-Push Checklist

Before running `git push`:

- [ ] No `.env` or `.env.local` in staging
- [ ] No `secrets/` or `secrets-local/` in staging
- [ ] No `__pycache__/` or `.pytest_cache/` in staging
- [ ] No API keys in code comments (search for `api_key=`, `token=`, `secret=`)
- [ ] All personas in `data/personas/` are included
- [ ] All GPT guides (`GPT_*.md`) are included
- [ ] Documentation (`docs/`, `README.md`) is up-to-date

**Command to verify**:

```bash
git status  # Should show only shareable files
git diff --cached  # Review what you're pushing
```

---

## 🔐 Secrets Management (Backend Only)

### For Local Development

```
Create: .env.local (user-specific, never committed)
Template: .env.example (shows structure, no real values)
Location: Repo root
Access: `from dotenv import load_dotenv; load_dotenv(".env.local")`
```

### For Production (GitHub Actions, Deployment)

```
Use: GitHub Secrets (Settings → Secrets and variables)
Never embed in code
Reference in CI/CD workflows (.github/workflows/*.yml)
Access: os.environ["GITHUB_ACTIONS_SECRET_NAME"]
```

### For Team Sharing

```
Use: Bitwarden / 1Password / LastPass (never Git)
Sync: scripts/secrets/generate_env_from_bitwarden.sh (if needed)
Document: which secrets are required (in SETUP guide, not the values)
```

---

## 📊 Quick Reference Table

| Category | Location | Shareable? | Action |
|----------|----------|-----------|--------|
| Personas | `data/personas/*.md` | ✅ | Push & share |
| Documentation | `docs/` | ✅ | Push & share |
| GPT Guides | `GPT_*.md` | ✅ | Push & upload to KB |
| Code | `src/` | ✅ | Push (verify no secrets) |
| Secrets | `.env.local`, `secrets-local/` | ❌ | Keep local, never push |
| Notebooks | `ai-workflow/*.ipynb` | ⚠️ | Sanitize before sharing |
| Lore | `lore/` | ✅ | Push & share |
| Research | `research/CODEX/` | ✅ | Push & share |
| Config | `config/` | ⚠️ | Share templates, never real keys |
| Archives | `artifacts/`, `scripts/archive/` | ❌ | Keep local |

---

## 🎯 Use This Document To

1. **Before you push**: Check if your files belong in SHAREABLE or INTERNAL
2. **When onboarding**: Tell new team members what to `.gitignore`
3. **Before GPT upload**: Verify files are from SHAREABLE category
4. **During code review**: Flag INTERNAL files accidentally staged
5. **For documentation**: Reference this as the authoritative classification

---

**Location**: `/home/tec_tgcr/tec-tgcr/SHAREABLE_VS_INTERNAL_CLASSIFICATION.md`

**Referenced by**: `.gitignore`, `PULL_AND_BUILD_GUIDE.md`, deployment checklists
