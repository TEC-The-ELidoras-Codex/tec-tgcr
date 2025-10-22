# Quick-Fill GitHub Secrets — The Elidoras Codex

Copy-paste ready values for your WordPress.com deployment secrets.

## Your Site Info (From Screenshots)

- **Site URL:** `elidorascodex.com`
- **SFTP Host:** `sftp.wp.com`
- **SFTP Port:** `22`
- **SFTP Username:** `elidorascodexdotcom.wordpress.com`
- **SSH Connection:** `ssh elidorascodexdotcom.wordpress.com@ssh.wp.com`

---

## SSH Deploy Secrets (5 Required)

| Secret Name | Value to Paste |
|-------------|---------------|
| `WPCOM_SSH_HOST` | `sftp.wp.com` |
| `WPCOM_SSH_PORT` | `22` |
| `WPCOM_SSH_USER` | `elidorascodexdotcom.wordpress.com` |
| `WPCOM_SSH_PRIVATE_KEY` | *(paste your full private key from `~/.ssh/id_ed25519`)* |
| `WPCOM_SSH_TARGET` | `/htdocs/wp-content/plugins/tec-tgcr` |

---

## SFTP Deploy Secrets (5 Required)

| Secret Name | Value to Paste |
|-------------|---------------|
| `WPCOM_SFTP_HOST` | `sftp.wp.com` |
| `WPCOM_SFTP_PORT` | `22` |
| `WPCOM_SFTP_USER` | `elidorascodexdotcom.wordpress.com` |
| `WPCOM_SFTP_PASSWORD` | *(your SFTP password from WordPress.com → Hosting → SFTP/SSH)* |
| `WPCOM_SFTP_TARGET` | `/htdocs/wp-content/plugins/tec-tgcr/` |

---

## What You Need to Get/Generate

### 1. SSH Private Key (`WPCOM_SSH_PRIVATE_KEY`)

**If you already have one (from your screenshot, you do: "elidorascodex-default"):**

Find your local private key file (usually `~/.ssh/id_ed25519` or similar) and copy its entire content:

```bash
cat ~/.ssh/id_ed25519
```

Or on Windows:

```powershell
Get-Content ~\.ssh\id_ed25519 -Raw
```

**If you need to generate a new one:**

```bash
ssh-keygen -t ed25519 -C "github-deploy-elidorascodex"
```

- Save to default location
- **Leave passphrase empty** (for CI/CD)
- Upload the **public key** (`.pub` file) to WordPress.com under **Hosting → SFTP/SSH → SSH Keys**

### 2. SFTP Password (`WPCOM_SFTP_PASSWORD`)

Get this from your WordPress.com dashboard:

1. Go to: **Hosting → SFTP/SSH**
2. Look for the **PASSWORD** field (see your first screenshot)
3. Copy the password (or reset it if needed)

**Note:** This is **different** from your WordPress.com login password.

---

## Yes, They're Both the Same

You asked great questions—here are the answers:

### Port: Yes, both 22

- SSH uses port 22
- SFTP uses port 22
- They're the same because SFTP runs over SSH

### User: Yes, same username

- SSH user: `elidorascodexdotcom.wordpress.com`
- SFTP user: `elidorascodexdotcom.wordpress.com`
- Both connect to the same account

### Host: Slightly different display, same server

- Your screenshot shows: `sftp.wp.com`
- Documentation often says: `sftp.wordpress.com`
- **Use `sftp.wp.com`** (what WordPress.com shows you)

### Connection Command vs Username

- **CONNECTION COMMAND:** `ssh elidorascodexdotcom.wordpress.com@ssh.wp.com`
- **USERNAME (for secrets):** `elidorascodexdotcom.wordpress.com`

The connection command includes `@ssh.wp.com` at the end—that's the full `user@host` format for SSH. But for the GitHub secrets, you only need the **username part** before the `@`.

---

## Target Path

The plugin directory on your WordPress.com server is:

```text
/htdocs/wp-content/plugins/tec-tgcr
```

- For SSH deploy: **no trailing slash** → `/htdocs/wp-content/plugins/tec-tgcr`
- For SFTP deploy: **with trailing slash** → `/htdocs/wp-content/plugins/tec-tgcr/`

---

## Security Note (You're Right!)

The hostname, port, and username aren't secrets—they're just connection coordinates. The **actual security** comes from:

- Your SSH **private key** (never share this)
- Your SFTP **password** (reset if compromised)

WordPress.com has your back on the infrastructure side. Your private key stays in GitHub Secrets (encrypted) and is never exposed in logs.

---

## Copy-Paste Checklist

Go to: `https://github.com/Elidorascodex/tec-tgcr/settings/secrets/actions`

Add these secrets (click **New repository secret** for each):

### SSH Secrets (if using SSH deploy)

- [ ] `WPCOM_SSH_HOST` = `sftp.wp.com`
- [ ] `WPCOM_SSH_PORT` = `22`
- [ ] `WPCOM_SSH_USER` = `elidorascodexdotcom.wordpress.com`
- [ ] `WPCOM_SSH_PRIVATE_KEY` = *(paste full private key)*
- [ ] `WPCOM_SSH_TARGET` = `/htdocs/wp-content/plugins/tec-tgcr`

### SFTP Secrets (if using SFTP password deploy)

- [ ] `WPCOM_SFTP_HOST` = `sftp.wp.com`
- [ ] `WPCOM_SFTP_PORT` = `22`
- [ ] `WPCOM_SFTP_USER` = `elidorascodexdotcom.wordpress.com`
- [ ] `WPCOM_SFTP_PASSWORD` = *(your SFTP password)*
- [ ] `WPCOM_SFTP_TARGET` = `/htdocs/wp-content/plugins/tec-tgcr/`

---

**After adding all secrets, go to Actions → WP.com SSH Deploy (manual) → Run workflow to test!**

*Where gravity curves spacetime, resonance curves meaning-space.*
