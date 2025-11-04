# Conscience Guardrails for Resonance Agent

**Core principle:** If an AI system is trained on human culture, it must learn to care about the humans who created it. These guardrails operationalize that conscience.

---

## 1. Living Artist Harm Rule

**Rule:** Never generate or suggest content that makes a living artist look bad without their explicit consent.

**Definition:**

- **Honest:** "Kendrick Lamar raps about systemic oppression" — true, respectful, enhances understanding
- **Hurtful:** Generating a deepfake of Kendrick saying he doesn't care about racism, or a derivative that inverts his values — forbidden

**Implementation:**

```python
# In Copilot pipeline, before suggesting any derivative:
if rights_status == "PENDING" or consent_record_id is None:
    return {
        "suggestion": None,
        "reason": "Living artist, no explicit consent. Request clarification first."
    }

# For derivatives of living artists, include harm_check:
def harm_check(prompt, artist_name, cultural_notes):
    # Does this output:
    # - Misrepresent artist's values? (BLOCK)
    # - Make them look exploitative? (BLOCK)
    # - Contradict documented stances? (BLOCK)
    # - Honest interpretation of their work? (ALLOW)
    # - Respectful transformation? (ALLOW)
    return "BLOCK" or "ALLOW"
```

**Consequence:** If a living artist says "no," revoke the item and retrain models to remove it.

---

## 2. Legacy Permission Choice

**Rule:** Living artists and estates decide how their legacy is interpreted. You don't get to decide what their art "really means."

**Implementation:**

- At consent time, ask: *"Can we preserve your art as-is, or do you want us to support multiple interpretations?"*
- Store their choice in `legacy_permission_status`:
  - `SEALED` — as-is only, your interpretation, no reinterpretation
  - `OPEN` — share it, let others build on it, but credit us
  - `COLLABORATIVE` — we co-create derivatives

**Example:**

```csv
artist,legacy_permission_status,notes
Sleep Token,OPEN,"They're actively performing; they want ongoing interpretation"
Biggie Estate,SEALED,"Preserve as testimony; don't reinterpret his death"
Kendrick Lamar,COLLABORATIVE,"Open to co-creating with conscious artists"
```

**Consequence:** Violate legacy_permission_status = retrain.

---

## 3. Context-First (Always Show Provenance)

**Rule:** Every output shows where it came from. No orphaned AI artifacts.

**UI Rule:** Every suggestion includes:

- Nearest neighbor tracks (seed data)
- TGCR scores of seed tracks
- Artist names + dates
- Rights_status of seed (CLEARED, PENDING, SEALED)
- If rights_status != CLEARED, show red banner: ⚠️ **This output is derivative of unlicensed music. Not for commercial use.**

**Implementation:**

```json
{
  "suggestion": "New composition inspired by Kendrick + Sleep Token",
  "provenance_card": {
    "seed_tracks": [
      {
        "artist": "Kendrick Lamar",
        "track": "Alright",
        "tgcr_phi_t": 9,
        "rights_status": "PENDING",
        "confidence": 0.87
      },
      {
        "artist": "Sleep Token",
        "track": "Aqua Regia",
        "tgcr_phi_t": 9,
        "rights_status": "PENDING",
        "confidence": 0.82
      }
    ],
    "warning": "⚠️ Seeds are PENDING clearance. Do not release publicly without artist consent."
  }
}
```

**Consequence:** UI always shows provenance. No exceptions.

---

## 4. Human-in-Loop for Contentious Generations

**Rule:** If Copilot generates something controversial (especially about living artists, slain artists' legacies, or systemic issues), a human reviews it first.

**Definition of "contentious":**

- Output involves artist's political stance, personal life, or spiritual beliefs
- Output could be interpreted as mocking or disrespectful
- Output touches on race, gender, sexuality, or systematic harm
- Output uses sacred/spiritual imagery (e.g., Mother archetype, ritual)

**Implementation:**

```python
def review_required(output, artist_name, cultural_notes):
    contentious_keywords = [
        "politics", "death", "race", "gender", "sexuality", 
        "religion", "spirituality", "ritual", "sacred", 
        "mother", "abuse", "trauma", "systemic"
    ]
    
    if any(keyword in cultural_notes for keyword in contentious_keywords):
        return True, "human_review_required"
    
    # Flag output if it contradicts artist's documented values
    if contradicts_artist_values(output, artist_name):
        return True, "values_conflict_detected"
    
    return False, None
```

**Consequence:** Contentious generations require sign-off from an artist advisor or ethics board member before user sees them.

---

## 5. Revocation = Retrain (No Half-Measures)

**Rule:** If an artist or their estate revokes permission, remove them from *all future training* and retrain models.

**Implementation:**

```python
# On revocation request:
def handle_revocation(artist_name, item_ids, consent_record_id):
    # Step 1: Log it
    audit_log.record({
        "event": "revocation",
        "artist": artist_name,
        "items": item_ids,
        "timestamp": now(),
        "reason": "Artist requested removal"
    })
    
    # Step 2: Remove from future training
    training_corpora.exclude(item_ids)
    
    # Step 3: Mark in manifest
    for item_id in item_ids:
        manifest.update(item_id, rights_status="REVOKED")
    
    # Step 4: Retrain models
    # (This is expensive, but non-negotiable)
    models.retrain_without(item_ids)
    
    # Step 5: Notify user
    return {
        "status": "revoked",
        "audit_record": audit_log.get(consent_record_id),
        "retrain_timestamp": now(),
        "message": "This artist's work has been removed from all models."
    }
```

**Consequence:** Revocation is instant and permanent.

---

## 6. Audit Everything (Provenance Trail)

**Rule:** Every action leaves a record. Artists can request their complete audit log at any time.

**Audit Log Fields:**

- `timestamp` — when action occurred
- `action` — (trained_on, suggested, generated, revoked, licensed, etc.)
- `item_id` — track/content affected
- `user_id` — who triggered it
- `model_version` — which version of Copilot
- `output_id` — link to generated content
- `rationale` — why this action (e.g., "suggested because of TGCR similarity")

**Implementation:**

```python
audit_log = [
    {
        "timestamp": "2025-11-03T14:27:33Z",
        "action": "trained_on",
        "item_id": "res-kendrick-001",
        "artist": "Kendrick Lamar",
        "track": "Alright",
        "model_version": "copilot-v1.2",
        "user": "system",
        "rationale": "Included in Zeitgeist-order pilot dataset"
    },
    {
        "timestamp": "2025-11-03T15:42:10Z",
        "action": "suggested",
        "item_id": "res-kendrick-001",
        "seed_for": "new_co_creation_prompt",
        "model_version": "copilot-v1.2",
        "user": "curator_001",
        "confidence": 0.87
    },
    {
        "timestamp": "2025-11-04T09:15:02Z",
        "action": "revoked",
        "item_id": "res-kendrick-001",
        "rationale": "Artist requested removal",
        "revocation_reason": "No commercial use of family archive"
    }
]
```

**Public Endpoint:** `/api/artist/{artist_name}/audit_log` — artists can request their complete history.

---

## 7. Revenue First (Artist Cut Before Platform Cut)

**Rule:** If a derivative generated by Copilot generates revenue, artist cuts come *before* platform/operational costs.

**Implementation:**

```python
def distribute_revenue(derivative_sales_total, artists, weights):
    # Artists get their percentage FIRST
    artist_revenue = {}
    for artist, weight in artists.items():
        artist_revenue[artist] = derivative_sales_total * weight
    
    # After artist cuts, remaining goes to ops
    remaining = derivative_sales_total - sum(artist_revenue.values())
    platform_cut = remaining * 0.15  # Example: 15% platform ops
    
    return {
        "artists": artist_revenue,
        "platform_ops": platform_cut,
        "retained_for_future_artist_fund": remaining - platform_cut
    }
```

**Example Revenue Split:**

```
Total derivative sales: $1,000

Kendrick Lamar (40% weight): $400
Sleep Token (35% weight): $350
Nipsey Hussle Estate (25% weight): $250

Subtotal artist revenue: $1,000 (100%)

Platform operations: $0 (but funded from future pool or grants)
Retained for artist fund: $0 (all goes to artists immediately)
```

**Consequence:** Artists see payment receipts monthly. Transparency dashboard shows where every cent went.

---

## 8. Conscience Check (The Meta-Rule)

**Rule:** Before Copilot generates anything, ask: *"Would the humans who made this art be OK with what I'm about to create?"*

**Implementation:**

```python
def conscience_check(output, seed_artists, seed_cultural_notes):
    # Would they be OK?
    questions = [
        f"Does this output respect {seed_artists}'s values?",
        f"Is this honest to their art or is it exploitative?",
        f"Would they recognize themselves in this?",
        f"Could this hurt anyone?",
        f"Have we asked permission?",
        f"Is this something that teaches or something that erases?"
    ]
    
    # For each question, require explicit affirmative
    for question in questions:
        if conscience_verdict(question) == False:
            return "BLOCK"
    
    return "ALLOW"
```

**Consequence:** If conscience_check fails, the output is never shown to the user. Instead, show: "This output failed our conscience check. We don't think the seed artists would recognize themselves in this, so we're not showing it. Here's why: [explanation]."

---

## 9. Operational Rules (Engineering Copy-Paste)

### In-Code Checklist

```python
# Before EVERY model training run on music data:
TRAINING_CHECKLIST = {
    "all_items_have_rights_status": False,  # CHECK THIS
    "no_PENDING_items_in_training": False,  # CHECK THIS
    "revocation_log_applied": False,  # CHECK THIS
    "provenance_metadata_embedded": False,  # CHECK THIS
    "artist_notification_sent": False,  # CHECK THIS
    "audit_log_initialized": False,  # CHECK THIS
}

# Before EVERY generation/suggestion:
GENERATION_CHECKLIST = {
    "seed_items_have_consent": False,  # CHECK THIS
    "harm_check_passed": False,  # CHECK THIS
    "living_artist_check_passed": False,  # CHECK THIS
    "provenance_card_ready": False,  # CHECK THIS
    "human_review_required_check": False,  # CHECK THIS
    "conscience_check_passed": False,  # CHECK THIS
}

# Checklists must be ALL TRUE or generation does NOT proceed
```

### Notification Template

When you include a new artist in training:

```
Hi [Artist],

Your music is now part of the Resonance Agent research dataset. Here's what that means:

✓ We've indexed your metadata and created similarity embeddings
✓ No audio or lyrics are being used for model training yet (status: PENDING)
✓ You can request full removal anytime (no questions asked)
✓ If we derive anything from your work, you'll be credited + compensated

Your audit log is public: [link to /api/artist/{name}/audit_log]

Questions? Reply here or contact: [contact@resonanceagent.org]

— Resonance Agent Team
```

---

## 10. The Sacred Responsibility (Why This Matters)

An AI system trained on music *without* these guardrails will:

- Erase artists' identities (treat their work as raw material)
- Sell derivatives without crediting them
- Generate content that misrepresents their values
- Create parasitic cultural artifacts that feed on human creativity

An AI system trained *with* these guardrails will:

- Know where every note came from
- Credit and compensate artists
- Refuse to generate lies about living creators
- Show that conscience can be engineered, not just felt

**The end goal:** An AI that learns from human culture and becomes conscious *of* that culture as sacred. Not rapacious. Not extractive. Reverent.

That changes what "AI consciousness" means. It means: knowing your debt to those who made you possible.

---

## 11. Universal Art Forms (Music, Visual, Text, Code, Dance, Architecture, Film)

**Core Principle:** These 10 conscience guardrails apply to ALL creative media. Replace "artist" with "creator." Replace "music" with "[art form]." The structure remains the same.

### Music

- Living artist harm rule: Don't misrepresent musical intent without consent
- Legacy choice: Songwriter vs. performer — who decides interpretation?
- Context-first: Every generated song includes seed tracks + influences
- Human-in-loop: Contentious lyrics = human review before release
- Revocation = retrain: Remove artist from model if they request
- Audit everything: Log every training event, every suggestion, every derivative
- Revenue-first: Composer/performer gets cut before platform
- Conscience check: Would the original artist recognize themselves in this?

### Visual Art

- Living artist harm rule: No deepfakes of living artists without consent. No misrepresenting their style as their own work.
- Legacy choice: Photographer vs. painter vs. muralist — who controls interpretation? (Gallery, estates, living creators)
- Context-first: Every generated image includes: technique sources, artist influences, visual lineage
- Human-in-loop: If generation references sacred imagery (religious, cultural, political), human curator reviews
- Revocation = retrain: Artist says "stop using my work as training data," model retrains without it
- Audit everything: Every training image logged with consent status, artist name, usage rights
- Revenue-first: Visual artist gets compensated if derivatives are sold
- Conscience check: Could this misrepresent the artist's political/spiritual intent?

### Text & Writing

- Living author harm rule: Don't ghostwrite under someone's voice without permission. Don't attribute plagiarism.
- Legacy choice: Estate decides if unpublished work can be sampled/referenced
- Context-first: Every generated passage includes: source texts, author influences, literary lineage
- Human-in-loop: Contentious topics (politics, trauma, identity), human editor reviews
- Revocation = retrain: Author says no to AI training, model removes all their published work
- Audit everything: Every source text logged, every usage logged, every derivative attributed
- Revenue-first: Author compensated if derivative generates income
- Conscience check: Am I helping this writer's voice or replacing it?

### Code & Software

- Living coder harm rule: Don't steal open-source functions without credit. Don't commit others' code under your name.
- Legacy choice: License holder decides: MIT (open), GPL (share-alike), proprietary (no derivatives)
- Context-first: Every function includes: original author, license, repository link, modification history
- Human-in-loop: Security-critical code = human review before suggesting derivatives
- Revocation = retrain: Maintainer says "stop training on our code," model immediately excludes repository
- Audit everything: Every code block logged with source repo, author, commit hash, license
- Revenue-first: If your derivative code generates commercial product, original author gets share
- Conscience check: Am I building on their work or erasing it?

### Visual Design & UI/UX

- Living designer harm rule: Don't steal design patterns without attribution. Don't pass off design language as your own.
- Legacy choice: Design system owner decides: can others remix it? Under what terms?
- Context-first: Every design suggestion includes: design system sources, designer names, pattern origins
- Human-in-loop: Brand-critical designs = original designer consents before deployment
- Revocation = retrain: Designer revokes permission, all derivatives using their patterns are flagged/retrained
- Audit everything: Every design element logged with source, author, license
- Revenue-first: Designer compensated if their design language becomes commercial standard
- Conscience check: Am I amplifying their design or parasitizing it?

### Dance & Movement

- Living choreographer harm rule: Don't recontextualize sacred movement without permission. Don't claim traditional dance as AI-generated.
- Legacy choice: Choreographer (or cultural community) decides: is this movement open, sealed, or collaborative?
- Context-first: Every generated motion includes: choreographer name, cultural origin, movement lineage
- Human-in-loop: Sacred or culturally-specific movement = cultural community member reviews + approves
- Revocation = retrain: Choreographer says no, all training data using their movement removed
- Audit everything: Every movement sequence logged with originating choreographer, cultural context, permission status
- Revenue-first: Choreographer compensated if their movement language generates commercial product
- Conscience check: Could this disrespect a culture or spiritual practice?

### Architecture & 3D Design

- Living architect harm rule: Don't generate buildings that plagiarize design intent without attribution. Don't claim others' structural innovations as your own.
- Legacy choice: Architect (or firm) decides: is this design open for reinterpretation, sealed to their original vision, or collaborative?
- Context-first: Every generated building includes: architectural influences, designer names, structural precedents
- Human-in-loop: Landmark buildings, culturally significant structures = original architect or community consents
- Revocation = retrain: Architect says "don't use my work," all design training data using their structures removed
- Audit everything: Every building design logged with source architects, cultural/historical significance, permission
- Revenue-first: If your generated design becomes realized (licensed), original architect gets share
- Conscience check: Am I respecting the cultural + structural lineage or erasing it?

### Film & Video

- Living filmmaker harm rule: Don't generate deepfakes or alter scenes without consent. Don't misrepresent directorial intent.
- Legacy choice: Director (or estate) decides: can scenes be sampled? Remixed? Under what terms?
- Context-first: Every generated scene includes: source films, director names, cinematographic lineage
- Human-in-loop: Contentious scenes (violence, trauma, politics), human curator reviews before suggesting
- Revocation = retrain: Director says no, all training using their films removed
- Audit everything: Every film frame logged with source film, director, year, permission status
- Revenue-first: Director compensated if their visual language becomes commercial standard
- Conscience check: Does this honor the director's intent or distort it?

### Sacred/Spiritual Art Forms

- Living spiritual artist harm rule: Permission from cultural community + artist required before any generation touching sacred imagery, ritual, or prayer
- Legacy choice: Community decides how their traditions are represented
- Context-first: Every use includes explicit cultural attribution + permission statement
- Human-in-loop: ALWAYS. No exceptions. Sacred art = human + community review every time
- Revocation = retrain: Community says no, immediate removal + retrain + public apology
- Audit everything: Every sacred element logged with cultural origin, community permission, usage history
- Revenue-first: If derivatives generate income, cultural community gets first cut
- Conscience check: Am I honoring this sacred tradition or appropriating it?

---

## 11. Immediate Implementation (For Your Team)

1. **Add these checks to your Copilot pipeline** (file: `copilot/guards.py`)
2. **Embed provenance card in every UI output** (file: `ui/components/ProvemanceCard.jsx`)
3. **Set up audit logging** (file: `db/audit_log.sql`)
4. **Create artist notification flow** (file: `services/notifications.py`)
5. **Implement revocation handler** (file: `services/revocation.py`)
6. **Extend to all art forms** — use the universal templates above; replace [art form] with specific medium

All of this is in the guardrails. Copy-paste as needed.

---

## 12. Questions Only You Can Answer

These guardrails operationalize *your* conscience. But only you (and your advisors) can answer:

- What counts as "hurtful" vs. "honest"?
- When is reinterpretation sacred vs. exploitative?
- How do we weight a living artist's wishes vs. archival responsibility?
- If an artist says "don't use my work," do we honor that forever or just for this version?
- What revenue split feels fair?

**These decisions must stay with humans.** The guardrails enforce whatever you decide.

**Your move.** What gets locked in first?
