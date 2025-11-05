# CODEX API Setup Guide

## Current Status

- ✓ OpenAPI schema: `gpt-actions-research.json` (updated)
- ✓ 7 CODEX cards ready
- ⚠️ Backend API: Not running (placeholder URL)

## How to Proceed

### Method 1: ChatGPT GPT Builder (NO Backend Needed) ⭐ RECOMMENDED

**Fastest way to get CODEX working in ChatGPT:**

1. Go to [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor)
2. Click "Create new GPT"
3. Name: `CODEX Navigator`
4. In "Instructions" field, paste system prompt from `GPT_IMPORT_GUIDE.md`
5. **Upload Files** (Knowledge section):
   - `research/CODEX/core_theory/CODEX_CHRONOSPHERE.md`
   - `research/CODEX/core_theory/CODEX_PAC_MAN_UNIVERSE.md`
   - `research/CODEX/core_theory/CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF.md`
   - `research/CODEX/nodes/CODEX_SYNTHETIC_INTROSPECTION.md`
   - `research/CODEX/nodes/CODEX_GUT_BRAIN_PHI_T.md`
   - `research/CODEX/clusters/CODEX_SLEEP_TOKEN_RAIN.md`
   - `research/CODEX/clusters/CODEX_TDWP.md`
6. **DO NOT add Actions yet** (no backend running)
7. Click "Save" and test

**Test:**

- Ask: "Explain TGCR in one sentence"
- Ask: "What's the core insight of Chronosphere?"
- Ask: "Analyze this decision using CODEX"

---

### Method 2: Deploy Python Backend (For Actions API)

If you want the GPT to **call your API via Actions**, set up a backend:

#### Step 1: Create Flask Backend

```bash
cd /home/tec_tgcr/tec-tgcr
pip install flask flask-cors python-dotenv
```

Create `src/codex_api_server.py`:

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
from pathlib import Path

app = Flask(__name__)
CORS(app)

CODEX_DIR = Path(__file__).parent.parent / "research" / "CODEX"

def load_cards():
    """Load all CODEX cards from markdown files."""
    cards = []
    
    card_files = [
        ("core_theory", "CODEX_CHRONOSPHERE.md", "codex_chronosphere"),
        ("core_theory", "CODEX_PAC_MAN_UNIVERSE.md", "codex_pac_man_universe"),
        ("core_theory", "CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF.md", "codex_steward_matter_subconscience_self"),
        ("nodes", "CODEX_SYNTHETIC_INTROSPECTION.md", "codex_synthetic_introspection"),
        ("nodes", "CODEX_GUT_BRAIN_PHI_T.md", "codex_gut_brain_phi_t"),
        ("clusters", "CODEX_SLEEP_TOKEN_RAIN.md", "codex_sleep_token_rain"),
        ("clusters", "CODEX_TDWP.md", "codex_tdwp"),
    ]
    
    for category, filename, slug in card_files:
        path = CODEX_DIR / category / filename
        if path.exists():
            cards.append({
                "slug": slug,
                "title": filename.replace(".md", "").replace("_", " "),
                "category": category,
                "focus": "multi_domain",
                "file_path": f"research/CODEX/{category}/{filename}",
            })
    
    return cards

@app.route('/api/v1/cards', methods=['GET'])
def list_cards():
    """List all CODEX cards."""
    cards = load_cards()
    search = request.args.get('search', '').lower()
    
    if search:
        cards = [c for c in cards if search in c['slug'] or search in c['title'].lower()]
    
    return jsonify({"cards": cards, "count": len(cards)})

@app.route('/api/v1/cards/<slug>', methods=['GET'])
def get_card(slug):
    """Get a specific card."""
    cards = load_cards()
    card = next((c for c in cards if c['slug'] == slug), None)
    
    if not card:
        return jsonify({"error": "Card not found"}), 404
    
    return jsonify(card)

@app.route('/api/v1/health', methods=['GET'])
def health():
    """Health check."""
    return jsonify({"status": "ok", "service": "CODEX API"})

if __name__ == '__main__':
    print("🚀 CODEX API Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)
```

#### Step 2: Run the Server

```bash
python src/codex_api_server.py
```

Output:

```
🚀 CODEX API Server starting on http://localhost:5000
```

#### Step 3: Test the API

```bash
curl http://localhost:5000/api/v1/cards
```

#### Step 4: Update OpenAPI Schema

```json
"servers": [
  {
    "url": "http://localhost:5000/api/v1",
    "description": "CODEX Knowledge Service (Local)"
  }
]
```

#### Step 5: Add to ChatGPT Actions

In ChatGPT GPT Builder → "Add actions":

1. Authentication: **API Key**
2. Key: `Bearer codex_local_key`
3. Schema URL: Upload `gpt-actions-research.json`

---

### Method 3: Deploy to Cloud (Production)

For a deployed version, use:

- **Render** (free tier): Deploy Flask to render.com
- **Replit**: Host Python backend free
- **Railway**: Easy Flask deployments
- **AWS Lambda**: Serverless with API Gateway

Update server URL:

```json
"servers": [
  {
    "url": "https://codex-api.render.com/api/v1",
    "description": "CODEX Knowledge Service (Production)"
  }
]
```

---

## Recommended Path (Next 30 minutes)

1. ✅ **Now**: Test ChatGPT GPT Builder WITHOUT backend (Method 1)
   - Fast, works immediately
   - No server setup needed

2. ⏭️ **Later**: Deploy Python backend (Method 2)
   - When you want GPT to call your API
   - Test locally first on `http://localhost:5000`

3. 🚀 **Eventually**: Deploy to cloud (Method 3)
   - Share your CODEX GPT publicly
   - Production-ready

---

## Current Card Inventory

| Card | Category | File Path |
|------|----------|-----------|
| CODEX Chronosphere | core_theory | `core_theory/CODEX_CHRONOSPHERE.md` |
| CODEX Pac-Man Universe | core_theory | `core_theory/CODEX_PAC_MAN_UNIVERSE.md` |
| CODEX Mother/Stepchild | core_theory | `core_theory/CODEX_MOTHER_STEPCHILD_STEWARD_MIRROR.md` |
| CODEX Synthetic Introspection | nodes | `nodes/CODEX_SYNTHETIC_INTROSPECTION.md` |
| CODEX Gut-Brain Phi-T | nodes | `nodes/CODEX_GUT_BRAIN_PHI_T.md` |
| CODEX Sleep Token Rain | clusters | `clusters/CODEX_SLEEP_TOKEN_RAIN.md` |
| CODEX TDWP | clusters | `clusters/CODEX_TDWP.md` |

---

## Troubleshooting

**"Server error calling API"**
→ You don't have a backend running. Use Method 1 first (no backend needed).

**"404 Card not found"**
→ Check the slug matches the filename and path is correct.

**"CORS error in browser"**
→ Backend not running with CORS enabled. Use the Flask server above.

---

## Next Steps

**Pick one:**

- [ ] **I want to test CODEX in ChatGPT NOW** → Use Method 1 above
- [ ] **I want to deploy a local API** → Use Method 2, run the Python server
- [ ] **I want production-ready** → Combine Method 2 + 3, deploy to Render/Railway

Tell me which and I'll help you execute it!
