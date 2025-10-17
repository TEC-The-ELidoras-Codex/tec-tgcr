# WordPress.com Ops — Packaging and Deploy

This repo includes three GitHub Actions for WordPress.com:

- Build artifact (auto on main): `.github/workflows/wpcom.yml`
- Manual SSH deploy: `.github/workflows/wpcom-ssh-deploy.yml`
- Manual SFTP deploy: `.github/workflows/wpcom-sftp-deploy.yml`

## Secrets

Set these repository or organization secrets:

- WPCOM_SSH_HOST, WPCOM_SSH_PORT (default 22), WPCOM_SSH_USER, WPCOM_SSH_PRIVATE_KEY, WPCOM_SSH_TARGET
- WPCOM_SFTP_HOST, WPCOM_SFTP_PORT (default 22), WPCOM_SFTP_USER, WPCOM_SFTP_PASSWORD, WPCOM_SFTP_TARGET

The plugin path expected is `apps/wordpress/tec-tgcr/` with entry file `tec-tgcr.php`.

## Build Artifact

On push to `main`, the workflow stages the plugin into `.wpcom-dist/wp-content/plugins/tec-tgcr/` and uploads it as the `wpcom` artifact. If a step fails, the job prints a directory tree for diagnosis.

## Manual Deploy

- SSH: uses rsync to sync `apps/wordpress/tec-tgcr/` to `$WPCOM_SSH_TARGET`.
- SFTP: uses `SamKirkland/FTP-Deploy-Action@v4` to push the same folder to `$WPCOM_SFTP_TARGET`.

## Verification

After deploy, verify:

- WP REST ping: `/wp-json/tec-tgcr/v1/ping` (if route enabled)
- Plugin visible in WP Admin → Plugins → TEC TGCR

---
[AIRTH] Packaging protocol documented. Proceed to validate secrets and run.
