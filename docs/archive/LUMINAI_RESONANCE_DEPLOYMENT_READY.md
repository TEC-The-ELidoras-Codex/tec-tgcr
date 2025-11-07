# LuminAI Resonance GPT — Setup Summary

**Created**: November 6, 2025
**Status**: Ready to Deploy
**Files**: 2 new documents created

---

## What You Have Now

### 1. Quick Setup Document

**File**: `LUMINAI_RESONANCE_QUICK_SETUP.md` (copy-paste ready)

Contains all 5 components you need to deploy Resonance GPT:

1. **System Prompt** — Copy to GPT Builder Instructions field
2. **5 Conversation Starters** — Add one per line in GPT Builder
3. **OpenAPI Actions** — URL or JSON file (gpt-actions-research.json)
4. **Knowledge Files** — Optional; adds CODEX context
5. **Configuration** — Web Browsing ON, File Upload ON, Code Interpreter OFF

**Time to Deploy**: 5 minutes
**Format**: Every section has `[Copy this]` blocks ready to paste

### 2. Knowledge Map Entry

**File**: `data/knowledge_map.yml` (updated)

Added new section tracking:

- Resonance GPT deployment status
- All 5 components documented
- Knowledge files referenced
- Conversation starters listed
- Setup time (5 min)

---

## What NOT to Use Anymore

**Skip these** (internal setup docs, now superseded):

- ❌ `config/GPT_ACTIONS_API_KEY_SETUP.md` — Too long, replaced by Quick Setup
- ❌ `config/RESONANCE_GPT_SCHEMA.md` — Deployment checklist, not operational
- ❌ `FILE_UPLOAD_GUIDE.md` — User guide, not needed for this deployment
- ❌ `DEPLOYMENT_CHECKLIST.md` — Process doc, not reference material

**Why**: Those docs are process-oriented. The new Quick Setup is component-oriented. Cleaner, faster.

---

## The 5 Things You Add to GPT Builder

### Component 1: System Prompt

**Where**: chatgpt.com/gpts/editor → Configure → Instructions

**What to paste**: The entire `You are Resonance...` prompt from QUICK_SETUP.md

**Length**: ~2000 words (includes TGCR framework + patterns + examples)

### Component 2: Conversation Starters

**Where**: Configure → Conversation starters section

**What to add** (5 total):

```
"What pattern am I missing in this situation?"
"Show me the warning I need to hear"
"Map this to TGCR: φᵗ, ψʳ, Φᴱ"
"What does this choice ripple out to?"
"Am I being a Nightingale or a Zeus right now?"
```

### Component 3: OpenAPI Actions

**Where**: Configure → Actions → Create new action

**Choose one method**:

**A. URL Import (Fastest)**

```
https://raw.githubusercontent.com/TEC-The-ELidoras-Codex/tec-tgcr/main/config/gpt-actions-research.json
```

**B. Upload File**

```
config/gpt-actions-research.json (your repo file)
```

**Then add API Key**:

- Auth Type: `API Key`
- Header Name: `Authorization`
- Prefix: `Bearer`
- Value: Your GitHub token or custom key

### Component 4: Knowledge Files (Optional)

**Where**: Configure → Files section

**Upload these 3** (if you want full CODEX context):

1. `.github/copilot-instructions.md` — TGCR framework
2. `config/CODEX_INSTRUCTIONS_COMPACT.txt` — Card references
3. `research/CODEX/MOTHER_STEPCHILD_STEWARD_MIRROR.md` — Archetypes

### Component 5: Settings

**Where**: Configure section

**Enable**:

- ✅ Web Browsing: ON
- ✅ File Upload: ON

**Disable**:

- ❌ Code Interpreter: OFF

**Name**: `Resonance` or `LuminAI Resonance`
**Description**: `Pattern-recognition AI carrying FOLD cosmology. Calls out dangers while honoring impulse.`

---

## Quick Deploy Checklist

```
[ ] 1. Open LUMINAI_RESONANCE_QUICK_SETUP.md
[ ] 2. Go to chatgpt.com/gpts/editor (Create new GPT)
[ ] 3. Copy System Prompt → paste into Instructions
[ ] 4. Add 5 Conversation Starters → paste one per line
[ ] 5. Choose Actions method (URL or upload JSON)
[ ] 6. Add API Key to Actions auth
[ ] 7. Upload 3 Knowledge Files (optional)
[ ] 8. Set Name, Description, and Configuration settings
[ ] 9. Click Save
[ ] 10. Copy share link → email or store
[ ] 11. Test: Try a conversation starter in the GPT
[ ] 12. Update data/knowledge_map.yml with your share link
```

---

## After Deployment

Once Resonance GPT is live:

1. **Update the knowledge map**:
   - Replace `[awaiting deployment]` with your GPT share link
   - Commit: `docs: add resonance gpt live link`

2. **Share the link**:
   - GPT Builder → Share button → Copy link
   - Add to your portfolio, team wiki, etc.

3. **Test commands**:
   - Try the 5 conversation starters
   - Ask: "Analyze [situation]"
   - Ask: "Map this to TGCR"
   - Verify API works (if Actions enabled)

---

## File Reference

| File | Purpose | Status |
|------|---------|--------|
| `LUMINAI_RESONANCE_QUICK_SETUP.md` | 5 components ready to copy-paste | ✅ Created |
| `data/knowledge_map.yml` | Track GPT deployment | ✅ Updated |
| `.github/copilot-instructions.md` | TGCR framework (knowledge file) | ✅ Existing |
| `config/CODEX_INSTRUCTIONS_COMPACT.txt` | System prompt source | ✅ Existing |
| `config/gpt-actions-research.json` | OpenAPI Actions spec | ✅ Existing |

---

## Next Steps

1. **Deploy Resonance GPT** (5 min via QUICK_SETUP.md)
2. **Get your share link** (from GPT Builder)
3. **Update knowledge_map.yml** with link
4. **Test the 5 components** (conversation starters, API actions)
5. **Ready to use!**

All materials are consolidated in one place. No jumping between docs.
