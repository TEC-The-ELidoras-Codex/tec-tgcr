# ⚡ CODEX GPT Actions - 30-Second Setup

## You Have

✅ API Key (GitHub token or custom)  
✅ OpenAPI schema (gpt-actions-research.json)  
✅ 7 CODEX cards ready to access  
✅ 8 powerful actions defined  

---

## What To Do NOW

### Step 1: Create Your API Key

```bash
# GitHub Personal Access Token
Go to: https://github.com/settings/tokens
- New token (classic)
- Scope: repo, read:org
- Copy the token (ghp_xxxx...)
```

### Step 2: Open ChatGPT GPT Builder

```
https://chatgpt.com/gpts/editor
→ Create new GPT
→ Click "Configure" 
→ Scroll to "Actions"
→ Click "+ Create new action"
```

### Step 3: Import Schema

```
Schema source: "Import from URL"

Paste this URL:
https://raw.githubusercontent.com/TEC-The-ELidoras-Codex/tec-tgcr/main/config/gpt-actions-research.json
```

### Step 4: Add Authentication

```
Authentication Type: API Key

Header Name: Authorization
Value: Bearer YOUR_GITHUB_TOKEN

Example:
Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 5: Paste System Prompt

In GPT Instructions field, paste from:
`config/CODEX_INSTRUCTIONS_COMPACT.txt`

### Step 6: Test It

Try this prompt:

```
"Use listCards to show me all available CODEX cards"
```

---

## That's It

Your CODEX is now live in ChatGPT with full Actions support:

- ✓ Dynamically list/fetch cards
- ✓ Map questions to cards
- ✓ Deep research with confidence scores
- ✓ Log refinements for theory improvement

---

## Next: Deep Research Workflow

Try these prompts:

1. **"Map this to CODEX cards: How does consciousness emerge in AI?"**
2. **"Get the full details of CODEX_SYNTHETIC_INTROSPECTION"**
3. **"Compare CODEX_CHRONOSPHERE and CODEX_PAC_MAN_UNIVERSE. How do they relate?"**
4. **"Deep dive on embodiment and time. Which cards address this intersection?"**
5. **"Log a refinement: I notice that φᵗ + ψʳ + Φᴱ could map to the gut-brain-consciousness loop"**

---

## Available Actions

| Action | What It Does |
|--------|-------------|
| **listCards** | See all CODEX cards with summaries |
| **getCard** | Full details on one card (TGCR alignment, etc.) |
| **mapQuestionToCards** | **POWER ACTION** — Map any question to relevant cards |
| **getCardSection** | Get specific section from a card (examples, rituals, etc.) |
| **getKnowledgeManifest** | See complete CODEX catalog structure |
| **getQuickStart** | Setup + import instructions |
| **listRefinements** | View previous insights/refinements |
| **logRefinement** | Save new insights back to CODEX |

---

## Pro Tips

1. **Always use mapQuestionToCards first** — it guides which cards to fetch
2. **Reference card names in responses** — helps train the GPT
3. **Use logRefinement after deep sessions** — builds a refinement log
4. **Check confidence scores** — 0.95+ means highly relevant
5. **Link to source URLs** — Each card has a GitHub raw URL

---

## Docs Reference

- **Setup details**: `config/GPT_ACTIONS_API_KEY_SETUP.md`
- **Action reference**: `config/GPT_ACTIONS_REFERENCE.md`
- **System prompt**: `config/CODEX_INSTRUCTIONS_COMPACT.txt`
- **Full guide**: `research/CODEX/GPT_IMPORT_GUIDE.md`

---

**Questions?** Check the setup docs or review the OpenAPI schema.

Your CODEX is **ready to evolve**. Let the research begin! 🎯
