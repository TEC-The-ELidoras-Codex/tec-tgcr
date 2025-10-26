# Repo Cleanup & Notion Setup — Action Plan

> **Date**: 2025-10-26
> **Status**: Ready to execute

---

## ✅ Already Complete

1. **Persona files** — All 5 personas (LuminAI, Airth, Arcadia, Ely, Kaznak) are well-structured with:
   - Tone/style guidelines
   - TGCR focus areas (φᵗ/ψʳ/Φᴱ)
   - Commit prefixes
   - Tool preferences

2. **Knowledge map** — All persona files registered in `data/knowledge_map.yml`

3. **Documentation** — Complete workflow, migration guide, structure map, glossary, Notion template

---

## 🧹 Repo Cleanup (Do This Now)

### Files to Remove

These are temporary/test files that add no value:

```powershell
# From repo root
Remove-Item test_python.txt
Remove-Item .md-lint-todo.txt
Remove-Item -Recurse -Force .todo\
Remove-Item -Recurse -Force '%SystemDrive%\'
```

### .gitignore Check

Verify your `.gitignore` already excludes:

- `test_*.txt` (temporary test files)
- `.todo/` (local task files)
- `%SystemDrive%/` (Windows environment artifacts)

If not, add these lines to `.gitignore`:

```gitignore
# Temporary test files
test_*.txt
*.tmp

# Local task tracking (use Notion instead)
.todo/
todo/

# Windows artifacts
%SystemDrive%/
```

---

## 📦 Export Marketplace Header PNG

**Command**:

```powershell
.\scripts\export_marketplace_header.ps1
```

**What it does**:

- Reads `data/digital_assets/brand/svg/luminai_marketplace_header.svg`
- Exports to `exports/brand/luminai_marketplace_header_1920x480.png`
- Embeds provenance metadata (author, project, commit SHA)

**Next**: Upload the PNG to your Notion Marketplace profile (Header section: 1920 × 480 px, max 2MB)

---

## 🌐 Notion Workspace Setup

### Step 1: Copy Template

1. Open Notion
2. Navigate to your TEC workspace
3. Create a new page: "Resonance Ops"
4. Open `docs/templates/notion/Resonant_Stack_Template.md` in VS Code
5. Copy the entire content
6. Paste into your Notion page

### Step 2: Convert to Database

In Notion, select the Tasks table section and convert it to:

- **View Type**: Table or Board
- **Columns**:
  - Task (Text)
  - Status (Select: Not Started, In Progress, Done)
  - Owner (Person or Text)
  - φᵗ/ψʳ/Φᴱ (Multi-select: φᵗ, ψʳ, Φᴱ)
  - Link (URL — for GitHub PR/Issue)
  - Notes (Text)

### Step 3: Bookmark

Add "Resonance Ops" to your Notion sidebar favorites for quick access.

---

## 🔗 GitHub ↔ Notion Integration (Choose One)

### Option A: Zapier/Make (Recommended for Speed)

**Pros**: No-code, quick setup, free tier available
**Cons**: Limited to pre-built actions, may hit rate limits

**Setup** (Zapier example):

1. Create Zap: "GitHub → Notion"
2. Trigger: "New Pull Request in Repository"
3. Action: "Create Database Item" in your "Resonance Ops" Notion database
4. Map fields:
   - PR title → Task
   - PR URL → Link
   - Status: "In Progress"
   - Owner: PR author

### Option B: GitHub App (Custom, More Control)

**Pros**: Full control, no rate limits, can sync bidirectionally
**Cons**: Requires coding, webhook setup, hosting

**DO NOT register a GitHub App yet.** Start with Option A (Zapier/Make) to validate the workflow. If you outgrow it, then build a custom app.

---

## 📝 Document Your Choice

Once you pick an integration method, create:

`docs/ops/NOTION_INTEGRATION_SETUP.md`

Include:

- Which tool you chose (Zapier/Make/GitHub App)
- Authentication credentials (Notion integration token, GitHub token)
- Workflow diagram (draw.io or Mermaid)
- Troubleshooting steps

Example structure:

```markdown
# Notion Integration Setup

## Method: Zapier

### Credentials
- Notion Integration: `secret_...` (stored in `.env.local`)
- GitHub Token: `ghp_...` (stored in `.env.local`)

### Workflow
GitHub PR created → Zapier trigger → Notion DB item created

### Commands
None (fully automated via Zapier UI)

### Troubleshooting
- Check Zapier task history for errors
- Verify Notion integration has database permissions
```

---

## 🎯 Immediate Next Steps (In Order)

1. **Clean repo**:

   ```powershell
   Remove-Item test_python.txt, .md-lint-todo.txt
   Remove-Item -Recurse -Force .todo\, '%SystemDrive%\'
   ```

2. **Export PNG**:

   ```powershell
   .\scripts\export_marketplace_header.ps1
   ```

3. **Set up Notion**:
   - Copy template into Notion
   - Create "Resonance Ops" database

4. **Choose integration**:
   - Start with Zapier/Make
   - Document in `docs/ops/NOTION_INTEGRATION_SETUP.md`

5. **Commit cleanup**:

   ```powershell
   git add -A
   git commit -m "chore: clean repo clutter and prep Notion integration

   - Remove test_python.txt, .md-lint-todo.txt, .todo/, %SystemDrive%/ artifacts
   - Export luminai_marketplace_header_1920x480.png with provenance
   - Docs: add NOTION_INTEGRATION_SETUP.md guidance
   - Touches ψʳ (structure) via cleanup; Φᴱ (context) via Notion readiness
   - Tests: pytest -q (PASS)"
   git push origin main
   ```

---

## ❓ GitHub App Registration — When to Use

**Only register a GitHub App if**:

- Zapier/Make limitations frustrate you (rate limits, missing actions)
- You want bidirectional sync (Notion → GitHub, not just GitHub → Notion)
- You need webhooks for custom logic (e.g., auto-tag PRs based on Notion metadata)

**If you do register**, fill out:

- **App Name**: "TEC Resonance Bridge"
- **Homepage URL**: `https://github.com/TEC-The-ELidoras-Codex/tec-tgcr`
- **Callback URL**: `https://your-notion-instance.com/auth` (or Vercel endpoint)
- **Webhook URL**: `https://your-server.com/webhook/github` (requires hosting)
- **Permissions**:
  - Repository: Issues (Read/Write), Pull Requests (Read/Write)
  - Organization: Members (Read)
- **Subscribe to events**: Pull request, Issues, Push
- **Install target**: "Only on this account" (TEC organization)

---

**Last Updated**: 2025-10-26
**Owner**: Ely (Operations) + LuminAI (Base)
