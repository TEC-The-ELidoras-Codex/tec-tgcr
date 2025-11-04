# Project Automations Guide

Quick reference for maintainers on how to trigger project automations and common workflows.

---

## Workflow Triggers (What Causes Actions)

### 1. **Issue Created → Auto-Added to Project**

When you create a new issue, it's automatically added to the **Backlog** column if:
- Issue contains a link to another issue or external URL
- `PROJECTS_TOKEN` is configured and not expired

**Example**: Create issue with body containing:
```
Related: #42
Blocked by: tec-tgcr#123
Reference: https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/issues/100
```

### 2. **PR Referenced → Auto-Added to Project**

When you create or edit a PR with issue links, the PR is added to **In Progress**.

**Example PR body**:
```markdown
## Summary
Implements resonance scoring engine for March 2026 MVP.

## Related Issues
Closes #42
Blocks #45

## Acceptance Tests
- [ ] φᵗ/ψʳ/Φᴱ scores computed correctly
- [ ] Circadian window bonus (+2) applied when 4:20 PM
- [ ] All tests passing
```

### 3. **Issue Closed → Auto-Move to Done**

When an issue is closed, it automatically moves to the **Done** column (no action needed).

### 4. **PR Merged → Auto-Move to Done**

When a PR is merged, linked issues move to **Done**.

---

## Manual Workflow Triggers

### Move Item to Ready

When backlog items are groomed:

```bash
# Via GitHub CLI
gh project item-add \
  --project=6 \
  --owner=TEC-The-ELidoras-Codex \
  --issue=123 \
  --status="Ready"
```

Or use GitHub UI: Project board → Backlog → item → Move to Ready

### Move Item to Blocked

When a dependency is discovered:

1. Add comment to issue:
```markdown
@LuminAI Blocked by #999 (waiting on API implementation)
```

2. Move item in project UI to **Blocked** column

3. Reference blocker in the item's status field

### Create Epic / Group Related Items

Use labels to group related work:

```bash
# Tag related issues
gh issue edit 123 --add-label="epic/music-platform"
gh issue edit 124 --add-label="epic/music-platform"
gh issue edit 125 --add-label="epic/music-platform"

# Filter in project: filter by label epic/music-platform
```

---

## Common Maintenance Tasks

### Weekly Triage Checklist

```bash
# 1. List all Backlog items (unprioritized)
gh issue list \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --state=open \
  --label="P0,P1,P2" \
  --jq='.[].number' \
  | wc -l

# 2. List all Blocked items
gh issue list \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --state=open \
  --label="status/blocked"

# 3. Check if any P0s need immediate action
gh issue list \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --state=open \
  --label="P0" \
  --assignee=""  # unassigned P0s
```

### Rotating Token

```bash
# 1. Generate new PAT at https://github.com/settings/tokens?type=beta

# 2. Update repository secret
gh secret set PROJECTS_TOKEN \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --body="[paste new token here]"

# 3. Verify by running test workflow
gh workflow run project-add-on-reference.yml \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr

# 4. Update PROJECT_METADATA.md with new expiry
# Commit & push
```

### Debugging Workflow Failures

```bash
# 1. Check workflow run logs
gh workflow view project-add-on-reference.yml \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --json=runs | head -20

# 2. Get latest run details
gh run list \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --workflow=project-add-on-reference.yml \
  --limit=1 \
  --json=number,status,conclusion

# 3. View full logs
gh run view 12345 --log \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr

# Common issues:
# - 403 Forbidden: Token expired or lacks 'project' scope
# - Item not found: Issue/PR number incorrect or repo permission issue
# - Project not found: PROJECT_NUMBER is wrong or org token needed
```

---

## Custom Workflow Examples

### Example 1: Add Issue to Project with Custom Fields

```yaml
name: Add to Project with Priority

on:
  issues:
    types: [opened, labeled]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    if: |
      contains(github.event.issue.labels.*.name, 'P0') ||
      contains(github.event.issue.labels.*.name, 'P1')
    steps:
      - name: Add high-priority issue to project
        uses: actions/add-to-project@v0.5.1
        with:
          project-url: https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
          github-token: ${{ secrets.PROJECTS_TOKEN }}
```

### Example 2: Auto-Set Status Based on Labels

```yaml
name: Auto-Status from Labels

on:
  issues:
    types: [labeled]

jobs:
  set-status:
    runs-on: ubuntu-latest
    steps:
      - name: Move to Ready if ready label added
        if: github.event.label.name == 'status/ready'
        uses: actions/update-project-item@v1
        with:
          project-url: https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
          github-token: ${{ secrets.PROJECTS_TOKEN }}
          status: Ready

      - name: Move to Blocked if blocked label added
        if: github.event.label.name == 'status/blocked'
        uses: actions/update-project-item@v1
        with:
          project-url: https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6
          github-token: ${{ secrets.PROJECTS_TOKEN }}
          status: Blocked
```

### Example 3: Notify on P0 Issues

```yaml
name: Alert on P0

on:
  issues:
    types: [opened, labeled]

jobs:
  notify:
    runs-on: ubuntu-latest
    if: contains(github.event.issue.labels.*.name, 'P0')
    steps:
      - name: Post to Slack
        uses: slackapi/slack-github-action@v1
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK }}
          payload: |
            text: "🚨 P0 Issue: ${{ github.event.issue.title }}"
            blocks:
              - type: "section"
                text:
                  type: "mrkdwn"
                  text: "*P0 Issue Created*\n${{ github.event.issue.html_url }}"
```

---

## Release Coordination (March 2026 MVP)

### Pre-Release Checklist (2 Weeks Before)

```bash
# 1. Verify all MVP items are in Ready or In Progress
gh issue list \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --milestone="Stable / MVP (March 6, 2026)" \
  --state=open

# 2. Flag any Blocked items
gh issue list \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --milestone="Stable / MVP (March 6, 2026)" \
  --label="status/blocked"

# 3. Move non-MVP work to next milestone (Beta or future)
```

### Release Day (March 6, 2026)

```bash
# 1. Close all MVP milestone issues with merged PRs
# 2. Verify Done column shows all MVP items
# 3. Generate release notes from completed issues
gh release create v1.0.0 \
  --repo=TEC-The-ELidoras-Codex/tec-tgcr \
  --title="FOLD MVP: March 6, 2026" \
  --generate-notes

# 4. Archive completed project items (create "Archive" column or script)
```

---

## Quick Links

- **GitHub CLI Docs**: https://cli.github.com/manual/gh_issue
- **GitHub Actions API**: https://docs.github.com/actions/learn-github-actions
- **Project GraphQL**: https://docs.github.com/graphql/reference/objects#projectv2
- **Repository Secrets**: https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/settings/secrets/actions

---

**Last Updated**: Nov 4, 2025  
**Status**: Ready to use  
**Audience**: Maintainers (@LuminAI, @Airth, @Ely, @Kaznak)
