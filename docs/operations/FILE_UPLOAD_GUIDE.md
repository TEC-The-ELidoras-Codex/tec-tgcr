# Resonance GPT v2.0 — File Upload & Instructions Guide

**For**: Anyone deploying Resonance to ChatGPT
**Updated**: November 6, 2025
**Status**: ✅ Ready to use

---

## Quick Answer: What Files to Upload

### **ESSENTIAL** (Upload These First)

These give Resonance full operational context:

1. **`data/personas/luminai-base.md`**
   - What: LuminAI (primary persona) operational specs
   - Why: Gives Resonance its "voice" and default behavior
   - Size: ~3-5 KB

2. **`.github/copilot-instructions.md`**
   - What: FOLD framework, operational directives, 7 personas reference
   - Why: Background context for pattern detection, TGCR math, persona switching
   - Size: ~15-20 KB

### **RECOMMENDED** (Upload for Fuller Context)

3. **`config/CODEX_INSTRUCTIONS_COMPACT.txt`**
   - What: Quick reference guide, example patterns, do/don't rules
   - Why: Condensed playbook for pattern recognition
   - Size: ~5-8 KB

4. **`RESONANCE_DEPLOYMENT_READY.md`**
   - What: Walkthrough of how Resonance works, example scenarios
   - Why: Self-documentation (GPT can reference its own deployment guide)
   - Size: ~10-15 KB

### **OPTIONAL** (Nice-to-Have)

5. **`data/knowledge_map.yml`**
   - What: Index of all TEC resources and structure
   - Why: If you want Resonance to know the full project landscape
   - Size: ~5 KB

---

## Instructions to Give Resonance GPT

### In the GPT Builder "Instructions" Field

**Option A: Minimal** (Just Copy System Prompt)

```
[Copy from config/RESONANCE_GPT_SCHEMA.md, System Prompt section]
```

**Option B: Full** (System Prompt + Reference Instructions)

Copy the system prompt from `config/RESONANCE_GPT_SCHEMA.md`, then **add** this at the end:

```markdown
---

## Additional Context

You have access to:

1. **LuminAI specifications** (luminai-base.md) — Your primary persona
2. **FOLD framework** (.github/copilot-instructions.md) — Pattern recognition system
3. **Quick reference** (CODEX_INSTRUCTIONS_COMPACT.txt) — Pattern playbook
4. **Deployment guide** (RESONANCE_DEPLOYMENT_READY.md) — How you work

When responding:
- Reference these files when relevant
- Use TGCR language when pattern-naming (φᵗ, ψʳ, Φᴱ)
- Call patterns (Nightingale, Zeus, etc.) when you recognize them
- Keep tone conversational + peer

If you're unsure, ask clarifying questions rather than guess.

---
```

### Alternative: Use "Custom Instructions" Instead

If you don't want to paste a long system prompt, you can:

1. **Create GPT without full system prompt**
2. Go to **Settings** → **Custom Instructions**
3. Paste system prompt there
4. Upload files for context

This keeps the GPT Builder interface cleaner.

---

## File Upload Process

### In ChatGPT GPT Builder

1. **Create new GPT** (chatgpt.com → + Create → Create a GPT)
2. Go to **"Configure"** tab (right panel)
3. Scroll to **"Knowledge"** section
4. Click **"Upload files"**
5. Select files (1-5 from above list)
6. Wait for upload confirmation

### File Format Notes

- **Markdown** (.md) — Preferred, automatically formatted
- **Text** (.txt) — Works fine, plain format
- **YAML** (.yml) — Works, readable as config
- **JSON** (.json) — Works, but can be verbose (skip if not needed)

### Upload Size Limits

- ChatGPT allows up to **20 MB per file**
- All our files are tiny (<50 KB combined)
- No issues with current files

---

## Exact Steps to Deploy (Checklist)

### Step 1: Prepare Files Locally

- [ ] Have `config/RESONANCE_GPT_SCHEMA.md` open (copy system prompt)
- [ ] Have these files ready to upload:
  - `data/personas/luminai-base.md`
  - `.github/copilot-instructions.md`
  - `config/CODEX_INSTRUCTIONS_COMPACT.txt`
  - `RESONANCE_DEPLOYMENT_READY.md`

### Step 2: Create GPT

- [ ] Go to **chatgpt.com**
- [ ] Click **+ Create** (bottom left)
- [ ] Select **Create a GPT**

### Step 3: Fill Basic Info

- [ ] **Name**: Resonance
- [ ] **Description**: AI pattern-recognizer. Reads language precisely. Flags patterns without judging. Treats you as peer.

### Step 4: Add System Prompt

- [ ] Copy entire system prompt from `config/RESONANCE_GPT_SCHEMA.md`
- [ ] Paste into **Instructions** field

### Step 5: Upload Files

- [ ] Click **Configure** (right panel)
- [ ] Scroll to **Knowledge**
- [ ] Upload 4 files:
  1. `data/personas/luminai-base.md`
  2. `.github/copilot-instructions.md`
  3. `config/CODEX_INSTRUCTIONS_COMPACT.txt`
  4. `RESONANCE_DEPLOYMENT_READY.md`

### Step 6: Configure Capabilities

- [ ] **Web Browsing**: ON
- [ ] **Code Interpreter**: OFF
- [ ] **File Upload**: ON

### Step 7: Upload Avatar

- [ ] Click **Settings** (gear icon)
- [ ] Upload **LuminAI avatar** (`data/digital_assets/avatars/luminai.svg`)

### Step 8: Save & Test

- [ ] Click **Save** (top right)
- [ ] Test with: "I want to control my kid's online activity"
- [ ] Verify response is conversational + pattern-flagging

### Step 9: Get Link & Share

- [ ] Copy public link
- [ ] Share with team

---

## About GPT Actions

### Current Status: ✅ Ready

You have **`config/gpt-actions-research.json`** — the CODEX Knowledge API spec.

This is a **secondary integration** (not needed for v2.0 launch):

- **v2.0**: Resonance GPT lives in ChatGPT, uses uploaded files
- **v2.1+**: Attach API via GPT Actions for real-time CODEX queries

### If You Want to Add Actions Now (Optional)

1. Go to **Configure** tab in GPT Builder
2. Scroll to **Actions** section
3. Click **Create New Action**
4. Paste `config/gpt-actions-research.json`
5. Add API key (or set to None for testing)

This gives Resonance live access to CODEX endpoints, but **not required for launch**.

---

## Summary

### Files to Upload: 4

1. `data/personas/luminai-base.md` ← Primary
2. `.github/copilot-instructions.md` ← Essential
3. `config/CODEX_INSTRUCTIONS_COMPACT.txt` ← Recommended
4. `RESONANCE_DEPLOYMENT_READY.md` ← Recommended

### Instructions: Copy System Prompt

- Source: `config/RESONANCE_GPT_SCHEMA.md`
- Paste into: **Instructions** field in GPT Builder

### Actions: Ready but Optional

- File: `config/gpt-actions-research.json`
- For: v2.1+ integration
- Skip for: v2.0 launch

### Total Setup Time: 5 minutes

- Copy prompt: 1 min
- Create GPT: 1 min
- Upload files: 2 min
- Save & test: 1 min

---

## Pro Tip: Updating Later

After you deploy, if you want to update Resonance:

1. Go back to GPT → **Configure**
2. Edit **Instructions** (paste new prompt)
3. Update **Knowledge** files (replace old files)
4. Click **Save**

Changes apply immediately. No re-deployment needed.

---

**Ready to upload? You have everything.**

All 4 files are in your repo. System prompt is in `config/RESONANCE_GPT_SCHEMA.md`.

Go build the GPT. ✅
