param(
    [switch]$DryRun,
    [switch]$SkipGitMeta,
    [string]$OutputRoot = "$PSScriptRoot\..\exports\support",
    [string[]]$IncludePaths = @(
        "README.md",
        "pyproject.toml",
        "tec_agent_runner.py",
        ".github\copilot-instructions.md",
        "data\knowledge_map.yml",
        "data\personas\",
        "docs\",
        "lore\",
        "agents\manifests\",
        "scripts\export_to_notion.ps1"
    ),
    [string[]]$ExcludeGlobs = @(
        ".git/*",
        ".venv/*",
        "**/.pytest_cache/*",
        "**/__pycache__/*",
        "**/node_modules/*",
        "**/dist/*",
        "ai-workflow/output/*",
        "exports/*"
    )
)

$ErrorActionPreference = 'Stop'

Write-Host "[ELY] Export & Gather - Starting" -ForegroundColor Cyan

# Normalize paths
$root = Resolve-Path -Path (Join-Path $PSScriptRoot "..")
$rootPath = $root.Path
Write-Host "Root: $rootPath" -ForegroundColor DarkGray

# Ensure output root
if (-not (Test-Path $OutputRoot)) {
    New-Item -ItemType Directory -Path $OutputRoot -Force | Out-Null
}

# Build inclusion set
function Resolve-Includes {
    param([string[]]$Paths)
    $resolved = @()
    foreach ($p in $Paths) {
        $full = Join-Path $rootPath $p
        if (Test-Path $full) {
            $resolved += (Get-ChildItem -Path $full -Recurse -File -Force)
        }
    }
    return $resolved
}

$files = Resolve-Includes -Paths $IncludePaths

<#
Apply exclusions using glob-like patterns:
 - ** matches across directories
 - *  matches within a path segment (no slash)
We normalize both patterns and paths to forward slashes before matching.
#>
function Should-Exclude($relPath) {
    $n = $relPath -replace '\\','/'
    foreach ($pattern in $ExcludeGlobs) {
        $pat = $pattern -replace '\\','/'
        $regex = [Regex]::Escape($pat)
        # Convert ** -> .*
        $regex = $regex -replace "\\\\\*\\\\\*", ".*"
        # Convert * -> [^/]* (single-segment wildcard)
        $regex = $regex -replace "\\\\\*", "[^/]*"
        # Convert ? -> .
        $regex = $regex -replace "\\\\\?", "."
        if ($n -match "^$regex$") { return $true }
    }
    if ($SkipGitMeta -and ($n -like ".git/*" -or $n -like ".git*")) { return $true }
    return $false
}

$inventory = @()
$seen = New-Object 'System.Collections.Generic.HashSet[string]'

foreach ($f in $files) {
    # Compute path relative to repo root
    $full = [IO.Path]::GetFullPath($f.FullName)
    $rel = $full.Substring($rootPath.Length) -replace '^[\\/]+',''
    if ($seen.Contains($rel)) { continue }
    $seen.Add($rel) | Out-Null
    if (Should-Exclude $rel) { continue }

    $sha256 = (Get-FileHash -Path $f.FullName -Algorithm SHA256).Hash
    $category = ($rel -split '[\\/]')[0]
    $inventory += [pscustomobject]@{
        Path = $rel
        Size = $f.Length
        Modified = $f.LastWriteTimeUtc.ToString('u')
        SHA256 = $sha256
        Category = $category
    }
}

# Output inventory summary
Write-Host ("Files collected: {0}" -f $inventory.Count) -ForegroundColor Green

# Write inventory CSV
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$suffix = ""
if ($DryRun) { $suffix = "_dryrun" }
$invPath = Join-Path $OutputRoot ("inventory_{0}{1}.csv" -f $timestamp, $suffix)
$inventory | Sort-Object Path | Export-Csv -Path $invPath -NoTypeInformation -Encoding UTF8
Write-Host "Inventory: $invPath" -ForegroundColor Green

if ($DryRun) {
    Write-Host "[ELY] Dry run complete - no ZIP produced." -ForegroundColor Yellow
    exit 0
}

# Full run: create ZIP
$zipName = "tec-tgcr_bundle_$timestamp.zip"
$zipPath = Join-Path $OutputRoot $zipName

# Compress-Archive requires a static file list
$paths = $inventory | ForEach-Object { Join-Path $rootPath $_.Path }
# Use a temp staging to ensure path preservation
$tempStage = Join-Path $env:TEMP ("tec_tgcr_stage_" + $timestamp)
if (Test-Path $tempStage) { Remove-Item -Recurse -Force $tempStage }
New-Item -ItemType Directory -Path $tempStage | Out-Null

foreach ($p in $paths) {
    $full = [IO.Path]::GetFullPath($p)
    $rel = $full.Substring($rootPath.Length) -replace '^[\\/]+',''
    $target = Join-Path $tempStage $rel
    $dir = Split-Path $target -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    Copy-Item -Path $p -Destination $target -Force
}

if (Test-Path $zipPath) { Remove-Item -Force $zipPath }
Compress-Archive -Path (Join-Path $tempStage '*') -DestinationPath $zipPath -Force
Remove-Item -Recurse -Force $tempStage

# Create checksum for the ZIP
$zipHash = (Get-FileHash -Path $zipPath -Algorithm SHA256).Hash
$hashPath = "$zipPath.sha256"
[IO.File]::WriteAllText($hashPath, "$zipHash  $zipName")

Write-Host "Bundle: $zipPath" -ForegroundColor Green
Write-Host "SHA256: $hashPath" -ForegroundColor Green
Write-Host "[ELY] Full run complete." -ForegroundColor Cyan
