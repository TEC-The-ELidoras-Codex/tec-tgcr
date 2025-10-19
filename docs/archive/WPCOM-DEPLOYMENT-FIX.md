# WordPress.com Deployment Fix — 404 & Workflow Errors

## Problem

You're seeing these errors in WordPress.com Deployments:

- ❌ **"The workflow is triggered on push"**
- ❌ **"The uploaded artifact has the required name"**

And the REST endpoint returns 404:

```json
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}
```

## Root Cause

Your WordPress.com deployment settings point to the **wrong workflow**:

- **Currently selected**: `wpcom-sftp-deploy.yml`
  - This workflow only runs on manual trigger (`workflow_dispatch`)
  - It does NOT create an artifact named `wpcom`
  - It does NOT trigger on push

- **Should be**: `wpcom.yml`
  - Triggers automatically on push to `main`
  - Creates artifact named `wpcom`
  - No secrets required

## Fix (2 minutes)

### Step 1: Update WordPress.com Deployment Settings

1. Go to [WordPress.com](https://wordpress.com/github-deployments/elidorascodex.com/manage/5573)
2. You should see "Manage a repository" page for `TEC-The-ELidoras-Codex/tec-tgcr`
3. Under **"Pick your deployment mode"**:
   - Select **Advanced** (for full workflow control)
4. Under **"Deployment workflow"** dropdown:
   - Change from `wpcom-sftp-deploy.yml` → **`wpcom.yml`** ⚠️
5. Confirm **"Artifact name"** is set to: `wpcom`
6. Click **Update** or **Save**

### Step 2: Trigger Deployment

Option A (Recommended): Push a small commit

```powershell
# In your tec-tgcr repo
git commit --allow-empty -m "trigger: WordPress.com deployment with correct workflow"
git push origin main
```

Option B: Run workflow manually

1. Go to [GitHub Actions](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/actions)
2. Select **"Publish to WordPress.com"** workflow
3. Click **Run workflow** → **Run workflow**

### Step 3: Verify

After ~1-2 minutes:

1. Check WordPress.com Deployments page for **green checkmark** ✅
2. Test the ping endpoint: <https://Elidorascodex.com/wp-json/tec-tgcr/v1/ping>
   - Should return: `{"ok":true,"message":"TEC:TGCR is alive",...}`
3. Test citation: <https://Elidorascodex.com/wp-json/tec-tgcr/v1/citation?persona=luminai>
   - Should return a JSON quote

If you still see 404:

- In WP Admin → Plugins, ensure **"TEC TGCR"** is active
- Go to Settings → Permalinks → click **Save Changes** (flushes rewrite rules)
- Clear any caching (if you have a caching plugin)

## Why This Happened

WordPress.com offers three deployment workflows in your repo:

1. **`wpcom.yml`** ✅ — Simple artifact mode (recommended)
   - Auto-triggered on push to `main`
   - Creates `wpcom` artifact
   - No secrets required

2. **`wpcom-ssh-deploy.yml`** — Manual SSH deploy
   - Only runs when you click "Run workflow" in GitHub Actions
   - Requires SSH secrets
   - For advanced use cases

3. **`wpcom-sftp-deploy.yml`** — Manual SFTP deploy
   - Only runs when you click "Run workflow" in GitHub Actions
   - Requires SFTP secrets
   - For advanced use cases

You selected #3 by accident. Use #1 for automatic, zero-config deployment.

## Summary

- ✅ Change workflow dropdown to `wpcom.yml`
- ✅ Push a commit or run the workflow manually
- ✅ Wait ~2 minutes
- ✅ Test <https://Elidorascodex.com/wp-json/tec-tgcr/v1/ping>

That's it. The plugin will deploy and the 404 will be gone.
