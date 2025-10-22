# TEC-TGCR Repository Consolidation Script
# Removes duplication, moves assets to canonical locations, cleans sprawl

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = 'Stop'

Write-Host "`n[CONSOLIDATE] TEC-TGCR Repository Cleanup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

if ($DryRun) {
    Write-Host "[DRY RUN MODE] - No changes will be made`n" -ForegroundColor Yellow
}

# Track changes
$changes = @()

function Log-Action {
    param($Action, $Path)
    $changes += "[${Action}] $Path"
    if ($DryRun) {
        Write-Host "[DRY RUN] ${Action}: $Path" -ForegroundColor Yellow
    } else {
        Write-Host "${Action}: $Path" -ForegroundColor Green
    }
}

## 1. CONSOLIDATE ASSETS
Write-Host "`n[1/6] Consolidating asset folders..." -ForegroundColor Cyan

# Compare assets/ vs data/digital_assets/
$assetsRoot = "assets"
$dataAssets = "data\digital_assets"

# Check if files in assets/ are duplicates
$avatarOld = "$assetsRoot\avatars\luminai.svg"
$avatarNew = "$dataAssets\avatars\luminai.svg"
$logoOld = "$assetsRoot\logos\tec-resonance-seal.svg"
$logoNew = "$dataAssets\brand\svg\tec_resonance_logo.svg"

if (Test-Path $avatarOld) {
    $oldHash = (Get-FileHash $avatarOld).Hash
    $newHash = (Get-FileHash $avatarNew).Hash

    if ($oldHash -eq $newHash) {
        Log-Action "SKIP (duplicate)" $avatarOld
    } else {
        Log-Action "BACKUP (different)" "$avatarOld -> $dataAssets\avatars\luminai_old.svg"
        if (-not $DryRun) {
            Copy-Item $avatarOld "$dataAssets\avatars\luminai_old.svg"
        }
    }
}

# Remove old assets/ folder (after backup if needed)
if (Test-Path $assetsRoot) {
    Log-Action "REMOVE" $assetsRoot
    if (-not $DryRun) {
        Remove-Item $assetsRoot -Recurse -Force
    }
}

## 2. MOVE ROOT-LEVEL CONFIGS TO config/
Write-Host "`n[2/6] Moving scattered configs..." -ForegroundColor Cyan

$configMoves = @{
    "github-luminai-api.yaml" = "config\integrations\github-luminai-api.yaml"
    "sharepoint-luminai-api.yaml" = "config\integrations\sharepoint-luminai-api.yaml"
}

foreach ($old in $configMoves.Keys) {
    if (Test-Path $old) {
        $new = $configMoves[$old]
        $newDir = Split-Path $new -Parent

        if (-not (Test-Path $newDir) -and -not $DryRun) {
            New-Item -ItemType Directory -Path $newDir -Force | Out-Null
        }

        Log-Action "MOVE" "$old -> $new"
        if (-not $DryRun) {
            Move-Item $old $new -Force
        }
    }
}

## 3. CONSOLIDATE DOCS ARCHIVE
Write-Host "`n[3/6] Cleaning docs/archive..." -ForegroundColor Cyan

# These are superseded by current guides and can be removed
$obsoleteDocs = @(
    "docs\archive\WORDPRESS-DEPLOYMENT-CHECKLIST.md",  # Superseded by WORDPRESS_WPCOM_OPS.md
    "docs\archive\WORDPRESS-DEPLOYMENT-ERROR-FIX.md",
    "docs\archive\WORDPRESS-REST-DEBUG.md",
    "docs\archive\WP-CONFIG-SNIPPETS.md",
    "docs\archive\WPCOM-DEPLOYMENT-FIX.md",
    "docs\archive\REPOSITORY-AUDIT-2025-10-15.md",  # Old audit
    "docs\archive\SIX_DIMENSION_VALIDATION_SUMMARY.md"
)

foreach ($doc in $obsoleteDocs) {
    if (Test-Path $doc) {
        Log-Action "DELETE (obsolete)" $doc
        if (-not $DryRun) {
            Remove-Item $doc -Force
        }
    }
}

## 4. REMOVE EMPTY/UNUSED DIRECTORIES
Write-Host "`n[4/6] Removing empty directories..." -ForegroundColor Cyan

$emptyDirs = @(
    "apps\voice-imprint-studio",
    "apps\widgets-sharepoint"
)

foreach ($dir in $emptyDirs) {
    if (Test-Path $dir) {
        $items = Get-ChildItem $dir -Recurse -File
        if ($items.Count -eq 0) {
            Log-Action "DELETE (empty)" $dir
            if (-not $DryRun) {
                Remove-Item $dir -Recurse -Force
            }
        } else {
            Write-Host "KEEP (has files): $dir" -ForegroundColor Yellow
        }
    }
}

## 5. CONSOLIDATE TODO FOLDERS
Write-Host "`n[5/6] Consolidating TODO tracking..." -ForegroundColor Cyan

# Keep .todo/ (hidden), remove todo/
if (Test-Path "todo") {
    $todoFiles = Get-ChildItem "todo" -File

    if ($todoFiles.Count -gt 0) {
        Log-Action "ARCHIVE" "todo -> .todo/archive"
        if (-not $DryRun) {
            if (-not (Test-Path ".todo\archive")) {
                New-Item -ItemType Directory -Path ".todo\archive" -Force | Out-Null
            }
            Copy-Item "todo\*" ".todo\archive\" -Recurse -Force
        }
    }

    Log-Action "DELETE" "todo"
    if (-not $DryRun) {
        Remove-Item "todo" -Recurse -Force
    }
}

## 6. CLEAN ORPHANED ARCHIVES
Write-Host "`n[6/6] Removing orphaned archive files..." -ForegroundColor Cyan

$orphanedArchives = @(
    "archives\luminai_origin.json"  # Duplicate of data\archives\luminai_origin.json
)

foreach ($archive in $orphanedArchives) {
    if (Test-Path $archive) {
        Log-Action "DELETE (duplicate)" $archive
        if (-not $DryRun) {
            Remove-Item $archive -Force
        }

        # Remove parent if empty
        $parent = Split-Path $archive -Parent
        if (Test-Path $parent) {
            $remaining = Get-ChildItem $parent
            if ($remaining.Count -eq 0) {
                Log-Action "DELETE (empty)" $parent
                if (-not $DryRun) {
                    Remove-Item $parent -Force
                }
            }
        }
    }
}

## SUMMARY
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "[SUMMARY] Consolidation complete" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Changes made: $($changes.Count)" -ForegroundColor Green

if ($DryRun) {
    Write-Host "`nThis was a DRY RUN. Re-run without -DryRun to apply changes.`n" -ForegroundColor Yellow
} else {
    Write-Host "`nRepository consolidated. Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Update knowledge_map.yml references" -ForegroundColor White
    Write-Host "  2. Run tests: python -m pytest -q" -ForegroundColor White
    Write-Host "  3. Commit: git add -A && git commit -m 'chore: consolidate repo structure'`n" -ForegroundColor White
}

# Return change log
return $changes
