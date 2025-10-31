# Project metadata — TEC Project 6

Project URL:

https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6

Project reference names:

- projectV2 number: 6  (use this as `PROJECT_NUMBER` in projectV2 workflows)
- If you need the GraphQL node id (used as `PROJECT_ID` in some scripts/workflows), see the commands below to fetch it.

Short description (copy this into the Project description field):

Central coordination project for TEC-The-ELidoras-Codex — tracks cross-repo work, release milestones, automations, and cross-team initiatives to deliver LuminAI platform features and infra improvements.

Longer description (optional, copy if you want more context):

This GitHub Project serves as a unified platform for planning and tracking within TEC-The-ELidoras-Codex. It aggregates issues and pull requests (PRs) that represent user-facing features, platform and infrastructure tasks, security and operational work, and cross-repository initiatives. The board is organized by lifecycle stages (Backlog → Ready → In Progress → Review → Done) and enhances repository labels and milestones. Automations add items when they are referenced in issues or PRs and utilize the project's workflow tokens. Use this project to prioritize releases, coordinate across agents and applications, and highlight blockers during triage meetings.

Quick copy blocks

One-line (recommended):

> Central coordination project for TEC-The-ELidoras-Codex — tracks cross-repo work, release milestones, automations, and cross-team initiatives to deliver LuminAI platform features and infra improvements.

Longer (optional):

> This GitHub Project serves as a unified platform for planning and tracking within TEC-The-ELidoras-Codex. It aggregates issues and pull requests (PRs) that represent user-facing features, platform and infrastructure tasks, security and operational work, and cross-repository initiatives. The board is organized by lifecycle stages (Backlog → Ready → In Progress → Review → Done) and enhances repository labels and milestones. Automations add items when they are referenced in issues or PRs and utilize the project's workflow tokens. Use this project to prioritize releases, coordinate across agents and applications, and highlight blockers during triage meetings.

How to paste the description (UI):

1. Open the project URL in your browser: https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
2. Click the settings (gear) or the edit icon in the Project header/description area.
3. Paste the one-line or longer description and Save.

How to get the GraphQL node id (PROJECT_ID)

Use this when a workflow or script requires the node `id` for the project (some classic/project integrations need it). Replace `ORG` and `NUMBER` below as needed.

Using the GitHub CLI (`gh`) — simple GraphQL query:

```bash
gh api graphql -f query='query { organization(login:"TEC-The-ELidoras-Codex") { projectV2(number:6) { id } } }'
```

This prints a JSON object with the `id` field. Make sure `gh auth status` shows you're authenticated to the org.

Using curl + GITHUB_TOKEN (bash):

```bash
export GITHUB_TOKEN="<your_token_with_org_scope>"
curl -s -H "Authorization: bearer $GITHUB_TOKEN" -X POST -d '{"query":"query { organization(login:\"TEC-The-ELidoras-Codex\") { projectV2(number:6) { id } } }"}' https://api.github.com/graphql | jq -r '.data.organization.projectV2.id'
```

Notes about classic Projects vs projectV2

- projectV2 (the new projects) exposes a `number` (6) which is stable and shown in the URL — many workflows use `PROJECT_NUMBER` for projectV2 operations.
- Classic Projects (the older Projects) often require a numeric `project_id` from the REST API or a GraphQL node id depending on the action. If a workflow expects `PROJECT_ID` and you only have a project number, use the GraphQL query above to obtain the node id and supply it.

Linking the Resonance project

You also mentioned @Elidorascodex's Resonance project. If that is a separate GitHub Project, add its URL here and I can help record the `PROJECT_NUMBER`/`PROJECT_ID` for it as well.

Want me to write the id into repo metadata?

If you'd like, I can add the `PROJECT_NUMBER: 6` and the discovered GraphQL `PROJECT_ID` into a small `.github/project-ids.yml` file so CI/workflows can reference it. Say the word and I'll fetch the GraphQL id (if you give me a token) or guide you to run the single `gh` command above and paste the result here for me to commit.
