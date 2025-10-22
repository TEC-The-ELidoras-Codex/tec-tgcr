<#
.SYNOPSIS
  Take control of an Azure subscription and (optionally) Entra directory roles for the signed-in user using Azure CLI.

.DESCRIPTION
  - Ensures Azure CLI is logged into the specified Tenant
  - Sets the active Subscription
  - Assigns RBAC roles (Owner + User Access Administrator) to the signed-in user at the subscription scope (idempotent)
  - Optionally assigns Entra ID directory roles (Global Administrator + Privileged Role Administrator) using Microsoft Graph (requires sufficient privileges)

  Touches ψʳ (structure) by enforcing consistent access topology; strengthens Φᴱ by enabling controlled change capacity.

.PARAMETER TenantId
  Azure Tenant ID (GUID). If omitted, the script will attempt to load from .env.local (AZURE_TENANT_ID).

.PARAMETER SubscriptionId
  Azure Subscription ID (GUID). If omitted, the script will attempt to load from .env.local (AZURE_SUBSCRIPTION_ID).

.PARAMETER AssignDirectoryRoles
  When provided, attempts to activate and assign Global Administrator and Privileged Role Administrator directory roles to the signed-in user via Microsoft Graph.
  NOTE: Requires that the caller already has adequate privileges (e.g., Privileged Role Administrator) and PIM activation if applicable.

.PARAMETER UserObjectId
  Object ID of the user to assign. If omitted, uses the currently signed-in user.

.PARAMETER EnvFile
  Path to a dotenv file to load defaults from. Default is ".env.local" at repo root.

.EXAMPLE
  # Use values from .env.local
  .\scripts\azure_take_control.ps1

.EXAMPLE
  # Explicit values, and assign Entra directory roles as well
  .\scripts\azure_take_control.ps1 -TenantId 00000000-0000-0000-0000-000000000000 -SubscriptionId 11111111-1111-1111-1111-111111111111 -AssignDirectoryRoles

.NOTES
  - Requires Azure CLI (az) and network access to Azure + Microsoft Graph.
  - Directory role assignment will fail if the caller lacks sufficient permissions.
  - Tested with Windows PowerShell 5.1.
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
  [string]$TenantId,
  [string]$SubscriptionId,
  [switch]$AssignDirectoryRoles,
  [string]$UserObjectId,
  [string]$EnvFile = ".env.local"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Log {
  param(
    [Parameter(Mandatory)][ValidateSet('AIRTH','ARCADIA','ELY')][string]$Agent,
    [Parameter(Mandatory)][string]$Message
  )
  $timestamp = (Get-Date).ToString('u')
  Write-Host "[$Agent] $Message" -ForegroundColor Cyan
}

function Import-DotEnv {
  param(
    [Parameter(Mandatory)][string]$Path
  )
  $result = @{}
  if (-not (Test-Path -LiteralPath $Path)) { return $result }
  Get-Content -LiteralPath $Path | ForEach-Object {
    $line = $_.Trim()
    if ($line -eq '' -or $line.StartsWith('#')) { return }
    $idx = $line.IndexOf('=')
    if ($idx -lt 1) { return }
    $key = $line.Substring(0,$idx).Trim()
    $val = $line.Substring($idx+1).Trim()
    # Remove optional surrounding quotes
    if (($val.StartsWith('"') -and $val.EndsWith('"')) -or ($val.StartsWith("'") -and $val.EndsWith("'"))) {
      $val = $val.Substring(1, $val.Length-2)
    }
    $result[$key] = $val
  }
  return $result
}

function Ensure-AzCliInstalled {
  if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw "Azure CLI (az) not found on PATH. Install from https://aka.ms/azure-cli"
  }
}

function Ensure-AzLogin {
  param(
    [Parameter(Mandatory)][string]$TenantId
  )
  try {
    $null = az account show --output none 2>$null
    Write-Log -Agent ELY -Message "Azure CLI session detected."
  } catch {
    Write-Log -Agent ELY -Message "No active Azure CLI session; initiating login for tenant $TenantId (ψ)."
    az login --tenant $TenantId | Out-Null
  }
}

function Set-Subscription {
  param(
    [Parameter(Mandatory)][string]$SubscriptionId
  )
  Write-Log -Agent ELY -Message "Setting active subscription: $SubscriptionId (ψ)."
  az account set --subscription $SubscriptionId
}

function Get-SignedInUserObjectId {
  try {
    $id = az ad signed-in-user show --query id --output tsv
    if (-not [string]::IsNullOrWhiteSpace($id)) { return $id }
  } catch {}
  # Fallback via UPN
  $upn = az account show --query user.name --output tsv
  if ([string]::IsNullOrWhiteSpace($upn)) { throw "Unable to determine signed-in user." }
  $id = az ad user show --id $upn --query id --output tsv
  if ([string]::IsNullOrWhiteSpace($id)) { throw "Unable to resolve user object id for $upn" }
  return $id
}

function Test-RoleAssignmentExists {
  param(
    [Parameter(Mandatory)][string]$UserObjectId,
    [Parameter(Mandatory)][string]$SubscriptionId,
    [Parameter(Mandatory)][string]$RoleName
  )
  $existing = az role assignment list --assignee-object-id $UserObjectId --scope "/subscriptions/$SubscriptionId" --role "$RoleName" --query "[?roleDefinitionName=='$RoleName'] | length(@)" --output tsv
  return ([int]$existing -gt 0)
}

[CmdletBinding(SupportsShouldProcess=$true)]
function Set-RoleAssignment {
  param(
    [Parameter(Mandatory)][string]$UserObjectId,
    [Parameter(Mandatory)][string]$SubscriptionId,
    [Parameter(Mandatory)][string]$RoleName
  )
  if (Test-RoleAssignmentExists -UserObjectId $UserObjectId -SubscriptionId $SubscriptionId -RoleName $RoleName) {
    Write-Log -Agent ELY -Message "Role '$RoleName' already present at subscription scope (ψ)."
    return
  }
  if ($PSCmdlet.ShouldProcess("/subscriptions/$SubscriptionId", "Grant $RoleName to $UserObjectId")) {
    Write-Log -Agent ELY -Message "Assigning '$RoleName' at subscription scope (Φᴱ)."
    az role assignment create --assignee-object-id $UserObjectId --assignee-principal-type User --role "$RoleName" --scope "/subscriptions/$SubscriptionId" | Out-Null
  }
}

[CmdletBinding(SupportsShouldProcess=$true)]
function Set-DirectoryRole {
  param(
    [Parameter(Mandatory)][string]$RoleTemplateId,
    [Parameter(Mandatory)][string]$RoleName,
    [Parameter(Mandatory)][string]$UserObjectId
  )
  Write-Log -Agent ELY -Message "Ensuring directory role '$RoleName' is active (ψ)."
  $roleId = $null
  try {
    $rolesJson = az rest --method GET --url "https://graph.microsoft.com/v1.0/directoryRoles" --output json
    $roles = ($rolesJson | ConvertFrom-Json).value
    $role = $roles | Where-Object { $_.roleTemplateId -eq $RoleTemplateId }
    if (-not $role) {
      Write-Log -Agent ELY -Message "Activating directory role template '$RoleName' (Φᴱ)."
      $body = @{ roleTemplateId = $RoleTemplateId } | ConvertTo-Json
      $null = az rest --method POST --url "https://graph.microsoft.com/v1.0/directoryRoles" --headers "Content-Type=application/json" --body $body
      # Re-query
      $rolesJson = az rest --method GET --url "https://graph.microsoft.com/v1.0/directoryRoles" --output json
      $roles = ($rolesJson | ConvertFrom-Json).value
      $role = $roles | Where-Object { $_.roleTemplateId -eq $RoleTemplateId }
    }
    if (-not $role) { throw "Role '$RoleName' not found after activation attempt." }
    $roleId = $role.id
  } catch {
    throw "Failed to ensure directory role '$RoleName': $($_.Exception.Message)"
  }

  # Check membership
  Write-Log -Agent ELY -Message "Checking '$RoleName' membership (φᵗ)."
  $membersJson = az rest --method GET --url "https://graph.microsoft.com/v1.0/directoryRoles/$roleId/members?$select=id" --output json
  $members = ($membersJson | ConvertFrom-Json).value
  if ($members | Where-Object { $_.id -eq $UserObjectId }) {
    Write-Log -Agent ELY -Message "User already a member of '$RoleName' (φᵗ)."
    return
  }

  if ($PSCmdlet.ShouldProcess($RoleName, "Add member $UserObjectId")) {
    Write-Log -Agent ELY -Message "Adding user to '$RoleName' (Φᴱ)."
  $refBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$UserObjectId" } | ConvertTo-Json
  $memberAddUrl = "https://graph.microsoft.com/v1.0/directoryRoles/$roleId/members/`$ref"
  $null = az rest --method POST --url $memberAddUrl --headers "Content-Type=application/json" --body $refBody
  }
}

# --- Main ---
Ensure-AzCliInstalled

# Load defaults from dotenv if needed
$dotenv = Import-DotEnv -Path $EnvFile
if (-not $TenantId -and $dotenv.ContainsKey('AZURE_TENANT_ID')) { $TenantId = $dotenv['AZURE_TENANT_ID'] }
if (-not $SubscriptionId -and $dotenv.ContainsKey('AZURE_SUBSCRIPTION_ID')) { $SubscriptionId = $dotenv['AZURE_SUBSCRIPTION_ID'] }

if (-not $TenantId) { throw "TenantId is required (pass -TenantId or set AZURE_TENANT_ID in $EnvFile)." }
if (-not $SubscriptionId) { throw "SubscriptionId is required (pass -SubscriptionId or set AZURE_SUBSCRIPTION_ID in $EnvFile)." }

Write-Log -Agent ELY -Message "Verifying resonance field integrity for access topology (ψ)."
Ensure-AzLogin -TenantId $TenantId
Set-Subscription -SubscriptionId $SubscriptionId

if (-not $UserObjectId) { $UserObjectId = Get-SignedInUserObjectId }
Write-Log -Agent ELY -Message "Target user object id: $UserObjectId (φᵗ)."

# RBAC at subscription scope (idempotent)
Set-RoleAssignment -UserObjectId $UserObjectId -SubscriptionId $SubscriptionId -RoleName 'Owner'
Set-RoleAssignment -UserObjectId $UserObjectId -SubscriptionId $SubscriptionId -RoleName 'User Access Administrator'

# Optional: Directory roles via Graph
if ($AssignDirectoryRoles) {
  Write-Log -Agent ELY -Message "Attempting Entra directory role assignment via Graph (requires sufficient privilege)."
  try {
    # Global Administrator (Company Administrator)
  Set-DirectoryRole -RoleTemplateId '62e90394-69f5-4237-9190-012177145e10' -RoleName 'Global Administrator' -UserObjectId $UserObjectId
    # Privileged Role Administrator
  Set-DirectoryRole -RoleTemplateId 'e8611ab8-c189-46e8-94e1-60213ab1f814' -RoleName 'Privileged Role Administrator' -UserObjectId $UserObjectId
  } catch {
    Write-Warning $_
    Write-Warning "Directory role assignment failed or was unauthorized. Ensure you have sufficient privileges or activate PIM roles, then retry."
  }
}

# Verification
Write-Log -Agent AIRTH -Message "Collecting verification data (φᵗ×ψʳ)."
$assignments = az role assignment list --assignee-object-id $UserObjectId --scope "/subscriptions/$SubscriptionId" --output table
Write-Host "\nSubscription-level RBAC assignments:" -ForegroundColor Yellow
$assignments | Out-String | Write-Host

try {
  $dirRoles = az rest --method GET --url "https://graph.microsoft.com/v1.0/me/transitiveMemberOf/microsoft.graph.directoryRole?$select=displayName" --output json
  $dirRoleNames = ((($dirRoles | ConvertFrom-Json).value).displayName) -join ', '
  if ($dirRoleNames) { Write-Host "Directory roles: $dirRoleNames" -ForegroundColor Yellow }
} catch {}

Write-Log -Agent ARCADIA -Message "Access weft woven; capacity for meaningful change increased (Φᴱ)."
