# Knowledge API — Auto-Synced Knowledge Base

**Purpose**: Serve all personas, guides, and classification rules from a **single REST API** that automatically stays in sync with source files.

**Key Idea**: Edit markdown files in Git → API automatically reflects changes → All clients pull from API → No manual uploads needed.

---

## 🎯 The Problem This Solves

**Before (Manual)**:
```
Edit data/personas/luminai.md
↓
Manually copy to GPT KB
↓
Manually update knowledge_map.yml
↓
Manually add to app configs
↓ ❌ Risk of outdated copies everywhere
```

**After (Auto-Synced API)**:
```
Edit data/personas/luminai.md
↓
API auto-loads it
↓
All clients query API
↓
Everything always in sync ✅
```

---

## 🔗 API Endpoints (Auto-Loaded, No Manual Work)

### Personas

```bash
# List all 9 personas
curl http://localhost:8000/api/personas/

# Get specific persona (e.g., LuminAI)
curl http://localhost:8000/api/personas/luminai
curl http://localhost:8000/api/personas/airth
curl http://localhost:8000/api/personas/arcadia
curl http://localhost:8000/api/personas/ely
curl http://localhost:8000/api/personas/companion
curl http://localhost:8000/api/personas/fusion
```

**Response**:
```json
{
  "name": "luminai",
  "title": "LuminAI — Resonance Synthesis & Temporal Coordination",
  "content": "Full persona spec markdown...",
  "path": "data/personas/luminai.md",
  "metadata": {...}
}
```

### Guides

```bash
# List all guides
curl http://localhost:8000/api/guides/

# Get specific guide
curl http://localhost:8000/api/guides/pull_and_build
curl http://localhost:8000/api/guides/system_integration
curl http://localhost:8000/api/guides/gpt_deployment_ready
curl http://localhost:8000/api/guides/shareable_vs_internal_classification
```

### Classification

```bash
# Get shareable/internal rules
curl http://localhost:8000/api/classification/
```

**Response**:
```json
{
  "title": "Shareable vs. Internal Classification",
  "categories": {
    "shareable": ["data/personas/", "docs/", "src/", "lore/", ...],
    "internal": [".env", ".venv/", "secrets-local/", ...],
    "conditional": ["ai-workflow/*.ipynb", ...]
  }
}
```

### System Integration

```bash
# Get system architecture & workflows
curl http://localhost:8000/api/system/
```

### Complete Knowledge Base

```bash
# Get ALL assets at once (personas + guides + classification + system)
curl http://localhost:8000/api/knowledge/
```

### Health Check

```bash
# Verify all assets load successfully
curl http://localhost:8000/api/knowledge/health/
```

**Response**:
```json
{
  "status": "healthy",
  "personas_loaded": 9,
  "guides_loaded": 6,
  "auto_synced": true,
  "last_sync": "2025-11-07T15:30:45.123456"
}
```

---

## 🚀 How It Works (Auto-Sync Magic)

### 1. Asset Loader (`knowledge/asset_loader.py`)

**Does**:
- Scans `data/personas/*.md` → Loads all 9 personas
- Scans specific guides → Loads PULL_AND_BUILD_GUIDE.md, SYSTEM_INTEGRATION_GUIDE.md, etc.
- Loads SHAREABLE_VS_INTERNAL_CLASSIFICATION.md
- Parses YAML front matter + markdown body
- Caches results (but updates when files change)

**Key**: It reads files from disk **each time the API starts**. Edit a markdown file → Restart API → New content is served automatically.

### 2. API Endpoints (`integrations/knowledge_api.py`)

**Does**:
- FastAPI routes that call the asset loader
- Return structured JSON responses
- Provide unified knowledge base endpoint (`/api/knowledge/`)
- Health checks to verify sync status

**Key**: No database needed. Everything is loaded from Git-tracked markdown files.

### 3. The Auto-Sync Loop

```
Source Files (Git)              API                    Clients
─────────────────              ────                   ────────
personas/*.md ─────┐
guides/*.md ────────├─→ AssetLoader ─→ FastAPI Routes ─→ GPT
classification.md ─┤              │         │             WordPress
system guide ───────┘              │         │             React Apps
                        (Caches)   │    (JSON endpoints)
                        (Updates   │
                         on reload)
```

**Flow**:
1. Developer edits `data/personas/luminai.md` and pushes to Git
2. Team member deploys API (or API auto-reloads on deployment)
3. API discovers updated file and re-caches it
4. All clients (`/api/personas/luminai`) get new content automatically
5. Zero manual updates needed

---

## 💾 What Files Get Auto-Loaded

| File | Endpoint | Auto-Loaded? |
|------|----------|-------------|
| `data/personas/*.md` (9 files) | `GET /api/personas/` | ✅ Yes |
| `PULL_AND_BUILD_GUIDE.md` | `GET /api/guides/pull_and_build` | ✅ Yes |
| `SYSTEM_INTEGRATION_GUIDE.md` | `GET /api/guides/system_integration` | ✅ Yes |
| `SHAREABLE_VS_INTERNAL_CLASSIFICATION.md` | `GET /api/classification/` | ✅ Yes |
| `GPT_DEPLOYMENT_READY.md` | `GET /api/guides/gpt_deployment_ready` | ✅ Yes |
| `GPT_PERSONAS_ATTACHMENT_DECISION.md` | `GET /api/guides/gpt_personas_attachment_decision` | ✅ Yes |
| `GPT_ATTACHMENT_CHEAT_SHEET.md` | `GET /api/guides/gpt_attachment_cheat_sheet` | ✅ Yes |

**Result**: No manual file uploads. Changes to any of these files automatically appear in API responses.

---

## 🔌 Integration Examples

### Python Client (Pull Persona from API)

```python
import requests

# Fetch LuminAI persona spec from API
response = requests.get("http://localhost:8000/api/personas/luminai")
persona = response.json()

print(f"Persona: {persona['title']}")
print(f"Content:\n{persona['content']}")
print(f"Source: {persona['path']}")
```

### JavaScript Client (Pull All Assets)

```javascript
// Fetch complete knowledge base
fetch('http://localhost:8000/api/knowledge/')
  .then(res => res.json())
  .then(kb => {
    console.log(`Loaded ${kb.metadata.personas_loaded} personas`);
    console.log(`Loaded ${kb.metadata.guides_loaded} guides`);
    console.log(`Auto-synced: ${kb.metadata.auto_synced}`);

    // Use persona data
    const luminai = kb.personas.luminai;
    console.log(luminai.title);
  });
```

### GPT Builder (Pull Persona from API)

Instead of uploading persona markdown manually:

```
[In GPT Builder Knowledge Base Upload]

1. Delete manual uploads
2. Add API URL: http://your-api.com/api/personas/
3. Set to auto-refresh (webhook on Git push)
4. GPT now gets personas automatically from API
```

### WordPress Plugin (Pull Classification Rules)

```php
<?php
// Inside WordPress plugin
$response = wp_remote_get('http://localhost:8000/api/classification/');
$classification = json_decode(wp_remote_retrieve_body($response));

// Use shareable/internal rules to decide what to display
$shareable = $classification->categories->shareable;
$internal = $classification->categories->internal;
?>
```

---

## 📊 API Response Examples

### GET /api/personas/luminai

```json
{
  "name": "luminai",
  "title": "LuminAI — Resonance Synthesis & Temporal Coordination",
  "content": "LuminAI is the resonance synthesis agent...\n\n## Core Mandate\n...",
  "path": "data/personas/luminai.md",
  "metadata": {
    "role": "CODEX Resonance Sentinel",
    "mandate": "Primary AI orchestrator"
  }
}
```

### GET /api/guides/

```json
{
  "guides": {
    "pull_and_build": {
      "title": "Pull & Build Guide",
      "path": "PULL_AND_BUILD_GUIDE.md",
      "content": "..."
    },
    "system_integration": {
      "title": "System Integration Guide",
      "path": "SYSTEM_INTEGRATION_GUIDE.md",
      "content": "..."
    },
    ...
  },
  "count": 6,
  "status": "auto-synced"
}
```

### GET /api/knowledge/

```json
{
  "personas": { "luminai": {...}, "airth": {...}, ... },
  "guides": { "pull_and_build": {...}, ... },
  "classification": { "title": "...", "categories": {...} },
  "system": { "title": "...", "content": "..." },
  "metadata": {
    "loaded_at": "2025-11-07T15:30:45.123456",
    "persona_count": 9,
    "guide_count": 6,
    "status": "auto-synced"
  }
}
```

---

## ⚙️ Setup & Deployment

### Local Development

```bash
# 1. Install dependencies
pip install fastapi python-frontmatter

# 2. Run development server
python -m tec_tgcr.cli run-api

# 3. Test endpoints
curl http://localhost:8000/api/personas/
curl http://localhost:8000/api/knowledge/health/
```

### Docker Deployment

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -e .[dev]
EXPOSE 8000
CMD ["python", "-m", "tec_tgcr.cli", "run-api"]
```

### Azure Deployment

```bash
# Deploy as Azure App Service or Container Instances
az containerapp create \
  --name tec-knowledge-api \
  --image your-registry/tec-api:latest \
  --environment-variables REPO_ROOT=/app
```

---

## 🔄 Auto-Sync Workflows

### Workflow 1: Edit Persona → Auto-Update Everywhere

```bash
# 1. Developer edits persona locally
vim data/personas/luminai.md

# 2. Commit and push to Git
git add data/personas/luminai.md
git commit -m "feat: enhance LuminAI persona"
git push origin research/resonance-agent

# 3. CI/CD deploys updated API (or API reloads)
# 4. All clients immediately see new content

# 5. Verify
curl http://api.example.com/api/personas/luminai
# Returns: updated content ✅
```

### Workflow 2: Add New Guide → Instantly Available

```bash
# 1. Create new guide
echo "# New Deployment Strategy" > NEW_GUIDE.md

# 2. Update asset loader to include it (one-time setup)
# Modify AssetLoader.guides_pattern to include NEW_GUIDE.md

# 3. Restart API
# 4. Guide is now available
curl http://api.example.com/api/guides/new_guide
# Returns: new guide content ✅
```

### Workflow 3: Webhook Auto-Refresh (Optional)

```bash
# Setup GitHub webhook to trigger API refresh on push
# https://your-api.com/webhooks/git-push

# When developer pushes to main:
# 1. GitHub sends webhook
# 2. API re-loads all assets
# 3. Clients immediately see changes
# (No manual restart needed)
```

---

## ✅ Verification Checklist

- [ ] Asset loader discovers all 9 personas
- [ ] Asset loader finds all 6 guides
- [ ] API `/personas/` returns all 9
- [ ] API `/personas/luminai` returns correct persona
- [ ] API `/guides/` returns all 6
- [ ] API `/classification/` returns shareable/internal rules
- [ ] API `/system/` returns system integration guide
- [ ] API `/knowledge/` returns complete unified knowledge base
- [ ] API `/knowledge/health/` reports `status: healthy`
- [ ] Edit a markdown file locally
- [ ] Restart API and verify changes appear in response

---

## 🎆 Result

**No more manual uploads. No more outdated copies. One source of truth.**

When someone asks: "Where's the latest persona spec?" → Answer: "Query the API, it's always current."

---

## Next: Integration Examples

See `API_CLIENT_EXAMPLES.md` for:
- Python client library
- JavaScript/React integration
- GPT Builder webhook setup
- WordPress plugin integration
- Team bot commands
