# Environment & Secrets Checklist (Agent + Local)

This aligns your Agent platform config and local `.env.local` with TEC-TGCR conventions. Touches ψʳ (structure) and Φᴱ (capacity) by removing config drift.

---

## What goes where

- Environment variables (non-sensitive; feature flags, IDs, public URLs)
  - ENVIRONMENT, DEBUG
  - AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID
  - REACT_APP_LUMINAI_API_URL, REACT_APP_LUMINAI_WS_URL
  - SHAREPOINT_SITE_ID
  - Optional toggles: AZURE_SUPPORT_ENABLED, ENTRA_GLOBAL_ADMIN_ENABLED, TEC_BILLING_ALERT_THRESHOLD
- Secrets (sensitive; tokens/keys/passwords)
  - TEC_OPENAI_API_KEY, ANTHROPIC_API_KEY, XAI_API_KEY (optional)
  - TEC_WPCOM_API_PASS
  - WPCOM_SSH_PRIVATE_KEY (if you deploy over SSH)
  - COINMC_API_KEY, COINDESK_API_KEY, CIVITAI_API_KEY, WORLDANVIL_API_KEY, SPOTIFY_CLIENT_ID/SECRET, etc.

Avoid placing secrets in variables used by the browser (no `REACT_APP_*` for secrets).

---

## Recommended set

Environment variables:

- ENVIRONMENT=development|staging|production
- DEBUG=true|false
- AZURE_TENANT_ID={tenant-guid}
- AZURE_SUBSCRIPTION_ID={subscription-guid}
- REACT_APP_LUMINAI_API_URL=[https://api.tec-codex.com](https://api.tec-codex.com)
- REACT_APP_LUMINAI_WS_URL=wss://ws.tec-codex.com
- SHAREPOINT_SITE_ID=https://{tenant}.sharepoint.com/sites/{site}
- Optional:
  - AZURE_SUPPORT_ENABLED=false
  - ENTRA_GLOBAL_ADMIN_ENABLED=false
  - TEC_BILLING_ALERT_THRESHOLD=100

Secrets:

- TEC_OPENAI_API_KEY, ANTHROPIC_API_KEY
- TEC_WPCOM_API_PASS
- XAI_API_KEY (optional), CIVITAI_API_KEY, WORLDANVIL_API_KEY
- SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET (server-side only)

Notes:

- Keep `.env.local` as your source of truth for local dev; it’s already gitignored.
- Mirror the same names into your Agent platform’s Environment and Secrets settings.

---

## Validate your setup

Run the validator from repo root (Windows PowerShell 5.1+):

```powershell
./scripts/check_env.ps1
```

It will:

- Check presence of required env vars and secrets (without printing secrets)
- Test Azure CLI session (tenant/subscription)
- Probe public endpoints and DNS for common services

If Azure isn’t logged in, do:

```powershell
az login --tenant $env:AZURE_TENANT_ID; az account set --subscription $env:AZURE_SUBSCRIPTION_ID
```

---

## Common pitfalls and fixes

- 403 with Microsoft Graph SDK — Use the Azure CLI token path in scripts (we do `az rest`) or consent the right scopes to the SDK (e.g., Directory.ReadWrite.All + admin consent).
- Directory roles missing — They may be inactive. Our `azure_take_control.ps1` will activate role templates and add you if you pass `-AssignDirectoryRoles` (requires sufficient privilege/PIM).
- Duplicate Azure OpenAI keys — Keep only the set you actually use; avoid both `AZURE_OPENAI_*` and `OPENAI_*` unless needed.
- WP.com credentials — Use App Password (REST) or SSH key (SFTP). Don’t put private keys into Environment variables; store them as Secrets.

---

## Related

- `./scripts/azure_take_control.ps1` — Assigns Owner + UAA at subscription scope; optional Entra roles.
- `docs/SECRETS.md` — Additional guidance on secret handling.
