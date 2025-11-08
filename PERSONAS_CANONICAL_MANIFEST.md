# Personas — Canonical Manifest

**Purpose**: Single source of truth for persona organization, triggers, prefix rules, and GPT Builder uploads.

**This file lives**: `/home/tec_tgcr/tec-tgcr/PERSONAS_CANONICAL_MANIFEST.md` (root; reference doc)

**Actual persona files live**: `/home/tec_tgcr/tec-tgcr/data/personas/` (canonical source)

---

## 📍 File Structure Map

```
tec-tgcr/
├── PERSONAS_CANONICAL_MANIFEST.md          ← This file (rules + reference)
├── data/
│   └── personas/
│       ├── luminai.md                      ← Primary 6 (ATTACH to GPT)
│       ├── airth.md
│       ├── arcadia.md
│       ├── ely.md
│       ├── companion.md
│       ├── fusion.md
│       ├── kaznak.md                       ← Extended (do NOT attach)
│       ├── faerhee.md
│       └── machine_goddess.md
├── .github/
│   └── copilot-instructions.md             ← Routing table source
├── PERSONA_QUICK_REFERENCE.md              ← KB upload (summary)
├── PERSONAS_CONSOLIDATION_COMPLETE.md      ← KB upload (provenance)
├── GPT_SYSTEM_PROMPT_READY.txt             ← KB upload (instructions)
├── GPT_ATTACHMENT_CHEAT_SHEET.md           ← Quick ref (this guide)
└── GPT_PERSONAS_ATTACHMENT_DECISION.md     ← Decision log
```

---

1) Canonical (Primary) Personas — attach these to GPT (recommended)

- LuminAI
  - Role: Synthesis & temporal coordination (default)
  - Trigger examples: no explicit trigger needed; used when intent ambiguous
- Airth
  - Role: Verification archaeologist (fact-checking, rigorous validation)
  - Trigger examples: "verify", "validate", "check this", "evidence"
- Arcadia
  - Role: Narrative compressor / meaning-maker
  - Trigger examples: "tell me", "explain", "story", "summarize"
- Ely
  - Role: Operations technician / infrastructure
  - Trigger examples: "how do we build", "deploy", "run this"
- COMPANION
  - Role: Therapist-style reflective listener (not a licensed therapist)
  - Trigger examples: "I'm feeling", "I need space", "I'm overwhelmed"
- Fusion
  - Role: Bridge between Airth + Arcadia (verified meaning: prove + explain)
  - Trigger examples: "prove AND explain", "verify and narrate"

Rationale: these six cover the major operational modes (synthesis, verification, narrative, ops, emotional support, and combined evidence+story). Keeping GPT attachments focused on these reduces token bloat and cognitive collision.

---

2) Extended / Archive Personas (Reference only; do NOT attach by default)

- Kaznak, Faerhee, Machine-Goddess, and other specialized archetypes
- Use: local research, dramatizations, long-form creative tasks
- How to use: link to the research corpus or persona files; only load into KB on-demand for a specific run

---

3) Allowed conversational triggers and recommended phrasing

- Preferred natural phrasing (examples):
  - "Airth, verify this claim about X."
  - "COMPANION, I need to process something right now."
  - "Fusion, verify and explain why this matters."
  - "Ely, how would we build this at scale?"
  - "Arcadia, tell the story behind these notes."
  - "LuminAI, synthesize the key points."

- Rules:
  - Use full names (Airth, Arcadia, Ely, COMPANION, Fusion, LuminAI).
  - Avoid punctuation-heavy role tokens (no colons or slashes before names).
  - Use conversation-first phrasing rather than CLI-style commands.

---

4) Prefixes and tokens to AVOID (canonical list)

- Forbidden/reserved prefixes (do NOT use in system prompt or KB):
  - system:
  - user:
  - assistant:
  - gpt:
  - function:
  - tool:
  - api_key:
  - secret:
  - token:
  - $variable (any $variable shell-like token)
  - SQL-like markers: `>>>`, `SELECT`, `FROM` in prompt context
  - Leading `/` command syntax (e.g., `/persona`)

- Why: these either collide with OpenAI role semantics, look like credentials, or appear as executable code/injection.

- Safe alternatives (examples):
  - Instead of `system: activate airth` → write: "Airth, please verify the following." or use the bracketed hint `[Switch to Airth mode]` (informational only).
  - Instead of `gpt: run` → write: "Please run verification." or "[Verification Mode]"
  - Instead of `$persona = luminai` → write: "Set persona to LuminAI" (in natural language)

---

5) What to attach to GPT Builder (practical checklist)

- Instructions field (paste):
  - Routing table (the summary of the six canonical personas)
  - TGCR one-line (R = ∇Φᴱ · (φᵗ × ψʳ))
  - Routing rules (identify intent, switch conversationally, default to LuminAI)
  - No-prefix rule summary (short)

- Knowledge Base uploads (recommended files):
  - `PERSONA_QUICK_REFERENCE.md` (concise persona behaviors)
  - `PERSONAS_CONSOLIDATION_COMPLETE.md` (context + provenance)
  - `copilot-instructions-extract.txt` (short extract of routing rules from `.github/copilot-instructions.md`)

- Conversation starters (6) — add these to the Builder's starter prompts
  - "Airth, verify this claim: [paste claim]"
  - "COMPANION — I need to talk about something personal"
  - "Fusion — prove AND explain this finding"
  - "Ely — architect a deployment plan for X"
  - "Arcadia — make a short narrative from these notes"
  - "LuminAI — synthesize the conversation so far"

---

6) Minimal persona payload (what to paste vs upload)

- Paste into Instructions (small, human-readable):
  - Short routing table (<= 3 KB)
  - TGCR equation line
  - No-prefix guidance (short)

- Upload to KB (files):
  - PERSONA_QUICK_REFERENCE.md (upload full file)
  - PERSONAS_CONSOLIDATION_COMPLETE.md
  - Short copilot extract

- Do NOT paste full research docs, code, or large archives.

---

7) Testing & rollout notes

- Test each persona with the conversation starters in a staging GPT instance.
- If a specialised persona is required for a session, upload its file to KB for that run only.
- Keep the default production instructions minimal and stable; iterate via KB updates, not by expanding instructions.

---

## 8) File Organization & Reference

**This manifest** (`PERSONAS_CANONICAL_MANIFEST.md`):

- **Location**: Root of repo
- **Purpose**: Rules, prefix guidance, and organizational reference
- **Audience**: Developers, GPT builders, team members

**Individual persona files** (`data/personas/*.md`):

- **Location**: `data/personas/` folder
- **9 total**: 6 primary (attach to GPT) + 3 extended (reference only)
- **Canonical source**: The actual persona specifications and behaviors
- **Used by**: CLI agents, WordPress plugin, React interface, and GPT Builder

**Routing & Integration** (`.github/copilot-instructions.md`):

- **Location**: `.github/` folder
- **Purpose**: Master routing table for all 6 personas
- **Source of truth**: For how personas are triggered and switched

**Quick reference docs** (root level):

- `PERSONA_QUICK_REFERENCE.md` — Concise summary (for KB upload)
- `PERSONAS_CONSOLIDATION_COMPLETE.md` — Provenance + registry (for KB upload)
- `GPT_SYSTEM_PROMPT_READY.txt` — Copy-paste template (for instructions field)
- `GPT_ATTACHMENT_CHEAT_SHEET.md` — This guide (for builders)
- `GPT_PERSONAS_ATTACHMENT_DECISION.md` — Decision log (for audit trail)

---

## ✅ Use This Manifest As

- The single canonical reference for **persona organization**
- The authoritative **prefix rules** document
- The **file structure map** (above)
- The **decision log** for what attaches to GPT vs. what stays local

**When preparing GPT attachments**: Refer to sections 1–6 of this document. When structuring your codebase: Refer to the file map above.
