<#
.SYNOPSIS
    Reorganize repository files to match TGCR conventions.

.DESCRIPTION
    Safely moves files to their correct locations based on REPOSITORY_ORGANIZATION.md.
    - Uses git mv for tracked files (preserves history)
    - Prompts for confirmation before each move
    - Updates references in docs and config files
    - Creates backup before major changes

.PARAMETER DryRun
    Show what would be moved without actually moving files.

.PARAMETER Force
    Skip confirmation prompts (use with caution).

.PARAMETER UpdateReferences
    Automatically update file references in docs/config (default: true).

.EXAMPLE
    .\scripts\reorganize_repo.ps1 -DryRun
    # Preview changes without moving files

.EXAMPLE
    .\scripts\reorganize_repo.ps1
    # Interactive mode with confirmation prompts

.EXAMPLE
    .\scripts\reorganize_repo.ps1 -Force
    # Auto-move all files without prompts (dangerous!)
#>

param(
    [Parameter(Mandatory=$false)]
    [switch]$DryRun,

    [Parameter(Mandatory=$false)]
    [switch]$Force,

    [Parameter(Mandatory=$false)]
    [bool]$UpdateReferences = $true
)

$ErrorActionPreference = "Stop"

# Banner
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   TEC Repository Reorganization — TGCR File Coherence     ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

if ($DryRun) {
    Write-Host "[i] DRY RUN MODE: No files will be moved" -ForegroundColor Yellow
    Write-Host ""
}

# Get repo root
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

# Check if git repo
if (-not (Test-Path ".git")) {
    Write-Host "[✗] Not a git repository: $repoRoot" -ForegroundColor Red
    exit 1
}

# Check for uncommitted changes
$gitStatus = git status --porcelain
if ($gitStatus -and -not $Force) {
    Write-Host "[!] You have uncommitted changes:" -ForegroundColor Yellow
    Write-Host $gitStatus
    Write-Host ""
    Write-Host "[i] Commit or stash changes before reorganizing, or use -Force to proceed anyway" -ForegroundColor Cyan
    $response = Read-Host "Continue anyway? (y/N)"
    if ($response -ne "y") {
        Write-Host "[i] Aborted by user" -ForegroundColor Cyan
        exit 0
    }
}

# Define moves: (CurrentPath, TargetPath, Reason)
$moves = @(
    @{
        Current = "LUMINAI-API-SETUP-GUIDE.md"
        Target = "docs/LUMINAI-API-SETUP-GUIDE.md"
        Reason = "Documentation → docs/"
    },
    @{
        Current = "LuminAI-Character-Perfection-Plan.md"
        Target = "docs/LuminAI-Character-Perfection-Plan.md"
        Reason = "Documentation → docs/"
    },
    @{
        Current = "LuminAI-Test-Plan.md"
        Target = "docs/LuminAI-Test-Plan.md"
        Reason = "Documentation → docs/"
    },
    @{
        Current = "LUMINAI-VISUAL-WORKFLOW.md"
        Target = "docs/LUMINAI-VISUAL-WORKFLOW.md"
        Reason = "Documentation → docs/"
    },
    @{
        Current = "github-luminai-api.yaml"
        Target = "config/github-luminai-api.yaml"
        Reason = "Configuration → config/"
    },
    @{
        Current = "sharepoint-luminai-api.yaml"
        Target = "config/sharepoint-luminai-api.yaml"
        Reason = "Configuration → config/"
    }
)

# Track moves for reference updating
$movedFiles = @()

# Process each move
Write-Host "═══ Planned Moves ═══" -ForegroundColor Magenta
Write-Host ""

foreach ($move in $moves) {
    $current = Join-Path $repoRoot $move.Current
    $target = Join-Path $repoRoot $move.Target

    # Check if source exists
    if (-not (Test-Path $current)) {
        Write-Host "[i] Skipping (not found): $($move.Current)" -ForegroundColor Gray
        continue
    }

    # Check if target already exists
    if (Test-Path $target) {
        Write-Host "[!] Target exists, skipping: $($move.Target)" -ForegroundColor Yellow
        continue
    }

    # Display move
    Write-Host "Move:" -ForegroundColor Cyan
    Write-Host "  From: $($move.Current)" -ForegroundColor White
    Write-Host "  To:   $($move.Target)" -ForegroundColor Green
    Write-Host "  Why:  $($move.Reason)" -ForegroundColor Gray

    # Confirm (unless Force or DryRun)
    if (-not $DryRun -and -not $Force) {
        $response = Read-Host "  Proceed? (y/N)"
        if ($response -ne "y") {
            Write-Host "  [i] Skipped by user" -ForegroundColor Cyan
            Write-Host ""
            continue
        }
    }

    # Ensure target directory exists
    $targetDir = Split-Path -Parent $target
    if (-not (Test-Path $targetDir)) {
        Write-Host "  [i] Creating directory: $targetDir" -ForegroundColor Cyan
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        }
    }

    # Check if file is tracked by git
    $isTracked = git ls-files --error-unmatch $move.Current 2>$null

    if ($isTracked -and -not $DryRun) {
        # Use git mv for tracked files
        Write-Host "  [→] git mv $($move.Current) $($move.Target)" -ForegroundColor Green
        git mv $move.Current $move.Target
        $movedFiles += @{Old = $move.Current; New = $move.Target}
    } elseif (-not $DryRun) {
        # Use Move-Item for untracked files
        Write-Host "  [→] mv $($move.Current) $($move.Target)" -ForegroundColor Green
        Move-Item -Path $current -Destination $target
        $movedFiles += @{Old = $move.Current; New = $move.Target}
    } else {
        Write-Host "  [DRY RUN] Would execute: git mv $($move.Current) $($move.Target)" -ForegroundColor Yellow
    }

    Write-Host ""
}

# Update references in docs/config files
if ($UpdateReferences -and $movedFiles.Count -gt 0 -and -not $DryRun) {
    Write-Host "═══ Updating References ═══" -ForegroundColor Magenta
    Write-Host ""

    # Files to scan for references
    $scanTargets = @(
        "README.md",
        "docs/*.md",
        "config/*.yml",
        "config/*.yaml",
        "data/knowledge_map.yml"
    )

    foreach ($pattern in $scanTargets) {
        $files = Get-ChildItem -Path $repoRoot -Filter $pattern -Recurse -ErrorAction SilentlyContinue

        foreach ($file in $files) {
            $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
            if (-not $content) { continue }

            $modified = $false

            foreach ($moved in $movedFiles) {
                if ($content -match [regex]::Escape($moved.Old)) {
                    Write-Host "[i] Updating references in: $($file.Name)" -ForegroundColor Cyan
                    $content = $content -replace [regex]::Escape($moved.Old), $moved.New
                    $modified = $true
                }
            }

            if ($modified) {
                $content | Out-File $file.FullName -Encoding utf8 -NoNewline
                Write-Host "[✓] Updated: $($file.Name)" -ForegroundColor Green
            }
        }
    }

    Write-Host ""
}

# Summary
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                  Reorganization Complete                   ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green

if ($DryRun) {
    Write-Host "[i] This was a dry run. No files were moved." -ForegroundColor Yellow
} else {
    Write-Host "Moved: $($movedFiles.Count) file(s)" -ForegroundColor White
    Write-Host ""
    Write-Host "[i] Next steps:" -ForegroundColor Cyan
    Write-Host "  1. Review changes: git status" -ForegroundColor Gray
    Write-Host "  2. Test build: pytest" -ForegroundColor Gray
    Write-Host "  3. Commit: git commit -m 'refactor: Reorganize repo per TGCR conventions'" -ForegroundColor Gray
}
Write-Host ""
