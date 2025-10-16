# TEC TGCR — Repo Cleanup + WordPress.com Step-by-step

This guide gets the repo tidy, builds the WordPress plugin, and verifies the deployment path on WordPress.com. Windows PowerShell commands are provided.

## 1) Clean the working tree (safe)

- What this does: removes generated artifacts and caches only.
- Source is untouched.

```powershell
# From repo root
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/clean_repo.ps1
```

Result: deletes `dist/`, `exports/`, `.wpcom-dist/`, test caches, and stray `*.zip` at repo root.

## 2) Run tests (baseline)

```powershell
# VS Code Task
# Terminal > Run Task… > Python: Run pytest
```

Expected: tests pass quietly.

## 3) Package the WordPress plugin

```powershell
# VS Code Task
# Terminal > Run Task… > Pack: WordPress plugin ZIP
```

- Output: `exports/wp-plugin/tec-tgcr-<version>.zip`
- Zip contents: top-level folder `tec-tgcr/` with `tec-tgcr.php`

## 4) WordPress.com deployment wiring

- Workflow used: `.github/workflows/wpcom.yml`
- Mode: Advanced
- Artifact name: `wpcom`

On WordPress.com → Hosting → Deployments → Manage repository:
- Repository: TEC-The-ELidoras-Codex/tec-tgcr
- Branch: main
- Deployment workflow: `wpcom.yml`
- Artifact name: `wpcom`

No secrets required for the default artifact workflow.

## 5) Publish

- Push to `main`, or manually run GitHub Action “Publish to WordPress.com”.

## 6) Verify on your site

- `https://YOURDOMAIN/wp-json/tec-tgcr/v1/ping` → `{ ok: true, plugin: "tec-tgcr", ... }`
- `https://YOURDOMAIN/wp-json/tec-tgcr/v1/citation?persona=luminai` → PD quote JSON
- Add a page with:
  - `[tec_tgcr_ping]`
  - `[tec_tgcr_citation persona="arcadia"]`

## 7) Optional SSH/SFTP

If you choose the SSH workflow instead of artifact mode, add secret `WPCOM_SSH_HOST=ssh.wp.com` and switch deployment workflow to `wpcom-ssh-deploy.yml` in WP.com settings.

## Notes

- `.gitignore` now excludes `dist/`, `exports/`, `.wpcom-dist/`, and generated zips to prevent re-adding artifacts.
- Use `scripts/clean_repo.ps1` before packing/releasing to keep history clean.
- See `docs/WORDPRESS-DEPLOYMENT-CHECKLIST.md` for more details and troubleshooting.
