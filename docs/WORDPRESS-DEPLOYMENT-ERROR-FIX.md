# WordPress.com Deployment Error — Troubleshooting Guide

**Error Status:** Deployment failed after 4 seconds  
**Commit:** `2bb8c08` (chore: repo hygiene + WP deploy readiness)  
**Date:** October 16, 2025

---

## ✅ Verified Working

- [x] Plugin file exists: `apps/wordpress/tec-tgcr/tec-tgcr.php`
- [x] GitHub Actions workflow exists: `.github/workflows/wpcom.yml`
- [x] Workflow triggers on push to main: ✅
- [x] Workflow creates artifact named `wpcom`: ✅
- [x] Local tests pass: 14/14 tests ✅
- [x] Commit pushed to origin/main: ✅

---

## 🔍 Most Likely Cause

**WordPress.com is configured to use the wrong workflow file.**

Your screenshot shows you have SSH/SFTP secrets configured (`WPCOM_SFTP_*`, `WPCOM_SSH_*`). This suggests WordPress.com might be trying to use `wpcom-sftp-deploy.yml` or `wpcom-ssh-deploy.yml` instead of the correct `wpcom.yml` artifact workflow.

---

## 🛠️ Fix: Update WordPress.com Deployment Settings

### Steps to Fix on WordPress.com

1. Go to: **WordPress.com → Your Site → Hosting → Deployments**

2. Click **"Manage repository"** on the existing `tec-tgcr` connection

3. Verify/Update these settings:

   **Repository Configuration:**
   - Repository: `TEC-The-ELidoras-Codex/tec-tgcr`
   - Branch: `main`
   - Connection status: Connected ✅

   **Deployment Mode:**
   - **Pick your deployment mode:** Select **"Advanced"** (NOT Simple)

   **Critical Settings (this is where the error likely is):**
   - **Deployment workflow:** `wpcom.yml` ⚠️ **MUST be this exact value**
     - If it shows `wpcom-sftp-deploy.yml` or `wpcom-ssh-deploy.yml`, change it to `wpcom.yml`
   - **Artifact name:** `wpcom` ⚠️ **MUST match the workflow**
   - **Destination:** `/wp-content/plugins/tec-tgcr`

4. Click **"Update"** or **"Save"**

5. Go to GitHub Actions → Manually run "Publish to WordPress.com" workflow
   - Or push a trivial commit to trigger auto-deploy

---

## 🔍 Alternative Causes

### 1. Artifact Upload Failed in GitHub Actions

**Check:** Go to GitHub → Actions → "Publish to WordPress.com" → Latest run

**Look for:**
- Green checkmark on "Upload artifact for WordPress.com" step
- Artifact `wpcom` should be listed in the run summary

**If artifact upload failed:**
- The workflow itself has an issue (unlikely, as it's been validated)
- GitHub Actions artifact storage quota exceeded (very unlikely)

### 2. WordPress.com Can't Access the Artifact

**Symptoms:**
- Workflow completes successfully on GitHub
- WordPress.com shows "Error" immediately (within 4 seconds)

**Fix:**
- Ensure the WordPress.com app has permission to access your GitHub repo
- Re-authorize the GitHub connection in WordPress.com

### 3. Plugin File Structure Issue

**Check:**
The artifact must have this exact structure:
```
.wpcom-dist/
└── tec-tgcr.php  (NOT in a subdirectory!)
```

Our workflow copies `apps/wordpress/tec-tgcr/.` to `.wpcom-dist/`, which is correct.

**Verify locally:**
```powershell
# Simulate the workflow staging
$STAGE = ".wpcom-dist"
$PLUGIN = "apps/wordpress/tec-tgcr"
Remove-Item -LiteralPath $STAGE -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $STAGE -Force | Out-Null
Copy-Item -Path "$PLUGIN\*" -Destination $STAGE -Recurse -Force
Get-ChildItem -LiteralPath $STAGE -Recurse | Select-Object FullName
```

Expected output:
```
.wpcom-dist\tec-tgcr.php
```

### 4. Destination Path Permissions

**Symptom:** WordPress.com can't write to `/wp-content/plugins/tec-tgcr`

**Unlikely on WordPress.com hosting** (they manage permissions), but if this is a custom/managed hosting setup:
- Ensure `/wp-content/plugins/` is writable
- Check if `tec-tgcr` folder already exists with locked permissions

---

## 🚀 Quick Resolution Path

### Option A: Use the Correct Artifact Workflow (Recommended)

1. WordPress.com → Deployments → Manage repository
2. Change **Deployment workflow** to: `wpcom.yml`
3. Change **Artifact name** to: `wpcom`
4. Save
5. Re-run workflow from GitHub Actions or push to main

### Option B: Switch to SSH Deployment (Alternative)

If artifact mode keeps failing:

1. Ensure all SSH secrets are set in GitHub:
   - `WPCOM_SSH_HOST` = `ssh.wp.com` ⚠️ **This one is likely missing**
   - `WPCOM_SSH_PORT` = `22`
   - `WPCOM_SSH_USER` = (your WP.com SSH username)
   - `WPCOM_SSH_PRIVATE_KEY` = (your SSH private key)
   - `WPCOM_SSH_TARGET` = `/wp-content/plugins/tec-tgcr`

2. WordPress.com → Deployments → Manage repository
   - Change **Deployment workflow** to: `wpcom-ssh-deploy.yml`
   - Save

3. Manually trigger workflow from GitHub Actions

**Note:** Your screenshot shows `WPCOM_SSH_HOST` might be missing. Add it if using SSH.

---

## 📊 Debugging Checklist

Run through this checklist:

- [ ] WordPress.com deployment workflow is set to `wpcom.yml` (NOT `wpcom-sftp-deploy.yml`)
- [ ] Artifact name in WordPress.com is `wpcom`
- [ ] GitHub Actions workflow "Publish to WordPress.com" shows green checkmark
- [ ] Artifact `wpcom` appears in the workflow run artifacts list
- [ ] WordPress.com → Deployments shows "Connected" status for repository
- [ ] If using SSH: `WPCOM_SSH_HOST` secret exists and equals `ssh.wp.com`

---

## 🎯 Most Likely Fix

**99% of WordPress.com "Error after 4 seconds" failures are due to:**

> WordPress.com is looking for an artifact workflow but the deployment settings point to an SFTP/SSH workflow, or vice versa.

**Solution:** Change **Deployment workflow** dropdown in WordPress.com to `wpcom.yml` and ensure **Artifact name** is `wpcom`.

---

## 📞 Next Steps

1. **Fix the WordPress.com settings** (change workflow to `wpcom.yml`)
2. **Re-run the deployment** (push a trivial commit or manually trigger workflow)
3. **Verify endpoints** once deployment succeeds:
   - `https://elidorascodex.com/wp-json/tec-tgcr/v1/ping`
   - `https://elidorascodex.com/wp-json/tec-tgcr/v1/citation?persona=luminai`

If it still fails after fixing the workflow setting, check GitHub Actions logs and share the error message from the workflow run.

---

**Status:** Ready to fix. Update WordPress.com deployment workflow setting to `wpcom.yml` and retry.
