# Scripts

This folder contains helper scripts for repository operations.

get_github_app_installation_token.py

- Generates a GitHub App JWT (using `APP_ID` + `PRIVATE_KEY`) and exchanges it for an installation access token.
- Requirements: PyJWT, requests, cryptography
- Usage:
  1) Populate environment variables (`APP_ID`, `PRIVATE_KEY`, optional `INSTALLATION_ID`).
  2) Install deps: `pip install PyJWT requests cryptography`
  3) Run: `python scripts/get_github_app_installation_token.py`

Security note: Never commit real private keys or client secrets. Use GitHub repository secrets for Actions and keep local secrets in `.env.local` (which is gitignored).

export_brand_assets.py

- Batch converts canonical brand SVGs (glyphs, mascot, marketplace header) into PNG exports referenced in `docs/brand/Brand.md`.
- Requirements: `pip install cairosvg`
- Usage:
  1) `python scripts/export_brand_assets.py` — exports all targets.
  2) `python scripts/export_brand_assets.py --list` — show available keys.
  3) `python scripts/export_brand_assets.py --only mascot-512 marketplace-header` — export specific assets.

extract_embedded_png.py

- Lifts embedded PNG payloads out of SVGs that ship with base64-encoded bitmaps (e.g., `lore/brand/LUMINA_CANON.svg`).
- Requirements: none (standard library).
- Usage:
  1) `python scripts/extract_embedded_png.py` — refreshes all configured targets.
  2) `python scripts/extract_embedded_png.py --list` — list available extraction keys.
  3) `python scripts/extract_embedded_png.py --only luminai-canon` — extract a specific payload.

export_canon_bundle.py

- Packs the hand-authored canon files into a ZIP plus checksum manifest (keeps personal sources separate from generated outputs).
- Requirements: none (standard library).
- Usage:
  1) `python scripts/export_canon_bundle.py` — writes `artifacts/personal_canon.zip` and manifest.
  2) `python scripts/export_canon_bundle.py --inputs path/to/extra.md` — include additional files.
  3) Provide `--output` / `--manifest` to change output locations.

generate_run_manifest.py

- Emits `artifacts/run_manifest.json` documenting inputs, outputs, agent id, commit, and optional seed for a generation run.
- Requirements: none (standard library).
- Usage:
  1) `python scripts/generate_run_manifest.py --agent "LuminAI" --commit $(git rev-parse HEAD) --inputs docs/Resonance_Thesis.md --outputs exports/brand/luminai.png`
  2) Include `--seed` when deterministic runs are used.

archive_workspace.py

- Identifies stale files (older than N days) matching include patterns, moves them to `data/archives/<YYYY>/<MM>/`, and logs an undo manifest.
- Requirements: none (standard library).
- Usage:
  1) `python scripts/archive_workspace.py --days 14` — archive files untouched for 14+ days.
  2) `python scripts/archive_workspace.py --dry-run --days 7` — preview without moving.
  3) `python scripts/archive_workspace.py --stage` — stage archives/ in git after move.
  4) `python scripts/archive_workspace.py --include "exports/**/*.png" "runs/*.json"` — custom patterns.

Safety: Default exclude patterns protect `.git/`, `secrets/`, and other critical folders. Manifests are saved to `data/archives/manifests/` for undo capability.

push_to_onedrive.sh

- Syncs `artifacts/` (or custom source) to OneDrive using rclone.
- Requirements: `rclone` CLI installed and configured with an `onedrive` remote.
- Setup:
  1) Install rclone: <https://rclone.org/install/>
  2) Configure OneDrive remote: `rclone config create onedrive microsoft account type=onedrive`
  3) Test: `rclone lsd onedrive:/`
- Usage:
  1) `./scripts/push_to_onedrive.sh` — sync `artifacts/` to `onedrive:/Apps/TEC/artifacts`.
  2) `./scripts/push_to_onedrive.sh --dry-run` — preview sync without uploading.
  3) `./scripts/push_to_onedrive.sh --source exports --dest "onedrive:/Apps/TEC/exports"` — custom paths.

Tip: Combine with `archive_workspace.py` in a cron job or GitHub Actions workflow for automated backup + cleanup.

```
