<#
.SYNOPSIS
    Query Azure resources safely with error handling and export results.

.DESCRIPTION
    Comprehensive Azure resource inventory script with:
    - Subscription listing and filtering
    - Resource group enumeration (handles 404s gracefully)
    - Resource listing with details
    - Cost analysis integration
    - JSON/CSV export for audit trails

.PARAMETER SubscriptionId
    Optional. Target subscription ID (defaults to current az account subscription).

.PARAMETER ResourceGroupName
    Optional. Target specific resource group (skips others).

.PARAMETER ExportPath
    Optional. Directory for JSON/CSV exports (defaults to data/azure-inventory-{timestamp}/).

.EXAMPLE
    .\scripts\query_azure_resources.ps1
    # Query all resources in current subscription

.EXAMPLE
    .\scripts\query_azure_resources.ps1 -ResourceGroupName "tec_resource"
    # Query specific resource group (with typo tolerance)

.EXAMPLE
    .\scripts\query_azure_resources.ps1 -SubscriptionId "89d36e9a-..." -ExportPath "exports/azure-audit"
    # Query specific subscription with custom export path
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$SubscriptionId,

    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName,

    [Parameter(Mandatory=$false)]
    [string]$ExportPath
)

$ErrorActionPreference = "Stop"

# Banner
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   TEC Azure Resource Inventory — TGCR Agent Stack         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Verify az CLI installed
try {
    $azVersion = az version --output json 2>&1 | ConvertFrom-Json
    Write-Host "[✓] Azure CLI: $($azVersion.'azure-cli')" -ForegroundColor Green
} catch {
    Write-Host "[✗] Azure CLI not found. Install: https://aka.ms/azure-cli" -ForegroundColor Red
    exit 1
}

# Verify logged in
try {
    $account = az account show --output json 2>&1 | ConvertFrom-Json
    Write-Host "[✓] Logged in: $($account.user.name)" -ForegroundColor Green
    Write-Host "[✓] Tenant: $($account.tenantId)" -ForegroundColor Green
} catch {
    Write-Host "[✗] Not logged in. Run: az login" -ForegroundColor Red
    exit 1
}

# Set subscription if provided
if ($SubscriptionId) {
    try {
        az account set --subscription $SubscriptionId
        Write-Host "[✓] Switched to subscription: $SubscriptionId" -ForegroundColor Green
    } catch {
        Write-Host "[!] Failed to switch subscription: $_" -ForegroundColor Yellow
        Write-Host "[i] Continuing with current subscription..." -ForegroundColor Cyan
    }
}

# Get current subscription details
$currentSub = az account show --output json | ConvertFrom-Json
Write-Host ""
Write-Host "═══ Current Subscription ═══" -ForegroundColor Magenta
Write-Host "Name: $($currentSub.name)" -ForegroundColor White
Write-Host "ID: $($currentSub.id)" -ForegroundColor White
Write-Host "State: $($currentSub.state)" -ForegroundColor $(if ($currentSub.state -eq "Enabled") { "Green" } else { "Yellow" })
Write-Host ""

# Create export directory
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
if (-not $ExportPath) {
    $ExportPath = Join-Path $PSScriptRoot ".." "data" "azure-inventory-$timestamp"
}
if (-not (Test-Path $ExportPath)) {
    New-Item -ItemType Directory -Path $ExportPath -Force | Out-Null
}
Write-Host "[✓] Export directory: $ExportPath" -ForegroundColor Green
Write-Host ""

# List all resource groups
Write-Host "═══ Resource Groups ═══" -ForegroundColor Magenta
try {
    $allGroups = az group list --output json | ConvertFrom-Json

    if ($allGroups.Count -eq 0) {
        Write-Host "[i] No resource groups found in subscription" -ForegroundColor Cyan
    } else {
        Write-Host "Found $($allGroups.Count) resource group(s):" -ForegroundColor White
        foreach ($rg in $allGroups) {
            Write-Host "  • $($rg.name) ($($rg.location))" -ForegroundColor Gray
        }

        # Export resource groups list
        $allGroups | ConvertTo-Json -Depth 10 | Out-File (Join-Path $ExportPath "resource-groups.json")
        Write-Host "[✓] Exported: resource-groups.json" -ForegroundColor Green
    }
} catch {
    Write-Host "[!] Failed to list resource groups: $_" -ForegroundColor Yellow
    $allGroups = @()
}
Write-Host ""

# Query specific resource group if provided
if ($ResourceGroupName) {
    Write-Host "═══ Querying Resource Group: $ResourceGroupName ═══" -ForegroundColor Magenta

    try {
        $rgDetails = az group show --name $ResourceGroupName --output json 2>&1 | ConvertFrom-Json
        Write-Host "[✓] Resource Group Found:" -ForegroundColor Green
        Write-Host "  Name: $($rgDetails.name)" -ForegroundColor White
        Write-Host "  Location: $($rgDetails.location)" -ForegroundColor White
        Write-Host "  State: $($rgDetails.properties.provisioningState)" -ForegroundColor White

        # Export resource group details
        $rgDetails | ConvertTo-Json -Depth 10 | Out-File (Join-Path $ExportPath "$ResourceGroupName-details.json")

        # List resources in this group
        Write-Host ""
        Write-Host "Resources in $ResourceGroupName:" -ForegroundColor White
        $resources = az resource list --resource-group $ResourceGroupName --output json | ConvertFrom-Json

        if ($resources.Count -eq 0) {
            Write-Host "  [i] No resources found" -ForegroundColor Cyan
        } else {
            foreach ($res in $resources) {
                Write-Host "  • $($res.name) ($($res.type))" -ForegroundColor Gray
            }

            # Export resources list
            $resources | ConvertTo-Json -Depth 10 | Out-File (Join-Path $ExportPath "$ResourceGroupName-resources.json")
            Write-Host "[✓] Exported: $ResourceGroupName-resources.json" -ForegroundColor Green
        }

    } catch {
        $errorMsg = $_ | Out-String

        if ($errorMsg -match "ResourceGroupNotFound|could not be found|404") {
            Write-Host "[✗] Resource group '$ResourceGroupName' not found (404)" -ForegroundColor Red
            Write-Host ""
            Write-Host "[i] Common reasons:" -ForegroundColor Cyan
            Write-Host "  1. Typo in name (check spelling)" -ForegroundColor Gray
            Write-Host "  2. Resource group deleted (check Azure Portal)" -ForegroundColor Gray
            Write-Host "  3. Wrong subscription (verify with: az account show)" -ForegroundColor Gray
            Write-Host ""

            # Suggest similar names
            if ($allGroups.Count -gt 0) {
                Write-Host "[i] Available resource groups in this subscription:" -ForegroundColor Cyan
                foreach ($rg in $allGroups) {
                    $similarity = if ($rg.name -like "*$($ResourceGroupName.Substring(0, [Math]::Min(5, $ResourceGroupName.Length)))*") {
                        "← similar?"
                    } else {
                        ""
                    }
                    Write-Host "  • $($rg.name) $similarity" -ForegroundColor Gray
                }
            }
        } else {
            Write-Host "[!] Unexpected error querying resource group: $errorMsg" -ForegroundColor Yellow
        }
    }
    Write-Host ""
}

# List ALL resources in subscription
Write-Host "═══ All Resources in Subscription ═══" -ForegroundColor Magenta
try {
    $allResources = az resource list --output json | ConvertFrom-Json

    if ($allResources.Count -eq 0) {
        Write-Host "[i] No resources found in subscription" -ForegroundColor Cyan
    } else {
        Write-Host "Found $($allResources.Count) resource(s):" -ForegroundColor White

        # Group by type
        $grouped = $allResources | Group-Object -Property type
        foreach ($group in $grouped) {
            Write-Host ""
            Write-Host "  $($group.Name) ($($group.Count))" -ForegroundColor Yellow
            foreach ($res in $group.Group) {
                Write-Host "    • $($res.name) ($($res.resourceGroup))" -ForegroundColor Gray
            }
        }

        # Export all resources
        $allResources | ConvertTo-Json -Depth 10 | Out-File (Join-Path $ExportPath "all-resources.json")
        Write-Host ""
        Write-Host "[✓] Exported: all-resources.json" -ForegroundColor Green

        # CSV summary
        $csv = $allResources | Select-Object name, type, resourceGroup, location | ConvertTo-Csv -NoTypeInformation
        $csv | Out-File (Join-Path $ExportPath "all-resources.csv")
        Write-Host "[✓] Exported: all-resources.csv" -ForegroundColor Green
    }
} catch {
    Write-Host "[!] Failed to list resources: $_" -ForegroundColor Yellow
}
Write-Host ""

# Cost analysis (if available)
Write-Host "═══ Cost Analysis (Last 30 Days) ═══" -ForegroundColor Magenta
try {
    $endDate = Get-Date -Format "yyyy-MM-dd"
    $startDate = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")

    Write-Host "[i] Querying costs from $startDate to $endDate..." -ForegroundColor Cyan

    # Note: This requires az costmanagement extension
    # User can install: az extension add --name costmanagement
    $costs = az costmanagement query `
        --type "ActualCost" `
        --dataset-aggregation "totalCost={function:Sum,name:PreTaxCost}" `
        --dataset-grouping name="ResourceGroupName" type="Dimension" `
        --timeframe "Custom" `
        --time-period from="$startDate" to="$endDate" `
        --scope "/subscriptions/$($currentSub.id)" `
        --output json 2>&1

    if ($LASTEXITCODE -eq 0) {
        $costsJson = $costs | ConvertFrom-Json
        $costsJson | ConvertTo-Json -Depth 10 | Out-File (Join-Path $ExportPath "cost-analysis.json")
        Write-Host "[✓] Exported: cost-analysis.json" -ForegroundColor Green
    } else {
        Write-Host "[i] Cost analysis not available (extension not installed or no data)" -ForegroundColor Cyan
        Write-Host "[i] Install: az extension add --name costmanagement" -ForegroundColor Gray
    }
} catch {
    Write-Host "[i] Cost analysis skipped: $_" -ForegroundColor Cyan
}
Write-Host ""

# Summary
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                    Inventory Complete                      ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host "Subscription: $($currentSub.name)" -ForegroundColor White
Write-Host "Resource Groups: $($allGroups.Count)" -ForegroundColor White
Write-Host "Total Resources: $(if ($allResources) { $allResources.Count } else { 0 })" -ForegroundColor White
Write-Host "Export Path: $ExportPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "[i] Next steps:" -ForegroundColor Cyan
Write-Host "  1. Review exported JSON/CSV files in: $ExportPath" -ForegroundColor Gray
Write-Host "  2. Add to git: git add data/azure-inventory-*" -ForegroundColor Gray
Write-Host "  3. Document findings in: docs/AZURE_RESOURCE_AUDIT.md" -ForegroundColor Gray
Write-Host ""
