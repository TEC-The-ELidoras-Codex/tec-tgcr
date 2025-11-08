# Pull & Build Guide — Fresh Clone Setup

**Purpose**: Step-by-step for cloning the repo, building locally, and understanding what's shareable vs. internal.

**Time**: ~10 minutes on first clone

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr
```

**You now have**:

- ✅ All persona files (`data/personas/`)
- ✅ All documentation (`docs/`, `README.md`, `lore/`)
- ✅ All code (`src/`, `tests/`)
- ✅ All GPT deployment guides (`GPT_*.md`)
- ✅ Research & theory (`research/CODEX/`)

**You do NOT have** (intentionally excluded by `.gitignore`):

- ❌ Secrets (`.env`, `secrets-local/`) — keep local only
- ❌ Virtual environment (`.venv/`) — you'll rebuild
- ❌ Build artifacts (`build/`, `dist/`) — you'll regenerate

---

## Step 2: Understand the Structure

### 🟢 SHAREABLE (What's in Git)

| Folder | Contents | Use |
|--------|----------|-----|
| `data/personas/` | 9 persona specs | Canonical source for all personas |
| `docs/` | Public documentation | Theory, guides, deployment checklists |
| `lore/` | Canonical lore & origin stories | Brand, narrative, cosmic framework |
| `research/CODEX/` | Research framework & theory | Published research methodology |
| `src/` | Core Python code | TEC agent runtime, tools, integrations |
| `tests/` | Test suite | Pytest coverage (no hardcoded secrets) |

### 🔴 INTERNAL (Not in Git)

| Item | Why | What To Do |
|------|-----|-----------|
| `.env` | Contains real API keys | Create locally from `.env.example` |
| `secrets-local/` | Personal credentials | Create locally; never commit |
| `.venv/` | Virtual environment | Rebuild locally |
| `__pycache__/`, `*.pyc` | Build artifacts | Regenerate on first run |
| `build/`, `dist/` | Distribution packages | Regenerate on first build |

---

## Step 3: Set Up Your Local Environment

### 3a. Create & Activate Virtual Environment

**On Linux/macOS**:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows (PowerShell 7)**:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3b. Install Dependencies

```bash
pip install --upgrade pip
pip install -e .[dev]
```

This installs:

- Core dependencies (from `pyproject.toml`)
- Dev tools (`pytest`, `ruff`, `black`, etc.)
- Editable mode (code changes take effect immediately)

### 3c. Create Local Secrets File

```bash
cp .env.example .env.local
```

**Then edit `.env.local`** with your actual credentials:

- Spotify API key
- OpenAI API key
- Notion API key
- Any other integrations you use

**Never commit `.env.local`** — it's in `.gitignore` for a reason.

---

## Step 4: Verify Everything Works

### 4a. Run Tests

```bash
python -m pytest tests/ -q
```

**Expected output**:

```
................................                                   [100%]
```

If tests pass: ✅ Your environment is set up correctly.

### 4b. Run the CLI

```bash
python -m tec_tgcr.cli chat "Hello LuminAI"
```

**Expected behavior**: Should load persona system and respond.

### 4c. Check Persona Access

```bash
ls -la data/personas/
```

**Expected**: 9 files (all 6 primary + 3 extended personas).

---

## Step 5: Understand What You Can & Cannot Share

### ✅ Safe to Share (Shareable Category)

You can freely:

- Push to GitHub
- Upload to GPT Knowledge Base
- Share with teammates
- Reference in documentation

**Examples**:

- `data/personas/*.md`
- `GPT_SYSTEM_PROMPT_READY.txt`
- `PERSONAS_CANONICAL_MANIFEST.md`
- `docs/`, `lore/`, `research/CODEX/`
- All code in `src/` (if no embedded secrets)

### ❌ DO NOT Share (Internal Category)

Never commit, never upload, never share:

- `.env.local` (your personal API keys)
- `secrets-local/` (credentials)
- `.venv/` (will be rebuilt anyway)
- Notebooks with embedded API keys
- Personal brainstorms or drafts

**Before pushing**: Run this check:

```bash
git status
```

If you see `.env`, `secrets/`, `.venv`, or `__pycache__/` listed as "modified": ⚠️ Don't push them. They should stay local.

---

## Step 6: Make Your First Edit & Commit

### 6a. Create a Branch

```bash
git checkout -b feature/my-feature
```

### 6b. Make Changes

Edit files in:

- `src/` (code)
- `data/personas/` (persona specs)
- `docs/` (documentation)
- `tests/` (tests)

**NOT in**:

- `.env*` files
- `secrets/` or `secrets-local/`

### 6c. Verify Tests Still Pass

```bash
python -m pytest tests/ -q
```

### 6d. Commit & Push

```bash
git add .
git commit -m "feat: your change description"
git push origin feature/my-feature
```

**Before committing, verify**:

- [ ] No `.env.local` staged
- [ ] No `secrets/` staged
- [ ] No `__pycache__/` staged
- [ ] Tests pass
- [ ] No API keys in commit message or code

---

## Reference: File Classification

**For full details on what's shareable vs. internal**, see:
👉 `SHAREABLE_VS_INTERNAL_CLASSIFICATION.md`

**Quick version**:

- 🟢 **Shareable**: personas, docs, code, lore, theory
- 🔴 **Internal**: `.env`, `secrets/`, `.venv`, personal notebooks
- 🟡 **Conditional**: notebooks (sanitize before sharing), config files (share templates, not values)

---

## Troubleshooting

### Issue: Tests fail after clone

**Likely cause**: Missing `.env.local` with required API keys

**Solution**:

```bash
cp .env.example .env.local
# Edit .env.local with your actual keys
python -m pytest tests/ -q
```

### Issue: `command not found: python`

**On Linux/macOS**, try:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .[dev]
```

### Issue: `.venv` takes up too much space

**This is normal**. It's not committed to Git. You can:

- Delete it locally: `rm -rf .venv`
- Rebuild: `python -m venv .venv && source .venv/bin/activate && pip install -e .[dev]`

### Issue: Git says `.env.local` is modified

**Do NOT commit it**. It's in `.gitignore`. To reset:

```bash
git checkout .env.local
```

---

## What To Do Next

1. ✅ **Setup complete?** Run tests to verify: `python -m pytest tests/ -q`
2. 🔧 **Want to contribute?** Create a branch and make your edits
3. 📚 **Want to understand the system?** Read:
   - `PERSONAS_CANONICAL_MANIFEST.md` — persona organization
   - `docs/README.md` — theory & framework
   - `lore/` — origin stories & cosmology
4. 🚀 **Want to build the GPT?** Follow:
   - `GPT_DEPLOYMENT_READY.md` — step-by-step GPT setup

---

## Quick Reference Commands

```bash
# Activate environment
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -e .[dev]

# Run tests
python -m pytest tests/ -q

# Run CLI
python -m tec_tgcr.cli chat "prompt here"

# Check status before push
git status
git diff --cached

# Create a branch
git checkout -b feature/my-feature

# Commit & push
git add .
git commit -m "message"
git push origin feature/my-feature
```

---

**Location**: `/home/tec_tgcr/tec-tgcr/PULL_AND_BUILD_GUIDE.md`

**See also**:

- `SHAREABLE_VS_INTERNAL_CLASSIFICATION.md` (full classification system)
- `README.md` (project overview)
- `docs/` (theory & documentation)
