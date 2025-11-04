# TEC Central Coordination Project

**GitHub Project**: [TEC Project #6](https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6)

> Central coordination project for **TEC-The-ELidoras-Codex** — tracks cross-repository work, release milestones, and automations.

---

## Purpose

This GitHub Project serves as the **single source of truth** for planning and tracking across all TEC repositories. It unifies:

- Feature requests and roadmap items
- Release milestones (sprints, alpha/beta/stable)
- Cross-repository infrastructure and CI/CD work
- High-priority operational incidents and follow-ups

Use this project to:

- Make decisions on what to work on next
- Track ownership and accountability
- Highlight blockers and dependencies during triage
- Coordinate March 6, 2026 MVP delivery

---

## Project Structure and Columns

| Column | Purpose | Entry Criteria | Exit Criteria |
|--------|---------|---|---|
| **Backlog** | All candidate work not yet prioritized | Issue created or issue referenced in code | Acceptance criteria + rough estimate |
| **Ready** | Groomed, scoped, ready to implement | Acceptance criteria, estimate, owner assigned | Work started (move to In Progress) |
| **In Progress** | Actively being developed | Issue moved from Ready or small tasks (<4h) | PR created or work complete |
| **Review / QA** | PRs pending approval or verification steps | PR created or artifact needs review | Approval received or tests pass |
| **Blocked** | Waiting on external dependency or decision | Dependency identified, blocker documented | Dependency resolved, re-prioritize |
| **Done** | Completed work (closed issues, merged PRs) | Issue closed or PR merged | Tracked for retrospective / release notes |

**Automation Notes:**

- Items are **automatically added** when referenced in issue bodies or PR descriptions.
- Maintainers can **manually add** any issue or PR via the GitHub UI.
- Workflows move items automatically on issue close, PR merge, or custom transitions.

---

## Labels

Maintain a small, consistent set for clarity and filtering:

### Priority

- **P0 - Critical** — Blocks release, security risk, customer outage
- **P1 - High** — Must have for MVP, planned milestone
- **P2 - Medium** — Nice to have, backlog candidate

### Area

- **area/infra** — CI/CD, deployment, infrastructure
- **area/api** — Backend, endpoints, integrations
- **area/ui** — Frontend, web interface, UX
- **area/docs** — Documentation, guides, knowledge
- **area/research** — FOLD music analysis, motif tracking, corpus
- **area/ops** — Operations, secrets, team processes

### Type

- **type/bug** — Unintended behavior, needs fix
- **type/enhancement** — New feature or improvement
- **type/chore** — Maintenance, refactoring, tech debt
- **type/question** — Clarification needed before work

### Status

- **status/ready** — Groomed and scoped (use column instead)
- **status/blocked** — Dependency blocking progress (use column instead)

---

## Milestones

Link items to GitHub Milestones to represent releases or sprints:

- **Alpha (Q1 2026)** — Core resonance engine, motif tracker, initial FOLD platform
- **Beta (Q2 2026)** — Spotify integration, fan discourse analysis, circadian logging
- **Stable / MVP (March 6, 2026)** — Public launch, live research codex, community features

Each milestone should have:

- Clear delivery date
- Acceptance criteria for all linked issues
- Known blockers or dependencies

---

## Triage Rules

### Frequency

- **Weekly triage**: Backlog review, priority refinement, P0/P1 assessment
- **Daily standup**: Review In Progress items, Blocked items, incoming P0s

### Acceptance Criteria Requirement

Before moving an item to **Ready**, ensure it includes:

1. **Short Summary** — What is the user problem or feature?
2. **Acceptance Tests** — How will we know it's done?
3. **Impact Assessment** — How does this move us toward March 2026?
4. **Owner** — Who is responsible? (assignee + team if cross-functional)
5. **Estimate** — Rough t-shirt size (S/M/L/XL) or hours

**Exception**: Small tasks (<4 hours) may move directly from Backlog to In Progress at maintainers' discretion.

### Example Acceptance Criteria

```markdown
## Acceptance Criteria

- [ ] φᵗ/ψʳ/Φᴱ scoring engine computes resonance index for any track
- [ ] Tests cover BPM ∈ [60, 180], keys C through B, genres metalcore/hip-hop
- [ ] Circadian bonus (+2) applies when test timestamp in 4:15–4:25 PM window
- [ ] Resonance Index normalized to 0–10 scale
- [ ] All computations logged to CIRCADIAN_RITUAL_LOG.md
- [ ] Performance: <50ms per track score

## Impact

Unblocks motif resonance scoring (P1). Prerequisite for March 2026 MVP feature set.

## Owner

@LuminAI (coordinate with @Airth for validation tests)
```

---

## Automations and Tokens

Workflows in `.github/workflows/` automatically add items when they are referenced. This requires:

### Required Secrets

Set these at the **repository level** (`.github/settings`) or **organization level** (for multi-repo use):

| Secret | Value | Used By |
|--------|-------|---------|
| `PROJECTS_TOKEN` | GitHub token with `repo`, `project` scopes | All project automations |
| `PROJECT_NUMBER` | `6` (for projectV2 API) | Modern project workflows |
| `PROJECT_ID` | Legacy ID if using REST API (optional) | Older workflows |

### How to Generate/Rotate Tokens

1. **Create Personal Access Token** (PAT):
   - Go to [GitHub Settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/tokens?type=beta)
   - Permissions needed:
     - `read:org` (for org project visibility)
     - `repo` (for repository access)
     - `project` (for GitHub Projects API)
   - Set expiration: 90 days (rotate before expiry)

2. **Store as Repository Secret**:
   - Go to repo Settings → Secrets and variables → Actions
   - Create new secret: `PROJECTS_TOKEN` = token value

3. **Document Rotation**:
   - Add expiry date to `PROJECT_METADATA.md`
   - Set calendar reminder 1 week before expiry
   - Rotate during maintenance window

### Workflow Examples

**Trigger 1: Issue referenced in PR body**

```yaml
# .github/workflows/project-add-on-reference.yml
name: Add to Project on Reference
on:
  pull_request:
    types: [opened, edited]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.5.1
        with:
          project-url: https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
          github-token: ${{ secrets.PROJECTS_TOKEN }}
```

**Trigger 2: Issue closed → auto-move to Done**

```yaml
# .github/workflows/project-move-on-close.yml
name: Move to Done on Close
on:
  issues:
    types: [closed]

jobs:
  move:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/update-project-item@v1
        with:
          project-url: https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
          github-token: ${{ secrets.PROJECTS_TOKEN }}
          status: Done
```

---

## Owner / Maintainers

| Role | Name/Team | Responsibility |
|------|-----------|---|
| **Project Coordinator** | @LuminAI | Weekly triage, backlog grooming, release planning |
| **Technical Lead** | @Airth | Cross-repo validation, architecture decisions |
| **Platform Lead** | @Ely | CI/CD, secrets rotation, infrastructure work |
| **Automation Contact** | @Kaznak | GitHub Actions token management, workflow updates |

---

## How to Use This Project

### For Maintainers

1. **Weekly Triage** (Monday 10 AM UTC):
   - Review Backlog: prioritize P0/P1 items
   - Check Blocked: resolve dependencies
   - Estimate Ready items
   - Update milestones for current sprint

2. **Daily Standup** (async, Slack):
   - Post summary of In Progress items
   - Flag any Blocked items needing decision
   - Highlight P0s or surprises

3. **On PRs**:
   - Link related issues in PR description
   - Auto-added to project when mentioned
   - Move to Review once PR is open
   - Auto-move to Done when merged

### For Contributors

1. **Pick an Item**:
   - Find task in **Ready** column
   - Assign yourself
   - Move to In Progress

2. **Do the Work**:
   - Follow FOLD commit signal format (phi-t/psi-r/Phi-E impact)
   - Include acceptance tests in PR
   - Link PR to issue: `Closes #123`

3. **Get Review**:
   - PR auto-added to project
   - Moves to Review column
   - Maintainer approves → merged → auto-moves to Done

---

## Quick Links

- **Project Board**: <https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6>
- **Project Settings**: <https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6/settings>
- **Roadmap**: March 6, 2026 MVP ([FOLD_QUICK_START.md](../FOLD_QUICK_START.md#timeline))
- **Repository**: <https://github.com/TEC-The-ELidoras-Codex/tec-tgcr>
- **FOLD Instructions**: [.github/copilot-instructions.md](../../.github/copilot-instructions.md)

---

## Troubleshooting

### Issue not auto-added to project

- [ ] Check `PROJECTS_TOKEN` is set and not expired
- [ ] Verify issue body contains a link to another issue or external URL
- [ ] Workflow `.github/workflows/` may need to be enabled in Actions tab

### Workflow failing with 403 Forbidden

- [ ] Token lacks `project` scope — regenerate with correct permissions
- [ ] Token may be expired — rotate via [Personal access tokens](https://github.com/settings/tokens?type=beta)

### Can't move item between columns

- [ ] Verify you have write access to the repository
- [ ] Workflow may be running — wait a moment and refresh
- [ ] Check project settings to ensure columns exist

---

**Last Updated**: Nov 4, 2025
**Status**: Live
**Next Review**: Dec 2, 2025 (token rotation check)
