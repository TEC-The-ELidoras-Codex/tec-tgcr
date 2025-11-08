# Knowledge API Quick Reference

**Auto-synced REST API for all personas, guides, and knowledge. No manual uploads.**

---

## 🔗 Endpoints

| Endpoint | Returns | Use Case |
|----------|---------|----------|
| `GET /api/personas/` | All 9 personas | List personas |
| `GET /api/personas/{name}` | Single persona (luminai, airth, etc.) | Get persona spec |
| `GET /api/guides/` | All 6 deployment guides | List guides |
| `GET /api/guides/{name}` | Single guide | Get guide content |
| `GET /api/classification/` | Shareable/internal rules | Get file classification |
| `GET /api/system/` | System integration guide | Get system info |
| `GET /api/knowledge/` | Complete knowledge base | Get everything at once |
| `GET /api/knowledge/health/` | Health check | Verify API status |

---

## 📝 Quick Tests

```bash
# Test personas endpoint
curl http://localhost:8000/api/personas/luminai | jq .title

# Test guides endpoint
curl http://localhost:8000/api/guides/pull_and_build | jq .title

# Test classification
curl http://localhost:8000/api/classification/ | jq .categories.shareable

# Test complete KB
curl http://localhost:8000/api/knowledge/ | jq .metadata

# Health check
curl http://localhost:8000/api/knowledge/health/
```

---

## 💻 Usage

### Python

```python
import requests

# Get persona
r = requests.get("http://localhost:8000/api/personas/airth")
persona = r.json()
print(persona['title'])
print(persona['content'])
```

### JavaScript

```javascript
// Get all knowledge
fetch('http://localhost:8000/api/knowledge/')
  .then(r => r.json())
  .then(kb => {
    console.log(`${kb.metadata.persona_count} personas loaded`);
  });
```

### Bash

```bash
# Get specific guide
curl http://localhost:8000/api/guides/gpt_deployment_ready | \
  jq -r '.content' | head -50
```

---

## 🚀 How It Works

1. **Source Files**: All knowledge stored in Git (markdown files)
   - `data/personas/*.md` (9 personas)
   - `PULL_AND_BUILD_GUIDE.md`, `SYSTEM_INTEGRATION_GUIDE.md`, etc.
   - `SHAREABLE_VS_INTERNAL_CLASSIFICATION.md`

2. **AssetLoader**: Auto-discovers and loads files from disk
   - Python class: `AssetLoader()` in `knowledge/asset_loader.py`
   - Caches results for performance
   - Updates when API restarts

3. **API Endpoints**: FastAPI routes serve as JSON
   - Python module: `knowledge_api.py` in `integrations/`
   - Registered routes: `/api/personas/`, `/api/guides/`, etc.
   - Returns structured JSON responses

4. **Auto-Sync**: When source files change → API reflects automatically
   - Edit `data/personas/luminai.md`
   - Commit to Git
   - Deploy API
   - Query `GET /api/personas/luminai`
   - ✅ Returns updated content

---

## 📊 Response Formats

### Persona Response

```json
{
  "name": "luminai",
  "title": "LuminAI — Resonance Synthesis & Temporal Coordination",
  "content": "Full markdown content...",
  "path": "data/personas/luminai.md",
  "metadata": {...}
}
```

### Guide Response

```json
{
  "name": "pull_and_build",
  "title": "Pull & Build Guide — Fresh Clone Setup",
  "content": "Full markdown content...",
  "path": "PULL_AND_BUILD_GUIDE.md"
}
```

### Knowledge Base Response

```json
{
  "personas": {...},
  "guides": {...},
  "classification": {...},
  "system": {...},
  "metadata": {
    "loaded_at": "2025-11-07T15:30:45.123456",
    "persona_count": 9,
    "guide_count": 6,
    "status": "auto-synced"
  }
}
```

---

## ✅ Verification Checklist

- [ ] AssetLoader loads 9 personas: `python -c "from src.tec_tgcr.knowledge.asset_loader import AssetLoader; loader = AssetLoader(); print(len(loader.load_personas()))"`
- [ ] AssetLoader loads 6 guides: `python -c "from src.tec_tgcr.knowledge.asset_loader import AssetLoader; loader = AssetLoader(); print(len(loader.load_guides()))"`
- [ ] API endpoints exist: `curl http://localhost:8000/api/personas/`
- [ ] Health check passes: `curl http://localhost:8000/api/knowledge/health/`
- [ ] All tests pass: `pytest tests/ -q`

---

## 📚 Documentation

- **Complete Guide**: See `KNOWLEDGE_API_GUIDE.md`
- **Implementation Details**: See `AUTO_SYNCED_KNOWLEDGE_API_COMPLETE.md`
- **Code**: `src/tec_tgcr/knowledge/asset_loader.py` + `src/tec_tgcr/integrations/knowledge_api.py`

---

## 🎯 Bottom Line

**Edit markdown files → Git → API auto-loads → Clients query API → Always in sync.**

No manual uploads. No outdated copies. Single source of truth.

✨ **Done.**
