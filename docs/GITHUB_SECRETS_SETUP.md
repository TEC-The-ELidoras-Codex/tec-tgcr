# GitHub Secrets & Authentication Setup Guide

> Why you don't need a PAT for everyday work, and when you do need GitHub Secrets.

---

## TL;DR

✅ **For pushing code to GitHub:** Use HTTPS (which you're doing). No PAT needed.

✅ **For CI/CD that needs secrets:** Use GitHub Secrets (encrypted, per-repo).

✅ **For sensitive local values:** Use Bitwarden + `.env.local` (never commit).

---

## Your Current Setup (Good!)

```bash
git remote -v
# origin  https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git (fetch)
# origin  https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git (push)
```

You're using **HTTPS** ✓. Git will prompt for credentials or use cached token. No action needed.

---

## Three Types of Secrets

### 1. GitHub Secrets (For CI/CD Workflows)

**What:** Encrypted environment variables available to GitHub Actions.

**When to use:**

- CI needs to call external APIs (OpenAI, Anthropic, GitHub API)
- Deploying to production (AWS, Azure, Vercel)
- Building/pushing Docker images
- WordPress deployment credentials

**How to set up:**

1. Go to **GitHub repo** → **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Name: `OPENAI_API_KEY` | Value: `sk-...` (paste your key)
4. Repeat for each secret

**In your `.github/workflows/ci-pytests.yml`, use them:**

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

**Example secrets your repo might need:**

- `OPENAI_API_KEY` — For AI tests
- `ANTHROPIC_API_KEY` — For Claude tests
- `WPCOM_SSH_PASSWORD` — For WordPress deployments
- `GITHUB_TOKEN` — Auto-provided by GitHub Actions (you get this free)

---

### 2. Bitwarden (For Local Development & Team)

**What:** Password manager where your team stores shared credentials.

**When to use:**

- Team needs to share API keys securely
- You need a backup of credentials
- Multiple people need access to the same secrets

**How:**

1. Store credentials in Bitwarden vault (e.g., folder: "TEC-TGCR")
2. Copy values to `.env.local` when you need them
3. `.env.local` is gitignored (never committed)

**Your `.env.local` might look like:**

```bash
# .env.local (never commit this!)
OPENAI_API_KEY=sk-... (copy from Bitwarden)
ANTHROPIC_API_KEY=claude-... (copy from Bitwarden)
WPCOM_SSH_PASSWORD=... (copy from Bitwarden)
```

Then load in your scripts:

```bash
source .env.local
python my_script.py  # Now has access to $OPENAI_API_KEY
```

---

### 3. .env.local (For Local Machine Only)

**What:** Local environment file that never leaves your machine.

**When to use:**

- You need credentials locally but don't want them in git
- Different team members have different local setups
- Testing with real API keys before CI

**Setup:**

```bash
# Copy the template
cp .env.example .env.local

# Add your real values
echo "OPENAI_API_KEY=sk-..." >> .env.local

# Git ignores it automatically (check .gitignore)
git status  # Should NOT show .env.local
```

**Never do this:**

```bash
# ✗ WRONG - Don't commit secrets!
git add .env.local
git commit -m "add secrets"  # NEVER
```

---

## Workflow Example: OpenAI API Testing

### Local (Your Machine)

```bash
# .env.local (gitignored)
OPENAI_API_KEY=sk-proj-abc123...
```

```bash
# Run locally
source .env.local
python -m pytest -q  # Tests read $OPENAI_API_KEY from env
```

### CI/CD (GitHub Actions)

```yaml
# .github/workflows/ci-pytests.yml
name: CI — Python tests

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - run: pip install -e .[dev]
      
      # GitHub Actions AUTOMATICALLY injects these as env vars
      - name: Run tests
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python -m pytest -q
```

---

## Do You Need a PAT (Personal Access Token)?

**Short answer: No, probably not.**

| Task | Method | PAT Needed? |
|------|--------|-----------|
| Push code (git push) | HTTPS (cached auth) | ❌ No |
| Run CI/CD workflows | GitHub Actions (built-in) | ❌ No |
| Call GitHub API from CI | `${{ secrets.GITHUB_TOKEN }}` | ❌ No |
| Call GitHub API locally | PAT or SSH key | ✓ Yes, if needed |

**When you'd need a PAT:**

- Writing a script that calls GitHub API locally (e.g., auto-create issues)
- Using GitHub CLI (`gh`) without SSH
- Programmatic access outside of Actions

**If you need a PAT:**

1. Go to **GitHub** → **Settings** → **Developer settings** → **Personal access tokens**
2. Create token with `repo` scope
3. Store in Bitwarden (not in code!)
4. Use: `git config --global credential.helper store` (caches locally)

---

## Your Bitwarden + GitHub Secrets Strategy

### Option A: Bitwarden is the Source of Truth (Recommended)

1. **Store all secrets in Bitwarden vault** (shared team folder)
2. **When CI needs a secret:**
   - Copy value from Bitwarden
   - Add as GitHub Secret (Settings → Secrets)
3. **When you code locally:**
   - Copy value from Bitwarden
   - Paste into `.env.local`

**Advantage:** Single source of truth, easy team collaboration.

### Option B: Automated Sync (Advanced)

Use tools like:

- [1Password/Bitwarden → GitHub Secrets sync](https://github.com/marketplace/actions/load-secret-action)
- Environment-specific vaults

**For now, Option A is simpler and secure.**

---

## Checklist: Set Up Your Secrets

- [ ] **GitHub Secrets Setup**
  - [ ] Go to repo Settings → Secrets and variables → Actions
  - [ ] Add `OPENAI_API_KEY`
  - [ ] Add `ANTHROPIC_API_KEY`
  - [ ] Add any deployment credentials

- [ ] **Local Setup**
  - [ ] Create `.env.local` (copied from `.env.example`)
  - [ ] Add your local values (copy from Bitwarden)
  - [ ] Verify `.env.local` is in `.gitignore`
  - [ ] Test: `source .env.local && echo $OPENAI_API_KEY`

- [ ] **Bitwarden**
  - [ ] Store copies of all credentials
  - [ ] Share vault with team
  - [ ] Document which secrets go where

---

## Quick Reference

```bash
# Load local secrets
source .env.local

# Check what's set
echo $OPENAI_API_KEY

# Verify .env.local is gitignored
git status  # Should NOT show .env.local

# Check GitHub Secrets exist (you need GitHub CLI for this)
gh secret list
```

---

## Why This Works

- ✅ **Code is public** (GitHub repo is open)
- ✅ **Secrets are private** (GitHub Secrets, Bitwarden, `.env.local`)
- ✅ **CI can run** (GitHub Actions injects secrets at runtime)
- ✅ **Team can collaborate** (Bitwarden shared vault)
- ✅ **Local dev works** (`.env.local` stays on your machine)

**You're not overcomplicating it. This is the standard pattern.** 🎯
