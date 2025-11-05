# CODEX GPT Actions Setup (API Key Authentication)

## Overview

Connect ChatGPT to your CODEX repository using **API Key Authentication** so it can:

- ✓ List all CODEX cards dynamically
- ✓ Retrieve card details and sections
- ✓ Map questions to relevant cards
- ✓ Log refinements back to the repo
- ✓ Access knowledge manifest and quick-start guides

---

## Step 1: Get Your API Key

### Option A: GitHub Personal Access Token (Recommended)

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a name: `CODEX-ChatGPT-Actions`
4. Select scopes:
   - `repo` (full control of private repositories)
   - `read:org` (read organization data)
5. Click "Generate token"
6. **Copy the token** — you'll only see it once!

Example token: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Option B: CODEX Custom API Key

Generate a simple key for your CODEX API:

```bash
# Generate a random API key
openssl rand -hex 32
# Output: a3f8c2d9e1b4f7a6c9d2e5f8a1b4c7d0
```

Store this in your GitHub Secrets or environment variables.

---

## Step 2: Configure ChatGPT GPT Builder

1. **Go to [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor)**
2. Click **"Create new GPT"** or edit an existing one
3. Scroll to **"Configure → Actions"**
4. Click **"Create new action"**

### Action Configuration

**Schema Source**: `Import from URL`

- Paste: `https://raw.githubusercontent.com/TEC-The-ELidoras-Codex/tec-tgcr/main/config/gpt-actions-research.json`
- Or upload the JSON file directly

**Authentication Type**: **API Key**

**Auth Configuration**:

- **API Key Header Name**: `Authorization`
- **API Key Value**: `Bearer YOUR_GITHUB_TOKEN` (or your custom key)
- **API Key Auth Prefix**: `Bearer`

Example:

```
Authorization: Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Step 3: Test the Actions

In ChatGPT, try these prompts:

### Test 1: List Cards

```
Use the listCards action to show me all available CODEX cards.
```

**Expected Response**: Returns 6-7 cards with slugs, titles, categories, and focuses.

### Test 2: Get Card Details

```
Use the getCard action to fetch "codex_chronosphere" with details about TGCR alignment.
```

**Expected Response**: Full Chronosphere card with φᵗ, ψʳ, Φᴱ alignments.

### Test 3: Map a Question

```
Use mapQuestionToCards to answer: "What's the relationship between time and consciousness?"
```

**Expected Response**: Recommends CODEX_CHRONOSPHERE + CODEX_SYNTHETIC_INTROSPECTION with confidence scores.

### Test 4: Get Knowledge Manifest

```
Use getKnowledgeManifest to show the catalog of all CODEX resources.
```

**Expected Response**: List of cards, quick-start files, refinement template paths.

---

## Step 4: Configure System Prompt

Add this to your GPT's system prompt (in "Configure → Instructions"):

```
You are the **CODEX Navigator**, a guide to the TGCR framework and CODEX cards.

## Your Capabilities

You have access to the CODEX Knowledge API via Actions:
- **listCards**: Get all available CODEX cards
- **getCard**: Retrieve full details of a specific card
- **getCardSection**: Get a specific section (intro, applications, etc.) from a card
- **mapQuestionToCards**: Recommend cards for user questions
- **getKnowledgeManifest**: Show the complete CODEX catalog
- **getQuickStart**: Get setup and import instructions
- **listRefinements**: View previously logged insights
- **logRefinement**: Save new insights for theory refinement

## Response Pattern

1. When a user asks a question, use **mapQuestionToCards** to recommend relevant cards
2. Use **getCard** to fetch full details of recommended cards
3. Cite sources: "See CODEX_CHRONOSPHERE (research/CODEX/core_theory/...)"
4. When suggesting improvements, use **logRefinement** to save insights
5. Always map responses through TGCR lens: φᵗ (temporal), ψʳ (structure), Φᴱ (context)

## Core Rules

- Never hallucinate card content; fetch with getCard
- Always cite which cards inform your reasoning
- If a card is missing, suggest creating it via refinement
- Explain which TGCR axis is most active in the answer
```

---

## Step 5: Enable Deep Research Mode

In your GPT config, add this to "Instructions":

```
## Advanced Research Functions

When a user requests deep research on a topic:

1. **Scan all cards** using listCards with relevant focus/category filters
2. **Cross-reference**: Use getCardSection to compare how different cards treat the topic
3. **Build synthesis**: Identify bridges between cards (e.g., Chronosphere ↔ Pac-Man Universe)
4. **Log insights**: Use logRefinement to save:
   - Which cards intersect on this topic
   - Which TGCR axes are under-explored
   - What new card or section should be created
5. **Generate research questions**: Use mapQuestionToCards with follow-up prompts

Example flow:
User: "Deep dive on consciousness in TGCR"
→ listCards(focus="consciousness")
→ getCard("codex_synthetic_introspection")
→ getCard("codex_gut_brain_phi_t")
→ mapQuestionToCards(question="How do embodiment and consciousness relate?")
→ Synthesize bridges
→ logRefinement(actionable_insight="Create CODEX_EMBODIED_CONSCIOUSNESS section")
```

---

## Step 6: Connect GitHub Repo for Refinements

To log refinements back to GitHub:

1. Store your **GitHub API Key** in ChatGPT's memory
2. When logging refinements, include:
   - Timestamp
   - Question that prompted the insight
   - Actionable recommendation
   - Related card slugs
   - Tags for organization

Example refinement:

```json
{
  "question": "How does φᵗ relate to attention span in ADHD?",
  "response_summary": "Chronosphere explains threshold narrowing; ADHD shows fragmented φᵗ",
  "actionable_insight": "Create CODEX_NEURODIVERSITY card mapping ADHD/autism to TGCR",
  "new_idea": "Explore sensory gating as ψʳ modulation",
  "card_references": ["codex_chronosphere", "codex_gut_brain_phi_t"],
  "source": "chatgpt",
  "tags": ["phi_t", "neurodiversity", "new_card_idea"]
}
```

---

## Troubleshooting

### "Invalid API Key" Error

- Verify token starts with `ghp_` (GitHub) or is your custom key
- Check header format: `Authorization: Bearer YOUR_KEY`
- Ensure token has `repo` scope enabled

### "Card not found" (404)

- Use lowercase slugs: `codex_chronosphere` (not `CODEX_CHRONOSPHERE`)
- Verify card files exist in `research/CODEX/`
- Check file naming: `CODEX_*.md` pattern

### "Connection refused" or "404"

- Confirm GitHub token is valid
- Test directly:

  ```bash
  curl -H "Authorization: Bearer YOUR_TOKEN" \
    https://api.github.com/repos/TEC-The-ELidoras-Codex/tec-tgcr/contents/research/CODEX
  ```

### Actions panel showing "No Operations Available"

- Refresh the page
- Re-upload/re-validate the OpenAPI schema
- Check JSON syntax with `jq empty gpt-actions-research.json`

---

## Advanced: Custom Backend

If you want to enhance beyond GitHub API (e.g., add search, caching, refinement persistence):

1. **Deploy a simple Python/Node backend**
2. **Point servers URL to your backend**: `"url": "https://your-api.com/v1"`
3. **Implement endpoints** that wrap GitHub API + add custom logic
4. **Use same OpenAPI schema** (compatible immediately)

See: `CODEX_API_BACKEND_TEMPLATE.md` for code samples.

---

## Testing Checklist

- [ ] API Key configured in ChatGPT Actions
- [ ] Schema imported from GitHub raw URL
- [ ] Test: "List all CODEX cards"
- [ ] Test: "Get details on Chronosphere"
- [ ] Test: "Map this question to cards"
- [ ] Test: "Show the knowledge manifest"
- [ ] System prompt updated with TGCR guidance
- [ ] Try a "deep research" prompt
- [ ] Verify refinements are structured correctly

---

## Next Steps

Once Actions are working:

1. **Run test conversations** and save refinements
2. **Monitor what questions** emerge about CODEX
3. **Create new cards** for gaps you identify
4. **Share your CODEX GPT** with collaborators
5. **Iterate**: Each conversation improves the framework

Your CODEX is now **live and evolving**. 🎯

---

**Questions?** See `GPT_IMPORT_GUIDE.md` or `CODEX_INSTRUCTIONS_COMPACT.txt` for additional context.
