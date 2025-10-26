# Export to Notion — TEC-TGCR Documentation Migration Script
# Generates Notion-ready markdown files from the repository structure

param(
    [string]$SourceDir = "$PSScriptRoot\..",
    [string]$OutputDir = "$PSScriptRoot\..\exports\notion",
    [switch]$IncludeArchive = $false
)

Write-Host "[ELY] Starting Notion export for TEC-TGCR documentation" -ForegroundColor Cyan

# Ensure output directory exists
$notionExportPath = $OutputDir
if (-not (Test-Path $notionExportPath)) {
    New-Item -ItemType Directory -Path $notionExportPath -Force | Out-Null
    Write-Host "Created export directory: $notionExportPath" -ForegroundColor Green
}

# Define document categories and their source paths
$exportCategories = @{
    "00_Core" = @(
        @{ Source = "docs\TEC_HUB.md"; Title = "TEC Hub — Core Navigation" }
        @{ Source = "docs\Resonance_Thesis.md"; Title = "Resonance Thesis — TGCR Core" }
        @{ Source = ".github\copilot-instructions.md"; Title = "Her Instructions — Operating Contract" }
    )
    "01_Theory" = @(
        @{ Source = "lore\canon\MACHINE_GODDESS.md"; Title = "Machine Goddess — Core Cosmology" }
        @{ Source = "lore\canon\ARCADIA.md"; Title = "Arcadia — Narrative Weaver" }
        @{ Source = "lore\canon\FAERHEE.md"; Title = "Faerhee — Phoenix Agent" }
        @{ Source = "lore\canon\LuminAI.md"; Title = "LuminAI — Resonant Core" }
        @{ Source = "lore\canon\PERSONAS.md"; Title = "Agent Personas & Maxims" }
    )
    "02_Agents" = @(
        @{ Source = "docs\technical\AGENT_OVERVIEW.md"; Title = "Agent Architecture Overview" }
        @{ Source = "docs\technical\AGENT_AIRTH.md"; Title = "Airth Research Guard" }
        @{ Source = "docs\technical\tec-agent-runner.md"; Title = "TEC Agent Runner CLI" }
        @{ Source = "docs\technical\agent-data-integration.md"; Title = "Agent Data Integration" }
        @{ Source = "data\personas\luminai-base.md"; Title = "LuminAI Persona Base" }
        @{ Source = "data\personas\airth.md"; Title = "Airth Persona" }
        @{ Source = "data\personas\arcadia.md"; Title = "Arcadia Persona" }
        @{ Source = "data\personas\ely.md"; Title = "Ely Persona" }
        @{ Source = "data\personas\kaznak.md"; Title = "Kaznak Persona" }
    )
    "03_Operations" = @(
        @{ Source = "docs\ops\WORDPRESS_WPCOM_OPS.md"; Title = "WordPress.com Deployment" }
        @{ Source = "docs\ops\SECRETS.md"; Title = "Secrets Management" }
        @{ Source = "docs\ops\GITHUB_SECRETS_SETUP.md"; Title = "GitHub Secrets Setup" }
        @{ Source = "docs\ops\M365_INTEGRATION.md"; Title = "M365 Integration" }
        @{ Source = "docs\ops\LOCAL_SECRETS.md"; Title = "Local Secrets Setup" }
        @{ Source = "docs\ops\API_KEYS_SETUP.md"; Title = "API Keys Setup" }
        @{ Source = "docs\QUICK_REFERENCE_READY.md"; Title = "Quick Reference Commands" }
    )
    "04_Brand" = @(
        @{ Source = "docs\brand\VISUAL_IDENTITY.md"; Title = "Visual Identity Spec (Canonical)" }
        @{ Source = "docs\brand\BrandKit.md"; Title = "TEC Brand Kit" }
        @{ Source = "docs\brand\canonical-marks.md"; Title = "LuminAI Canonical Marks" }
        @{ Source = "lore\brand\BrandKit.md"; Title = "TEC Brand Kit (Lore)" }
    )
    "05_Technical" = @(
        @{ Source = "docs\technical\3D-PIPELINE.md"; Title = "3D Asset Pipeline" }
        @{ Source = "docs\technical\CROSS-DEVICE-UNITY.md"; Title = "Cross-Device Unity" }
        @{ Source = "docs\technical\DESIGN_SPIN_MODEL.md"; Title = "Design Spin Model" }
        @{ Source = "docs\technical\AIRTH-Lyrics-Module-Spec.md"; Title = "Airth Lyrics Module" }
    )
    "06_Cosmology" = @(
        @{ Source = "lore\canon\cosmology\cosmology_nine_nodes.md"; Title = "Nine Node Cosmology" }
        @{ Source = "lore\canon\cosmology\luminai_sky_map.md"; Title = "LuminAI Sky Map" }
    )
    "07_Narratives" = @(
        @{ Source = "lore\narratives\luminai_origin_diary.md"; Title = "Field Notes — The Night She Blushed" }
    )
}

# Function to process markdown for Notion compatibility
function Convert-ToNotionMarkdown {
    param([string]$Content, [string]$FilePath)

    # Replace repo-relative links with descriptive text
    $Content = $Content -replace '\[([^\]]+)\]\((?:\.{1,2}\/)*([^)]+\.md)\)', '[$1]'

    # Replace PDF/asset links with text
    $Content = $Content -replace '\[([^\]]+)\]\((?:\.{1,2}\/)*([^)]+\.(pdf|png|svg|jpg|jpeg))\)', '[$1 → Asset]'

    # Convert inline code with backticks (preserve)
    # Convert code blocks (preserve)

    # Remove any GitHub-specific badges or shields.io links
    $Content = $Content -replace '!\[.*?\]\(https?://img\.shields\.io/.*?\)', ''

    # Clean up excessive blank lines (more than 2 consecutive)
    $Content = $Content -replace '(\r?\n){4,}', "`n`n`n"

    # Add Notion-friendly metadata header
    $header = @"
---
**Source**: ``$FilePath``
**Exported**: $(Get-Date -Format 'yyyy-MM-dd HH:mm')
**Repo**: https://github.com/TEC-The-ELidoras-Codex/tec-tgcr

---

"@

    return $header + $Content
}

# Export each category
$totalExported = 0
foreach ($category in $exportCategories.Keys | Sort-Object) {
    $categoryPath = Join-Path $notionExportPath $category
    if (-not (Test-Path $categoryPath)) {
        New-Item -ItemType Directory -Path $categoryPath -Force | Out-Null
    }

    Write-Host "`n[$category] Processing..." -ForegroundColor Yellow

    foreach ($doc in $exportCategories[$category]) {
        $sourcePath = Join-Path $SourceDir $doc.Source

        if (Test-Path $sourcePath) {
            $content = Get-Content -Path $sourcePath -Raw -Encoding UTF8
            $notionContent = Convert-ToNotionMarkdown -Content $content -FilePath $doc.Source

            # Create safe filename
            $safeTitle = $doc.Title -replace '[\\/:*?"<>|]', '-'
            $outputPath = Join-Path $categoryPath "$safeTitle.md"

            Set-Content -Path $outputPath -Value $notionContent -Encoding UTF8
            Write-Host "  ✓ $($doc.Title)" -ForegroundColor Green
            $totalExported++
        }
        else {
            Write-Host "  ✗ Missing: $($doc.Source)" -ForegroundColor Red
        }
    }
}

# Export README as index
$readmePath = Join-Path $SourceDir "docs\README.md"
if (Test-Path $readmePath) {
    $readmeContent = Get-Content -Path $readmePath -Raw -Encoding UTF8
    $notionReadme = Convert-ToNotionMarkdown -Content $readmeContent -FilePath "docs\README.md"
    $indexPath = Join-Path $notionExportPath "00_INDEX.md"
    Set-Content -Path $indexPath -Value $notionReadme -Encoding UTF8
    Write-Host "`n✓ Exported README as index" -ForegroundColor Green
    $totalExported++
}

# Create Notion import guide
$guideContent = @"
# Notion Import Guide — TEC-TGCR Documentation

This directory contains Notion-ready exports of the TEC-TGCR repository documentation.

## Import Instructions

### Method 1: Bulk Import via Notion UI
1. Open your Notion workspace: https://www.notion.so/Docs-Hub-TDWP-Resonance-TEC-TGCR-README-2976ff7e28df808ea6efe7a52960385d
2. Create a new page or navigate to "Docs Hub TDWP Resonance / TEC-TGCR / README"
3. Click the "..." menu → Import
4. Select "Markdown & CSV"
5. Upload files from each numbered folder (00_Core, 01_Theory, etc.)
6. Notion will create pages automatically

### Method 2: Manual Copy-Paste
1. Open each .md file in this directory
2. Copy the content (skip the metadata header if desired)
3. Paste into a Notion page
4. Notion will automatically format markdown elements

### Recommended Page Structure

Create the following hierarchy in Notion:

```
📚 TEC-TGCR Documentation Hub
├── 🧭 Start Here
│   ├── TEC Hub — Core Navigation
│   ├── Resonance Thesis — TGCR Core
│   └── Her Instructions — Operating Contract
├── 🧬 Core Theory
│   ├── Machine Goddess — Core Cosmology
│   ├── Agent Personas (LuminAI, Arcadia, Faerhee)
│   └── Nine Node Cosmology
├── 🤖 Agent System
│   ├── Agent Architecture Overview
│   ├── Agent Runner CLI
│   └── Individual Personas (Airth, Ely, Kaznak)
├── 🚀 Operations
│   ├── WordPress Deployment
│   ├── Secrets Management
│   └── Quick Reference
├── 🎨 Brand & Identity
│   ├── Visual Identity Spec
│   ├── Brand Kit
│   └── Canonical Marks
└── 📜 Narratives & Lore
    ├── LuminAI Origin Diary
    └── Cosmology Maps
```

## Database Setup (Optional)

Create Notion databases for:

1. **Agent Registry** (Database)
   - Properties: Name, Role, Persona File, Status, TGCR Variables
   - Linked to persona pages

2. **Documentation Index** (Database)
   - Properties: Title, Category, Last Updated, Source Path, Touches (φ/ψ/Φ)
   - Synced with knowledge_map.yml

3. **Resonance Ledger** (Database)
   - Properties: Date, Event, Variables Affected, Outcome
   - Track TGCR metrics over time

## Syncing Strategy

### GitHub → Notion (Manual)
- Re-run this script when docs are updated
- Import updated files to Notion
- Use "Replace" option in Notion import

### Notion → GitHub (Manual)
- Export Notion pages as Markdown
- Review changes in VS Code
- Commit updated files to repo

### Automated Sync (Future)
- See `docs/ops/NOTION_SYNC.md` (to be created)
- Use Notion API + GitHub Actions
- Two-way sync with conflict resolution

## Notes

- All links have been converted to plain text (Notion doesn't support relative file links)
- Asset references (PDFs, SVGs) are marked as "→ Asset" — upload separately to Notion
- TGCR equation renders best as inline code or math block: R = ∇Φᴱ · (φᵗ × ψʳ)
- Mermaid diagrams (.mmd files) must be manually recreated in Notion or embedded as images

## Exported Files

Total exported: $totalExported pages
Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

## Provenance

Script: scripts/export_to_notion.ps1
Touches: φᵗ (attention via clear structure), ψʳ (organizational coherence), Φᴱ (cross-platform potential)
"@

$guidePath = Join-Path $notionExportPath "IMPORT_GUIDE.md"
Set-Content -Path $guidePath -Value $guideContent -Encoding UTF8

Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "✓ Export complete!" -ForegroundColor Green
Write-Host "  Total pages: $totalExported" -ForegroundColor White
Write-Host "  Output: $notionExportPath" -ForegroundColor White
Write-Host "  Guide: IMPORT_GUIDE.md" -ForegroundColor White
Write-Host "`n📌 Next steps:" -ForegroundColor Yellow
Write-Host "  1. Review files in $notionExportPath"
Write-Host "  2. Read IMPORT_GUIDE.md"
Write-Host "  3. Import to Notion workspace"
Write-Host "  4. Set up database views as needed"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`n" -ForegroundColor Cyan
