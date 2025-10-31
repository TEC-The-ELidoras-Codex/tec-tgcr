## TEC Project: Central Coordination (GitHub Project)

Short description (one-line, use this as the Project description):

"Central coordination project for TEC-The-ELidoras-Codex — tracks cross-repo work, release milestones, automations, and cross-team initiatives to deliver LuminAI platform features and infra improvements."

Longer description (copy into the Project description field if you want more detail):

"This GitHub Project unifies planning and tracking for TEC-The-ELidoras-Codex. It collects issues and PRs that represent user-facing features, platform/infrastructure tasks, security/operational work, and cross-repo initiatives. The board is organized by lifecycle (Backlog → Ready → In Progress → Review → Done) and augments repository labels and milestones. Automations add items when referenced from issues/PRs and use the project's workflow tokens. Use this project to prioritize releases, coordinate across agents and apps, and surface blockers during triage meetings."

---

## Purpose

This Project is the single source of truth for cross-repo planning and release coordination. It brings together:

- Feature requests and roadmap items
- Release milestones (sprints, alpha/beta/stable)
- Cross-repo infrastructure and CI work
- High-priority operational incidents and follow-ups

Use the Project to decide what to work on next, who owns it, and when it ships.

## Project structure and columns

Recommended columns (you can adapt to your workflow):

- Backlog — all candidate work not yet prioritized
- Ready — groomed and ready for implementation
- In Progress — actively being worked on
- Review / QA — PRs or verification steps pending approval
- Blocked — waiting on an external dependency or decision
- Done — completed work (closed issues / merged PRs)

Column behavior notes:
- Move items from Backlog to Ready after acceptance criteria and rough estimate are present.
- Only items in Ready should be picked up for In Progress.
- Use Blocked to make dependencies visible in standups.

## Labels, milestones and owners

- Keep a small, consistent label set: priority (P0/P1/P2), area (infra, api, ui, docs), type (bug, enhancement, chore), and status-specific labels where needed.
- Use GitHub Milestones to represent releases or sprints and link them to project items.
- Add an Owner field (assignee or project custom field) so each item has a clear owner.

## How items get added

1. Automated: The repository includes workflows that add referenced issues to this Project when issue bodies include references to other issues/URLs. Ensure `PROJECTS_TOKEN` and `PROJECT_ID`/`PROJECT_NUMBER` secrets are configured for automations to run.
2. Manual: Maintainers can add any issue or PR to the project via the GitHub UI or the "Add to project" action.

## Triage rules

- Triage frequency: weekly kick-off meeting or as-needed for P0/P1 items.
- Acceptance criteria required before moving to Ready: short summary, acceptance tests, impact, and owner.
- Small tasks (< 4h) may be moved directly to In Progress at the maintainer's discretion.

## Automations and tokens

- Workflows in `.github/workflows/` (classic and projectV2) may add items automatically. These workflows expect one or more repository secrets:
  - `PROJECTS_TOKEN` — token used by automations to add items
  - `PROJECT_ID` (classic) or `PROJECT_NUMBER` (projectV2) — the identifier for this project

Store tokens as repository secrets (or use organization-level secrets for multi-repo projects).

## Owner / Maintainers

- Project Maintainer: Team/Person to coordinate backlog grooming and release planning (replace with your team's contact info).
- Automation contact: person who manages the GitHub Actions tokens and mapping.

## Quick copy blocks

Use these to populate the GitHub Project description field.

One-line description (copy-paste):

> Central coordination project for TEC-The-ELidoras-Codex — tracks cross-repo work, release milestones, automations, and cross-team initiatives to deliver LuminAI platform features and infra improvements.

Longer description (copy-paste if you prefer more context):

> This GitHub Project unifies planning and tracking for TEC-The-ELidoras-Codex. It collects issues and PRs that represent user-facing features, platform/infrastructure tasks, security/operational work, and cross-repo initiatives. The board is organized by lifecycle (Backlog → Ready → In Progress → Review → Done) and augments repository labels and milestones. Automations add items when referenced from issues/PRs and use the project's workflow tokens. Use this project to prioritize releases, coordinate across agents and apps, and surface blockers during triage meetings.

---

## How to use this README

- Paste the one-line description into the GitHub Project's description field for a concise summary.
- If you want a fuller description, paste the longer block.
- Update the Owner / Maintainers section with team members and change the column names to match your preferred workflow.

If you'd like, I can also:
- Add a small `PROJECT_METADATA.md` with the `PROJECT_ID`/`PROJECT_NUMBER` values and how to rotate tokens.
- Create a `.github/project-automations.md` with examples for maintainers to trigger automations.
