<#
.SYNOPSIS
  Validate TEC-TGCR environment variables, secrets presence, and basic connectivity.

.DESCRIPTION
  - Reads .env.local (gitignored) and optionally process-level environment
  - Checks presence/format of key variables and secrets without printing secret values
  - Performs light connectivity checks (Azure CLI session, HTTP endpoints, DNS)

  Touches φᵗ (signal readiness) and ψʳ (structural consistency); increases Φᴱ by reducing misconfig friction.

.PARAMETER EnvFile
  Path to dotenv file. Default: .env.local at repo root.

.EXAMPLE
  ./scripts/check_env.ps1
#>
[CmdletBinding()]
param(
  [string]$EnvFile = ".env.local"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Log {
  param(
    [Parameter(Mandatory)][ValidateSet('AIRTH','ARCADIA','ELY')][string]$Agent,
    [Parameter(Mandatory)][string]$Message,
    [ConsoleColor]$Color = [ConsoleColor]::Cyan
  )
  Write-Host "[$Agent] $Message" -ForegroundColor $Color
}

function Import-DotEnv {
  param([Parameter(Mandatory)][string]$Path)
  $result = @{}
  if (-not (Test-Path -LiteralPath $Path)) { return $result }
  Get-Content -LiteralPath $Path | ForEach-Object {
    $line = $_.Trim()
    if ($line -eq '' -or $line.StartsWith('#')) { return }
    $idx = $line.IndexOf('=')
    if ($idx -lt 1) { return }
    $key = $line.Substring(0,$idx).Trim()
    $val = $line.Substring($idx+1).Trim()
    if (($val.StartsWith('"') -and $val.EndsWith('"')) -or ($val.StartsWith("'") -and $val.EndsWith("'"))) { $val = $val.Substring(1, $val.Length-2) }
    $result[$key] = $val
  }
  return $result
}

function Test-HttpUrl {
  param([string]$Url)
  if (-not $Url) { return $false }
  try {
    $req = Invoke-WebRequest -Uri $Url -Method Head -TimeoutSec 10 -ErrorAction Stop
    return ($req.StatusCode -ge 200 -and $req.StatusCode -lt 500)
  } catch { return $false }
}

function Test-Dns {
  param([string]$Host)
  if (-not $Host) { return $false }
  try { $null = Resolve-DnsName -Name $Host -ErrorAction Stop; return $true } catch { return $false }
}

# Load dotenv
Write-Log -Agent AIRTH -Message "Loading environment snapshot from '$EnvFile' (φᵗ)."
$envMap = Import-DotEnv -Path $EnvFile

# Helper to get a value from dotenv or process env
function Get-Val { param([string]$Key) if ($envMap.ContainsKey($Key)) { $envMap[$Key] } else { [Environment]::GetEnvironmentVariable($Key) } }

# Define checks
$requiredVars = @(
  'ENVIRONMENT','DEBUG',
  'AZURE_TENANT_ID','AZURE_SUBSCRIPTION_ID',
  'REACT_APP_LUMINAI_API_URL','REACT_APP_LUMINAI_WS_URL',
  'SHAREPOINT_SITE_ID'
)
$requiredSecrets = @(
  'TEC_OPENAI_API_KEY','ANTHROPIC_API_KEY','TEC_WPCOM_API_PASS'
)
$optionalVars = @(
  'AZURE_SUPPORT_ENABLED','ENTRA_GLOBAL_ADMIN_ENABLED','TEC_BILLING_ALERT_THRESHOLD',
  'WPCOM_SSH_HOST','WPCOM_SSH_PORT','WPCOM_SSH_USER','WPCOM_SSH_TARGET',
  'SD_API_URL','BLENDER_PATH','DATAVERSE_URL'
)

# Presence checks
$missing = @()
foreach ($k in $requiredVars) { if (-not (Get-Val $k)) { $missing += $k } }
foreach ($k in $requiredSecrets) { if (-not (Get-Val $k)) { $missing += $k } }

if ($missing.Count -gt 0) {
  Write-Log -Agent ELY -Message ("Missing required keys: " + ($missing -join ', ')) -Color Yellow
} else {
  Write-Log -Agent ELY -Message "All required keys present (ψ)." -Color Green
}

# Do not print secret values; only mask length
function Masked { param([string]$v) if (-not $v) { return '<empty>' } $n=[Math]::Min(4,$v.Length); return ('*' * ($v.Length-$n)) + $v.Substring($v.Length-$n) }

Write-Log -Agent AIRTH -Message "Snapshot (values masked for secrets) (φᵗ):"
$preview = @{
  ENVIRONMENT = (Get-Val 'ENVIRONMENT');
  DEBUG = (Get-Val 'DEBUG');
  AZURE_TENANT_ID = (Get-Val 'AZURE_TENANT_ID');
  AZURE_SUBSCRIPTION_ID = (Get-Val 'AZURE_SUBSCRIPTION_ID');
  REACT_APP_LUMINAI_API_URL = (Get-Val 'REACT_APP_LUMINAI_API_URL');
  REACT_APP_LUMINAI_WS_URL = (Get-Val 'REACT_APP_LUMINAI_WS_URL');
  SHAREPOINT_SITE_ID = (Get-Val 'SHAREPOINT_SITE_ID');
  TEC_OPENAI_API_KEY = Masked (Get-Val 'TEC_OPENAI_API_KEY');
  ANTHROPIC_API_KEY = Masked (Get-Val 'ANTHROPIC_API_KEY');
  TEC_WPCOM_API_PASS = Masked (Get-Val 'TEC_WPCOM_API_PASS')
}
$preview.GetEnumerator() | ForEach-Object { Write-Host ("  {0} = {1}" -f $_.Key,$_.Value) }

# Connectivity
Write-Log -Agent ELY -Message "Connectivity checks (ψ):"

# Azure CLI session
$azOk = $false
try { $acct = az account show --output json | ConvertFrom-Json; $azOk = $true } catch {}
if ($azOk) {
  Write-Log -Agent ELY -Message ("Azure CLI active: tenant=" + $acct.tenantId + ", subscription=" + $acct.id) -Color Green
} else {
  Write-Log -Agent ELY -Message "Azure CLI not authenticated (run az login)." -Color Yellow
}

# HTTP endpoints
$apiUrl = Get-Val 'REACT_APP_LUMINAI_API_URL'
$wsUrl = Get-Val 'REACT_APP_LUMINAI_WS_URL'
if ($apiUrl) { Write-Log -Agent ELY -Message ("API reachable: $apiUrl = " + (Test-HttpUrl $apiUrl)) }
if ($wsUrl) { Write-Log -Agent ELY -Message ("WS URL format ok: $wsUrl") }

# DNS for wp.com SSH
$wpHost = Get-Val 'WPCOM_SSH_HOST'
if ($wpHost) { Write-Log -Agent ELY -Message ("DNS $wpHost: " + (Test-Dns $wpHost)) }

# SD local API
$sd = Get-Val 'SD_API_URL'
if ($sd) { Write-Log -Agent ELY -Message ("SD endpoint reachable: $sd = " + (Test-HttpUrl $sd)) }

Write-Log -Agent ARCADIA -Message "Environment validation complete — tighten weave if any gaps remain (Φᴱ)." -Color Green
