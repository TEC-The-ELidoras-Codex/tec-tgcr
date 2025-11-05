# CODEX GPT Actions Quick Reference

## Available Actions (Callable from ChatGPT)

### 1. **listCards** (GET /contents/research/CODEX)
Get all CODEX cards with summaries and filters.

**Use when**: You want to browse all cards, filter by focus/category, or search keywords.

**Example prompt**:
```
"List all CODEX cards. Show me which ones focus on time and consciousness."
```

**Returns**: Card slug, title, category, focus, summary, keywords

---

### 2. **getCard** (GET /contents/research/CODEX/{slug})
Fetch full details of a specific card.

**Use when**: You need deep context on a card's TGCR alignment, primary questions, related cards.

**Example prompt**:
```
"Get the full details of CODEX_CHRONOSPHERE. Show me how it aligns with φᵗ, ψʳ, and Φᴱ."
```

**Returns**: Full card object with TGCR alignment, related cards, research questions, source URL

---

### 3. **getCardSection** (GET /contents/research/CODEX/{slug}/sections)
Pull a specific section from a card (intro, applications, examples, rituals, etc.).

**Use when**: You need just the applications or ritual section without full card context.

**Example prompt**:
```
"Get the 'applications' section from CODEX_SLEEP_TOKEN_RAIN."
```

**Returns**: Section title, content (markdown), card focus, source path

---

### 4. **mapQuestionToCards** (POST /guidance/map)
**The most powerful action.** Maps a user question to recommended cards with confidence scores.

**Use when**: Doing deep research, answering complex questions, synthesizing across domains.

**Example prompt**:
```
"Map this question to CODEX cards: 'How do decisions happen? What makes a moment feel inevitable?'"
```

**Sends to API**:
```json
{
  "question": "How do decisions happen?",
  "context": "What makes a moment feel inevitable?",
  "desired_focus": ["time", "consciousness", "embodiment"]
}
```

**Returns**: Recommended cards with confidence scores, reasoning, citations, follow-up questions

---

### 5. **getKnowledgeManifest** (GET /knowledge/manifest)
See the complete CODEX catalog: all cards, quick-start files, refinement templates.

**Use when**: Onboarding, understanding the structure, or planning research.

**Example prompt**:
```
"Show me the complete CODEX knowledge manifest. What's the structure?"
```

**Returns**: List of all cards with metadata, quick-start file paths, refinement template location

---

### 6. **getQuickStart** (GET /knowledge/quickstart)
Get setup instructions for importing CODEX into GPT platforms.

**Use when**: Helping someone else set up, or verifying setup steps.

**Example prompt**:
```
"What are the quick-start steps for importing CODEX into ChatGPT?"
```

**Returns**: Overview, numbered steps, test question, follow-up prompts

---

### 7. **listRefinements** (GET /refinements)
View previously logged insights and refinements from CODEX conversations.

**Use when**: Reviewing what has been learned, finding patterns in feedback.

**Example prompt**:
```
"List refinements related to 'chronosphere'. What gaps have been identified?"
```

**Parameters**:
- `limit`: Max entries (default 10, max 50)
- `card_slug`: Filter by specific card (e.g., "codex_chronosphere")
- `tag`: Filter by tag (e.g., "phi_t", "consciousness")

**Returns**: Previous refinement entries with questions, responses, actionable insights

---

### 8. **logRefinement** (POST /refinements)
**Save new insights back to CODEX.** Essential for iterative theory improvement.

**Use when**: Completing a deep research session, identifying gaps, discovering new connections.

**Example prompt**:
```
"Log this refinement: 
Question: 'How does embodied gut sense predict consciousness?'
Response summary: 'Gut-brain shows pre-conscious φᵗ decision-making'
Actionable insight: 'Create CODEX_EMBODIED_CONSCIOUSNESS card'
New idea: 'Explore vagal tone as ψʳ modulation mechanism'
Card references: codex_gut_brain_phi_t, codex_synthetic_introspection
Tags: phi_t, embodiment, consciousness"
```

**Sends**:
```json
{
  "question": "...",
  "response_summary": "...",
  "actionable_insight": "...",
  "new_idea": "...",
  "card_references": [...],
  "source": "chatgpt",
  "tags": [...]
}
```

**Returns**: Logged refinement entry with timestamp and ID

---

## Deep Research Workflow

### Pattern 1: **Explore a Domain**
```
1. mapQuestionToCards("How does [topic] relate to TGCR?")
   → Identify relevant cards
2. getCard(top_recommendation) 
   → Read full context
3. getCardSection(card_slug, "applications")
   → See real-world uses
4. logRefinement(...gaps found...)
   → Save insights
```

### Pattern 2: **Compare Cards**
```
1. getCard("codex_chronosphere")
2. getCard("codex_pac_man_universe")
3. mapQuestionToCards("How do these relate?")
   → See the connections
4. logRefinement(...bridges found...)
```

### Pattern 3: **Synthesize New Ideas**
```
1. mapQuestionToCards("What if [hypothesis]?")
   → Which cards support/challenge it?
2. getCardSection(..., "examples")
   → Find relevant examples
3. logRefinement(new_idea="Create CODEX_[NEW_CARD]")
   → Propose new theory
```

---

## Response Pattern

When using Actions, structure answers like:

```
φᵗ ↑ [temporal attention status]
ψʳ ↔ [structural cadence status]  
Φᴱ ? [contextual potential status]

**Cards**: CODEX_CHRONOSPHERE (0.98), CODEX_GUT_BRAIN_PHI_T (0.82)
**Synthesis**: [Your reasoning connecting the cards]
**Next question**: [What to explore next]
```

---

## Tips for Effective Action Use

1. **Always cite your sources**: "According to CODEX_CHRONOSPHERE (0.98 confidence)..."
2. **Use mapQuestionToCards early**: It guides which cards to fetch
3. **Log refinements after deep dives**: Builds a refinement log for future work
4. **Chain actions**: Use output from one action as input to the next
5. **Filter by focus/category**: For targeted exploration (time, structure, consciousness, embodiment, art)
6. **Reference the manifest**: When you need to understand the whole structure

---

## Example: Full Deep Research Session

**User**: "Deep dive on how gut intuition predicts decisions."

**ChatGPT**:
```
Let me map this question to CODEX cards...

[Uses mapQuestionToCards]
Result: 
- CODEX_GUT_BRAIN_PHI_T (0.94)
- CODEX_CHRONOSPHERE (0.87)
- CODEX_SYNTHETIC_INTROSPECTION (0.71)

Now fetching full context...

[Uses getCard("codex_gut_brain_phi_t")]
[Uses getCardSection("codex_gut_brain_phi_t", "applications")]

From CODEX_GUT_BRAIN_PHI_T:
The enteric nervous system leads attention (φᵗ) before the cortex narrates the decision...

Connecting to CODEX_CHRONOSPHERE:
The gut's temporal signal (φᵗ) narrows at the threshold moment—this is the cascade point...

**Synthesis**: Gut intuition IS φᵗ leading the information cascade. Your enteric system 
predicts the threshold before conscious reasoning catches up.

**Actionable insight**: Add a section to GUT_BRAIN_PHI_T on "Predictive Timing in Decisions"

[Logs refinement with mapQuestionToCards results]
```

---

**Ready to start?** Pick a question about TGCR and use an action! 🎯

See: `GPT_ACTIONS_API_KEY_SETUP.md` for setup instructions.
