# WordPress Plugin Deployment Checklist

## Current Status: ✅ READY

### Plugin: `apps/wordpress/tec-tgcr/tec-tgcr.php`

- ✅ Plugin header complete (Name, Description, Version, Author)
- ✅ REST endpoints implemented:
  - `/wp-json/tec-tgcr/v1/ping` → proof-of-life JSON response
  - `/wp-json/tec-tgcr/v1/citation?persona=<name>` → public-domain quotes
- ✅ Shortcodes implemented:
  - `[tec_tgcr_ping]` → link to ping endpoint
  - `[tec_tgcr_citation persona="luminai"]` → server-side fetched PD quote
  - `[tec_tgcr_model src="..." autoplay="1" camera-controls="1"]` → GLB/GLTF embed via model-viewer
- ✅ No hardcoded secrets; relies on PD content pool only
- ✅ Security: ABSPATH check, sanitized inputs, permission callbacks

### Deployment Workflow: `.github/workflows/wpcom.yml`

- ✅ Artifact mode (Simple deployment)
- ✅ Uploads `wpcom` artifact from `apps/wordpress/tec-tgcr/`
- ✅ Triggers on push to `main` + manual workflow_dispatch
- ✅ No secrets required (WP.com pulls artifact directly)

### Optional SSH Workflow: `.github/workflows/wpcom-ssh-deploy.yml`

- ✅ Manual workflow_dispatch only
- ⚠️ **Missing secret**: `WPCOM_SSH_HOST` (see below)
- ✅ Other secrets set: `WPCOM_SSH_USER`, `WPCOM_SSH_PORT`, `WPCOM_SSH_PRIVATE_KEY`, `WPCOM_SSH_TARGET`

### Optional SFTP Workflow: `.github/workflows/wpcom-sftp-deploy.yml`

- ✅ Manual workflow_dispatch only
- ℹ️ Requires `WPCOM_SFTP_*` secrets (not currently used; Simple mode preferred)

---

## Action Items

### 1. Add Missing Secret (if using SSH deploy)

Go to GitHub → Settings → Secrets and variables → Actions → Repository secrets:

- Add `WPCOM_SSH_HOST` = `ssh.wp.com`

### 2. WordPress.com Configuration (if not already done)

Site → Hosting → Deployments → Connect a repository:

- Repository: `TEC-The-ELidoras-Codex/tec-tgcr`
- Branch: `main`
- Destination: `/wp-content/plugins/tec-tgcr`
- Mode: **Advanced** (for full control)
- **Deployment workflow**: `wpcom.yml` ⚠️ **MUST use this workflow, not wpcom-sftp-deploy.yml**
- Artifact name: `wpcom`

### 3. Verify Deployment

After next push to `main` (or manual "Publish to WordPress.com" workflow run):

- Check WP.com Deployments page for success
- Visit `https://YOURDOMAIN/wp-json/tec-tgcr/v1/ping` (should return JSON `{ "ok": true, ... }`)
- Visit `https://YOURDOMAIN/wp-json/tec-tgcr/v1/citation?persona=luminai` (should return PD quote)
- Test shortcode on a page: `[tec_tgcr_ping]`
- Test shortcode on a page: `[tec_tgcr_citation persona="arcadia"]`
- Test model embed (if you have a GLB uploaded): `[tec_tgcr_model src="/wp-content/uploads/test.glb"]`

### 4. Activate Plugin (if needed)

- In WP Admin → Plugins, ensure "TEC TGCR – Agent & Tools Bootstrap" is active
- No additional configuration required; plugin is self-contained

---

## No Other WordPress Files Needed

The plugin is minimal and self-contained. You do NOT need:

- ❌ Additional PHP files
- ❌ wp-config.php changes (no secrets used)
- ❌ Database setup
- ❌ Theme modifications
- ❌ Custom post types or taxonomies

---

## Troubleshooting WordPress.com Deployment Errors

### Error: "The workflow is triggered on push"

**Cause**: You selected a workflow that only runs on `workflow_dispatch` (manual trigger).
**Fix**: In WordPress.com → Deployments → Manage repository:

- Change **Deployment workflow** from `wpcom-sftp-deploy.yml` to `wpcom.yml`
- This workflow is triggered on push to `main` and creates the required artifact.

### Error: "The uploaded artifact has the required name"

**Cause**: The selected workflow doesn't create an artifact named `wpcom`.
**Fix**: Same as above—use `wpcom.yml` which creates the artifact.

### Quick Fix Steps

1. Go to WordPress.com → Your Site → Hosting → Deployments
2. Click "Manage a repository" on your existing connection
3. Under "Pick your deployment mode", ensure **Advanced** is selected
4. Change **Deployment workflow** dropdown to: `wpcom.yml`
5. **Artifact name** should be: `wpcom`
6. Click **Update** (or **Save**)
7. Push a commit or manually run "Publish to WordPress.com" workflow in GitHub Actions

---

## Next Steps After Deployment

1. **Push to `main`** (or run "Publish to WordPress.com" workflow manually)
2. **Verify ping endpoint** responds with JSON
3. **Test shortcodes** on a page or post
4. **Optional**: Add `WPCOM_SSH_HOST` secret if you want SSH deploy as backup

**Recommended**: Stick with Simple artifact mode; it's automatic and requires no secrets.
