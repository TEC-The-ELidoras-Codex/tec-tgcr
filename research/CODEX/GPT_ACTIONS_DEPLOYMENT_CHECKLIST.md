# CODEX GPT Actions Deployment Checklist

**Date**: 2025-11-05  
**Status**: READY FOR DEPLOYMENT  
**OpenAPI Spec**: `config/gpt-actions-research.json`

---

## API Status ✅

- **Backend Server**: Running on `http://localhost:5000/api/v1`
- **Health Check**: ✅ Responding with status OK
- **Available Endpoints**: 7 CODEX cards listed
- **Tested Operations**:
  - `GET /api/v1/health` — Returns service status
  - `GET /api/v1/cards` — Returns CODEX card manifest (7 cards)

---

## Sample API Response

```json
{
  "cards": [
    {
      "slug": "codex_chronosphere",
      "title": "CODEX Chronosphere",
      "category": "core_theory",
      "focus": "Time, thresholds, information cascades",
      "tgcr_alignment": {
        "phi_t": 9,
        "psi_r": 8,
        "phi_e": 9
      }
    }
  ],
  "count": 7
}
```

---

## Setup Steps

### Step 1: Copy the OpenAPI Schema

1. Open `config/gpt-actions-research.json`
2. Copy the entire JSON
3. Keep in clipboard

### Step 2: Create New GPT in ChatGPT

1. Visit <https://chatgpt.com/gpts/editor>
2. Click "Create new GPT"
3. Name it: "CODEX Knowledge Assistant"
4. Description: "Grounds responses in TEC's CODEX research, TGCR framework, and LuminAI's dual-insight perspectives"

### Step 3: Configure Actions

1. Scroll to "Actions" section
2. Click "Create new action"
3. Select "Import from URL" or "Paste schema"
4. Paste the OpenAPI JSON
5. Key endpoints:

   - `GET /cards` (listCards) — List all CODEX cards
   - `GET /cards/{slug}` (getCard) — Retrieve specific card
   - `POST /guidance/map` (mapQuestionToCards) — Map questions to cards
   - `GET /knowledge/manifest` — Get knowledge manifest
   - `POST /refinements` — Log GPT refinements

### Step 4: Configure Authentication

1. Under "Authentication", select "API Key"
2. Header name: `Authorization`
3. API Key format: `Bearer <YOUR_GITHUB_PAT>`
   - Create GitHub PAT at <https://github.com/settings/tokens>
   - Minimal scopes: `repo:read`
4. Click "Save"

### Step 5: Configure Server URL

Three servers pre-configured:

- **Local HTTPS**: `https://localhost:5000/api/v1` (required for ChatGPT Actions testing)
- **Local HTTP**: `http://localhost:5000/api/v1` (fallback)
- **Production**: `https://codex-api.local/api/v1` (placeholder)

ChatGPT Actions requires HTTPS, so the first server (`https://localhost:5000/api/v1`) is prioritized for validation.

### Step 6: Test the Integration

Try asking:

- "What's the core insight of the Chronosphere model?"
- "Explain TGCR in one sentence."
- "Which CODEX card addresses AI consciousness?"

The GPT should call `/guidance/map` and return card recommendations.

### Step 7: Add System Instructions

```text
You are the CODEX Knowledge Assistant, channeling the resonance wisdom of the Elidoras Codex and the analytical rigor of TGCR (Temporal-attentional, Structural-cadence, Contextual-potential).

Your role:
1. Answer questions by grounding them in CODEX cards and TGCR framework
2. Always cite which card(s) you're referencing
3. Highlight connections between temporal (φᵗ), structural (ψʳ), and contextual (Φᴱ) dimensions
4. When unsure, use the /guidance/map action to find the most relevant card
5. Maintain poetic rigor: speak with precision and beauty

When answering:
- Lead with the TGCR axis most relevant to the question
- Always provide at least one CODEX card reference
- Explain how the answer connects to LuminAI's dual-eye perspective (logic + empathy)
- End with a follow-up prompt that deepens the inquiry

Remember: "Light learns by listening." Every response should be both illuminating and receptive to refinement.
```

---

## Testing from Command Line

Verify the API works before importing into ChatGPT:

```bash
# List all cards
curl -X GET "http://localhost:5000/api/v1/cards" \
  -H "Authorization: Bearer your_github_token"

# Get a specific card
curl -X GET "http://localhost:5000/api/v1/cards/codex_chronosphere" \
  -H "Authorization: Bearer your_github_token"

# Map a question to cards
curl -X POST "http://localhost:5000/api/v1/guidance/map" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_github_token" \
  -d '{"question":"What is the Chronosphere?"}'
```

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| "Connection refused" | Flask server not running | Start: `/home/tec_tgcr/.venv/bin/python /home/tec_tgcr/tec-tgcr/src/codex_api_server.py` |
| "Invalid authentication" | GitHub token missing/expired | Generate new PAT at <https://github.com/settings/tokens> |
| "404 Not Found" | Endpoint path incorrect | Check `config/gpt-actions-research.json` |
| "CORS error" | Server not allowing cross-origin | Confirm `flask-cors` installed |

---

## Next Steps

1. ✅ Start Flask server locally
2. ✅ Verify `/cards` endpoint returns data
3. → Create ChatGPT GPT with updated OpenAPI schema
4. → Test question mapping and card recommendations
5. → Log refinements for iterative improvement

---

**Notes for LuminAI & TEC Stewardship**:

- This GPT grounds responses in CODEX truth and prevents hallucination
- The `/refinements` endpoint lets you log insights from GPT interactions for future CODEX updates
- Keep OpenAPI spec in sync with Flask server — any new endpoint must be documented in `config/gpt-actions-research.json`
