# Which API Keys Do You ACTUALLY Need?

**Date**: Nov 4, 2025
**Your Question**: "Do I use OpenAI API?"
**Answer**: It depends. See below.

---

## The Three Scenarios

### Scenario 1: Deploy Resonance GPT to ChatGPT (TODAY) ✅

**What**: Copy system prompt → chatgpt.com → Save
**API Keys Needed**: ❌ **NONE**

```
Resonance GPT in ChatGPT GPT Builder (free)
├─ Uses your ChatGPT+ subscription (if you have one)
├─ No OpenAI API key required
└─ No FOLD key required (GPT Builder is just a UI)
```

**Time**: 5 minutes
**Cost**: Free (uses your existing ChatGPT subscription)

---

### Scenario 2: Connect GPT to Your FOLD Research API (THIS WEEK) ✅

**What**: Make Resonance GPT call your music analysis endpoints
**API Keys Needed**: ✅ **FOLD_RESEARCH_API_KEY** (fold_sk_...)

```
Resonance GPT (in ChatGPT)
├─ User asks: "Search motif"
├─ GPT calls: POST https://api.tec-fold.local/motif/search
├─ Header: X-FOLD-API-Key: fold_sk_YOUR_KEY
└─ Returns: Motif results (no OpenAI API call needed)
```

**Time**: 30 minutes
**Cost**: Free (you're running your own API)

---

### Scenario 3: Call OpenAI API from Your Python Code (LATER) ⏭️

**What**: Use ChatGPT inside your own Python scripts
**API Keys Needed**: ✅ **OPENAI_API_KEY** (sk-...)
**Use Cases**:

- Generate AI-powered motif descriptions automatically
- Analyze fan discourse with ChatGPT
- Fine-tune models with your FOLD data
- Build AI features into your backend

```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Analyze this motif..."}]
)
```

**Time**: 10 minutes (to add to code)
**Cost**: Pay-per-token (~$0.01–$0.10 per API call)

---

## What to Store in Bitwarden RIGHT NOW

### Required ✅ (Store Today)

```
Item: FOLD Research API Credentials
├─ Name: FOLD Research API Key
├─ Username: fold-api
├─ Password: fold_sk_lbTY3kKJ2_n5xQ8pZ9m0wA1bC2dE3fG4hI5jK6lM7nO8pQ9rS
├─ URI: https://api.tec-fold.local
└─ Folder: FOLD Project (4811be94-254e-465c-8ea6-b363013aaef8)
```

### Optional ⏭️ (Store Later if Needed)

```
Item: OpenAI API Credentials (skip for now, add later)
├─ Name: OpenAI API Key
├─ Username: openai-api
├─ Password: sk-proj-YOUR_OPENAI_KEY
├─ URI: https://api.openai.com
└─ Folder: FOLD Project
```

---

## Your `.env.local` (TODAY)

```bash
# .env.local (gitignored, never commit)

# ===== FOLD RESEARCH API (REQUIRED) =====
FOLD_RESEARCH_API_KEY=fold_sk_lbTY3kKJ2_n5xQ8pZ9m0wA1bC2dE3fG4hI5jK6lM7nO8pQ9rS
FOLD_API_URL=https://api.tec-fold.local

# ===== OPENAI API (OPTIONAL - add LATER) =====
# OPENAI_API_KEY=sk-proj-...
# (Only needed if you want AI-powered features in your code)
```

---

## Quick Decision Tree

```
Q: Do I need OpenAI API key?

├─ "I just want to deploy Resonance GPT to ChatGPT"
│  └─ Answer: ❌ NO
│     (Use free GPT Builder, no key needed)
│
├─ "I want Resonance GPT to call my FOLD Research API"
│  └─ Answer: ✅ YES (but it's FOLD key, not OpenAI)
│     (fold_sk_... for your custom API)
│
└─ "I want AI features in my Python code"
   └─ Answer: ✅ YES (add later)
      (sk-... from OpenAI dashboard, pay-per-call)
```

---

## Timeline: When to Add Each Key

| Phase | When | Action | Blocker | Key Needed |
|-------|------|--------|---------|-----------|
| **Phase 2 (Today)** | Now | Deploy Resonance GPT to ChatGPT | None | ❌ None |
| **Phase 2a (This Week)** | This week | Connect to FOLD Research API | None | ✅ FOLD key |
| **Phase 2b (Next Week)** | Optional | Add AI-powered features | No | ⏭️ OpenAI key (optional) |
| **Phase 3 (March 2026)** | Later | Full platform | No | ⏭️ OpenAI key (optional) |

---

## Your Action Items (TODAY)

### Step 1: Generate FOLD Research API Key

```bash
python3 << 'EOF'
import secrets
key = f"fold_sk_{secrets.token_urlsafe(32)}"
print(f"Your FOLD API Key:\n{key}")
EOF
```

### Step 2: Store in Bitwarden

1. Open **Bitwarden Vault**
2. **New Item** → **Login**
3. **Name**: `FOLD Research API Key`
4. **Username**: `fold-api`
5. **Password**: [Paste your generated key]
6. **URI**: `https://api.tec-fold.local`
7. **Folder**: Your FOLD project (`4811be94-254e-465c-8ea6-b363013aaef8`)
8. **Save**

### Step 3: Add to `.env.local`

```bash
# Copy from Bitwarden → paste into .env.local
FOLD_RESEARCH_API_KEY=fold_sk_YOUR_KEY
FOLD_API_URL=https://api.tec-fold.local
```

### Step 4: Add to GitHub Secrets (CI/CD)

```bash
# Go to: Settings → Secrets and variables → Actions → New repository secret
Name:  FOLD_RESEARCH_API_KEY
Value: [paste from Bitwarden]
```

### Step 5: Test

```bash
python3 -c "import os; print(f'✅ Loaded: {os.getenv(\"FOLD_RESEARCH_API_KEY\")[:10]}...')"
```

---

## DO NOT Add OpenAI Key Yet

You **don't need OpenAI API key** to:

- ✅ Deploy Resonance GPT to ChatGPT
- ✅ Connect to your FOLD Research API
- ✅ Run the music analysis platform

You **would need OpenAI API key** if:

- ❌ You want AI to generate motif descriptions (later)
- ❌ You want to call ChatGPT from Python (later)
- ❌ You want fine-tuned models (phase 3)

**Skip OpenAI for now. Add it later when you need it.**

---

## Summary

| Key | Need Now? | Store in Bitwarden? | Store in `.env.local`? | Format |
|-----|-----------|-------------------|----------------------|--------|
| **FOLD_RESEARCH_API_KEY** | ✅ YES | ✅ YES | ✅ YES | `fold_sk_...` |
| **FOLD_API_URL** | ✅ YES | ✅ YES | ✅ YES | `https://api.tec-fold.local` |
| **OPENAI_API_KEY** | ❌ NO | ⏭️ Later | ⏭️ Later | `sk-proj-...` |

---

**Ready to generate your FOLD API key?** Run the Python command above, then store it in Bitwarden. That's all you need for today.
