# Packs the TEC TGCR WordPress plugin into a distributable ZIP
# Usage (from workspace root):
#   pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/pack_wp_plugin.ps1
# Output: exports/wp-plugin/tec-tgcr-<version>.zip

param(
    [string]$PluginRelPath = 'apps/wordpress/tec-tgcr',
    [string]$OutRelDir = 'exports/wp-plugin'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$workspace = (Resolve-Path "$PSScriptRoot/..\").Path
$pluginPath = Join-Path $workspace $PluginRelPath
$mainFile   = Join-Path $pluginPath 'tec-tgcr.php'
$outDir     = Join-Path $workspace $OutRelDir
$stageRoot  = Join-Path $workspace 'dist/wp-plugin'
$stageDir   = Join-Path $stageRoot 'tec-tgcr'

Write-Host "[pack] Workspace: $workspace"
Write-Host "[pack] Plugin path: $pluginPath"

if (-not (Test-Path $pluginPath)) {
    throw "Plugin directory not found: $pluginPath"
}
if (-not (Test-Path $mainFile)) {
    throw "Main plugin file not found: $mainFile"
}

# Extract Version from plugin header
$version = '0.0.0'
$header = Get-Content -LiteralPath $mainFile -ErrorAction Stop | Select-String -Pattern '^\s*Version\s*:\s*(.+)$' -CaseSensitive:$false | Select-Object -First 1
if ($header) {
    $version = ($header.Matches[0].Groups[1].Value).Trim()
} else {
    $version = (Get-Date -Format 'yyyyMMdd-HHmmss')
}

Write-Host "[pack] Version: $version"

# Prepare staging and output directories
if (Test-Path $stageDir) { Remove-Item -LiteralPath $stageDir -Recurse -Force }
New-Item -ItemType Directory -Force -Path $stageDir | Out-Null
New-Item -ItemType Directory -Force -Path $outDir   | Out-Null

# Copy plugin contents to staging under folder 'tec-tgcr' so the ZIP has correct top-level folder
Write-Host "[pack] Copying files to stage..."
Copy-Item -LiteralPath (Join-Path $pluginPath '*') -Destination $stageDir -Recurse -Force

$zipPath = Join-Path $outDir ("tec-tgcr-$version.zip")
if (Test-Path $zipPath) { Remove-Item -LiteralPath $zipPath -Force }

Write-Host "[pack] Creating ZIP at: $zipPath"
# Compress the folder itself so the top-level inside ZIP is 'tec-tgcr'
Compress-Archive -LiteralPath $stageDir -DestinationPath $zipPath -Force

# Basic sanity check: ensure main file exists inside the zip
$zip = [IO.Compression.ZipFile]::OpenRead($zipPath)
try {
    $entry = $zip.Entries | Where-Object { $_.FullName -match '^tec-tgcr/tec-tgcr\.php$' }
    if (-not $entry) { throw "ZIP missing expected file 'tec-tgcr/tec-tgcr.php'" }
}
finally { $zip.Dispose() }

Write-Host "[pack] Done. Packaged plugin -> $zipPath"
