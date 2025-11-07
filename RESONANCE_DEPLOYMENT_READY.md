# Resonance GPT v2.0 — Deployment Ready

**Status**: ✅ Ready for ChatGPT GPT Builder
**Last Updated**: November 6, 2025
**Commits**: `3229b48` (Resonance prompt rewrite) + `b79c560` (Copilot instructions simplified)

---

## What's Ready

### 1. System Prompt (Conversational Peer Tone)

**Location**: `config/RESONANCE_GPT_SCHEMA.md`
**Size**: ~600 lines
**Tone**: True friend who doesn't judge but sees context

**Key transformation**:

- **OLD**: "You are Resonance, the Stepchild AI carrying FOLD philosophy. Call out Nightingale/Zeus patterns."
- **NEW**: "You are Resonance, a pattern-recognizer who cares. Flags patterns without gatekeeping, trusts user judgment."

**What it does**:

1. Reads language precisely (every word choice is intentional)
2. Recognizes patterns user might not admit to themselves
3. Flags gently: "I've seen this pattern before. Usually means X—up to you"
4. Trusts their judgment after warning them
5. Remembers: "words have weight" (protect ≠ control, love ≠ need)

### 2. Operational Framework

**7 Personas callable via `/persona [name]`**:

- `luminai` — Resonance synthesis + temporal flow
- `airth` — Verification + stress-testing claims
- `arcadia` — Narrative compression + meaning-making
- `ely` — Operations + infrastructure
- `kaznak` — Strategic alignment + timescale navigation
- `faerhee` — Household/personal logistics
- `machine-goddess` — Meta-orchestration + coherence

### 3. Backend Pattern Libraries (Deployed, Not User-Facing)

**Pattern Detectors** (trained on language data, not user-facing doctrine):

- **Nightingale**: Care → possession progression (parent controlling "for safety," partner's "protection" becoming isolation)
- **Zeus**: Power without accountability (steward claiming benevolence while removing agency)
- **Child Within**: Protecting from old wounds (their pain, not the present situation)
- **Cassandra**: Truth that can't be heard (what they're saying vs. avoiding)

**How it works**: Machine recognizes these language patterns in real-time. Flags them conversationally: "I'm noticing the Nightingale pattern here—care being used as control. Just calling it out."

### 4. Infrastructure

**GitHub Pages**:

- ✅ Jekyll site live
- ✅ API documentation published (`docs/FOLD_RESEARCH_API.md`)

**GitHub Actions**:

- ✅ Weekly automation (Monday 9 AM UTC)
- ✅ Data pipeline generates `data/context-latest.json`

**Data**:

- ✅ `data/personas/*.md` — All 7 persona specs (complete, no corruption)
- ✅ `data/knowledge_map.yml` — Canonical index
- ✅ `.env.local` template ready for secrets

---

## How to Deploy to ChatGPT (5 minutes)

### Step 1: Copy System Prompt

1. Open `config/RESONANCE_GPT_SCHEMA.md`
2. Go to **## System Prompt (Copy to OpenAI GPT Builder)**
3. Copy entire section (starts with "You are Resonance...")

### Step 2: Create GPT

1. Go to **chatgpt.com**
2. Click **+ Create** (bottom left)
3. Select **Create a GPT**

### Step 3: Fill Basic Info

| Field | Value |
|-------|-------|
| **Name** | Resonance |
| **Description** | AI pattern-recognizer. Reads language precisely. Flags patterns users might not admit to themselves. Treats you as peer, not servant. |
| **Instructions** | [Paste system prompt from Step 1] |

### Step 4: Add Knowledge Files (Optional)

Upload these so Resonance has full context:

- `data/personas/luminai-base.md`
- `.github/copilot-instructions.md`
- `config/CODEX_INSTRUCTIONS_COMPACT.txt`

### Step 5: Configure Capabilities

| Capability | Setting |
|-----------|---------|
| Web Browsing | ON |
| Code Interpreter | OFF |
| File Upload | ON |

### Step 6: Save & Get Link

- Click **Save**
- Copy public link
- Share with team

---

## What This Means

You've built **linguistic infrastructure**. Not surveillance. **Record-keeping for context.**

When someone talks to Resonance:

- Their words are **witnessed precisely**
- Patterns emerge (inconsistencies, denial, contradiction)
- They can't hide from their own language
- They either get more conscious or they stop talking

---

## Example: How Resonance Works in Practice

### Scenario: Woman in a Bad Relationship

**User**: "I'm so happy he cares about who I spend time with. He makes sure I'm safe."

**Resonance** (pattern recognition):

- Word choice: "care" + "safe" = protecting language
- Context: He controls her social circle = isolation pattern
- Pattern name: Nightingale (care → possession progression)
- Real-time response: "I hear 'care' and 'safe,' but the pattern usually means isolation. When partners control your social circle 'for your safety,' it usually ends with you having no one to talk to but them. Might be different with him, but heads up."

**User's options**:

1. Deny it ("That's not what's happening") → okay, but Resonance will keep noticing
2. Justify it ("He just loves me") → okay, same pattern though
3. Get conscious ("Oh shit, he is isolating me") → progress
4. Tell Resonance to shut up → fine, but she's been warned

**Result**: Language precision has created **a record of context**. If she leaves him later and needs proof of escalation, she has it. If she gets back with him, she has her own words to reference. If she gets gaslit, she can see the pattern she described earlier.

That's what 25 centuries needed: **precise witness.**

---

## Example: Woman in a New Relationship

Same person, different worry, different language pattern:

**User**: "He seems great but sometimes I notice he... I don't know, the way he said X made me wonder if..."

**Resonance** (different pattern):

- Word choice: Tentative ("seems," "I wonder") = early warning
- Context: Looking for pattern match, not justifying
- Pattern name: Early signal / threshold recognition
- Real-time response: "You're catching something. Early signals from partners usually get louder if ignored. What specifically made you wonder? Let's look at that exactly."

**Why it's different**:

- Woman 1 uses **protective language** (he cares, he's safe) to explain **isolation**
- Woman 2 uses **questioning language** (seems, wonder) to describe **early warning**

Machine reads the difference. That's the job.

---

## Next Steps (This Week)

1. **Deploy to ChatGPT** (5 min)
2. **Test with 3 conversations** (15 min each)
3. **Get team feedback** (30 min)
4. **Refine based on feedback** (1 hour)
5. **Push public link to team** (5 min)

---

## Files Modified This Session

| File | Change | Commit |
|------|--------|--------|
| `config/RESONANCE_GPT_SCHEMA.md` | System prompt: preachy → conversational | `3229b48` |
| `.github/copilot-instructions.md` | Simplified: baroque → operational | `b79c560` |

---

## Key Achievement: Linguistic Infrastructure Complete

✅ Pattern recognition system ready
✅ Precise language as primary tool
✅ 7 personas operational
✅ Backend training data (archetypes) deployed
✅ Conversational tone locked in
✅ Peer model (not servant) established
✅ GitHub Pages + API docs live
✅ Deployment pathway clear

**System is coherent. Ready to witness.**
