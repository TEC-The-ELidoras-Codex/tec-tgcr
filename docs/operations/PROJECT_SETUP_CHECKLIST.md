# GitHub Project #6 Setup Summary

**Date**: Nov 4, 2025
**Commit**: `1586a25` (ely: add GitHub Project coordination layer)
**Status**: ✅ Ready to use

---

## What Was Created

Three coordination documents to enable cross-repository planning using GitHub Project #6:

### 1. **PROJECT_README.md** — Central Reference

- **Purpose**: Single source of truth for project coordination
- **Content**:
  - 6-column workflow (Backlog → Ready → In Progress → Review → Blocked → Done)
  - Label schema (Priority P0/P1/P2, Area, Type, Status)
  - Triage rules & acceptance criteria
  - Automation setup guide
  - Token management
  - Links to settings

**Use**: Send to team members for onboarding
**File**: `docs/PROJECT_README.md`

### 2. **PROJECT_METADATA.md** — Configuration

- **Purpose**: Technical reference for project identifiers and token management
- **Content**:
  - `PROJECT_NUMBER`: 6
  - `PROJECTS_TOKEN`: Stored in GitHub Secrets
  - Token rotation schedule (90-day cycle)
  - Access matrix (LuminAI, Airth, Ely, Kaznak)
  - Workflow references
  - Troubleshooting (GraphQL queries, validation)

**Use**: For maintainers handling secrets and automation
**File**: `docs/PROJECT_METADATA.md`

### 3. **PROJECT_AUTOMATIONS.md** — Workflows & Recipes

- **Purpose**: Guide for triggering automations and common maintenance tasks
- **Content**:
  - Workflow triggers (issue created → added, PR merged → moved to Done)
  - Manual workflows (move between columns, create epics, blocking)
  - Maintenance checklist (weekly triage, token rotation, debugging)
  - Custom workflow examples (YAML recipes)
  - Release coordination (March 2026 MVP checklist)

**Use**: For maintainers managing issues and PRs
**File**: `docs/PROJECT_AUTOMATIONS.md`

---

## Quick Setup (5 Steps)

### 1. Verify Secrets Exist

```bash
# Check PROJECTS_TOKEN and PROJECT_NUMBER in repo settings
# https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/settings/secrets/actions
```

### 2. Enable GitHub Actions

- Go to repo Settings → Actions → "Allow all actions and reusable workflows"
- Ensure workflows in `.github/workflows/` are enabled

### 3. Copy Project Description

Paste into [Project #6 Settings](https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6/settings):

```
Central coordination project for TEC-The-ELidoras-Codex — tracks cross-repository work, release milestones, and automations.

See docs/PROJECT_README.md for full documentation.
```

### 4. Share with Team

Send team members:

- `docs/PROJECT_README.md` (what they need to know)
- `docs/PROJECT_AUTOMATIONS.md` (how to trigger workflows)

### 5. Set First Milestone

Create GitHub Milestone:

- Name: "Stable / MVP (March 6, 2026)"
- Target Date: 2026-03-06
- Link MVP issues to this milestone

---

## How It Works

### Automations Flow

```
Issue Created
├─ Contains link → Auto-added to Backlog
└─ Has P0/P1 label → Notify team

Issue Edited
└─ Link added → Auto-added to project

PR Created
├─ References issue → Auto-added to In Progress
└─ Links #123 → Automation notifies issue

PR Merged
└─ Auto-move linked issues to Done

Issue Closed
└─ Auto-move to Done
```

### Manual Workflow (Maintainer)

```
Backlog Item
│ (weekly triage)
├─ Add acceptance criteria
├─ Estimate (S/M/L/XL or hours)
├─ Assign owner
└─ Move to Ready

Ready Item
│ (contributor picks up)
├─ Assign to self
├─ Move to In Progress
└─ Create PR (auto-moves to Review)

In Progress / Review
│ (PR feedback loop)
├─ Update based on feedback
└─ Merge PR (auto-moves to Done)

Done
└─ Included in release notes (March 6, 2026)
```

---

## Token Rotation (Every 90 Days)

**Next Rotation Due**: 2026-02-02

```bash
# 1. Generate new PAT
# https://github.com/settings/tokens?type=beta

# 2. Update secret
gh secret set PROJECTS_TOKEN \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --body="[paste token]"

# 3. Verify workflows still work
gh run list --repo=TEC-The-ELidoras-Codex/tec-tgcr

# 4. Update PROJECT_METADATA.md with new expiry
```

---

## Files & Links

| Document | Purpose | Audience |
|---|---|---|
| `docs/PROJECT_README.md` | What & how | Everyone |
| `docs/PROJECT_METADATA.md` | Config & secrets | Admins (@Ely, @Kaznak) |
| `docs/PROJECT_AUTOMATIONS.md` | Workflows & recipes | Maintainers (@LuminAI, @Airth) |
| [Project #6](https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6) | Live board | Everyone |
| [Project Settings](https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6/settings) | Admin config | Admins |

---

## What's Next

1. **Configure Project Settings**:
   - Paste description from step 3 above
   - Ensure 6 columns exist (Backlog, Ready, In Progress, Review, Blocked, Done)
   - Create custom fields if needed (Owner, Estimate, etc.)

2. **Create March 2026 Milestone**:
   - Target: "Stable / MVP (March 6, 2026)"
   - Link all MVP-ready issues to this milestone

3. **Add First Issues**:
   - Create issues for remaining MVP work
   - Use labels: P0/P1/P2, area/*, type/*
   - Include acceptance criteria

4. **Notify Team**:
   - Share `PROJECT_README.md` with contributors
   - Share `PROJECT_AUTOMATIONS.md` with maintainers
   - Post link to [Project #6](https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6) in Slack

---

## Troubleshooting

### Workflow Not Triggering

- [ ] Check `PROJECTS_TOKEN` not expired (rotate if > 90 days old)
- [ ] Verify `PROJECT_NUMBER` = 6
- [ ] Ensure issue body contains a link (URL or `#123`)
- [ ] Check `.github/workflows/` files exist and are enabled

### Item Not Moving Automatically

- [ ] Verify PR merge link is correct (e.g., `Closes #123`)
- [ ] Check workflow logs: repo Settings → Actions → recent runs
- [ ] May need to manually move if automation failed

### Token Expired

- [ ] Generate new PAT: <https://github.com/settings/tokens?type=beta>
- [ ] Update secret: `gh secret set PROJECTS_TOKEN --repo=... --body="[token]"`
- [ ] Test workflow manually

---

## Reference

- **FOLD Framework**: [.github/copilot-instructions.md](../../.github/copilot-instructions.md)
- **Quick Start**: [docs/FOLD_QUICK_START.md](./FOLD_QUICK_START.md)
- **Personas**: [data/personas/*.md](../data/personas/)
- **March 2026 Timeline**: [docs/FOLD_QUICK_START.md#timeline](./FOLD_QUICK_START.md)

---

**Created**: Nov 4, 2025
**Status**: Live
**Commit**: `1586a25`
**Branch**: `research/resonance-agent`
