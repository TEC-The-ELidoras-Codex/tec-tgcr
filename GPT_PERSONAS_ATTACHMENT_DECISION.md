# GPT Personas Attachment Decision

**Date**: November 7, 2025
**Status**: FINAL

---

## Summary

**Which personas to attach**: Primary 6 only (LuminAI, Airth, Arcadia, Ely, COMPANION, Fusion)
**Why**: Covers all major operational modes; avoids token waste; no cognitive collision.

---

## The Primary 6 (ATTACH to GPT)

| Persona | Files to Upload | Size | Use Case |
|---------|-----------------|------|----------|
| LuminAI (default) | system prompt only | ~0.5 KB | Synthesis, routing, default |
| Airth | PERSONA_QUICK_REFERENCE.md excerpt | ~0.3 KB | Verification, fact-checking |
| Arcadia | PERSONA_QUICK_REFERENCE.md excerpt | ~0.3 KB | Narrative, compression, storytelling |
| Ely | PERSONA_QUICK_REFERENCE.md excerpt | ~0.3 KB | Operations, infrastructure, deployment |
| COMPANION | PERSONA_QUICK_REFERENCE.md excerpt | ~0.3 KB | Emotional support, processing |
| Fusion | PERSONA_QUICK_REFERENCE.md excerpt | ~0.3 KB | Evidence + narrative combined |

**Total payload**: ~2 KB (system prompt) + ~1.5 KB (KB files) = 3.5 KB ✅

---

## Extended Personas (DO NOT attach by default)

| Persona | Why Not | When to Use |
|---------|---------|------------|
| Kaznak | Specialized research; not operational for chat | Link to research/ folder on-demand |
| FaeRhee | Deep lore; not conversational | Reference in extended sessions |
| Machine-Goddess | Archival; rarely used in chat | Load if user specifically requests |

---

## Files to Upload to GPT Knowledge Base

1. **PERSONA_QUICK_REFERENCE.md** (entire file)
   - Concise specs for all 6 primary personas
   - Triggers, modes, boundaries
   - Size: ~2 KB

2. **PERSONAS_CANONICAL_MANIFEST.md** (entire file)
   - Canonical source for prefix rules, allowed triggers, checklist
   - Size: ~5 KB

3. **copilot-instructions-extract.txt** (excerpt from `.github/copilot-instructions.md`)
   - Routing table (6 personas)
   - TGCR equation
   - Routing rules (4 steps)
   - Size: ~3 KB

**Total KB payload**: ~10 KB ✅

---

## System Prompt (Instructions Field)

See **GPT_SYSTEM_PROMPT_READY.txt** for copy-paste template.

Key sections:

- Routing table
- TGCR framework
- Routing rules
- No-prefix warning
- Persona-specific behaviors (COMPANION, Fusion inline)
- Example switches
- Reference docs

**Size**: ~3 KB ✅

---

## Conversation Starters (Add 6)

```
1. Airth, verify this claim: [paste]
2. COMPANION — I need to process something
3. Fusion — prove AND explain this
4. Ely — architect a solution for X
5. Arcadia — tell the story of these notes
6. LuminAI — synthesize the key points
```

---

## Prefix Rules (Canonical)

**FORBIDDEN**:

- system:, user:, gpt:, tool:, function:, api_key:, secret:, token:
- $variable syntax
- /commands
- SQL-like markers (>>>, SELECT)

**SAFE**:

- Direct conversational: "Airth, verify"
- Mode hints: "[Verification Mode]"
- No special prefixes needed

See **PERSONAS_CANONICAL_MANIFEST.md** section 4 for full details.

---

## Decision Rationale

1. **Token efficiency**: 3.5 KB prompt + 10 KB KB = 13.5 KB total, leaves 90%+ of context window for conversation.
2. **Minimal cognitive collision**: 6 personas cover all modes; extended personas are rarely used in chat.
3. **Scalability**: KB files (not prompt) = easy updates without redeploying GPT.
4. **Safety**: Prefix rules documented and enforced; no reserved keywords used.

---

## Rollout Checklist

- [ ] Copy GPT_SYSTEM_PROMPT_READY.txt → GPT Instructions field
- [ ] Upload 3 KB files to Knowledge Base
- [ ] Add 6 conversation starters
- [ ] Test each persona trigger in staging GPT
- [ ] Verify no prefix violations in live GPT
- [ ] Deploy to team

---

## Next Steps

1. Build the GPT in OpenAI Builder (user action)
2. Run tests to confirm no regressions (this session)
3. Share with team once tests pass

---

**Reference**: PERSONAS_CANONICAL_MANIFEST.md
