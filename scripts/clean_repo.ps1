<#
  Cleans generated artifacts and caches from the repo working tree.
  Safe to run anytime. Does NOT touch source files.

  Usage (from repo root):
    pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/clean_repo.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = (Resolve-Path "$PSScriptRoot/..\").Path
Write-Host "[clean] Root: $root"

$paths = @(
  'dist',
  'exports',
  '.wpcom-dist',
  '.pytest_cache',
  '.parcel-cache',
  '.cache',
  'logs',
  'reports'
)

foreach ($rel in $paths) {
  $full = Join-Path $root $rel
  if (Test-Path $full) {
    Write-Host "[clean] Removing: $rel"
    Remove-Item -LiteralPath $full -Recurse -Force -ErrorAction SilentlyContinue
  }
}

# Remove stray zip files at repo root (e.g., tec-resonance-player.zip)
Get-ChildItem -LiteralPath $root -Filter '*.zip' -File -ErrorAction SilentlyContinue |
  ForEach-Object {
    Write-Host "[clean] Removing root zip: $($_.Name)"
    Remove-Item -LiteralPath $_.FullName -Force -ErrorAction SilentlyContinue
  }

Write-Host "[clean] Done"
