# Local Secrets Handling

Keep credentials local and out of git. This repo already ignores `.env`, `.env.*` (except `.env.example`), and common key files.

## Quick Start: Set Up Your API Keys

1. **Copy the template**

```bash
cp .env.example .env.local
```

1. **Edit `.env.local`** with your actual keys

```bash
code .env.local
# Or: notepad .env.local
```

1. **Verify it's ignored by git**

```bash
git status
# .env.local should NOT appear in "Untracked files"
```

1. **Load secrets in your terminal**

```powershell
# PowerShell
.\scripts\load_env.ps1

# Or manually:
Get-Content .env.local | ForEach-Object {
  if ($_ -match '^(?<k>[^#=]+)=(?<v>.*)$') {
    [Environment]::SetEnvironmentVariable($Matches['k'].Trim(), $Matches['v'])
  }
}
```

## Your Current API Keys

Based on your message, you have:

| **Service** | **Variable Name** | **Used For** |
|-------------|-------------------|--------------|
| OpenAI | `TEC_OPENAI_API_KEY` | GPT-4, DALL-E, embeddings |
| Anthropic | `ANTHROPIC_API_KEY` | Claude (LuminAI conversations) |
| xAI | `XAI_API_KEY` | Grok (experimental) |
| WorldAnvil | `WORLDANVIL_API_KEY` | Lore integration, world-building |
| CoinMarketCap | `COINMC_API_KEY` | Crypto data for TEC ecosystem |
| CoinDesk | `COINDESK_API_KEY` | Additional crypto data |
| WordPress.com | `TEC_WPCOM_API_PASS` | REST API (application password) |

**Azure keys**: Hold off until billing dispute resolves 💸

## Store secrets locally

- Use `.env.local` (not committed) for development-only variables
- Or create a folder `.secrets/` and keep per-tool files inside
- Never commit private keys; only share public keys

### Suggested layout

```text
/secrets          (not tracked)
/.secrets         (not tracked)
  wpcom_id_ed25519         # SSH private key (NO COMMIT)
  wpcom_id_ed25519.pub     # SSH public key
.env.local                 # Local environment overrides
```

## Load secrets in PowerShell

```powershell
# Load .env.local into current session
$envPath = ".env.local"
if (Test-Path $envPath) {
  Get-Content $envPath | ForEach-Object {
    if ($_ -match '^(?<k>[^#=]+)=(?<v>.*)$') {
      $k = $Matches['k'].Trim(); $v = $Matches['v']
      [System.Environment]::SetEnvironmentVariable($k, $v)
    }
  }
  Write-Host "Loaded env vars from .env.local" -ForegroundColor Green
}
```

## Recommended variables

```env
# WordPress.com (local testing)
WPCOM_SSH_HOST=sftp.wp.com
WPCOM_SSH_PORT=22
WPCOM_SSH_USER=e

lidorascodexdotcom.wordpress.com
WPCOM_SSH_TARGET=/htdocs/wp-content/plugins/tec-tgcr

# MS Entra ID / Graph (if used locally)
AZURE_TENANT_ID=
AZURE_CLIENT_ID=
AZURE_CLIENT_SECRET=
```

## Notes

- Use GitHub Secrets for CI/CD; use `.env.local` only for your machine
- Rotate keys periodically; prefer SSH keys over passwords
- If in doubt, assume a file is secret and keep it out of git
