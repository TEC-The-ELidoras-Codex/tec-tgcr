# Verifies file integrity against CHECKSUMS.md
# Usage (from workspace root):
#   pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/verify_checksums.ps1

param(
    [string]$ChecksumFile = 'CHECKSUMS.md'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$workspace = (Resolve-Path "$PSScriptRoot/..\").Path
$checksumPath = Join-Path $workspace $ChecksumFile

Write-Host "[verify] Workspace: $workspace"
Write-Host "[verify] Checksums: $checksumPath"

if (-not (Test-Path $checksumPath)) {
    Write-Host "ERROR: Checksums file not found: $checksumPath" -ForegroundColor Red
    exit 1
}

# Parse CHECKSUMS.md to extract file paths and expected hashes
$content = Get-Content -LiteralPath $checksumPath -Raw
$pattern = '`([^`]+)`\s+\|\s+`([A-F0-9]{64})`'
$checkMatches = [regex]::Matches($content, $pattern)

if ($checkMatches.Count -eq 0) {
    Write-Host "WARNING: No checksums found in $ChecksumFile" -ForegroundColor Yellow
    exit 0
}

Write-Host "`n[verify] Checking $($checkMatches.Count) files...`n"

$passed = 0
$failed = 0
$missing = 0

foreach ($match in $checkMatches) {
    $relPath = $match.Groups[1].Value
    $expectedHash = $match.Groups[2].Value
    $fullPath = Join-Path $workspace $relPath

    if (-not (Test-Path $fullPath)) {
        Write-Host "  MISSING: $relPath" -ForegroundColor Yellow
        $missing++
        continue
    }

    $actualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $fullPath).Hash

    if ($actualHash -eq $expectedHash) {
        Write-Host "  OK: $relPath" -ForegroundColor Green
        $passed++
    }
    else {
        Write-Host "  MISMATCH: $relPath" -ForegroundColor Red
        Write-Host "    Expected: $expectedHash"
        Write-Host "    Actual:   $actualHash"
        $failed++
    }
}

Write-Host "`n[verify] Results:"
Write-Host "  Passed:  $passed" -ForegroundColor Green
Write-Host "  Failed:  $failed" -ForegroundColor $(if ($failed -gt 0) { 'Red' } else { 'Gray' })
Write-Host "  Missing: $missing" -ForegroundColor $(if ($missing -gt 0) { 'Yellow' } else { 'Gray' })

if ($failed -gt 0) {
    Write-Host "`n[verify] FAILURE: Some files have incorrect checksums." -ForegroundColor Red
    exit 1
}
elseif ($missing -gt 0) {
    Write-Host "`n[verify] WARNING: Some files are missing." -ForegroundColor Yellow
    exit 0
}
else {
    Write-Host "`n[verify] SUCCESS: All checksums verified." -ForegroundColor Green
    exit 0
}
