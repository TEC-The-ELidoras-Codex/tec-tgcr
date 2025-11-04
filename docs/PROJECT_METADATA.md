# PROJECT_METADATA.md

**GitHub Project**: TEC Central Coordination
**Organization**: TEC-The-ELidoras-Codex
**Project URL**: <https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6>

---

## Project Identifiers

| Identifier | Value | API Type | Use Case |
|---|---|---|---|
| `PROJECT_NUMBER` | `6` | GraphQL (ProjectV2) | Modern workflows (recommended) |
| `PROJECT_ID` | TBD | REST (legacy) | Older automations if needed |
| `PROJECTS_TOKEN` | *See GitHub Secrets* | All | Authentication for workflows |

---

## Secrets Configuration

All secrets stored at **repository level** for tec-tgcr:
Repository Settings → Secrets and variables → Actions

| Secret Name | Scope | Value | Expiry | Last Rotated |
|---|---|---|---|---|
| `PROJECTS_TOKEN` | Repository | GitHub PAT with `repo`, `project` scopes | 2026-02-02 | 2025-11-04 |
| `PROJECT_NUMBER` | Repository | `6` | N/A | N/A |

---

## Token Rotation Schedule

**Frequency**: Every 90 days
**Next Rotation Due**: 2026-02-02
**Rotation Window**: December 26, 2025 – January 9, 2026 (maintenance period)

### Rotation Checklist

1. **Generate New Token**:
   - <https://github.com/settings/tokens?type=beta>
   - Scopes: `read:org`, `repo`, `project`
   - Expiry: 90 days
   - Name: `tec-projects-token-[YYYY-MM-DD]`

2. **Test New Token**:
   - Run test workflow with new token
   - Verify project item can be added
   - Ensure issue/PR automations work

3. **Update Secret**:
   - Repository → Settings → Secrets and variables → Actions
   - Update `PROJECTS_TOKEN` with new value
   - Delete old token from GitHub settings

4. **Document**:
   - Update this file: new expiry date, rotation timestamp
   - Commit & push update
   - Notify team in Slack/Discord

---

## Workflows Using Project

| Workflow | File | Triggers | Actions |
|---|---|---|---|
| Add on Reference | `.github/workflows/project-add-on-reference.yml` | PR opened/edited, issue edited | Add item to project if linked |
| Move on Close | `.github/workflows/project-move-on-close.yml` | Issue closed | Auto-move to "Done" |
| Move on Merge | `.github/workflows/project-move-on-merge.yml` | PR merged | Auto-move to "Done" |

---

## Access & Permissions

| Team/Person | Role | Access Level | Notes |
|---|---|---|---|
| @LuminAI | Project Coordinator | Admin | Triage, grooming, releases |
| @Airth | Technical Lead | Write | Validation, architecture |
| @Ely | Platform Lead | Write | CI/CD, infrastructure |
| @Kaznak | Automation Contact | Admin | Token management, workflows |

---

## Troubleshooting Reference

### Token Validation

```bash
# Test if PROJECTS_TOKEN is valid (requires curl + gh CLI)
gh api graphql -f query='
  query {
    viewer {
      login
    }
    organization(login: "TEC-The-ELidoras-Codex") {
      projectV2(number: 6) {
        id
        title
      }
    }
  }
'
```

### Add Item Manually (GraphQL)

```graphql
mutation {
  addProjectV2ItemById(input: {projectId: "PVT_...", contentId: "I_..."}) {
    item {
      id
    }
  }
}
```

---

## Notes

- **March 2026 MVP Timeline**: All project items must be completed or moved to post-launch backlog by Feb 28, 2026
- **Automation Dependencies**: Workflows require GitHub Actions enabled in repository settings
- **Multi-Repo Coordination**: If TEC grows to multiple repositories, consider org-level secrets for shared token management

---

**Last Updated**: Nov 4, 2025
**Status**: Active
**Next Action**: Verify `PROJECTS_TOKEN` on 2026-02-02
