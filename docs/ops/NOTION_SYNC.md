# Notion ↔ GitHub Sync Documentation

**Status**: Manual workflow established; automated sync planned for Phase 2

This document describes how to maintain synchronization between the TEC-TGCR GitHub repository and the Notion workspace.

---

## 🎯 Sync Philosophy

**GitHub = Source of Truth for:**

- Code (Python, JavaScript, scripts)
- Technical documentation (agent specs, ops guides)
- Configuration files (YAML, JSON, .env templates)
- Asset source files (SVGs, 3D models)

**Notion = Source of Truth for:**

- Team collaboration notes
- Meeting minutes and action items
- Draft narratives and brainstorming
- Visual dashboards and database views

**Bidirectional (Both Valid):**

- Strategy documents (decision logs, roadmaps)
- Resonance Ledger entries
- Brand guidelines (when collaborating with designers)

---

## 📤 GitHub → Notion (Export Workflow)

### Manual Export (Current)

**When to Sync:**

- After significant doc updates (daily or per-commit basis)
- Before team review sessions
- When releasing new features or agents
- Weekly maintenance sync

**Steps:**

1. **Run Export Script**

   ```powershell
   cd "c:\Users\Ghedd\OneDrive - TEC - The Elidoras Codex\Projects\TEC\tec-tgcr"
   pwsh scripts\export_to_notion.ps1
   ```

2. **Review Exported Files**
   - Navigate to `exports\notion\`
   - Verify content, especially TGCR equation and code blocks
   - Check for broken internal links (should be converted to plain text)

3. **Import to Notion**
   - Open [Docs Hub](https://www.notion.so/Docs-Hub-TDWP-Resonance-TEC-TGCR-README-2976ff7e28df808ea6efe7a52960385d)
   - Navigate to the relevant section (Core, Theory, Agents, etc.)
   - Click "..." menu → Import → Markdown & CSV
   - Select files from the appropriate folder
   - Choose "Replace" mode if updating existing pages
   - Notion will preserve page IDs and database links

4. **Update Documentation Index**
   - Open Documentation Index database in Notion
   - Update "Last Synced" date for imported pages
   - Change Status from "Outdated" to "Current"

5. **Verify Links and Formatting**
   - Check that key pages link correctly
   - Ensure TGCR equation displays properly
   - Verify embedded assets (images, PDFs) render
   - Update any broken `@mentions` to Notion pages

**Time Estimate**: 10-15 minutes for full sync, 3-5 minutes for single-page update

### Automated Export (Planned — Phase 2)

**GitHub Actions Workflow**: `.github/workflows/notion-sync.yml`

**Trigger**: On push to `docs/**`, `lore/**`, `data/personas/**`, or manual dispatch

**Process**:

1. Run `export_to_notion.ps1` in CI environment
2. Use Notion API to update pages programmatically
3. Match GitHub file paths to Notion page IDs (via Documentation Index database)
4. Update "Last Synced" metadata
5. Post summary to Slack/Discord (optional)

**Implementation Requirements**:

- Notion Integration token stored in GitHub Secrets (`NOTION_TOKEN`)
- Notion Database IDs configured in workflow
- Mapping file: `config/notion_page_map.yml` (maps GitHub paths → Notion page IDs)

**Status**: Not implemented; see `docs/ops/NOTION_SYNC_AUTOMATION.md` (to be created)

---

## 📥 Notion → GitHub (Import Workflow)

### Manual Import (Current)

**When to Sync:**

- Collaborative narrative drafts ready for version control
- Strategy decisions made in Notion (decision log updates)
- Resonance Ledger entries created during team sessions
- Brand updates from design team working in Notion

**Steps:**

1. **Export from Notion**
   - Select the page or database view
   - Click "..." menu → Export
   - Format: Markdown & CSV
   - Include subpages: Yes (if needed)
   - Download ZIP

2. **Extract and Review**
   - Extract ZIP to a temporary directory
   - Review markdown files in VS Code
   - Note: Notion exports may have non-standard formatting

3. **Clean Up Notion-Specific Formatting**
   - Remove Notion page IDs from links: `[Title](https://notion.so/Title-abc123)` → `[Title](./title.md)`
   - Convert Notion callouts to standard markdown blockquotes
   - Fix code block formatting (Notion sometimes adds extra backticks)
   - Remove Notion export metadata (footer timestamps)

4. **Place in Correct Repo Location**
   - Narratives → `lore/narratives/`
   - Strategy docs → `data/strategy/`
   - Agent specs → `docs/technical/` or `data/personas/`
   - Brand updates → `docs/brand/` or `lore/brand/`

5. **Update Knowledge Map**
   - Edit `data/knowledge_map.yml`
   - Add new entries under appropriate section
   - Update provenance note

6. **Commit with Provenance**

   ```powershell
   git add <files>
   git commit -m "docs(notion-import): <description>

   - Source: Notion page '<Page Title>'
   - Date: <export date>
   - Collaborators: <names>
   - Touches: <φᵗ/ψʳ/Φᴱ>
   - Provenance: Team collaboration via Notion workspace"
   ```

**Time Estimate**: 5-10 minutes per page

### Automated Import (Future — Phase 3)

**Notion Webhook → GitHub Actions**

**Trigger**: Notion sends webhook on page update (for select pages only)

**Process**:

1. Webhook receiver validates source
2. Fetch page content via Notion API
3. Convert Notion blocks to markdown
4. Create pull request with changes
5. Auto-assign reviewers (Airth for verification)

**Challenges**:

- Notion's markdown export is lossy (some formatting lost)
- Conflict resolution (what if GitHub version changed?)
- Security (validate webhook signatures)

**Status**: Not implemented; requires Notion Enterprise plan for webhooks

---

## 🔄 Bidirectional Sync Patterns

### Strategy Documents (Decision Log, Roadmaps)

**Pattern**: Notion as collaborative draft → GitHub as canonical version

1. Team edits Decision Log in Notion (live collaboration)
2. Weekly export to GitHub (manual or scheduled)
3. GitHub version tagged as "canonical"
4. Major decisions committed with full provenance

**Conflict Resolution**: GitHub wins; Notion can be re-imported if needed

### Resonance Ledger

**Pattern**: Dual entry (events can be added to either platform)

1. Code-related events: Add to GitHub, sync to Notion
2. Team events (meetings, experiments): Add to Notion, sync to GitHub monthly
3. Both platforms maintained with "Last Synced" metadata

**Conflict Resolution**: Merge entries; use timestamp as tiebreaker

### Brand Guidelines

**Pattern**: Design drafts in Notion → Finalized specs in GitHub

1. Designers work in Notion with rich media
2. Export finalized specs as markdown + assets
3. Commit to `docs/brand/` with asset files
4. GitHub becomes authoritative version
5. Notion page updated with "See GitHub for canonical version" note

---

## 🛠️ Tools & Scripts

### Export Script

**File**: `scripts/export_to_notion.ps1`

**Usage**:

```powershell
pwsh scripts\export_to_notion.ps1
pwsh scripts\export_to_notion.ps1 -IncludeArchive  # Include archived docs
```

**Output**: `exports/notion/` with categorized markdown files

**Customization**: Edit `$exportCategories` hashtable in script to add/remove docs

### Import Cleanup Script (To Be Created)

**File**: `scripts/import_from_notion.ps1`

**Planned Features**:

- Auto-detect Notion export format
- Clean up Notion-specific markdown
- Convert links to repo-relative paths
- Validate against markdownlint rules

### Notion API Helper (To Be Created)

**File**: `src/tec_tgcr/tools/notion_api.py`

**Planned Features**:

- Authenticate with Notion Integration token
- Fetch page content by ID
- Update pages programmatically
- Query databases (Documentation Index, Resonance Ledger)

---

## 📋 Sync Checklists

### Weekly Sync Checklist

- [ ] Run `export_to_notion.ps1`
- [ ] Import to Notion (replace mode)
- [ ] Update Documentation Index "Last Synced" dates
- [ ] Review Notion → GitHub imports (strategy docs, resonance ledger)
- [ ] Update knowledge map if new pages added
- [ ] Commit any changes with provenance note
- [ ] Verify TGCR equation renders correctly in Notion

### Pre-Release Sync Checklist

- [ ] Full export of all docs
- [ ] Fresh import to Notion (clean slate if major refactor)
- [ ] Update all database entries (Agent Registry, Doc Index)
- [ ] Create release notes page in Notion
- [ ] Link Notion release page to GitHub release
- [ ] Tag sync in git: `git tag notion-sync-YYYY-MM-DD`

### Monthly Audit Checklist

- [ ] Compare GitHub `docs/` with Notion Documentation Index
- [ ] Identify orphaned pages (in Notion but not in GitHub, or vice versa)
- [ ] Archive outdated Notion pages
- [ ] Update "Status" field in Documentation Index
- [ ] Run `git log --oneline --since="1 month ago" -- docs/ lore/` and verify Notion reflects changes

---

## 🚨 Conflict Scenarios & Resolutions

### Scenario 1: Same Page Edited on Both Platforms

**Symptoms**: GitHub has commits since last Notion import; Notion page also edited

**Resolution**:

1. Export Notion version as `page_notion.md`
2. Compare with GitHub version: `git diff docs/page.md page_notion.md`
3. Manually merge changes in VS Code (3-way merge if possible)
4. Commit merged version to GitHub
5. Re-export to Notion (GitHub version wins)

### Scenario 2: Page Deleted on GitHub, Still Exists in Notion

**Resolution**:

1. Archive Notion page (don't delete, for provenance)
2. Update Documentation Index: Status = "Archived"
3. Add note: "Removed from GitHub on [date]; see commit [hash]"

### Scenario 3: Page Renamed on GitHub

**Resolution**:

1. Update Notion page title to match
2. Update "Source Path" in Documentation Index
3. Preserve Notion page ID (no need to recreate)
4. Update internal `@mentions` if linking changed

### Scenario 4: Large Restructure (e.g., `docs/` folder reorganized)

**Resolution**:

1. Create Notion restructure plan (new page hierarchy)
2. Bulk export GitHub docs with new structure
3. Archive old Notion pages
4. Import fresh structure
5. Update all database relations
6. Communicate change to team

---

## 📊 Sync Metrics (Optional Tracking)

Track these in Resonance Ledger or a dedicated "Sync Health" Notion page:

- **Sync Frequency**: Times per week GitHub → Notion sync run
- **Outdated Pages**: Number of pages with "Last Synced" > 30 days
- **Conflict Events**: Number of manual merge conflicts resolved
- **Automation Uptime**: % of automated syncs that succeed (when implemented)

---

## 🔐 Security & Access Control

### GitHub Secrets

Store in GitHub Secrets (Settings → Secrets and variables → Actions):

- `NOTION_TOKEN`: Notion Integration token (Internal Integration)
- `NOTION_DATABASE_IDS`: JSON object mapping database names to IDs

### Notion Permissions

**Integration Permissions**:

- Read content: Yes (for querying databases)
- Update content: Yes (for syncing pages)
- Insert content: Yes (for creating new pages)

**Team Access**:

- Docs Hub: Full access for core team
- Databases: Edit access for leads, view-only for contributors
- Sync logs: View-only for all

**Sensitive Content**:

- Do NOT sync secrets, API keys, or credentials to Notion
- Use separate "Private" section in Notion for team-only content (not synced to GitHub)

---

## 🗺️ Roadmap

### Phase 1: Manual Sync (Current)

- ✅ Export script created
- ✅ Import guide written
- ✅ Workflow documented
- 🔲 Team trained on manual sync process

### Phase 2: Semi-Automated (Q1 2026)

- GitHub Actions workflow for export
- Notion API integration (update pages programmatically)
- Slack notifications on sync
- Mapping file for GitHub paths → Notion page IDs

### Phase 3: Full Automation (Q2 2026)

- Bidirectional sync (Notion webhooks → GitHub PRs)
- Conflict detection and auto-merge (where safe)
- Dashboard showing sync health
- Version history integration (Notion <-> Git commits)

---

## 📌 Provenance

**Created**: 2025-10-25
**Last Updated**: 2025-10-25
**Maintained By**: Ely (Operations Agent)
**Source**: `docs/ops/NOTION_SYNC.md`

**TGCR Impact**:

- φᵗ: Reduces cognitive load by automating sync
- ψʳ: Maintains structural coherence across platforms
- Φᴱ: Enables team collaboration without sacrificing version control

**Related Docs**:

- `docs/ops/NOTION_WORKSPACE_SETUP.md` — Workspace structure
- `scripts/export_to_notion.ps1` — Export automation
- `data/knowledge_map.yml` — Knowledge registry

---

*"Information flows where structure allows." — Ely Maxim*
