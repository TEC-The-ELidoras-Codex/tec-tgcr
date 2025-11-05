# FOLD Research API — Authentication Setup for GPT Actions

**Date**: Nov 4, 2025
**API**: FOLD Research (OpenAPI 3.1.0)
**Purpose**: Configure auth for GPT Actions integration

---

## Your Current Setup

**API Schema**: `config/gpt-actions-research.json` (OpenAPI 3.1.0) ✅

**Current Auth Definition**:

```json
"securitySchemes": {
  "bearerAuth": {
    "type": "http",
    "scheme": "bearer",
    "bearerFormat": "JWT"
  }
}
```

This means: **Bearer Token** (expects `Authorization: Bearer YOUR_TOKEN`)

---

## What You Need: The Decision Matrix

| Option | Setup Time | Security | Best For |
|--------|------------|----------|----------|
| **None** | 5 min | Low | Quick testing, demos |
| **API Key** | 15 min | Medium | Development & internal |
| **Bearer Token** | 30 min | High | Production |

---

## RECOMMENDED: API Key (Best for Now) — Using Bitwarden

You already have **Bitwarden loaded** with project `4811be94-254e-465c-8ea6-b363013aaef8`. Use it directly.

### Step 1: Store API Key in Bitwarden

1. Open **Bitwarden Vault**
2. Click **New Item** → **Login**
3. Fill:
   - **Name**: `FOLD Research API Key`
   - **Username**: `fold-api`
   - **Password**: `fold_sk_[generate or paste your key]`
   - **URI**: `https://api.tec-fold.local`
4. **Folder**: Select your FOLD project folder (UUID: `4811be94-254e-465c-8ea6-b363013aaef8`)
5. **Save**

### Step 2: Retrieve from Bitwarden CLI

Once stored, pull directly into your environment:

```bash
# Install Bitwarden CLI (if not already)
# macOS: brew install bitwarden-cli
# Linux: npm install -g @bitwarden/cli
# Windows: choco install bitwarden-cli

# Unlock vault
bw unlock

# Get the stored key (retrieve by name)
bw get password "FOLD Research API Key"
# Output: fold_sk_lbTY3kKJ2_n5xQ8pZ9m0wA1bC2dE3fG4hI5jK6lM7nO8pQ9rS
```

### Step 3: Load into `.env.local` (Never Commit!)

```bash
# .env.local (gitignored)
export FOLD_RESEARCH_API_KEY=$(bw get password "FOLD Research API Key")
export FOLD_API_URL=https://api.tec-fold.local
```

Or manually paste from Bitwarden:

```bash
# .env.local
FOLD_RESEARCH_API_KEY=fold_sk_lbTY3kKJ2_n5xQ8pZ9m0wA1bC2dE3fG4hI5jK6lM7nO8pQ9rS
FOLD_API_URL=https://api.tec-fold.local
```

### Step 4: Add to GitHub Secrets (for CI/CD)

Copy the key from Bitwarden → GitHub Secrets:

```
Settings → Secrets and variables → Actions → New repository secret
Name:  FOLD_RESEARCH_API_KEY
Value: [paste from Bitwarden]
```

**Your Bitwarden Project UUID**: `4811be94-254e-465c-8ea6-b363013aaef8` ✅ (stored safe)

### Step 3: Add Auth Check to Your API

If using FastAPI:

```python
# In your FOLD Research API handler
from fastapi import FastAPI, Header, HTTPException
import os

app = FastAPI()

async def verify_fold_api_key(x_fold_api_key: str = Header(None)):
    """Verify incoming API key matches FOLD_RESEARCH_API_KEY"""
    expected_key = os.getenv("FOLD_RESEARCH_API_KEY")
    if not x_fold_api_key or x_fold_api_key != expected_key:
        raise HTTPException(status_code=401, detail="Invalid FOLD API Key")
    return x_fold_api_key

# Add to all endpoints
@app.post("/motif/search", dependencies=[Depends(verify_fold_api_key)])
async def search_motifs(query: str):
    # Your logic here
    pass
```

### Step 4: Configure in GPT Builder

1. Open **ChatGPT** → Click your **Resonance GPT** (or create new)
2. Click **Configure** or **Actions** (depending on UI)
3. **Add Action** → **Import from URL** OR paste schema manually
4. Paste contents of `config/gpt-actions-research.json`
5. When prompted for **Authentication**:
   - **Type**: API Key
   - **Auth Type**: Header
   - **Custom Header Name**: `X-FOLD-API-Key`
   - **API Key Value**: Paste your `fold_sk_...` key
6. **Save & Test**

---

## Test It

### From Command Line

```bash
curl -X POST https://api.tec-fold.local/motif/search \
  -H "X-FOLD-API-Key: fold_sk_YOUR_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"query": "Observer Amplification"}'
```

### From GPT

Ask your Resonance GPT: *"Search for Observer Amplification motif"*

Expected: GPT makes the API call with your key attached.

---

## Your Credentials Checklist

✅ **API Endpoint**: `https://api.tec-fold.local`
✅ **Auth Method**: API Key (Header-based)
✅ **Header Name**: `X-FOLD-API-Key`
✅ **Key Format**: `fold_sk_[32-char random token]`
✅ **Key Storage**: `.env.local` (gitignored) + GitHub Secrets
✅ **Verification Logic**: Added to API endpoints
✅ **Schema**: OpenAPI 3.1.0 with bearer token reference

---

## Production Upgrade (Later)

When you're ready for real deployment (March 2026):

### Migrate to OAuth 2.0

1. Implement token endpoint:

```python
@app.post("/auth/token")
async def get_token(client_id: str, client_secret: str):
    # Verify credentials
    token = jwt.encode(
        {"sub": client_id, "exp": datetime.now() + timedelta(hours=1)},
        SECRET_KEY,
        algorithm="HS256"
    )
    return {"access_token": token, "token_type": "bearer"}
```

2. Update OpenAPI schema:

```json
"securitySchemes": {
  "oauth2": {
    "type": "oauth2",
    "flows": {
      "clientCredentials": {
        "tokenUrl": "https://api.tec-fold.local/auth/token",
        "scopes": {
          "read:motifs": "Search motifs",
          "read:resonance": "Score resonance",
          "read:artists": "Analyze artists"
        }
      }
    }
  }
}
```

3. Configure in GPT Builder:
   - Auth Type: OAuth 2.0
   - Token URL: `https://api.tec-fold.local/auth/token`
   - Client ID & Secret: Store in GitHub Secrets
   - Scopes: `read:motifs read:resonance read:artists`

---

## Right Now (Today)

| Step | Action | Status |
|------|--------|--------|
| 1 | Generate API key | Do now |
| 2 | Store in `.env.local` | Do now |
| 3 | Add to GitHub Secrets | Do now |
| 4 | Implement verification in API | To code |
| 5 | Upload schema to GPT Builder | To do |
| 6 | Test with Resonance GPT | To test |

---

## Security Notes

- Never commit `.env.local` (add to `.gitignore`)
- Rotate keys every 90 days
- Use GitHub Secrets for CI/CD
- In production, use OAuth 2.0 + HTTPS enforced
- Log all API access for audit trail

---

## Status

✅ API schema ready (OpenAPI 3.1.0)
✅ Endpoints defined (5 FOLD research operations)
✅ Auth method chosen (API Key recommended)
⏳ **Next**: Generate key + add verification logic + test in GPT Builder

---

**Your Stuff Summary:**

| Item | What It Is | Where It Goes |
|------|-----------|---------------|
| **API Key** | `fold_sk_[random]` | `.env.local` + GitHub Secrets |
| **Header Name** | `X-FOLD-API-Key` | Request headers from GPT |
| **API URL** | `https://api.tec-fold.local` | `gpt-actions-research.json` |
| **Verification** | Check header in FastAPI | API endpoint code |
| **Schema** | OpenAPI 3.1.0 spec | Upload to GPT Builder |

**Ready to implement?** Let me know if you want the complete FastAPI code template or help configuring the GPT Builder UI.
