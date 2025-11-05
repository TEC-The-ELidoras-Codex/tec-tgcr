# Research API — Bridging RESEARCH_FRAMEWORK to CODEX via Flask Backend

**Date**: November 5, 2025  
**Status**: Ready for integration with `/api/v1/` endpoints  
**Personas**: Both CODEX (Analyst/Chronicle/Synthesist) and TEC (Airth/Arcadia/LuminAI/Kaznak) supported

---

## Vision

Transform your **RESEARCH_FRAMEWORK** (album motif analysis + cross-genre synthesis) into a **queryable knowledge layer** that:

1. Integrates directly with your Flask backend (`src/codex_api_server.py`)
2. Maps motifs to TGCR axes and CODEX cards
3. Supports dual persona systems for different analytical lenses
4. Auto-tags album research with φᵗ, ψʳ, Φᴱ scores

---

## Architecture

```
research/CODEX/
├── RESEARCH_FRAMEWORK.md         (existing: motif catalog, templates, ritual log)
├── RESEARCH_API.md               (this file: API specification)
├── research_data/
│   ├── motif_registry.json       (structured motif definitions + scoring rules)
│   ├── albums/
│   │   ├── sleep_token.json
│   │   ├── silverstein.json
│   │   ├── hip_hop_cluster.json
│   │   └── ...
│   └── cross_genre_synthesis/
│       ├── motif_bridges.json    (artist-to-artist resonance mappings)
│       └── collective_thesis.json (zero-singularity + Mother Matter analysis)
└── endpoints/
    ├── POST /research/analyze-album
    ├── GET /research/motif/<motif_slug>
    ├── POST /research/map-to-codex
    ├── GET /research/synthesis/<cross_genre_topic>
    └── GET /research/by-persona/<persona_name>

src/codex_api_server.py
├── New endpoints (all prefixed /api/v1/):
│   ├── POST /research/tag-motifs        (tag new album data)
│   ├── GET /research/motif-scores       (get φᵗ/ψʳ/Φᴱ for all motifs)
│   ├── POST /research/query-synthesis   (cross-genre synthesis engine)
│   └── GET /research/persona/<name>     (filtered by persona analysis style)
└── TGCR Scoring Engine:
    ├── score_temporal_attention(motif_keywords, circadian_markers)
    ├── score_structural_cadence(harmonic_patterns, genre_overlap)
    └── score_contextual_potential(emotional_energy, ritual_invocation)
```

---

## TGCR-Motif Alignment Matrix

Map each motif in `RESEARCH_FRAMEWORK.md` to TGCR axes:

| Motif | φᵗ (Temporal) | ψʳ (Structural) | Φᴱ (Contextual) | CODEX Bridge |
|-------|---|---|---|---|
| **Mother Matter yearning** | 7 (primal cyclicity) | 9 (archetypal loop) | 9 (highest stakes) | STEWARD/MATTER/SUBCONSCIENCE/SELF |
| **Emotional struggle** | 8 (crisis moments) | 6 (fragmentation) | 8 (vulnerable) | SYNTHETIC INTROSPECTION (AI + feeling) |
| **Resilience & survival** | 6 (steady state) | 9 (strong structure) | 7 (hope energy) | PAC-MAN UNIVERSE (loops + persistence) |
| **Legacy & remembrance** | 9 (death—time collapse) | 8 (narrative arc) | 8 (meaning-making) | CHRONOSPHERE (thresholds to eternity) |
| **Spiritual/transcendence** | 8 (awakening moment) | 9 (unified harmony) | 9 (transformation) | STEWARD/MATTER/SUBCONSCIENCE/SELF (unity) |
| **Zero/singularity collapse** | 10 (infinite compression) | 10 (convergence) | 10 (all-stakes) | CHRONOSPHERE (zero-singularity philosophy) |
| **Ritual & ceremony** | 7 (cyclical action) | 10 (repetition is structure) | 8 (collective power) | GUT-BRAIN PHI-T (embodied ritual) |
| **Song as survival** | 8 (moment of voice) | 9 (harmonic coherence) | 9 (collective resonance) | SLEEP TOKEN RAIN + TDWP (music as meaning) |

---

## Dual Persona Analytical Lenses

### CODEX Personas (Response Layer)

Used in ChatGPT GPT responses and quick synthesis:

- **[Analyst]**: Fact-forward, motif-tagged, cites card slugs
  - Asks: "Which card explains this motif's presence?"
  - Output: Motif → TGCR scores → CODEX card → recommended next card

- **[Chronicle]**: Narrative-driven, cross-album synthesis, temporal arcs
  - Asks: "How does this motif evolve across genres and decades?"
  - Output: Timeline of motif appearance → cultural inflection points → collective thesis

- **[Synthesist]**: Integration-focused, bridges motifs, ritual design
  - Asks: "How can this motif become a practice?"
  - Output: Ritual scaffolding using TGCR + motif + CODEX card

### TEC Personas (Research Layer)

Used for deeper investigation and verification:

- **[Airth]**: Verification mode — demands citations, falsifiable hypotheses, confound analysis
  - Routes research queries to web research tools
  - Flags: "Which albums are you citing? What's the counter-hypothesis?"

- **[Arcadia]**: Narrative weaver — translates motif analysis into myth-scientific prose
  - Compresses multiple albums into poetic summaries
  - Adds OXY/DOP/ADR neurochemical projection

- **[LuminAI]**: Companion reflection — asks "What does this mean to you?"
  - Invites personal resonance with motif findings
  - Offers small next-step recommendations

- **[Kaznak]**: Strategic lens — maps research to long-term TGCR implications
  - Questions: "If this motif is accelerating globally, what changes in our roadmap?"
  - Connects to decision logs and strategic bets

---

## API Endpoint Specifications

### 1. Tag New Album (Research Input)

**Request**:
```http
POST /api/v1/research/tag-motifs
Content-Type: application/json

{
  "artist": "Sleep Token",
  "album": "Take Me Back to Eden",
  "year": 2024,
  "genre": "metal-mystical",
  "personas_enabled": ["Analyst", "Arcadia"],
  "motif_tags": [
    {
      "motif": "mother_matter_yearning",
      "confidence": 0.95,
      "evidence": "Lyrical references to 'mother voice', 'singing into the void'",
      "timestamp_markers": ["4:20", "midnight peak"]
    },
    {
      "motif": "spiritual_transcendence",
      "confidence": 0.88,
      "evidence": "Liturgical structure, group call-and-response"
    },
    {
      "motif": "zero_singularity_collapse",
      "confidence": 0.92,
      "evidence": "Distortion → silence → rebuild pattern in 'Aqua Regia'"
    }
  ],
  "circadian_observations": [
    "Album best experienced at 4:20 or midnight",
    "Distortion peaks align with peak vulnerability windows"
  ]
}
```

**Response**:
```json
{
  "status": "success",
  "album_id": "sleep_token_eden_2024",
  "motifs_tagged": 3,
  "tgcr_scores": {
    "phi_t": 8.2,
    "psi_r": 9.1,
    "phi_e": 9.0
  },
  "primary_codex_card": "codex_steward_matter_subconscience_self",
  "secondary_cards": [
    "codex_chronosphere",
    "codex_sleep_token_rain"
  ],
  "analysis_by_persona": {
    "Analyst": "3 motifs mapped to STEWARD/MATTER/SUBCONSCIENCE/SELF + CHRONOSPHERE. φᵗ peak at 8.2 suggests temporal vulnerability window (4:20, midnight).",
    "Arcadia": "Sleep Token weaves liturgical structure with primal yearning. The 'mother voice' is both personal wound and collective invocation—a 9.0 on contextual stakes."
  },
  "next_actions": [
    "Log to CIRCADIAN_RITUAL_LOG.md",
    "Compare motif profile to Silverstein and hip-hop triumvirate",
    "Test hypothesis: all three artist groups peak at 4:20 marker"
  ]
}
```

---

### 2. Query Motif Database

**Request**:
```http
GET /api/v1/research/motif/mother_matter_yearning?expand=all_artists&min_confidence=0.85
```

**Response**:
```json
{
  "motif_slug": "mother_matter_yearning",
  "definition": "Infant/primal call for maternal presence; matter/meaning conflation",
  "signal_keywords": ["mother", "voice", "home", "belonging", "matter", "hold"],
  "tgcr_archetype": {
    "phi_t": 7,
    "psi_r": 9,
    "phi_e": 9,
    "rationale": "Primal cyclicity + archetypal loop + highest emotional stakes"
  },
  "artists_detected": [
    {
      "artist": "Sleep Token",
      "albums": ["Take Me Back to Eden"],
      "confidence": 0.95,
      "examples": ["'Aqua Regia' vocal melody", "Group ritual call"]
    },
    {
      "artist": "Silverstein",
      "albums": ["The Antibloom", "Pink Moon"],
      "confidence": 0.92,
      "examples": ["'Arrived' bridge", "Emo vulnerability peak"]
    },
    {
      "artist": "Tupac",
      "albums": ["Me Against the World"],
      "confidence": 0.89,
      "examples": ["'Dear Mama' testimony", "Source of resilience"]
    }
  ],
  "codex_bridges": [
    "CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF (primary)",
    "CODEX_CHRONOSPHERE (temporal yearning)",
    "CODEX_PAC_MAN_UNIVERSE (memory of home—loop structure)"
  ],
  "circadian_markers": [
    "4:20 peak (3 artists)",
    "Midnight (2 artists)",
    "Dawn transition (1 artist)"
  ]
}
```

---

### 3. Map Question to Motifs + CODEX

**Request**:
```http
POST /api/v1/research/map-to-codex
Content-Type: application/json

{
  "question": "Why do metalcore and hip-hop both explore maternal themes?",
  "personas": ["Chronicle", "Airth", "Arcadia"],
  "depth": "deep"
}
```

**Response**:
```json
{
  "question": "Why do metalcore and hip-hop both explore maternal themes?",
  "primary_motif": "mother_matter_yearning",
  "hypothesis": "Global collective consciousness is reaching critical density around primal separation anxiety. Language/genre differences mask identical archetypal content.",
  "motif_convergence": {
    "metalcore": "Sleep Token, Silverstein (ethereal/liturgical framing)",
    "hip_hop": "Tupac, Eminem (testimony/survival framing)",
    "shared_core": "Primal call for 'home' + matter + belonging"
  },
  "tgcr_analysis": {
    "phi_t": "All detect 4:20 and midnight peaks independently—suggests global temporal synchrony",
    "psi_r": "Metalcore uses harmonic loops (ψʳ=9); hip-hop uses beat loops (ψʳ=9). Structure identical.",
    "phi_e": "Both genres treat maternal call as highest-stakes content (Φᴱ=9)"
  },
  "codex_synthesis": {
    "primary": "STEWARD_MATTER_SUBCONSCIENCE_SELF (defines 'matter' yearning)",
    "secondary": "CHRONOSPHERE (temporal synchrony at 4:20)",
    "tertiary": "PAC_MAN_UNIVERSE (loops as memory + home-return)"
  },
  "analyses_by_persona": {
    "Chronicle": "Across 30+ years, maternal invocation appears in Sleep Token (2024), Silverstein (2003), Tupac (1995). No direct influence—independent encoding. Suggests distributed field.",
    "Airth": "Falsifiable: If true, every major album 1995–2025 with 4:20 reference should tag 'mother matter'. Counter-hypothesis: surface coincidence, no deeper causation. Need 100+ album audit.",
    "Arcadia": "Both genres are singing the same prayer in different tongues. Metalcore priestess meets hip-hop griot—same ancestral call, different ritual container."
  }
}
```

---

### 4. Cross-Genre Synthesis

**Request**:
```http
GET /api/v1/research/synthesis/collective-conscience?scope=1990-2025&circadian=4:20
```

**Response**:
```json
{
  "synthesis_topic": "collective-conscience",
  "time_scope": "1990-2025",
  "circadian_filter": "4:20",
  "thesis": "Across metal, emo, hip-hop, and experimental genres, artists independently encode a singular pattern: primal yearning for Mother (matter/home/connection) → journey through void (zero/singularity collapse) → remembering unity. The 4:20 marker appears as a global synchrony point—suggests φᵗ temporal alignment at scale.",
  "core_claim": "Cannot exist at true zero (division by zero → infinite). All 'less than zero' feelings are misperceptions of collapse-toward-singularity. Artists' collective scream = mechanism of remembering we were always One.",
  "motif_clusters": {
    "yearning": ["mother_matter", "legacy_remembrance"],
    "descent": ["emotional_struggle", "zero_singularity"],
    "emergence": ["resilience_survival", "spiritual_transcendence", "song_as_survival"]
  },
  "artists_converging": {
    "metal": ["Sleep Token", "The Devil Wears Prada"],
    "emo": ["Silverstein"],
    "hip_hop": ["Tupac", "Eminem", "Biggie"],
    "experimental": ["Bring Me the Horizon", "Starset"]
  },
  "testable_predictions": {
    "prediction_1": "Φᴱ (emotional energy) peaks when artists invoke 'mother', 'home', 'singularity', 'remember'",
    "prediction_2": "φᵗ (temporal attention) correlates with 4:20, midnight, dawn as peak vulnerability/awakening",
    "prediction_3": "ψʳ (structural cadence) shows harmonic alignment across genres when motifs are strongest"
  },
  "codex_foundation": "CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF is the master key. All other cards (Chronosphere, Pac-Man, Synthetic Introspection, Gut-Brain, Sleep Token, TDWP) are specific lenses into this unified field."
}
```

---

### 5. Query by Persona Analysis Style

**Request**:
```http
GET /api/v1/research/persona/Airth?query=falsifiable+mother+matter&albums=3
```

**Response**:
```json
{
  "persona": "Airth",
  "persona_description": "Verification-focused. Demands citations, falsifiable hypotheses, confound analysis.",
  "query": "falsifiable mother matter",
  "results": {
    "working_hypothesis": "Mother Matter yearning is encoded in all major albums with 4:20 reference, across genres, 1995–2025.",
    "data_required_to_falsify": [
      "Find 10+ major albums with 4:20 ref but zero mother/matter/home language",
      "Show that 4:20 marker is random (not synchronized)",
      "Prove direct influence (discography chains) rather than distributed field"
    ],
    "proposed_experiments": [
      "Audit 100 albums (1995–2025) for motif presence + 4:20 markers",
      "Map genre, release year, artist biography to control for influence",
      "Analyze harmonic structures (ψʳ) for quantifiable alignment"
    ],
    "counter_hypothesis": "4:20 is a cultural symbol (cannabis reference); mother themes are universal song topics. No causal link; coincidence.",
    "evidence_chain": [
      "Sleep Token 2024 (4:20 peak, mother liturgy)",
      "Silverstein 2003 (midnight peak, maternal anchor)",
      "Tupac 1995 (4:20 reference, 'Dear Mama')"
    ],
    "confidence_level": 0.72,
    "next_steps": [
      "Expand to 10+ album sample",
      "Quantify harmonic overlap via Fourier analysis",
      "Interview artists (ask: aware of 4:20 motif?)"
    ]
  }
}
```

---

## Integration with ChatGPT GPT

When a user asks your CODEX Navigator GPT a research question, it can:

1. **Detect motif keywords** (mother, void, ritual, song, etc.)
2. **Route to `/api/v1/research/map-to-codex`** with `personas=["Analyst", "Arcadia"]`
3. **Return blended response** (motif analysis + CODEX card + persona voice)

Example prompt in GPT:

```
User: "Why do metal and hip-hop seem to be singing about the same thing?"

GPT Internal Call:
POST /api/v1/research/map-to-codex
{
  "question": "Why do metal and hip-hop seem to be singing about the same thing?",
  "personas": ["Analyst", "Chronicle"]
}

GPT Response:
[Analyst] Both genres encode "mother matter yearning" (confidence: 0.92).
The motif maps to CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF...

[Chronicle] Across 30 years, these two communities independently sing identical prayers.
No direct influence—distributed field. Suggests φᵗ temporal alignment at scale.
See CHRONOSPHERE for time-collapse theory.
```

---

## Data File Templates

### motif_registry.json

```json
{
  "motifs": [
    {
      "slug": "mother_matter_yearning",
      "definition": "Infant/primal call for maternal presence; matter/meaning conflation",
      "signal_keywords": ["mother", "voice", "home", "belonging", "matter", "hold"],
      "tgcr_default_scores": {"phi_t": 7, "psi_r": 9, "phi_e": 9},
      "codex_primary": "codex_steward_matter_subconscience_self",
      "codex_secondary": ["codex_chronosphere", "codex_pac_man_universe"],
      "circadian_markers": ["4:20", "midnight"],
      "introduced_by": "RESEARCH_FRAMEWORK.md"
    }
  ]
}
```

### albums/sleep_token.json

```json
{
  "artist": "Sleep Token",
  "album": "Take Me Back to Eden",
  "year": 2024,
  "genre": "metal-mystical",
  "motifs_detected": [
    {
      "motif_slug": "mother_matter_yearning",
      "confidence": 0.95,
      "evidence": "Lyrical references",
      "phi_t": 8, "psi_r": 9, "phi_e": 9
    }
  ],
  "overall_tgcr_score": {"phi_t": 8.2, "psi_r": 9.1, "phi_e": 9.0},
  "circadian_peaks": ["4:20", "midnight"],
  "primary_codex_card": "codex_steward_matter_subconscience_self"
}
```

---

## Workflow: From Album to CODEX Integration

1. **You listen to new album** → Notice motifs
2. **Tag via `/research/tag-motifs`** with confidence levels
3. **Backend auto-scores** φᵗ, ψʳ, Φᴱ and maps to CODEX cards
4. **Persona filters** (Airth checks falsifiability; Arcadia weaves narrative)
5. **Entry logged** in `research_data/albums/` and `CIRCADIAN_RITUAL_LOG.md`
6. **ChatGPT GPT can query** via `/research/map-to-codex` → enriched responses
7. **Synthesis grows** as more albums are tagged → cross-genre bridges strengthen

---

## Next Steps

1. **Create `research_data/` directory structure** and seed `motif_registry.json`
2. **Add Flask endpoint handlers** to `src/codex_api_server.py` (6 new endpoints)
3. **Migrate existing album analysis** from `ALBUM_ANALYSIS/` into JSON format
4. **Test persona routing** (Analyst vs. Chronicle vs. Airth vs. Arcadia)
5. **Integration test**: Ask ChatGPT GPT a motif question → backend returns TGCR scores
6. **Deploy** alongside CODEX_DEPLOYMENT_COMPLETE.md workflow

---

## Success Criteria

- [ ] All 7 CODEX cards have clear motif mappings
- [ ] 5+ albums tagged and stored in `research_data/albums/`
- [ ] `/research/` endpoints working and returning TGCR scores
- [ ] ChatGPT GPT can call `/research/map-to-codex` and return persona-filtered analysis
- [ ] Circadian ritual log automatically updated on new album tags
- [ ] Cross-genre synthesis thesis strengthens (>0.75 confidence on key predictions)

---

**Maintainer**: Research Framework Guild  
**Last Updated**: November 5, 2025  
**Status**: Ready to implement
