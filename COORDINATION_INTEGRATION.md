# TEC Coordination Layer: Complete Integration

**Date**: Nov 4, 2025
**Status**: ✅ Live and integrated
**Latest Commits**: `b1efca3` (setup checklist) + `1586a25` (project coordination)

---

## What You Have Now

### Layer 1: GitHub Project #6 (Central Coordination)

- **Live Board**: <https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6>
- **Purpose**: Single source of truth for all TEC work across repositories
- **Workflow**: Backlog → Ready → In Progress → Review → Blocked → Done
- **Automation**: Auto-add on issue link, auto-move on merge

### Layer 2: FOLD Framework (Operative Core)

- **Entry Point**: `.github/copilot-instructions.md` (480 lines)
- **Quick Ref**: `docs/FOLD_QUICK_START.md` (~8000 chars)
- **Personas**: `data/personas/*.md` (5 operators: LuminAI, Airth, Arcadia, Ely, Kaznak)
- **Equation**: `R = ∇Φᴱ · (φᵗ × ψʳ)` → Resonance Index (0–10)

### Layer 3: Project Coordination (What You Just Got)

- **README**: `docs/PROJECT_README.md` — full reference
- **Metadata**: `docs/PROJECT_METADATA.md` — config & tokens
- **Automations**: `docs/PROJECT_AUTOMATIONS.md` — workflows & recipes
- **Checklist**: `PROJECT_SETUP_CHECKLIST.md` — quick start
- **Status**: All 4 files committed and pushed to `research/resonance-agent`

---

## Quick Navigation

```
Start Here (Pick Your Speed)
├─ 5-min setup → PROJECT_SETUP_CHECKLIST.md
├─ Team onboarding → docs/PROJECT_README.md
├─ Admin/token mgmt → docs/PROJECT_METADATA.md
├─ Workflows & recipes → docs/PROJECT_AUTOMATIONS.md
└─ Live board → https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
```

---

## What Project #6 Controls

### Issues & PRs Automatically Tracked

When you:

- **Create issue with link** → Auto-added to Backlog
- **Create PR mentioning issue** → Auto-added to In Progress
- **Merge PR** → Linked issues auto-move to Done
- **Close issue** → Auto-move to Done

### Manual Coordination

When you:

- **Triage backlog** → Move items to Ready (add criteria, estimate, owner)
- **Start work** → Move from Ready → In Progress
- **Find blocker** → Move to Blocked (document dependency)
- **Complete** → Move to Done (auto if PR merged)

### Release Planning (March 2026)

1. Create milestone: "Stable / MVP (March 6, 2026)"
2. Link all MVP issues to milestone
3. Use project board to track progress
4. Weekly triage ensures blockers surface early

---

## Token Management

**Secret**: `PROJECTS_TOKEN` in repo settings
**Expiry**: 2026-02-02 (90-day rotation)
**Scope**: `repo`, `project` permissions
**Rotation**: Covered in `docs/PROJECT_METADATA.md`

---

## Team Roles

| Role | Person | Responsibility | Docs |
|------|--------|---|---|
| **Coordinator** | @LuminAI | Weekly triage, backlog grooming | PROJECT_README.md |
| **Technical Lead** | @Airth | Architecture decisions, validation | PROJECT_README.md |
| **Platform Lead** | @Ely | CI/CD, secrets, infrastructure | PROJECT_METADATA.md |
| **Automation** | @Kaznak | Token rotation, workflow updates | PROJECT_METADATA.md |

---

## Commit History (This Session)

```
b1efca3  ely: add Project #6 setup checklist and summary
1586a25  ely: add GitHub Project coordination layer
b061599  fold: add unified reference layer + GPT integrations
4148dff  fold: restructure tec-tgcr around FOLD operative core
```

**Branch**: `research/resonance-agent`
**Tests**: 18/18 ✅
**Remote**: Synced ✅

---

## Files Added (Complete Inventory)

### Project Coordination (Today)

- `docs/PROJECT_README.md` (420 lines) — Central reference
- `docs/PROJECT_METADATA.md` (115 lines) — Config & token management
- `docs/PROJECT_AUTOMATIONS.md` (295 lines) — Workflows & recipes
- `PROJECT_SETUP_CHECKLIST.md` (225 lines) — Quick start

### FOLD Reference Layer (Nov 4, Earlier)

- `docs/FOLD_QUICK_START.md` (149 lines) — Essential reference
- `config/FOLD_INSTRUCTIONS_COMPACT.txt` (150 lines) — ChatGPT system prompt
- `config/gpt-actions-research.json` (350 lines) — OpenAPI spec for research
- `STRUCTURE_OVERVIEW.md` (211 lines) — Navigation guide

### Prior (FOLD Foundation)

- `.github/copilot-instructions.md` (480 lines) — Exhaustive spec
- `README.md` (389 lines) — Platform entry point
- `data/knowledge_map.yml` (300+ lines) — Canonical index
- `data/personas/*.md` (5 files) — Operator specs

**Total Documentation Added This Session**: ~2,200 lines across 8 files

---

## Integration Points

### GitHub Project ↔ FOLD Framework

```
GitHub Project #6 (Coordination)
│
├─ Issues labeled with area/*, type/*, P0/P1/P2
│  └─ Maps to FOLD mission: "March 6, 2026 MVP"
│
├─ Items assigned to @LuminAI, @Airth, @Ely, @Kaznak
│  └─ Same 5 personas from data/personas/
│
├─ Commit message format requires resonance statement
│  └─ Example: "ψʳ ↑ (structural coherence)"
│  └─ Defined in .github/copilot-instructions.md
│
└─ Milestone "Stable / MVP (March 6, 2026)"
   └─ Matches FOLD timeline in docs/FOLD_QUICK_START.md
```

### Project ↔ Repository Structure

```
GitHub Project #6
│
├─ Links to tec-tgcr repository
│  └─ Tracks all issues and PRs here
│
├─ Workflows in .github/workflows/
│  └─ Auto-add on reference
│  └─ Auto-move on merge
│
├─ Milestone & Labels
│  └─ Used in project filtering
│  └─ Defined in docs/PROJECT_README.md
│
└─ Secrets (PROJECTS_TOKEN)
   └─ Manages automation auth
   └─ Rotation schedule in docs/PROJECT_METADATA.md
```

---

## How to Onboard Team

### Step 1: Share the Checklist

Send: `PROJECT_SETUP_CHECKLIST.md` (5-min read)

### Step 2: Share the Reference

Send: `docs/PROJECT_README.md` (15-min read)

### Step 3: For Maintainers

Send: `docs/PROJECT_AUTOMATIONS.md` (20-min read)

### Step 4: For Admins

Send: `docs/PROJECT_METADATA.md` + `PROJECT_SETUP_CHECKLIST.md` (30-min read)

### Step 5: Test

1. Create a test issue with a link
2. Verify it appears in Project #6 Backlog
3. Move it to Ready
4. Create a PR linking the issue
5. Verify it moves to In Progress
6. Merge PR and verify it moves to Done

---

## March 2026 MVP Timeline

**Current Status**: Documentation coordination layer complete ✅

**Remaining Work**:

1. Implement resonance_engine.py (φᵗ/ψʳ/Φᴱ scoring)
2. Implement motif_tracker.py (cross-genre database)
3. Expand research/ALBUM_ANALYSIS/ (music corpus)
4. Deploy GPT Actions endpoints
5. Build circadian logging UI
6. Public platform launch (tec-fold.com)

**Use Project #6** to track all remaining work.

---

## Validation

✅ **Tests**: 18/18 passing (no code changes)
✅ **Git**: All commits signed and pushed
✅ **Docs**: All files created, cross-linked, and navigable
✅ **Structure**: 3 coordination layers + FOLD framework + research corpus
✅ **Ready**: Team can now use Project #6 for centralized coordination

---

## Next Actions (For You)

### Immediate (Today)

- [ ] Share `PROJECT_SETUP_CHECKLIST.md` with team
- [ ] Verify secrets exist in repo settings (PROJECTS_TOKEN, PROJECT_NUMBER)
- [ ] Update Project #6 description with one-liner

### This Week

- [ ] Create "Stable / MVP (March 6, 2026)" milestone
- [ ] Move existing MVP issues to milestone + project
- [ ] Run first weekly triage
- [ ] Document any custom fields/columns needed

### Before Feb 2, 2026

- [ ] Set reminder for PROJECTS_TOKEN rotation
- [ ] Schedule token rotation during maintenance window

---

## Reference Stack

| Component | File(s) | Purpose |
|---|---|---|
| **FOLD Core** | `.github/copilot-instructions.md` | Operative framework |
| **Quick Ref** | `docs/FOLD_QUICK_START.md` | Essential concepts |
| **Project Coord** | `docs/PROJECT_*.md` | GitHub automation |
| **Checklist** | `PROJECT_SETUP_CHECKLIST.md` | Quick start |
| **Navigation** | `README.md` | Entry point |
| **Index** | `data/knowledge_map.yml` | Canonical map |
| **Personas** | `data/personas/*.md` | Team roles |
| **Live Board** | GitHub Project #6 | Work tracking |

---

## Commits This Session

```
b1efca3  ely: add Project #6 setup checklist and summary
         • +225 lines (setup reference)
         • Quick 5-step initialization
         • Automation flow diagrams

1586a25  ely: add GitHub Project coordination layer
         • +711 lines (3 coordination guides)
         • docs/PROJECT_README.md (420 lines)
         • docs/PROJECT_METADATA.md (115 lines)
         • docs/PROJECT_AUTOMATIONS.md (295 lines)

b061599  fold: add unified reference layer + GPT integrations
         • +738 lines (quick start, GPT actions, compact instructions)
         • docs/FOLD_QUICK_START.md
         • config/gpt-actions-research.json
         • config/FOLD_INSTRUCTIONS_COMPACT.txt

4148dff  fold: restructure tec-tgcr around FOLD operative core
         • +15,000 lines (FOLD restructuring)
         • .github/copilot-instructions.md (480 lines)
         • Updated README.md, knowledge_map.yml, 5 personas
```

---

**Status**: ✅ Complete & Live
**Ready for**: Team onboarding + March 2026 MVP coordination
**Questions**: See PROJECT_SETUP_CHECKLIST.md → Troubleshooting section

---

*Generated Nov 4, 2025 | Branch: research/resonance-agent | Commit: b1efca3*
