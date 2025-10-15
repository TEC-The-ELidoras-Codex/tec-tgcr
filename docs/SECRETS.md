# Secrets and Environment Variables

This repo uses a mix of local `.env` files and deployment secrets. Use this guide to place credentials in the right place with the right names.

## TL;DR
- Local development: copy `.env.example` to `.env` and fill only local, non-browser secrets (never commit `.env`).
- GitHub Actions (CI/CD): add secrets in your repo Settings → Secrets and variables → Actions (env-specific when possible).
- WordPress plugin (TEC Resonance Player): put Spotify creds in `wp-config.php` as constants — never in the theme or DB.

- WordPress agent (TEC LuminAI Agent): put OpenAI/Azure OpenAI keys in `wp-config.php` as constants; your site becomes the API proxy.

## What to add where

### 1) WordPress (server-side only)
The WordPress plugin reads constants from `wp-config.php`:

```php
// wp-config.php
// Spotify Client Credentials (Client Credentials flow)
define('TEC_SPOTIFY_CLIENT_ID', 'your_spotify_client_id');
define('TEC_SPOTIFY_CLIENT_SECRET', 'your_spotify_client_secret');

// Optional: point the plugin to your backend (if you have one)
// define('TEC_ARCADIA_URL', 'https://api.your-backend.com/spotify/resonance');
```

Never expose Spotify secrets client-side. The plugin also falls back to `SPOTIFY_CLIENT_ID` / `SPOTIFY_CLIENT_SECRET` constants if you prefer generic names.

### 2) GitHub Actions (CI/CD)
Add these in GitHub → Settings → Secrets and variables → Actions:

- OPENAI_API_KEY
- OPENAI_ORG_ID (optional)
- LUMINAI_API_URL (if your build/deploy references it)
- GITHUB_CLIENT_ID (for the React app build if you wire it)
- SHAREPOINT_CLIENT_ID (for the React app build if you wire it)
- Any service tokens needed by your deployment or tests (e.g., `ARCADIA_API_KEY` if applicable)

If you later add a workflow that deploys the WP plugin, you can also store `WP_HOST`, `WP_USERNAME`, `WP_PASSWORD`/`WP_APPLICATION_PASSWORD` as secrets to drive deployment steps. Avoid storing Spotify client secrets in GitHub unless your CI must call Spotify server-to-server (not typical for the WP plugin).

Mapping to front-ends:

- `LUMINAI_API_URL` → point to your site proxy: `https://your-site.com/wp-json/tec/v1/agent`

### 3) Local `.env`
The provided `.env.example` now includes placeholders for:

- OPENAI_API_KEY, OPENAI_ORG_ID
- SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET (use only if a local backend consumes them — not for the browser)
- TEC_ARCADIA_URL (optional)
- Existing keys for Civitai, World Anvil, Azure OpenAI, and the React app

WordPress Agent keys (local reference only; final values go in wp-config.php):

- TEC_OPENAI_API_KEY
- TEC_OPENAI_API_BASE (optional)
- TEC_OPENAI_MODEL (optional)
- AZURE_OPENAI_ENDPOINT / AZURE_OPENAI_KEY / AZURE_OPENAI_VERSION / AZURE_OPENAI_DEPLOYMENT_NAME (optional)

Create your local file:

```bash
cp .env.example .env
# then edit .env and fill values
```

## Naming guidance
- Prefer service-prefixed names: `TEC_SPOTIFY_CLIENT_ID`, `TEC_SPOTIFY_CLIENT_SECRET` in WordPress.
- For GitHub Actions, keep names simple and UPPER_SNAKE_CASE: `OPENAI_API_KEY`, `GITHUB_CLIENT_ID`.
- Never commit secrets. `.gitignore` already excludes `.env*` and `secrets/`.

## Why not GitHub Secrets for Spotify?
The WordPress plugin runs inside your WP host; its config should live with the site (in `wp-config.php`). GitHub Secrets are best for your CI/CD pipeline and static front-end builds. If you add a workflow that needs Spotify (e.g., batch analytics), you can add separate CI-only `SPOTIFY_CLIENT_ID`/`SPOTIFY_CLIENT_SECRET` to GitHub.

## Verification checklist
- [ ] WordPress: `wp-config.php` contains Spotify constants; `/wp-json/tec/v1/resonance` works.
- [ ] Front-end: no Spotify secrets in bundled JS.
- [ ] GitHub: Actions secrets added; referenced via `${{ secrets.NAME }}` in workflows.
- [ ] Local: `.env` exists; never committed.

## SharePoint / Microsoft Graph app registration (for future integration)

If you plan to integrate SharePoint or Graph API calls:

1. In Microsoft Entra ID → App registrations → New registration
	- Name your app, choose "Accounts in this organizational directory only"
	- Record Application (client) ID and Directory (tenant) ID
2. Certificates & secrets → New client secret
	- Record the Value (you'll never see it again)
3. API permissions → Add a permission → Microsoft Graph
	- Recommended least privilege: Sites.Selected (Application permission)
	- Alternative broad: Files.ReadWrite.All (Application) if absolutely necessary
	- Grant admin consent
4. Optional: Authentication → Add a Redirect URI if you'll run delegated auth flows
5. Store values:
	- In GitHub Actions: `SHAREPOINT_CLIENT_ID`, `SHAREPOINT_TENANT_ID`, `SHAREPOINT_CLIENT_SECRET`
	- In WordPress (if needed server-side): define constants in `wp-config.php` and keep calls server-side

For Sites.Selected, you must assign site permissions per site using Microsoft Graph to approve the app for specific sites.

---

## WordPress.com deploy: connect, artifact, SSH (optional)

There are two supported ways to deploy code to your WordPress.com site.

### A) Simple “artifact” deployments (recommended)

What it does: WordPress.com pulls a GitHub Actions artifact named `wpcom` from this repo and places it into your destination directory (configured in the WP.com UI).

Repo status: We ship `.github/workflows/wpcom.yml`. It uploads `apps/wordpress/tec-tgcr/` as `wpcom` on every push to `main` (and manual runs).

Steps on WordPress.com (Site → Hosting → Deployments → Connect a repository):

1) Select repository: `TEC-The-ELidoras-Codex/tec-tgcr`.
2) Deployment branch: `main`.
3) Destination directory: `/wp-content/plugins/tec-tgcr`.
4) Deployment mode: Simple.
5) Choose “Create new workflow” if prompted (we already committed one). Ensure artifact name is `wpcom`.
6) Save. After your next push, the plugin will deploy to that folder. Proof-of-life route will be:
	- `https://YOURDOMAIN/wp-json/tec-tgcr/v1/ping`

No secrets are required for this mode; WP.com pulls from GitHub directly.

### B) SSH deployments (manual, optional)

Use when you need to push files yourself, or for non‑standard hosts. We ship `.github/workflows/wpcom-ssh-deploy.yml` which syncs `apps/wordpress/tec-tgcr/` to a remote path.

Required GitHub Secrets:

- `WPCOM_SSH_HOST` → e.g., `ssh.wp.com`
- `WPCOM_SSH_PORT` → optional, default `22`
- `WPCOM_SSH_USER` → e.g., `elidorascodexdotcom.wordpress.com`
- `WPCOM_SSH_PRIVATE_KEY` → contents of your private key (PEM). Add passphrase only if your runner supports it.
- `WPCOM_SSH_TARGET` → absolute path, e.g., `/wp-content/plugins/tec-tgcr`

Run it manually in GitHub Actions (workflow dispatch). It performs an rsync:

`apps/wordpress/tec-tgcr/` → `$WPCOM_SSH_USER@$WPCOM_SSH_HOST:$WPCOM_SSH_TARGET/`

Local SSH test from Windows PowerShell (adjust username/host):

```powershell
ssh elidorascodexdotcom.wordpress.com@ssh.wp.com
```

If connection succeeds, you can list the target directory and verify the plugin files exist.

---

## GitHub Secrets Cheat Sheet

Add in GitHub → Settings → Secrets and variables → Actions (organization or repo scope as appropriate).

Core (builds/tests):
- `OPENAI_API_KEY` — used by notebooks/tests or agents during CI.
- `LUMINAI_API_URL` — base URL for your WP agent proxy, e.g., `https://elidorascodex.com/wp-json/tec/v1/agent`.

WordPress.com SSH (optional):
- `WPCOM_SSH_HOST` = `ssh.wp.com`
- `WPCOM_SSH_USER` = `elidorascodexdotcom.wordpress.com`
- `WPCOM_SSH_PORT` = `22` (optional)
- `WPCOM_SSH_PRIVATE_KEY` = private key text (PEM)
- `WPCOM_SSH_TARGET` = `/wp-content/plugins/tec-tgcr`

Microsoft Graph (if used):
- `SHAREPOINT_CLIENT_ID`, `SHAREPOINT_TENANT_ID`, `SHAREPOINT_CLIENT_SECRET`

Front-end only (safe for public build envs):
- Avoid placing sensitive tokens here unless the app runs server-side. Prefer the WP proxy for calls that require secrets.

WordPress server constants (in `wp-config.php` — not GitHub):

```php
define('TEC_SPOTIFY_CLIENT_ID', '...');
define('TEC_SPOTIFY_CLIENT_SECRET', '...');
// Optional OpenAI/Azure keys for server-side agent if used on WP
define('TEC_OPENAI_API_KEY', '...');
// Azure variant
// define('AZURE_OPENAI_ENDPOINT', 'https://<name>.openai.azure.com');
// define('AZURE_OPENAI_KEY', '...');
// define('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o-mini');
```

Verification:
- WP.com Deployments page shows successful runs.
- Visit `/wp-json/tec-tgcr/v1/ping` to confirm plugin is active.
- No secrets are printed in browser console or page source.

### WP.com SSH quick-setup (your site details)

From Hosting → Settings → SFTP/SSH on WordPress.com:

- Host: `ssh.wp.com` → set GitHub secret `WPCOM_SSH_HOST=ssh.wp.com`
- User: `elidorascodexdotcom.wordpress.com` → set `WPCOM_SSH_USER=elidorascodexdotcom.wordpress.com`
- Port: `22` → set `WPCOM_SSH_PORT=22`
- Target path: `/wp-content/plugins/tec-tgcr` → set `WPCOM_SSH_TARGET=/wp-content/plugins/tec-tgcr`

Generate an SSH key on Windows and add the private key to GitHub Secrets:

```powershell
# Create a new keypair (ed25519 recommended)
ssh-keygen -t ed25519 -C "wpcom-deploy" -f "$env:USERPROFILE\.ssh\wpcom_deploy"

# Print the public key (record it for reference)
Get-Content "$env:USERPROFILE\.ssh\wpcom_deploy.pub"

# Copy the private key into GitHub secret WPCOM_SSH_PRIVATE_KEY
Get-Content "$env:USERPROFILE\.ssh\wpcom_deploy" | Set-Clipboard
```

Run the manual SSH workflow:

1) GitHub → Actions → "WP.com SSH Deploy (manual)" → Run workflow.
2) Confirm logs show rsync to `$WPCOM_SSH_USER@$WPCOM_SSH_HOST:$WPCOM_SSH_TARGET/`.
3) Verify files on the host via SSH:

```powershell
ssh elidorascodexdotcom.wordpress.com@ssh.wp.com
ls -la /wp-content/plugins/tec-tgcr
```

Verification checklist (SSH mode):

- [ ] Workflow completed successfully.
- [ ] Files exist at `/wp-content/plugins/tec-tgcr`.
- [ ] Endpoint `https://YOURDOMAIN/wp-json/tec-tgcr/v1/ping` returns `{ ok: true }`.
- [ ] Shortcode `[tec_tgcr_ping]` renders a link to the ping route.
- [ ] PD citations endpoint works: `https://YOURDOMAIN/wp-json/tec-tgcr/v1/citation?persona=luminai`.
