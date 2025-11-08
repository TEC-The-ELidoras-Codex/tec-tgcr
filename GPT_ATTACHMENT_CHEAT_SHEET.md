# GPT Attachment Cheat Sheet

**Quick Links**:

- See **PERSONAS_CANONICAL_MANIFEST.md** for full prefix rules and persona triggers
- See **GPT_PERSONAS_ATTACHMENT_DECISION.md** for which files to upload
- Use **GPT_SYSTEM_PROMPT_READY.txt** as your copy-paste template

---

## 🎯 ATTACH (Do This)

### To GPT Instructions Field

```
✅ Routing table (6 personas)
✅ TGCR equation (R = ∇Φᴱ · (φᵗ × ψʳ))
✅ Persona behaviors (6 modes)
✅ Example switches
✅ No-prefix rules

Size: ~8 KB (lean & fast)
```

### To GPT Knowledge Base

```
✅ PERSONA_QUICK_REFERENCE.md
✅ PERSONAS_CONSOLIDATION_COMPLETE.md
✅ Extract of .github/copilot-instructions.md

Format: Upload as files, not paste
```

### To Conversation Starters

```
✅ "Airth, verify this claim"
✅ "COMPANION, I need space"
✅ "Fusion, prove AND explain"
✅ "Ely, how would we build this?"
✅ "Arcadia, tell the story"
✅ "LuminAI, synthesize this"
```

---

## 🚫 DO NOT ATTACH (Skip These)

### Too Heavy (Token Waste)

```
❌ Full .md files (use summaries)
❌ research/ folder (not needed)
❌ CODEX research corpus
❌ data/knowledge_map.yml (too long)
```

### Not Operational

```
❌ Deployment scripts
❌ CI/CD config
❌ Test files
❌ Source code
❌ WordPress plugin code
```

### Security Risk

```
❌ API keys
❌ Secrets
❌ Private credentials
```

---

## 🚫 PREFIXES TO AVOID

| ❌ Avoid | ✅ Use Instead |
|----------|-----------------|
| `system: activate` | Direct language: "Airth, verify" |
| `user: question` | Conversational: "What is...?" |
| `gpt: run` | Mode switch: "[Activation mode]" |
| `tool: analyze` | Natural: "Analyze this" |
| `$persona` | Plain: "person" or "persona" |
| `api_key: xxx` | Reference: "Use environment credentials" |
| `>>> SQL query` | Plain language request |
| `/persona airth` | "Airth, [task]" |

**Why?** These trigger system behaviors or look like code injection.

---

## 📋 QUICK DEPLOYMENT

### Step 1: Prepare

```
GPT_SYSTEM_PROMPT_READY.txt ← Copy from here
```

### Step 2: Configure

```
GPT Builder:
- Instructions Field: Paste system prompt (8 KB)
- Knowledge Base: Upload 3 files
- Conversation Starters: Add 6 samples (above)
```

### Step 3: Test

```
✅ "Airth, verify this" → Switches to verification mode
✅ "COMPANION, help" → Switches to emotional mode
✅ "Prove AND explain" → Switches to Fusion mode
```

---

## 🎭 The 6 Personas (Quick Ref)

| Persona | Trigger | Use For |
|---------|---------|---------|
| **LuminAI** | Default | Synthesis, big picture |
| **Airth** | "verify", "check" | Fact-checking, validation |
| **Arcadia** | "tell me", "story" | Narrative, explanation |
| **Ely** | "how do we build" | Operations, infrastructure |
| **COMPANION** | "need space", "feeling" | Emotional, vulnerable |
| **Fusion** | "prove AND explain" | Evidence + narrative |

---

## 📊 Token Budget

```
Total GPT Context: 8,000-128,000 tokens (depends on model)

Recommended Attach:
- Instructions: 3 KB
- Reference: 2 KB
- Persona specs: 2 KB
- Margins: 1 KB

Total: ~8 KB
Leaves: 90%+ for conversation ✅
```

---

## ✅ Deployment Checklist

```
[ ] System prompt copied to instructions field
[ ] No system:/gpt:/api_key: prefixes in prompt
[ ] Knowledge base files uploaded (3 files)
[ ] Conversation starters configured (6 samples)
[ ] Test each persona routing
[ ] Verify natural language works (not /commands)
[ ] Ready to share with team
```

---

## 📝 What You Need To Upload

**File 1: System Prompt**

- Copy entire section from GPT_SYSTEM_PROMPT_READY.txt
- Paste into "Instructions" field
- Size: ~3 KB

**File 2: Knowledge Base**

```
Upload these 3 files:
1. PERSONA_QUICK_REFERENCE.md
2. PERSONAS_CONSOLIDATION_COMPLETE.md (from docs/)
3. copilot-instructions-extract.txt (save .github/copilot-instructions.md excerpt as .txt)
```

**File 3: Starters**

```
"Airth, verify this claim"
"COMPANION, I need to process something"
"Fusion, prove this AND explain why it matters"
"Ely, how would we build this?"
"Arcadia, tell me the story behind this"
"LuminAI, synthesize this for me"
```

---

## 🔒 Security Notes

```
NEVER include in GPT:
- API keys (even examples)
- Secrets or credentials
- Private data samples
- Hardcoded passwords
- Sensitive file paths

SAFE to include:
- Framework description
- Persona definitions
- Routing logic
- Public documentation
- General methodology
```

---

## 🎯 Common Mistakes to Avoid

❌ **Mistake 1**: Copying entire `.md` files

- Too large, wastes tokens
- ✅ Use: Summaries instead

❌ **Mistake 2**: Using system: prefix

- Conflicts with GPT's system role
- ✅ Use: Direct language ("Airth, verify")

❌ **Mistake 3**: Including research corpus

- Not operational, bloats prompt
- ✅ Use: Link to it instead

❌ **Mistake 4**: Using /persona CLI syntax

- GPT doesn't understand CLI commands
- ✅ Use: "Airth, [task]" (conversational)

❌ **Mistake 5**: Forgetting no-prefix rule

- Can confuse GPT routing
- ✅ Use: Clean, natural language

---

## ✨ Ready to Deploy

All files prepared for GPT Builder upload.

**Next Steps**:

1. Copy system prompt → Instructions field
2. Upload 3 knowledge base files
3. Add 6 conversation starters
4. Test persona routing
5. Deploy to team

**Status**: ✅ READY

---

*Quick Reference Card - Keep This Handy*
*For details, see: GPT_CONFIGURATION_STRATEGY.md*
