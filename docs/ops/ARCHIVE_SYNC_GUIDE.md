# Archive & OneDrive Sync Guide

This guide covers automated archival of stale workspace files and syncing to OneDrive for cross-device backup and continuity.

## Overview

Two tools work together:

1. **`scripts/archive_workspace.py`** — identifies stale files, moves them to `data/archives/<YYYY>/<MM>/`, logs an undo manifest
2. **`scripts/push_to_onedrive.sh`** — syncs `artifacts/` to OneDrive via rclone for backup + continuity

## Setup

### Step 1: Configure Archive Thresholds (Optional)

Edit `scripts/archive_workspace.py` to customize patterns:

```python
# Default patterns to archive (glob-style)
DEFAULT_INCLUDE = [
    "exports/**/*.png",
    "exports/**/*.jpg",
    "runs/*.json",
    ".pytest_cache/**",
    ".ruff_cache/**",
]

# Patterns to never touch
DEFAULT_EXCLUDE = [
    "artifacts/**",
    ".git/**",
    "secrets/**",
    "secrets-local/**",
    "node_modules/**",
]
```

### Step 2: Install & Configure rclone (For OneDrive Sync)

1. **Install rclone:**

   ```bash
   # macOS
   brew install rclone
   
   # Linux (Debian/Ubuntu)
   sudo apt-get install rclone
   
   # Or from source: https://rclone.org/install/
   ```

2. **Configure OneDrive remote:**

   ```bash
   rclone config create onedrive microsoft account type=onedrive
   ```

   - Follow the interactive flow (you may need to authorize in a browser)
   - Name the remote **`onedrive`** (scripts expect this)
   - Verify: `rclone lsd onedrive:/`

3. **Test sync (dry-run):**

   ```bash
   ./scripts/push_to_onedrive.sh --dry-run
   ```

## Usage

### Archive Stale Files

```bash
# Preview files older than 14 days (default)
python3 scripts/archive_workspace.py --dry-run

# Archive files older than 14 days
python3 scripts/archive_workspace.py

# Archive files older than 7 days
python3 scripts/archive_workspace.py --days 7

# Archive custom patterns
python3 scripts/archive_workspace.py --include "temp/**" "cache/**" --days 30

# Archive and stage in git
python3 scripts/archive_workspace.py --stage
```

**Manifest:** After archiving, a manifest is saved to `data/archives/manifests/archive-run-<TIMESTAMP>.json` for undo capability.

### Sync to OneDrive

```bash
# Preview sync without uploading
./scripts/push_to_onedrive.sh --dry-run

# Sync artifacts/ to OneDrive
./scripts/push_to_onedrive.sh

# Sync custom source
./scripts/push_to_onedrive.sh --source exports --dest "onedrive:/Apps/TEC/exports"

# One-liner with archive + sync
python3 scripts/archive_workspace.py --days 14 && ./scripts/push_to_onedrive.sh
```

## Automation

### Option 1: Cron Job (Linux/macOS)

Add to crontab (`crontab -e`):

```bash
# Archive + sync every Sunday at 2 AM
0 2 * * 0 cd /home/tec_tgcr/tec-tgcr && python3 scripts/archive_workspace.py --days 14 --stage && bash scripts/push_to_onedrive.sh
```

### Option 2: GitHub Actions Workflow

Create `.github/workflows/archive-sync.yml`:

```yaml
name: Archive & Sync to OneDrive

on:
  schedule:
    # Every Sunday at 2 AM UTC
    - cron: '0 2 * * 0'
  workflow_dispatch:

jobs:
  archive-sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Archive stale files
        run: python3 scripts/archive_workspace.py --days 14 --stage

      - name: Commit archives manifest
        run: |
          git config user.name "Archive Bot"
          git config user.email "bot@tec.local"
          git add data/archives/manifests/
          git commit -m "chore: archive stale files" || true

      - name: Install rclone
        run: |
          curl https://rclone.org/install.sh | sudo bash

      - name: Sync to OneDrive
        env:
          RCLONE_CONFIG: ${{ secrets.RCLONE_CONFIG }}
        run: |
          mkdir -p ~/.config/rclone
          echo "$RCLONE_CONFIG" > ~/.config/rclone/rclone.conf
          bash scripts/push_to_onedrive.sh
```

Then store your rclone config as a GitHub secret (`RCLONE_CONFIG`):

```bash
# Export your local config
cat ~/.config/rclone/rclone.conf | base64 | pbcopy  # macOS
# or
cat ~/.config/rclone/rclone.conf | base64 | xclip   # Linux

# Add as GitHub secret: Settings > Secrets > New repository secret
# Name: RCLONE_CONFIG
# Value: [pasted base64]
```

## Archive Structure

After running `archive_workspace.py`, files are organized as:

```
data/
  archives/
    2025/
      11/
        exports__brand__logo.png
        runs__ingest.json
    manifests/
      archive-run-2025-11-02T17:15:30.json
```

**Manifest format:**

```json
{
  "archive_run_timestamp_utc": "2025-11-02T17:15:30Z",
  "archived_files": [
    {
      "original_path": "exports/brand/logo.png",
      "archive_path": "data/archives/2025/11/exports__brand__logo.png",
      "timestamp_utc": "2025-11-02T17:15:30Z",
      "original_mtime": "2025-10-15T12:30:45"
    }
  ]
}
```

## Undo / Restore

To restore an archived file:

1. Find the manifest: `data/archives/manifests/archive-run-<TIMESTAMP>.json`
2. Locate the file entry
3. Copy from `archive_path` back to `original_path`:

   ```bash
   cp data/archives/2025/11/exports__brand__logo.png exports/brand/logo.png
   ```

## Safety Notes

- **Never touches**: `.git/`, `secrets/`, `secrets-local/`, `.gitignore`
- **Logs everything**: All moves are recorded in manifests for audit + undo
- **Git-aware**: Optional `--stage` flag adds archives to index (useful for CI integration)
- **Dry-run first**: Always preview with `--dry-run` before executing

## Troubleshooting

### rclone: onedrive remote not found

```bash
rclone config list  # Check configured remotes
rclone config create onedrive microsoft account type=onedrive  # Reconfigure
```

### Permission denied on archive_workspace.py

```bash
chmod +x scripts/archive_workspace.py
```

### OneDrive sync fails with "403 Forbidden"

- OneDrive token expired; reconfigure:

  ```bash
  rclone config reconnect onedrive
  ```

## References

- `scripts/archive_workspace.py` — Python 3 archive tool
- `scripts/push_to_onedrive.sh` — Bash rclone wrapper
- `scripts/README.md` — All available scripts
- `docs/ops/PROVENANCE_BUNDLES.md` — Provenance & canon bundle separation
