# API Keys Setup Guide — TEC-TGCR Agent Stack

**Your API keys, secure and local. No git commits. No Azure drama.**

---

## 🔐 Quick Setup (3 Steps)

### 1. Copy the Template

```powershell
# In repo root
cp .env.example .env.local
```

### 2. Add Your Keys

Open `.env.local` in your editor:

```powershell
code .env.local
# Or: notepad .env.local
```

Paste your actual keys:

```env
TEC_OPENAI_API_KEY=sk-proj-your-actual-key-here
ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
XAI_API_KEY=xai-your-actual-key-here
WORLDANVIL_API_KEY=your-actual-key-here
COINMC_API_KEY=your-actual-key-here
COINDESK_API_KEY=your-actual-key-here
TEC_WPCOM_API_PASS=xxxx xxxx xxxx xxxx
```

### 3. Load Keys in Terminal

```powershell
# PowerShell (recommended)
.\scripts\load_env.ps1

# Bash/WSL (alternative)
export $(cat .env.local | grep -v '^#' | xargs)
```

**Done!** Your keys are now loaded for this terminal session.

---

## 🎯 Your Current API Keys

Based on your message, here's what you have:

| **Service** | **Variable** | **What It's For** |
|-------------|--------------|-------------------|
| 🤖 **OpenAI** | `TEC_OPENAI_API_KEY` | GPT-4, DALL-E, embeddings for LuminAI |
| 🧠 **Anthropic** | `ANTHROPIC_API_KEY` | Claude models (LuminAI conversations) |
| 🚀 **xAI** | `XAI_API_KEY` | Grok API (experimental, Musk's LLM) |
| 🌍 **WorldAnvil** | `WORLDANVIL_API_KEY` | Lore database, world-building integration |
| 💰 **CoinMarketCap** | `COINMC_API_KEY` | Crypto pricing for TEC token ecosystem |
| 💵 **CoinDesk** | `COINDESK_API_KEY` | Additional crypto data sources |
| 📝 **WordPress.com** | `TEC_WPCOM_API_PASS` | REST API access (application password) |

**Azure**: On hold until billing dispute resolves (fuck Azure 💸)

---

## 🛡️ Security Best Practices

### ✅ DO

- ✅ Use `.env.local` for local development (already gitignored)
- ✅ Use GitHub Secrets for CI/CD workflows
- ✅ Use `wp-config.php` constants for WordPress.com production
- ✅ Rotate keys periodically (every 90 days)
- ✅ Use application-specific passwords (not main account password)

### ❌ DON'T

- ❌ Commit `.env.local` to git (it's ignored, but double-check)
- ❌ Share keys in Discord/Slack/chat (use secret managers)
- ❌ Hardcode keys in source code (use env vars)
- ❌ Use the same key across multiple projects (scope keys)
- ❌ Leave keys in terminal history (use `load_env.ps1`)

---

## 📂 File Locations

### `.env.local` (YOUR KEYS HERE)

```text
c:\Users\Ghedd\OneDrive - TEC - The Elidoras Codex\Projects\TEC\tec-tgcr\.env.local
```

**Status**: ✅ Gitignored (safe to edit)

### `.env.example` (PUBLIC TEMPLATE)

```text
c:\Users\Ghedd\OneDrive - TEC - The Elidoras Codex\Projects\TEC\tec-tgcr\.env.example
```

**Status**: 📦 Committed (no secrets, just structure)

### `.secrets/` (SSH KEYS)

```text
c:\Users\Ghedd\OneDrive - TEC - The Elidoras Codex\Projects\TEC\tec-tgcr\.secrets\
  wpcom_id_ed25519         # SSH private key (NEVER COMMIT)
  wpcom_id_ed25519.pub     # SSH public key (safe to share)
```

**Status**: ✅ Gitignored

---

## 🔧 Using Keys in Code

### Python

```python
import os

# Load from environment
openai_key = os.getenv("TEC_OPENAI_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")

# Or use python-dotenv (auto-loads .env.local)
from dotenv import load_dotenv
load_dotenv(".env.local")
```

### PowerShell

```powershell
# After running .\scripts\load_env.ps1
$openaiKey = $env:TEC_OPENAI_API_KEY
$anthropicKey = $env:ANTHROPIC_API_KEY
```

### PHP (WordPress)

```php
// In wp-config.php (server-side)
define('TEC_OPENAI_API_KEY', getenv('TEC_OPENAI_API_KEY'));
define('ANTHROPIC_API_KEY', getenv('ANTHROPIC_API_KEY'));
```

---

## 🚨 Key Compromised? Rotate Immediately

### OpenAI

1. Visit: <https://platform.openai.com/api-keys>
2. **Revoke** old key
3. **Create** new key
4. Update `.env.local`

### Anthropic

1. Visit: <https://console.anthropic.com/settings/keys>
2. Delete old key
3. Generate new key
4. Update `.env.local`

### xAI

1. Visit: <https://console.x.ai/> (check official docs)
2. Regenerate API key
3. Update `.env.local`

### WorldAnvil

1. Visit: <https://www.worldanvil.com/api>
2. Revoke/regenerate key
3. Update `.env.local`

### WordPress.com

1. Visit: <https://wordpress.com/me/security/application-passwords>
2. **Revoke** old password
3. **Generate** new application password
4. Update `.env.local` and GitHub Secret `TEC_WPCOM_API_PASS`

---

## 🧪 Testing Your Keys

### Test OpenAI

```powershell
.\scripts\load_env.ps1

# Python
python -c "import openai; print(openai.Model.list())"
```

### Test Anthropic (Claude)

```powershell
python -c "import anthropic; client = anthropic.Anthropic(); print(client.models.list())"
```

### Test WordPress.com

```powershell
$user = "your-username"
$pass = $env:TEC_WPCOM_API_PASS
$site = "elidorascodex.wordpress.com"

curl -u "${user}:${pass}" "https://public-api.wordpress.com/rest/v1.1/sites/${site}/posts"
```

---

## 🎭 Azure Drama Resolution (Pending)

Once billing dispute resolves:

1. **Create Entra ID App Registration**:

   ```powershell
   az ad app create --display-name "TEC-TGCR Service"
   ```

2. **Generate Client Secret**:

   ```powershell
   az ad app credential reset --id <app-id>
   ```

3. **Add to `.env.local`**:

   ```env
   AZURE_TENANT_ID=7d290c31-2df1-4e76-ab86-e26f12753bde
   AZURE_CLIENT_ID=<your-app-id>
   AZURE_CLIENT_SECRET=<your-client-secret>
   AZURE_SUBSCRIPTION_ID=89d36e9a-a518-4151-95b3-087ec1b88ec5
   ```

**For now**: Skip Azure until refund processed 💸

---

## 📋 Verification Checklist

After setup, verify:

- [ ] `.env.local` exists and has your actual keys
- [ ] `.env.local` does NOT appear in `git status`
- [ ] `.\scripts\load_env.ps1` runs without errors
- [ ] All keys show `[✓]` in verification output
- [ ] Test at least one API (OpenAI recommended)
- [ ] GitHub Secrets set for CI/CD (if deploying)

---

## 📚 Related Docs

- **Local Secrets Guide**: `docs/LOCAL_SECRETS.md`
- **GitHub Secrets Setup**: `docs/GITHUB_SECRETS_SETUP.md`
- **M365 Integration**: `docs/M365_INTEGRATION.md` (when Azure unfucks itself)
- **WordPress Deployment**: `docs/WORDPRESS_WPCOM_OPS.md`

---

**"Where keys are kept sacred, resonance remains unbroken."** 🔐✨

---

_Last updated: 2025-10-18 by TGCR Agent Stack_
_Status: All keys ready except Azure (pending billing resolution)_
