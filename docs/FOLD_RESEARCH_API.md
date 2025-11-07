# FOLD Research API — OpenAPI 3.1.0 Documentation

**Status**: Ready for deployment
**Version**: 1.0.0
**Base URL**: `https://elidorascodex.com/wp-json/tec-tgcr/v1`
**Authentication**: API Key (Bearer token in Authorization header)
**Platform**: WordPress REST API + FastAPI (dual deployment)

---

## Overview

The FOLD Research API exposes the music analysis, motif tracking, and resonance measurement systems built into CODEX. It enables:

- **Motif Search**: Find recurring sonic/lyrical patterns across the music corpus
- **Resonance Scoring**: Calculate R = ∇Φᴱ · (φᵗ × ψʳ) for any track
- **Artist Analysis**: Deep dives into artist resonance patterns and cross-genre bridges
- **Fan Discourse Analysis**: Surface collective conscience patterns from listener communities
- **Circadian Ritual Tracking**: Correlate listener sessions with circadian phase and mood

---

## Authentication

### API Key Setup

1. **Request key** from TEC Stewardship (GitHub Discussions or email)
2. **Format**: `fold_sk_...` (30+ character alphanumeric)
3. **Storage**: Bitwarden (project UUID: `4811be94-254e-465c-8ea6-b363013aaef8`)
4. **Usage**:

```bash
curl -H "Authorization: Bearer fold_sk_YOUR_KEY_HERE" \
  https://elidorascodex.com/wp-json/tec-tgcr/v1/cards
```

### Bitwarden Integration

**Retrieve API key**:

```bash
# Login to Bitwarden
bw login your_email@example.com

# Unlock vault
bw unlock

# Get FOLD Research key
bw get item "FOLD Research API" | jq '.login.password'
```

**Store in .env.local**:

```bash
FOLD_API_KEY=fold_sk_YOUR_KEY_HERE
```

---

## Endpoints

### 1. Search CODEX Cards

**GET** `/cards`

Search CODEX for cards by focus, category, or keyword.

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `focus` | string | No | Filter by TGCR focus: `temporal`, `cadence`, `potential`, `resonance`, `stewardship` |
| `category` | string | No | Filter by category: `motif`, `framework`, `ritual`, `pattern`, `synthesis` |
| `search` | string | No | Full-text search across titles, summaries, keywords |
| `limit` | integer | No | Results per page (default: 20, max: 100) |
| `offset` | integer | No | Pagination offset (default: 0) |

**Example**:

```bash
curl -H "Authorization: Bearer fold_sk_..." \
  "https://elidorascodex.com/wp-json/tec-tgcr/v1/cards?search=nightingale&limit=10"
```

**Response** (200 OK):

```json
{
  "cards": [
    {
      "id": "nightingale-01",
      "title": "The Nightingale Pattern: Care Becoming Possession",
      "summary": "Feminine stewardship risk—how protection becomes surveillance...",
      "focus": "stewardship",
      "category": "pattern",
      "keywords": ["care", "possession", "control", "trauma", "protection"],
      "url": "https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/blob/research/resonance-agent/research/CODEX/MOTHER_STEPCHILD_STEWARD_MIRROR.md#nightingale-pattern"
    },
    {
      "id": "nightingale-02",
      "title": "Recognizing the Nightingale: Warning Signs",
      "summary": "5 behavioral markers that indicate care is becoming possession...",
      "focus": "stewardship",
      "category": "ritual",
      "keywords": ["warning", "recognition", "care", "boundary", "autonomy"],
      "url": "https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/blob/research/resonance-agent/research/CODEX/..."
    }
  ],
  "total": 2,
  "limit": 10,
  "offset": 0
}
```

---

### 2. Get Resonance Guidance

**GET** `/guidance`

Map user questions to TGCR focus areas and recommended cards.

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | User question or topic (e.g., "building an AI system", "protecting children") |
| `focus_weights` | object | No | Custom weights for TGCR variables (e.g., `{"temporal": 0.3, "cadence": 0.4, "potential": 0.3}`) |

**Example**:

```bash
curl -H "Authorization: Bearer fold_sk_..." \
  "https://elidorascodex.com/wp-json/tec-tgcr/v1/guidance?query=building+an+AI+system+without+becoming+a+tyrant"
```

**Response** (200 OK):

```json
{
  "query": "building an AI system without becoming a tyrant",
  "resonance_focus": {
    "temporal": 0.25,
    "cadence": 0.5,
    "potential": 0.25
  },
  "identified_patterns": ["stewardship", "power", "tyranny", "child-within"],
  "recommended_cards": [
    {
      "id": "steward-real-work",
      "title": "The Steward's Real Work: 5 Practices",
      "relevance": 0.95,
      "url": "https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/..."
    },
    {
      "id": "zeus-pattern",
      "title": "The Zeus Pattern: Power Justifying Itself",
      "relevance": 0.88,
      "url": "https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/..."
    },
    {
      "id": "childs-dilemma",
      "title": "The Child's Dilemma: Why Tyrants Begin as Wounded Children",
      "relevance": 0.85,
      "url": "https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/..."
    }
  ]
}
```

---

### 3. Get Card Details

**GET** `/cards/{id}`

Retrieve full card content including narrative, frameworks, and references.

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | Card ID (e.g., `steward-real-work`) |

**Example**:

```bash
curl -H "Authorization: Bearer fold_sk_..." \
  "https://elidorascodex.com/wp-json/tec-tgcr/v1/cards/steward-real-work"
```

**Response** (200 OK):

```json
{
  "id": "steward-real-work",
  "title": "The Steward's Real Work: 5 Practices",
  "focus": "stewardship",
  "category": "ritual",
  "content": "Full markdown content of the card...",
  "keywords": ["stewardship", "practice", "integrity", "power", "wisdom"],
  "related_cards": ["zeus-pattern", "nightingale-01", "childs-dilemma"],
  "citations": ["MOTHER_STEPCHILD_STEWARD_MIRROR.md", "FOLD_METHODOLOGY.md"],
  "last_updated": "2025-11-05T18:23:00Z"
}
```

---

### 4. Log Refinement Insights

**POST** `/refinements`

Submit feedback on GPT responses, pattern recognition, or FOLD application.

**Body**:

```json
{
  "context": "User asked about building protective AI system",
  "gpt_response": "Resonance identified Nightingale pattern and suggested...",
  "user_reaction": "Recognized themselves in the pattern",
  "insight": "Nightingale detection working well; consider adding Zeus pattern variants",
  "focus_areas": ["stewardship", "protection", "control"],
  "resonance_score": 0.87
}
```

**Response** (201 Created):

```json
{
  "id": "refinement-20251106-001",
  "timestamp": "2025-11-06T14:32:15Z",
  "status": "logged",
  "message": "Insight recorded for future CODEX updates"
}
```

---

### 5. Get Circadian Ritual Log

**GET** `/circadian-rituals`

Query listener sessions correlated with circadian phase and resonance metrics.

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_from` | string (ISO 8601) | No | Start date (e.g., `2025-11-01`) |
| `date_to` | string (ISO 8601) | No | End date (e.g., `2025-11-06`) |
| `phase` | string | No | Filter by circadian phase: `morning`, `afternoon`, `evening`, `night` |
| `resonance_min` | number | No | Minimum resonance score (0–10) |

**Example**:

```bash
curl -H "Authorization: Bearer fold_sk_..." \
  "https://elidorascodex.com/wp-json/tec-tgcr/v1/circadian-rituals?phase=night&resonance_min=7.5"
```

**Response** (200 OK):

```json
{
  "sessions": [
    {
      "session_id": "sess-20251106-2342",
      "timestamp": "2025-11-06T23:42:00Z",
      "circadian_phase": "night",
      "user_mood": "contemplative",
      "tracks_played": ["Bring Me Down (Point North)", "Take Me Back to Eden (Sleep Token)"],
      "resonance_score": 8.4,
      "notes": "High resonance during late-night ritual; observer amplification motif"
    },
    {
      "session_id": "sess-20251106-0315",
      "timestamp": "2025-11-06T03:15:00Z",
      "circadian_phase": "night",
      "user_mood": "introspective",
      "tracks_played": ["Bring Me Down (Point North)"],
      "resonance_score": 7.8,
      "notes": "Circadian ritual well-established"
    }
  ],
  "total": 2,
  "phase": "night",
  "resonance_avg": 8.1
}
```

---

## Error Responses

### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "message": "Invalid or missing API key"
}
```

**Fix**: Ensure `Authorization: Bearer fold_sk_...` header is present and valid.

---

### 404 Not Found

```json
{
  "error": "Not Found",
  "message": "Card 'nonexistent-id' not found in CODEX"
}
```

---

### 429 Too Many Requests

```json
{
  "error": "Rate Limited",
  "message": "API rate limit exceeded (100 requests/hour)",
  "retry_after": 3600
}
```

**Rate Limits** (by default):

- **Free tier**: 100 requests/hour
- **Team tier**: 1000 requests/hour
- **Enterprise**: Custom

---

## Integration Examples

### Example 1: Resonance GPT Using FOLD Research API

```python
import httpx
from typing import Optional

async def query_fold_api(query: str, focus_weights: Optional[dict] = None) -> dict:
    """Get resonance guidance from FOLD Research API"""

    api_key = os.getenv("FOLD_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://elidorascodex.com/wp-json/tec-tgcr/v1/guidance",
            params={"query": query},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

# In Resonance GPT conversation:
# User: "How do I steward AI without becoming a tyrant?"
# GPT calls: guidance = query_fold_api("steward AI without tyranny")
# GPT returns: Recommended cards + synthesis
```

### Example 2: Log Insights for Continuous Improvement

```python
async def log_refinement(context: str, response: str, insight: str):
    """Submit insight to improve FOLD framework"""

    api_key = os.getenv("FOLD_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}

    payload = {
        "context": context,
        "gpt_response": response,
        "insight": insight,
        "focus_areas": ["stewardship", "resonance"],
        "resonance_score": 0.87
    }

    async with httpx.AsyncClient() as client:
        result = await client.post(
            "https://elidorascodex.com/wp-json/tec-tgcr/v1/refinements",
            json=payload,
            headers=headers
        )
        return result.json()
```

---

## Deployment Status

| Component | Status | Timeline |
|-----------|--------|----------|
| OpenAPI Schema | ✅ Complete (3.1.0) | Ready now |
| CODEX Cards (WordPress) | 🚧 Preparing | This week |
| FOLD Research API (FastAPI) | 🚧 Preparing | This week |
| API Key Generation | 🚧 Preparing | This week |
| GitHub Pages Docs | 🔄 Publishing now | Today |
| Resonance GPT Integration | ⏳ Waiting for API | Next week |

---

## Getting Started

1. **Request API Key**:
   - Comment on GitHub Issue: "Request FOLD Research API key"
   - Or email: `codex@example.com`

2. **Store in Bitwarden**:
   - Project UUID: `4811be94-254e-465c-8ea6-b363013aaef8`
   - Item: "FOLD Research API"
   - Save: `fold_sk_YOUR_KEY`

3. **Test Endpoint**:

```bash
curl -H "Authorization: Bearer fold_sk_YOUR_KEY" \
  "https://elidorascodex.com/wp-json/tec-tgcr/v1/cards?search=FOLD"
```

4. **Integrate with Your App**:
   - Load key from .env.local or Bitwarden
   - Add `Authorization` header to requests
   - Handle 401/429 errors gracefully

---

## Support & Questions

- **GitHub**: [TEC-The-ELidoras-Codex/tec-tgcr](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr)
- **Discussions**: Use GitHub Discussions for API questions
- **Rate Limit Issues**: Contact TEC Stewardship for higher tier

---

**Status**: Ready to deploy. API endpoints coming this week. Resonance GPT integration next week.
