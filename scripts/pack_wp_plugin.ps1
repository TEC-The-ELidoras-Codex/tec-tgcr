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
# Use -Path so the wildcard expands; -LiteralPath would treat '*' literally
Copy-Item -Path (Join-Path $pluginPath '*') -Destination $stageDir -Recurse -Force

# Embed build-info.json with commit, branch, dirty flag, timestamp, and main file hash
$commit = $null; $branch = $null; $dirtyList = $null
try { $commit = (git rev-parse HEAD) 2>$null } catch {}
try { $branch = (git rev-parse --abbrev-ref HEAD) 2>$null } catch {}
try { $dirtyList = (git status --porcelain) 2>$null } catch {}
$dirty = if ($dirtyList) { $true } else { $false }
$timestamp = (Get-Date).ToString('o')
$mainHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $mainFile).Hash

$buildInfo = [ordered]@{
  name = 'tec-tgcr'
  version = $version
  commit = if ($commit) { $commit.Trim() } else { 'unknown' }
  branch = if ($branch) { $branch.Trim() } else { 'unknown' }
  dirty = $dirty
  build_timestamp = $timestamp
  main_sha256 = $mainHash
}
$buildInfoPath = Join-Path $stageDir 'build-info.json'
$buildInfo | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $buildInfoPath -Encoding UTF8

$zipPath = Join-Path $outDir ("tec-tgcr-$version.zip")
if (Test-Path $zipPath) { Remove-Item -LiteralPath $zipPath -Force }

Write-Host "[pack] Creating ZIP at: $zipPath"
# Compress the folder itself so the top-level inside ZIP is 'tec-tgcr'
Compress-Archive -LiteralPath $stageDir -DestinationPath $zipPath -Force

# Basic sanity check: ensure main file exists inside the zip
# Ensure compression assembly is available for ZipFile static methods
try { Add-Type -AssemblyName System.IO.Compression.FileSystem -ErrorAction Stop } catch { }
$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
    $entry = $zip.Entries | Where-Object { $_.FullName -match '^tec-tgcr/tec-tgcr\.php$' }
    if (-not $entry) { throw "ZIP missing expected file 'tec-tgcr/tec-tgcr.php'" }
}
finally { $zip.Dispose() }

Write-Host "[pack] Done. Packaged plugin -> $zipPath"
