<#
.SYNOPSIS
    Quick setup script for API keys — create .env.local from template.

.DESCRIPTION
    Interactive wizard to set up your API keys in .env.local.
    - Copies .env.example to .env.local if it doesn't exist
    - Opens .env.local in your editor
    - Verifies .gitignore coverage
    - Optionally loads keys into current session

.EXAMPLE
    .\scripts\setup_env.ps1
    # Interactive setup wizard
#>

$ErrorActionPreference = "Stop"

# Colors
$cyan = "Cyan"
$green = "Green"
$yellow = "Yellow"
$white = "White"

# Banner
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor $cyan
Write-Host "║   TEC-TGCR API Keys Setup — Quick Start Wizard            ║" -ForegroundColor $cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor $cyan
Write-Host ""

# Get repo root
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$envExample = Join-Path $repoRoot ".env.example"
$envLocal = Join-Path $repoRoot ".env.local"

# Step 1: Check if .env.example exists
if (-not (Test-Path $envExample)) {
    Write-Host "[✗] Template file not found: $envExample" -ForegroundColor Red
    Write-Host "[i] This repo should have .env.example checked in" -ForegroundColor $yellow
    exit 1
}

Write-Host "[✓] Found template: $envExample" -ForegroundColor $green

# Step 2: Check if .env.local already exists
if (Test-Path $envLocal) {
    Write-Host "[i] $envLocal already exists" -ForegroundColor $yellow
    Write-Host ""
    $response = Read-Host "Overwrite it? (y/N)"
    if ($response -ne "y") {
        Write-Host "[i] Keeping existing $envLocal" -ForegroundColor $cyan
        Write-Host ""
        $response = Read-Host "Open it in editor? (Y/n)"
        if ($response -ne "n") {
            Write-Host "[→] Opening $envLocal..." -ForegroundColor $cyan
            code $envLocal
        }

        $response = Read-Host "Load keys into current session? (Y/n)"
        if ($response -ne "n") {
            & "$PSScriptRoot\load_env.ps1"
        }
        exit 0
    }
}

# Step 3: Copy template to .env.local
Write-Host ""
Write-Host "[→] Copying $envExample to $envLocal..." -ForegroundColor $cyan
Copy-Item $envExample $envLocal
Write-Host "[✓] Created $envLocal" -ForegroundColor $green

# Step 4: Verify .gitignore
Write-Host ""
Write-Host "[→] Checking .gitignore..." -ForegroundColor $cyan

$gitignoreContent = Get-Content ".gitignore" -Raw -ErrorAction SilentlyContinue

if ($gitignoreContent -match "\.env\.local" -or $gitignoreContent -match "\.env\.\*") {
    Write-Host "[✓] .env.local is gitignored (safe!)" -ForegroundColor $green
} else {
    Write-Host "[!] WARNING: .env.local may not be gitignored!" -ForegroundColor $yellow
    Write-Host "[i] Make sure .gitignore contains: .env.* or .env.local" -ForegroundColor $cyan
}

# Step 5: Show instructions
Write-Host ""
Write-Host "════════════════════════════════════════════════════════════" -ForegroundColor $green
Write-Host "Next Steps:" -ForegroundColor $white
Write-Host ""
Write-Host "1. Edit $envLocal with your actual API keys" -ForegroundColor $white
Write-Host "   Replace placeholders like 'sk-proj-...' with real values" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Your keys:" -ForegroundColor $white
Write-Host "   • TEC_OPENAI_API_KEY      (OpenAI GPT-4)" -ForegroundColor Gray
Write-Host "   • ANTHROPIC_API_KEY       (Claude)" -ForegroundColor Gray
Write-Host "   • XAI_API_KEY             (Grok)" -ForegroundColor Gray
Write-Host "   • WORLDANVIL_API_KEY      (Lore)" -ForegroundColor Gray
Write-Host "   • COINMC_API_KEY          (CoinMarketCap)" -ForegroundColor Gray
Write-Host "   • COINDESK_API_KEY        (CoinDesk)" -ForegroundColor Gray
Write-Host "   • TEC_WPCOM_API_PASS      (WordPress.com)" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Load keys into terminal:" -ForegroundColor $white
Write-Host "   .\scripts\load_env.ps1" -ForegroundColor $cyan
Write-Host ""
Write-Host "4. Verify loaded keys:" -ForegroundColor $white
Write-Host "   Get-ChildItem Env:TEC_OPENAI_API_KEY" -ForegroundColor $cyan
Write-Host ""
Write-Host "════════════════════════════════════════════════════════════" -ForegroundColor $green

# Step 6: Offer to open editor
Write-Host ""
$response = Read-Host "Open $envLocal in editor now? (Y/n)"

if ($response -ne "n") {
    Write-Host ""
    Write-Host "[→] Opening $envLocal in VS Code..." -ForegroundColor $cyan

    # Try VS Code first
    if (Get-Command code -ErrorAction SilentlyContinue) {
        code $envLocal
    } elseif (Get-Command notepad -ErrorAction SilentlyContinue) {
        notepad $envLocal
    } else {
        Write-Host "[i] Could not find editor. Manually open: $envLocal" -ForegroundColor $yellow
    }
}

Write-Host ""
Write-Host "[✓] Setup complete! Edit $envLocal and run load_env.ps1 when ready." -ForegroundColor $green
Write-Host ""
