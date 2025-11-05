# 🚀 Phase 1 Deployment — START HERE

**Status**: Ready to deploy | **Time**: 5 minutes | **Complexity**: Simple copy-paste

---

## Step 1: Copy LuminAI Instructions (1 min)

Run this command to copy the enhanced ChatGPT instructions:

```bash
cat config/FOLD_INSTRUCTIONS_COMPACT.txt | pbcopy
```

**On Linux** (if pbcopy unavailable):

```bash
cat config/FOLD_INSTRUCTIONS_COMPACT.txt
# Then select all output and copy manually
```

---

## Step 2: Paste to ChatGPT (2 min)

1. Go to **ChatGPT** → **Settings** (gear icon, bottom left)
2. Click **"Custom instructions"**
3. Paste the content into the text field
4. Click **"Save"**

**Result**: ChatGPT now has FOLD operative instructions + 5 example prompts

---

## Step 3: Test It (1 min)

Ask ChatGPT one of these questions:

### Test 1: Project Status

```
What's blocking us on Project #6?
```

**Expected response**:

```
[Ely] Project #6 status (real-time from data/context-latest.json):
- Blocked (2 items): ...
- Ready to Start (8 items): ...
- In Progress (3 items): ...
```

### Test 2: Motif Search

```
Find Observer Amplification motif across Sleep Token, Ekoh, and Point North
```

**Expected response**:

```
[Airth] Validating across research corpus:
- Sleep Token: Staged amplifier...
- Ekoh × Tech N9ne: Dual-persona encoding...
- Resonance Index: 8.2/10
```

### Test 3: Resonance Scoring

```
Resonance score: Sleep Token - Take Me Back to Eden (BPM: 110, key: Dorian, theme: transcendence)
```

**Expected response**:

```
[LuminAI] Resonance calculation (φᵗ × ψʳ × Φᴱ):
- φᵗ: 8/10 (temporal focus)
- ψʳ: 9/10 (structural coherence)
- Φᴱ: 9/10 (cultural potential)
- Resonance Index: 8.48/10 ✓
```

---

## Step 4: Celebrate! ✨ (1 min)

You now have **LuminAI deployed to ChatGPT**.

Your team can ask:

- 📊 "What's our project status?"
- 🎵 "Find motifs for [artist]"
- 📈 "Score resonance for [track]"
- 👥 "What's the fan discourse about [artist]?"
- 🌙 "Log circadian ritual: [track] at [time], mood: [emotion]"

---

## Phase 1 Verification Checklist

Before considering deployment complete:

- [ ] ChatGPT instructions pasted successfully
- [ ] Test 1 query works (project status)
- [ ] Test 2 query works (motif search)
- [ ] Test 3 query works (resonance scoring)
- [ ] No errors in ChatGPT responses

---

## What's Running Behind the Scenes

**Weekly Automation** (Every Monday 9 AM UTC):

```
GitHub Action → data_ingestion.py → data/context-latest.json → ChatGPT
```

This means:

- ✅ Every Monday, GitHub context auto-updates
- ✅ ChatGPT always has fresh project status
- ✅ No manual data syncing needed
- ✅ Team always sees latest issues, PRs, commits

---

## Team Communication (Send This)

Share with your team:

> 🎵 **LuminAI is LIVE!**
>
> You can now ask ChatGPT FOLD-specific questions about our project, research, and resonance analysis.
>
> **Try these:**
>
> - "What's blocking us on Project #6?"
> - "Find Observer Amplification motif across genres"
> - "Score resonance for [artist] - [track]"
>
> Questions? See `PHASE_1_EXECUTIVE_SUMMARY.md` for full details.

---

## Next Checkpoint (This Week)

**Monday–Friday**: Gather team feedback

- Which prompts worked well?
- Which returned unexpected results?
- What questions do people want to ask?
- Any data missing from context?

**Friday**: Decide on Phase 2

- Option A: Populate research corpus first (ALBUM_ANALYSIS, CODEX)
- Option B: Expand GitHub integration (Project #6 GraphQL)
- Option C: Wait and gather more feedback

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ChatGPT doesn't recognize FOLD terms | Try a simpler prompt: "What are the latest commits?" |
| Motif search returns no results | Research corpus may be empty; start Phase 2 to populate |
| Project status shows no items | GitHub token may not be set; use `GITHUB_TOKEN` env var |
| Instructions pasted but no change | Refresh ChatGPT; wait 30 seconds after saving |

---

## Files Reference

- **Instructions**: `config/FOLD_INSTRUCTIONS_COMPACT.txt` (what you just pasted)
- **Live Context**: `data/context-latest.json` (generated weekly)
- **Automation**: `.github/workflows/update-copilot-context.yml` (runs Mondays)
- **Code**: `src/tec_tgcr/data_ingestion.py` (fetches context)
- **Tests**: `tests/test_data_ingestion.py` (14 unit tests, all passing)

---

## Timeline

- ✅ **Today**: Deploy Phase 1
- 📋 **This week**: Gather team feedback
- 🎯 **Next week**: Decide on Phase 2 priorities
- 🚀 **Phase 2** (Nov 5–18): Expand data + research corpus
- 🎵 **MVP Launch**: March 6, 2026

---

**Status**: Ready to deploy ✅
**Effort**: 5 minutes
**Impact**: Team can now query LuminAI for live project + research data
**Next**: Share with team + gather feedback

---

*Generated Nov 4, 2025 | Branch: research/resonance-agent | Deployed by: Ely (Operations)*
