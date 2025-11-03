# Dependencies & Setup Guide

**TL;DR:** Run this once and you're done:

```bash
bash scripts/setup_environment.sh
```

Then just use the scripts—no manual dependency management needed.

---

## Overview

The `scripts/setup_environment.sh` script handles **all** dependency installation automatically:

- ✅ Python packages (pip)
- ✅ System packages (apt/Homebrew)
- ✅ Git hooks
- ✅ Bitwarden tools
- ✅ One-time rclone setup (optional)

---

## What Gets Installed

### Python Packages

| Package | Purpose | Why |
|---------|---------|-----|
| `PyJWT` | GitHub App JWT signing | Generate GitHub tokens |
| `requests` | HTTP library | GitHub API calls |
| `cryptography` | Crypto operations | JWT key handling |
| `cairosvg` | SVG → PNG conversion | Brand asset exports |

**Install location**: `~/.local/bin/` (system Python site-packages)

### System Packages (Linux/Debian)

| Package | Purpose |
|---------|---------|
| `git` | Version control (probably already installed) |
| `build-essential` | C compiler + headers (for pip build) |
| `python3-dev` | Python development headers |
| `rclone` | OneDrive sync (optional) |

### Bitwarden Tools

| Tool | Purpose |
|------|---------|
| `bws` (Bitwarden Secrets Manager CLI) | Fetch secrets from Bitwarden |
| `bw` (Bitwarden CLI) | Optional: additional secret management |

---

## Setup Steps

### Step 1: Run the Setup Script (One Time)

```bash
cd /path/to/tec-tgcr
bash scripts/setup_environment.sh
```

**What it does:**

- Installs Python packages via pip
- Installs system packages (prompts for sudo password on Linux)
- Sets up Git pre-commit hooks
- Checks for Bitwarden tools
- Verifies `.env.local` exists

**Time: ~2-3 minutes** (depends on download speeds)

### Step 2: Configure Secrets (Optional)

If using Bitwarden Secrets Manager:

```bash
export BWS_ACCESS_TOKEN="your_bws_token_here"
python3 scripts/secrets/generate_env_from_bws.sh
```

Or generate from local mapping:

```bash
bash scripts/secrets/generate_env_from_bws.sh
```

### Step 3: Configure OneDrive Sync (If Using)

One-time rclone setup:

```bash
rclone config create onedrive microsoft account type=onedrive
```

Then test:

```bash
./scripts/push_to_onedrive.sh --dry-run
```

---

## Which Scripts Need What

### Archive Workspace

```bash
python3 scripts/archive_workspace.py --dry-run
```

**Needs**: Python 3 (standard library only)  
**Setup time**: ~10 seconds

### Push to OneDrive

```bash
./scripts/push_to_onedrive.sh
```

**Needs**: `rclone` (installed by setup script)  
**Setup time**: One-time rclone config (5 min)

### Export Brand Assets

```bash
python3 scripts/export_brand_assets.py
```

**Needs**: Python 3 + `cairosvg` (installed by setup script)  
**Setup time**: Included in main setup

### Extract Embedded PNG

```bash
python3 scripts/extract_embedded_png.py
```

**Needs**: Python 3 (standard library only)  
**Setup time**: ~5 seconds

### GitHub App Token Generation

```bash
python3 scripts/get_github_app_installation_token.py
```

**Needs**: Python 3 + PyJWT + requests + cryptography (all installed by setup script)  
**Setup time**: Included in main setup

---

## Verification

After setup, verify everything works:

```bash
# Test Python packages
python3 -c "import jwt, requests, cryptography, cairosvg; print('✓ All packages OK')"

# Test rclone
rclone version

# Test scripts
python3 scripts/archive_workspace.py --dry-run
./scripts/push_to_onedrive.sh --dry-run
python3 scripts/extract_embedded_png.py --list
```

---

## Troubleshooting

### "pip: command not found"

```bash
# macOS
brew install python3

# Linux
sudo apt-get install python3-pip
```

### "rclone: command not found"

```bash
# macOS
brew install rclone

# Linux
curl https://rclone.org/install.sh | sudo bash
```

### "sudo: password required" during setup

This is normal! The setup script needs `sudo` to install system packages. Just type your password when prompted (you won't see it being typed—that's normal).

### "cairosvg import error"

```bash
# Reinstall
python3 -m pip install --force-reinstall cairosvg

# Or check system Cairo library (Linux)
sudo apt-get install libcairo2-dev
python3 -m pip install cairosvg
```

### ".env.local not found"

The setup script checks for `.env.local` but doesn't create it. Create manually:

```bash
cp secrets/mapping.example.json .env.local
# Or generate from Bitwarden:
bash scripts/secrets/generate_env_from_bws.sh
```

---

## Minimal vs. Full Setup

### Minimal (Just Archive + Cleanup)

```bash
python3 scripts/setup_environment.sh
# Only answer "yes" to Python packages
# Skip rclone if you don't need OneDrive
```

### Full (All Tools)

```bash
bash scripts/setup_environment.sh
# Answer "yes" to all prompts
rclone config create onedrive microsoft account type=onedrive
```

---

## Re-running Setup

It's safe to run the setup script multiple times:

- ✅ Already-installed packages are skipped
- ✅ Git hooks are idempotent
- ✅ No data is deleted

```bash
bash scripts/setup_environment.sh  # Safe to run anytime
```

---

## Automation

### Cron Job (Runs scripts without re-setup)

```bash
# Every Sunday at 2 AM: archive + sync
0 2 * * 0 cd /home/tec_tgcr/tec-tgcr && python3 scripts/archive_workspace.py --days 14 --stage && bash scripts/push_to_onedrive.sh
```

No setup needed on cron—dependencies are already installed.

### GitHub Actions Workflow

CI workflows automatically install dependencies:

```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.12'

- name: Install dependencies
  run: |
    python3 -m pip install PyJWT requests cryptography cairosvg
```

---

## What's NOT Included

- **Docker**: If you want containerized setup, see `Dockerfile`
- **Node.js**: Not used by core scripts; optional for some tools
- **Java**: Not needed for TEC scripts
- **Ruby/Go/Rust**: Not needed

---

## Next Steps

1. **Run setup**: `bash scripts/setup_environment.sh`
2. **Verify**: `python3 scripts/archive_workspace.py --dry-run`
3. **Configure secrets**: Edit `.env.local` or use Bitwarden
4. **Try a script**: `python3 scripts/export_brand_assets.py --list`
5. **Automate**: Add cron jobs or GitHub Actions

---

## Quick Reference

| Task | Command | Setup Time |
|------|---------|-----------|
| One-time setup | `bash scripts/setup_environment.sh` | 2-3 min |
| Archive files | `python3 scripts/archive_workspace.py` | 0 (pre-setup) |
| Sync to OneDrive | `./scripts/push_to_onedrive.sh` | 5 min (first time) |
| Export brand assets | `python3 scripts/export_brand_assets.py` | 0 (pre-setup) |
| Run tests | `pytest` or `python3 scripts/run_ingest_check.py` | 0 (pre-setup) |

---

## Support

- **Bitwarden setup**: <https://bitwarden.com/help/>
- **rclone setup**: <https://rclone.org/docs/>
- **Python pip**: <https://pip.pypa.io/>
- **GitHub Apps**: <https://docs.github.com/en/apps>
