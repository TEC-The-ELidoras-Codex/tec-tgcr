<#
.SYNOPSIS
    Load environment variables from .env.local into current PowerShell session.

.DESCRIPTION
    Parses .env.local file and sets environment variables for the current session.
    Useful for local development with API keys, secrets, and config overrides.

.PARAMETER EnvFile
    Path to .env file (defaults to .env.local in repo root).

.EXAMPLE
    .\scripts\load_env.ps1
    # Loads .env.local from repo root

.EXAMPLE
    .\scripts\load_env.ps1 -EnvFile ".env.production"
    # Load specific env file
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$EnvFile = ".env.local"
)

$ErrorActionPreference = "Stop"

# Get repo root
$repoRoot = Split-Path -Parent $PSScriptRoot
$envPath = Join-Path $repoRoot $EnvFile

# Check if file exists
if (-not (Test-Path $envPath)) {
    Write-Host "[!] Environment file not found: $envPath" -ForegroundColor Yellow
    Write-Host "[i] Create one from template:" -ForegroundColor Cyan
    Write-Host "    cp .env.example .env.local" -ForegroundColor Gray
    exit 1
}

Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   Loading Environment Variables — TGCR Agent Stack        ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Parse and load
$loadedCount = 0
$skippedCount = 0

Get-Content $envPath | ForEach-Object {
    $line = $_.Trim()

    # Skip empty lines and comments
    if (-not $line -or $line.StartsWith("#")) {
        return
    }

    # Parse KEY=VALUE format
    if ($line -match '^(?<k>[^=]+)=(?<v>.*)$') {
        $key = $Matches['k'].Trim()
        $value = $Matches['v'].Trim()

        # Skip if value is empty or placeholder
        if (-not $value -or $value -eq "..." -or $value -like "*your*key*here*") {
            Write-Host "[→] Skipped (empty): $key" -ForegroundColor Gray
            $skippedCount++
            return
        }

        # Set environment variable for current session
        [System.Environment]::SetEnvironmentVariable($key, $value, [System.EnvironmentVariableTarget]::Process)

        # Display loaded key (mask value)
        $maskedValue = if ($value.Length -gt 10) {
            "$($value.Substring(0, 8))...$($value.Substring($value.Length - 4))"
        } else {
            "***"
        }

        Write-Host "[✓] Loaded: $key = $maskedValue" -ForegroundColor Green
        $loadedCount++
    }
}

Write-Host ""
# Backwards-compatible aliases for scripts that expect APP_ID / PRIVATE_KEY / INSTALLATION_ID
# If the repo .env uses GITHUB_APP_ID / GITHUB_PRIVATE_KEY / GITHUB_INSTALLATION_ID,
# create equivalent process-level env vars so older scripts work without change.
$aliasMap = @{
    "APP_ID" = "GITHUB_APP_ID"
    "PRIVATE_KEY" = "GITHUB_PRIVATE_KEY"
    "INSTALLATION_ID" = "GITHUB_INSTALLATION_ID"
}

foreach ($pair in $aliasMap.GetEnumerator()) {
    $aliasName = $pair.Key
    $sourceName = $pair.Value
    $current = [Environment]::GetEnvironmentVariable($aliasName)
    if (-not $current) {
        $srcVal = [Environment]::GetEnvironmentVariable($sourceName)
        if ($srcVal) {
            [Environment]::SetEnvironmentVariable($aliasName, $srcVal, [System.EnvironmentVariableTarget]::Process)
            # Print a concise mapping notice without exposing secret contents
            if ($aliasName -eq 'PRIVATE_KEY') {
                Write-Host "[⇄] Mapped $sourceName -> $aliasName (private key loaded)" -ForegroundColor Cyan
            } else {
                Write-Host "[⇄] Mapped $sourceName -> $aliasName = $($srcVal.Substring(0, [Math]::Min(8, $srcVal.Length)))..." -ForegroundColor Cyan
            }
        }
    }
}

Write-Host "════════════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "Loaded: $loadedCount variable(s)" -ForegroundColor White
Write-Host "Skipped: $skippedCount empty/placeholder(s)" -ForegroundColor Gray
Write-Host ""
Write-Host "[i] Variables available for this PowerShell session only" -ForegroundColor Cyan
Write-Host "[i] To persist, add to system environment or re-run this script" -ForegroundColor Cyan
Write-Host ""

# Verify key variables
$keyVars = @(
    "TEC_OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "XAI_API_KEY",
    "WORLDANVIL_API_KEY",
    "TEC_WPCOM_API_PASS"
)

Write-Host "Key Variable Check:" -ForegroundColor Magenta
foreach ($var in $keyVars) {
    $value = [Environment]::GetEnvironmentVariable($var)
    if ($value) {
        Write-Host "  [✓] $var" -ForegroundColor Green
    } else {
        Write-Host "  [✗] $var (not set)" -ForegroundColor Yellow
    }
}
Write-Host ""
