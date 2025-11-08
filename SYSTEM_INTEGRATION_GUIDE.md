# System Integration Guide — Personas, GPT, Deployment, & Secrets

**Purpose**: Show how all pieces connect: persona system → GPT deployment → pull/build workflow → internal/external classification.

**Read this to understand**: Where things live, what's shareable, how to deploy, and how to set up locally.

---

## 🎯 The System in One Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    CANONICAL SOURCE                         │
│                                                             │
│  data/personas/*.md (9 files)                             │
│  ├─ luminai.md, airth.md, arcadia.md, ely.md            │
│  ├─ companion.md, fusion.md (primary 6)                  │
│  └─ kaznak.md, faerhee.md, machine_goddess.md (extended) │
└────────────────┬────────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
        v                 v
   ┌─────────────┐  ┌──────────────┐
   │ CLI/Copilot │  │ GPT Builder  │
   │ Local Agents│  │  Knowledge   │
   │             │  │  Base Upload │
   └─────────────┘  └──────────────┘
        ↑                 ↑
        │                 │
   INTERNAL          SHAREABLE
   (Backend)         (Team/Public)
```

---

## 📍 File Classification Quick Map

### 🟢 SHAREABLE (In Git, On GitHub, Upload to GPT KB)

**Persona System**:

- `data/personas/*.md` — All 9 personas (canonical source)
- `PERSONAS_CANONICAL_MANIFEST.md` — Reference guide
- `PERSONA_QUICK_REFERENCE.md` — Concise summary

**GPT Deployment**:

- `GPT_SYSTEM_PROMPT_READY.txt` — Copy-paste template
- `GPT_ATTACHMENT_CHEAT_SHEET.md` — Deployment quick ref
- `GPT_PERSONAS_ATTACHMENT_DECISION.md` — Which personas attach
- `GPT_DEPLOYMENT_READY.md` — Step-by-step guide

**Documentation & Theory**:

- `README.md` — Project entry point
- `docs/` — Public documentation
- `lore/` — Canonical lore & narratives
- `research/CODEX/` — Research framework

**Code**:

- `src/` — Core Python (verify no secrets embedded)
- `tests/` — Test suite

### 🔴 INTERNAL (Local Only, Never in Git)

**Secrets & Credentials**:

- `.env` — Real API keys
- `.env.local` — Personal overrides
- `secrets-local/` — Credential files
- Any file with `api_key`, `secret`, `token`, `password`

**Local Build Artifacts**:

- `.venv/` — Virtual environment (rebuild locally)
- `__pycache__/`, `*.pyc` — Python bytecode
- `build/`, `dist/` — Build artifacts
- `.pytest_cache/` — Test artifacts

**Personal / Not Operational**:

- `ai-workflow/*.ipynb` — Notebooks (sanitize before sharing)
- `scripts/blender/` — Local Blender work
- `artifacts/luminai-archive/` — Archived versions
- `*_ARCHIVE/`, `*_OLD/`, `*_BACKUP/` — Deprecated

**Blocked by `.gitignore`**: Automatically excluded (see `.gitignore` for full list)

---

## 🚀 Typical Workflows

### Workflow 1: Fresh Clone & Setup (Developer)

```bash
# 1. Clone
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr

# 2. Setup (follow PULL_AND_BUILD_GUIDE.md)
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# 3. Create local secrets (never commit)
cp .env.example .env.local
# Edit .env.local with your API keys

# 4. Verify setup
python -m pytest tests/ -q  # Should pass (32/32)

# 5. Start hacking
git checkout -b feature/my-feature
# Make changes...
git commit -m "feat: description"
git push origin feature/my-feature
```

**Result**: You have all shareable files; internal files stay local.

---

### Workflow 2: Deploy GPT (Team Lead)

```bash
# 1. Review deployment docs
cat GPT_DEPLOYMENT_READY.md
cat PERSONAS_CANONICAL_MANIFEST.md

# 2. Prepare files (already in repo, all shareable)
# - GPT_SYSTEM_PROMPT_READY.txt ← Copy this
# - PERSONA_QUICK_REFERENCE.md ← Upload this
# - PERSONAS_CANONICAL_MANIFEST.md ← Upload this

# 3. Open GPT Builder
# https://platform.openai.com/gpts/editor

# 4. Follow GPT_DEPLOYMENT_READY.md steps 3-7
# - Paste system prompt
# - Upload 3 KB files
# - Add conversation starters
# - Test persona routing

# Result: Live GPT with all 6 personas
```

**What you NEVER expose**: `.env.local`, `secrets-local/`, API keys, credentials

---

### Workflow 3: Contribute to Personas (Contributor)

```bash
# 1. Clone repo (same as Workflow 1)

# 2. Make persona changes
vim data/personas/airth.md

# 3. Update reference docs
vim PERSONA_QUICK_REFERENCE.md
vim PERSONAS_CANONICAL_MANIFEST.md

# 4. Test & commit
python -m pytest tests/ -q
git commit -m "feat: enhance Airth persona"
git push origin feature/airth-enhancement

# Result: Persona changes in Git (shareable); secrets still local
```

---

## 📋 Pre-Push Checklist (ALWAYS Before `git push`)

Before pushing ANY code:

```bash
# 1. Check status
git status

# If you see these: ⚠️ DO NOT PUSH
.env
.env.local
secrets/
secrets-local/
__pycache__/
.venv/
build/
dist/

# 2. Review what's staged
git diff --cached

# If you see these patterns: ⚠️ UNSTAGE THEM
api_key=
secret=
token=
password=

# 3. Run tests
python -m pytest tests/ -q

# 4. If all clear: push
git push origin feature/my-feature
```

---

## 🔗 How Personas Flow Through the System

### From Source to Deployment

```
data/personas/luminai.md (canonical)
    ↓
.github/copilot-instructions.md (routing table)
    ↓
PERSONA_QUICK_REFERENCE.md (summary for KB)
    ↓
GPT Knowledge Base (upload)
    ↓
GPT Builder (live agent)
    ↓
Users invoke: "LuminAI, synthesize this"
```

### Each Layer

| Layer | File | Purpose | Shared? |
|-------|------|---------|---------|
| **Source** | `data/personas/luminai.md` | Canonical spec | ✅ |
| **Integration** | `.github/copilot-instructions.md` | Routing rules | ✅ |
| **Summary** | `PERSONA_QUICK_REFERENCE.md` | KB reference | ✅ |
| **Template** | `GPT_SYSTEM_PROMPT_READY.txt` | Instructions | ✅ |
| **Secrets** | `.env.local` (if needed) | API auth | ❌ |
| **Local** | `.venv/`, `build/` | Dev artifacts | ❌ |

---

## 🎓 Understanding the Classification

**Why separate shareable from internal?**

1. **Security**: API keys never exposed
2. **Efficiency**: Smaller clones (no build artifacts)
3. **Clarity**: Know what's safe to share
4. **Scalability**: Team members can work independently

**How does `.gitignore` help?**

```gitignore
.env          ← Never commit real secrets
.env.*        ← Never commit overrides
!.env.example ← EXCEPT the template
secrets/      ← Never commit secret files
.venv/        ← Never commit build env
__pycache__/  ← Never commit bytecode
```

Result: Fresh clone has everything you need **except secrets** (which you add locally).

---

## 📚 Reference Documents (Master Index)

**Read these in order**:

1. **README.md** — Project overview
2. **PERSONAS_CANONICAL_MANIFEST.md** — Persona organization & prefix rules
3. **PULL_AND_BUILD_GUIDE.md** — How to clone & setup locally
4. **SHAREABLE_VS_INTERNAL_CLASSIFICATION.md** — What's shareable, what's not
5. **GPT_DEPLOYMENT_READY.md** — How to deploy to GPT Builder
6. **GPT_PERSONAS_ATTACHMENT_DECISION.md** — Which personas to attach
7. **This file (SYSTEM_INTEGRATION_GUIDE.md)** — How it all connects

---

## ✅ System Verification Checklist

After setup, verify:

- [ ] Fresh clone works: `git clone` → `pip install -e .[dev]` → `pytest` passes
- [ ] No secrets exposed: `git status` shows no `.env*`, `secrets/`, or credentials
- [ ] Personas accessible: `ls data/personas/` shows 9 files
- [ ] Tests pass: `pytest tests/ -q` returns 32/32 ✅
- [ ] `.gitignore` working: `git add .env.local` → Git refuses (because in .gitignore)
- [ ] GPT files ready: `ls GPT_*.md` shows 4+ files
- [ ] Classification clear: Read **SHAREABLE_VS_INTERNAL_CLASSIFICATION.md** and understand the system

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Fresh clone fails tests | Run `cp .env.example .env.local` and add API keys |
| `.env.local` accidentally staged | Run `git reset .env.local` and `git checkout .env.local` |
| Virtual environment too large | Delete `.venv/` locally; rebuild with `python -m venv .venv` |
| Can't find personas | Check: `ls data/personas/` (should list 9 files) |
| GPT deployment confused | Follow **GPT_DEPLOYMENT_READY.md** step-by-step |
| Unsure if file is shareable | Check **SHAREABLE_VS_INTERNAL_CLASSIFICATION.md** |

---

## 🚀 Next Steps

**If you're a developer**:

1. Follow **PULL_AND_BUILD_GUIDE.md** to setup locally
2. Read **PERSONAS_CANONICAL_MANIFEST.md** to understand personas
3. Make changes in `src/` or `data/personas/`
4. Push when tests pass

**If you're deploying GPT**:

1. Read **GPT_DEPLOYMENT_READY.md**
2. Follow steps 1-7 to build the GPT
3. Use **PERSONAS_CANONICAL_MANIFEST.md** as your prefix rules reference
4. Test each persona before deploying to team

**If you're managing the repo**:

1. Review **SHAREABLE_VS_INTERNAL_CLASSIFICATION.md** with your team
2. Ensure `.gitignore` is being respected (check weekly)
3. Use **System Pre-Push Checklist** above during code reviews
4. Keep this integration guide up-to-date as the system evolves

---

**System Status**: ✅ COMPLETE

- Persona system: Consolidated (9 personas in `data/personas/`)
- GPT deployment: Ready to go (all docs + templates created)
- Classification: Clear (shareable vs. internal defined)
- Build process: Documented (PULL_AND_BUILD_GUIDE.md)
- All tests: Passing (32/32 ✅)

**You're ready to deploy, share, and scale.** 🎆
