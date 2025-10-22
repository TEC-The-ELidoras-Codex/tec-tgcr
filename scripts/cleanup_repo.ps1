# Cleans local workspace artifacts (safe deletions only)
# Usage:
#   pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/cleanup_repo.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = (Resolve-Path "$PSScriptRoot/..\").Path
Set-Location $root

function Remove-IfExists([string]$path) {
  if (Test-Path -LiteralPath $path) { Write-Host "[clean] removing $path"; Remove-Item -LiteralPath $path -Recurse -Force }
}

# Python cache and coverage
Remove-IfExists ".pytest_cache"
Remove-IfExists "htmlcov"
Remove-IfExists ".coverage"

# Build/dist artifacts
Remove-IfExists "dist"
Remove-IfExists "exports/wp-plugin"
Remove-IfExists ".wpcom-dist"

# AI workflow outputs
Remove-IfExists "ai-workflow/output"
Remove-IfExists "ai-workflow/generated"

# Logs
Get-ChildItem -Recurse -Filter "*.log" -ErrorAction SilentlyContinue | ForEach-Object {
  Write-Host "[clean] removing $($_.FullName)"; Remove-Item -LiteralPath $_.FullName -Force
}

# Node build outputs under apps/*
Get-ChildItem -Directory -Recurse -ErrorAction SilentlyContinue apps | Where-Object { $_.Name -in @('dist','build','.cache') } | ForEach-Object {
  Write-Host "[clean] removing $($_.FullName)"; Remove-Item -LiteralPath $_.FullName -Recurse -Force
}

Write-Host "[clean] done."
