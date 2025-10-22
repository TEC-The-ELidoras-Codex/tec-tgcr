# GitHub Repository Secrets Setup Guide

This guide shows you **exactly** where to add GitHub secrets for WordPress.com deployment workflows.

## Quick Navigation

- [Where to Add Secrets](#where-to-add-secrets)
- [Required Secrets List](#required-secrets-list)
- [SSH Deploy Secrets](#ssh-deploy-secrets)
- [SFTP Deploy Secrets](#sftp-deploy-secrets)
- [How to Get WordPress.com Credentials](#how-to-get-wordpresscom-credentials)
- [Validation Steps](#validation-steps)

---

## Where to Add Secrets

### Step 1: Go to Your Repository Settings

1. Open your GitHub repository: `https://github.com/Elidorascodex/tec-tgcr`
2. Click the **Settings** tab (top navigation)
3. In the left sidebar, find **Security** section
4. Click **Secrets and variables** → **Actions**

### Step 2: Add a New Secret

1. Click the **New repository secret** button (green button, top right)
2. Enter the **Name** (exactly as shown below, case-sensitive)
3. Paste the **Value** (from your WordPress.com credentials)
4. Click **Add secret**
5. Repeat for each secret below

---

## Required Secrets List

### For SSH Deploy (`wpcom-ssh-deploy.yml`)

You need **5 secrets** for SSH-based deployment:

| Secret Name | Description | Example Value | Required |
|------------|-------------|---------------|----------|
| `WPCOM_SSH_HOST` | WordPress.com SFTP hostname | `sftp.wordpress.com` | ✅ Yes |
| `WPCOM_SSH_PORT` | SSH/SFTP port | `22` | ⚠️ Optional (defaults to 22) |
| `WPCOM_SSH_USER` | Your WordPress.com username | `yoursite@sftp.wordpress.com` | ✅ Yes |
| `WPCOM_SSH_PRIVATE_KEY` | SSH private key (full content) | `-----BEGIN OPENSSH PRIVATE KEY-----`... | ✅ Yes |
| `WPCOM_SSH_TARGET` | Target directory on server | `/htdocs/wp-content/plugins/tec-tgcr` | ✅ Yes |

### For SFTP Deploy (`wpcom-sftp-deploy.yml`)

You need **5 secrets** for SFTP password-based deployment:

| Secret Name | Description | Example Value | Required |
|------------|-------------|---------------|----------|
| `WPCOM_SFTP_HOST` | WordPress.com SFTP hostname | `sftp.wordpress.com` | ✅ Yes |
| `WPCOM_SFTP_PORT` | SFTP port | `22` | ⚠️ Optional (defaults to 22) |
| `WPCOM_SFTP_USER` | Your WordPress.com username | `yoursite@sftp.wordpress.com` | ✅ Yes |
| `WPCOM_SFTP_PASSWORD` | SFTP password | `your-sftp-password` | ✅ Yes |
| `WPCOM_SFTP_TARGET` | Target directory on server | `/htdocs/wp-content/plugins/tec-tgcr/` | ✅ Yes |

---

## SSH Deploy Secrets

### 1. `WPCOM_SSH_HOST`

**What it is:** The hostname for WordPress.com SFTP access.

**How to get it:**

- WordPress.com Business/eCommerce plans: `sftp.wordpress.com`
- Check your WordPress.com dashboard under **Hosting → SFTP/SSH**

**Add to GitHub:**

```text
Name:  WPCOM_SSH_HOST
Value: sftp.wordpress.com
```

### 2. `WPCOM_SSH_PORT`

**What it is:** The SSH port (usually 22).

**How to get it:**

- Default: `22`
- Only change if WordPress.com specifies a different port

**Add to GitHub:**

```text
Name:  WPCOM_SSH_PORT
Value: 22
```

**Note:** Optional—workflow defaults to 22 if not set.

### 3. `WPCOM_SSH_USER`

**What it is:** Your WordPress.com SFTP username.

**How to get it:**

1. Go to WordPress.com → **Hosting** → **SFTP/SSH**
2. Copy the username (format: `yoursite@sftp.wordpress.com` or similar)

**Add to GitHub:**

```text
Name:  WPCOM_SSH_USER
Value: yoursite@sftp.wordpress.com
```

### 4. `WPCOM_SSH_PRIVATE_KEY`

**What it is:** Your SSH private key for passwordless authentication.

**How to generate it:**

If you don't have an SSH key pair:

```bash
ssh-keygen -t ed25519 -C "github-actions-deploy"
```

- Save to default location (e.g., `~/.ssh/id_ed25519`)
- Leave passphrase empty for CI/CD use
- **Public key** (`.pub` file): upload to WordPress.com
- **Private key** (no extension): add to GitHub secrets

**How to get the private key content:**

```bash
cat ~/.ssh/id_ed25519
```

Copy the **entire output**, including:

```text
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
...
(many lines)
...
-----END OPENSSH PRIVATE KEY-----
```

**Add to GitHub:**

```text
Name:  WPCOM_SSH_PRIVATE_KEY
Value: (paste the entire private key, including BEGIN/END lines)
```

**Upload public key to WordPress.com:**

1. Copy your public key: `cat ~/.ssh/id_ed25519.pub`
2. Go to WordPress.com → **Hosting** → **SFTP/SSH**
3. Add the public key under **SSH Keys**

### 5. `WPCOM_SSH_TARGET`

**What it is:** The full path to your plugin directory on the WordPress.com server.

**How to get it:**

- WordPress.com standard path: `/htdocs/wp-content/plugins/tec-tgcr`
- Check via SFTP to confirm the exact path

**Add to GitHub:**

```text
Name:  WPCOM_SSH_TARGET
Value: /htdocs/wp-content/plugins/tec-tgcr
```

---

## SFTP Deploy Secrets

### 1. `WPCOM_SFTP_HOST`

**Same as SSH:** `sftp.wordpress.com`

```text
Name:  WPCOM_SFTP_HOST
Value: sftp.wordpress.com
```

### 2. `WPCOM_SFTP_PORT`

**Same as SSH:** `22`

```text
Name:  WPCOM_SFTP_PORT
Value: 22
```

**Note:** Optional—workflow defaults to 22.

### 3. `WPCOM_SFTP_USER`

**Same as SSH user.**

```text
Name:  WPCOM_SFTP_USER
Value: yoursite@sftp.wordpress.com
```

### 4. `WPCOM_SFTP_PASSWORD`

**What it is:** Your SFTP password (not your WordPress login password).

**How to get it:**

1. Go to WordPress.com → **Hosting** → **SFTP/SSH**
2. Reset/copy your SFTP password (this is **different** from your WordPress.com login password)

**Add to GitHub:**

```text
Name:  WPCOM_SFTP_PASSWORD
Value: your-sftp-password-here
```

### 5. `WPCOM_SFTP_TARGET`

**Same as SSH target.**

```text
Name:  WPCOM_SFTP_TARGET
Value: /htdocs/wp-content/plugins/tec-tgcr/
```

**Note:** Include trailing slash for SFTP deploy.

---

## How to Get WordPress.com Credentials

### Access WordPress.com SFTP/SSH Settings

1. Log in to [WordPress.com](https://wordpress.com)
2. Select your site
3. Go to **Hosting** → **SFTP/SSH** (Business/eCommerce plans only)
4. You'll see:
   - **Hostname:** `sftp.wordpress.com`
   - **Port:** `22`
   - **Username:** `yoursite@sftp.wordpress.com` (or similar)
   - **Password:** Reset if needed
   - **SSH Keys:** Add your public key here

### Verify SFTP Access Locally First

Before adding secrets, test your credentials locally:

```bash
# Test SFTP with password
sftp -P 22 yoursite@sftp.wordpress.com

# Test SFTP with SSH key
sftp -i ~/.ssh/id_ed25519 -P 22 yoursite@sftp.wordpress.com
```

If successful, you'll see:

```text
Connected to sftp.wordpress.com.
sftp>
```

Navigate to confirm the plugin directory path:

```text
sftp> cd /htdocs/wp-content/plugins
sftp> ls
```

---

## Validation Steps

### After Adding All Secrets

1. **Check secrets are visible (values hidden):**
   - Go to **Settings** → **Secrets and variables** → **Actions**
   - You should see all secret names listed (values will be `***`)

2. **Test SSH Deploy Workflow:**
   - Go to **Actions** tab
   - Select **WP.com SSH Deploy (manual)**
   - Click **Run workflow** → **Run workflow**
   - Watch the logs for errors

3. **Test SFTP Deploy Workflow:**
   - Go to **Actions** tab
   - Select **WP.com SFTP Deploy (manual)**
   - Click **Run workflow** → **Run workflow**
   - Watch the logs for errors

### Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `Permission denied (publickey)` | SSH key not uploaded to WP.com | Upload public key to WordPress.com |
| `Host key verification failed` | Known hosts issue | Workflow handles this; check `ssh-keyscan` step logs |
| `Authentication failed` | Wrong password | Reset SFTP password in WordPress.com |
| `No such file or directory` | Wrong target path | Verify path via local SFTP session |

---

## Quick Checklist

Before triggering a deploy workflow:

- [ ] All 5 SSH secrets added (if using SSH deploy)
- [ ] All 5 SFTP secrets added (if using SFTP deploy)
- [ ] SSH public key uploaded to WordPress.com (if using SSH)
- [ ] SFTP credentials tested locally
- [ ] Target directory exists on WordPress.com server
- [ ] Artifact build workflow succeeded (creates the plugin ZIP)

---

## Security Notes

- **Never commit secrets to the repository** (they belong in GitHub Settings only)
- **Use SSH keys** instead of passwords when possible (more secure)
- **Rotate credentials** periodically
- **Limit secret access** to necessary workflows only (GitHub manages this automatically)

---

*Where gravity curves spacetime, resonance curves meaning-space.*
