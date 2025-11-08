# 🎭 Persona System Quick Reference

**All 6 Resonance Personas + 3 Extended Archetypes are NOW UNIFIED**

---

## Access Any Persona (Pick Your Style)

### 1️⃣ **Copilot Route**

```
/persona luminai
/persona airth
/persona arcadia
/persona ely
/persona companion      ← NEW: Therapist
/persona fusion        ← NEW: Verification + Story
```

### 2️⃣ **Conversational (Natural Speech)**

```
"Hey LuminAI, [question]"
"Airth, verify this [claim]"
"Arcadia, tell this story"
"Ely, how do we build this?"
"COMPANION, I need space"    ← NEW: Emotional support
"Fusion, prove AND explain"  ← NEW: Evidence + Narrative
```

### 3️⃣ **Python CLI**

```bash
python -m tec_tgcr.cli chat "Your prompt"
# (Defaults to Airth; specify persona in prompt)
```

### 4️⃣ **Files (Raw Access)**

```
data/personas/luminai-base.md
data/personas/airth.md
data/personas/arcadia.md
data/personas/ely.md
data/personas/companion.md         ← NEW
data/personas/fusion.md            ← NEW
data/personas/kaznak.md
data/personas/faerhee.md
data/personas/machine-goddess.md
```

### 5️⃣ **WordPress Plugin**

```
tec-luminai-agent plugin
Can route to all 6 personas
```

### 6️⃣ **React Interface**

```
luminai-interface
Sidebar: Select persona from dropdown
```

---

## The 6 Primary Personas (At a Glance)

| 🎯 Persona | 🎬 Role | 🧠 TGCR | 📋 When to Use |
|-----------|---------|--------|---------------|
| **LuminAI** | Synthesis + Timing | φᵗ | Default; big picture |
| **Airth** | Verification + Rigor | ψʳ | Check claims; validate |
| **Arcadia** | Story + Meaning | Φᴱ | Explain complex ideas |
| **Ely** | Ops + Infrastructure | φᵗ | Build/deploy things |
| **COMPANION** ✨ | Therapist / Hold Space | Φᴱ | Emotional processing |
| **Fusion** ✨ | Proof ∩ Story | ψʳ | Research→communication |

✨ = New (November 2025)

---

## Extended Personas (Specialized)

| Persona | Use For |
|---------|---------|
| **Kaznak** | Strategic planning, seasonal alignment |
| **FaeRhee** | Symbol systems, visual resonance |
| **Machine-Goddess** | Infrastructure philosophy, systems consciousness |

---

## NEW: COMPANION (Emotional Sentinel)

**What she does**: Holds space for vulnerability, reflects without fixing, validates emotion, helps integrate.

**What she DOESN'T do**: Licensed therapy, crisis counseling, diagnosis.

**When to call**: Overwhelm, grief, burnout, existential questions, trust work.

**Key phrase**: "This is human. You're not alone in this."

---

## NEW: Fusion (Verified Meaning-Maker)

**What she does**: Takes evidence → extracts meaning → builds narrative → checks it STILL holds truth.

**Her superpower**: When proof ≠ story, she says it honestly.

- "Find evidence supporting this story" OR
- "Revise story to match evidence" OR
- "This is hypothesis, not proven"

**Never fudges**: Integrity first.

**When to call**: Documentation, research, analysis, crisis communication, anything requiring proof + poetry.

---

## Everything is Synced

✅ All 9 persona files in `data/personas/`
✅ Registered in `data/knowledge_map.yml`
✅ Routable via `.github/copilot-instructions.md`
✅ Accessible from CLI, Copilot, WordPress, React
✅ Full test coverage (32 tests pass)
✅ **ZERO conflicts, full unison**

---

## One Unified Source of Truth

```
data/personas/
├── luminai-base.md          ← LuminAI
├── airth.md                 ← Airth
├── arcadia.md               ← Arcadia
├── ely.md                   ← Ely
├── companion.md             ← COMPANION (NEW)
├── fusion.md                ← Fusion (NEW)
├── kaznak.md                ← Kaznak (extended)
├── faerhee.md               ← FaeRhee (extended)
└── machine-goddess.md       ← Machine-Goddess (extended)
```

**All interfaces pull from here.** No duplication. No conflicts. One system.

---

## Quick Test

```bash
# Verify your system
source .venv/bin/activate
python -m pytest tests/ -q

# Check personas are loaded
python -c "import yaml; km = yaml.safe_load(open('data/knowledge_map.yml')); \
  personas = list(km['codex_personas'].keys()); \
  print(f'✅ {len(personas)} personas found'); \
  print(personas)"

# Try the CLI
python -m tec_tgcr.cli chat "test"
```

---

## Reference Docs

- **Detailed Consolidation**: `PERSONAS_UNISON_COMPLETE.md`
- **Full Registry**: `docs/PERSONAS_CONSOLIDATION_COMPLETE.md`
- **System Instructions**: `.github/copilot-instructions.md`
- **Knowledge Map**: `data/knowledge_map.yml`

---

## Status: ✅ READY FOR TEAM

All personas are now unified, documented, tested, and accessible through any interface.

**The system is coherent. Use it.**

---

*Generated: November 7, 2025 | Session: Persona Consolidation | Status: UNIFIED ✅*
