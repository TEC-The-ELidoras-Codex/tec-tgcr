Param(
    [switch]$Dev
)

$ErrorActionPreference = 'Stop'
Write-Host "[TEC] Bootstrapping venv and tools..." -ForegroundColor Cyan

if (-not (Test-Path .venv)) {
    Write-Host "[TEC] Creating virtual environment (.venv)" -ForegroundColor Cyan
    py -m venv .venv
}

$python = ".\.venv\Scripts\python.exe"
& $python -m pip install --upgrade pip setuptools wheel | Out-Null

if ($Dev) {
    Write-Host "[TEC] Installing package with [dev] extras" -ForegroundColor Cyan
    & $python -m pip install -e .[dev]
} else {
    Write-Host "[TEC] Installing package (core)" -ForegroundColor Cyan
    & $python -m pip install -e .
}

Write-Host "[TEC] Installing/ensuring pytest present" -ForegroundColor Cyan
& $python -m pip install pytest | Out-Null

Write-Host "[TEC] Verifying CLI" -ForegroundColor Cyan
try {
    .\.venv\Scripts\tec-agent.exe --help | Out-Null
    Write-Host "[TEC] tec-agent available" -ForegroundColor Green
} catch {
    Write-Host "[TEC] tec-agent script not found; using python -m fallback" -ForegroundColor Yellow
}

Write-Host "[TEC] Done. Quick commands:" -ForegroundColor Cyan
Write-Host "  .\\.venv\\Scripts\\python.exe -m pytest -q" -ForegroundColor DarkGray
Write-Host "  pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/pack_support_bundle.ps1" -ForegroundColor DarkGray