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
