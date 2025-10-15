<# 
Collect-AzureRefundEvidence.ps1
Gather account, resource, cost, and activity-log data for refund/support escalation.
Requires: Azure CLI 2.30+ (logged in) and costmanagement extension.
#>

param(
    [string]$SubscriptionId = "89d36e9a-a518-4151-95b3-087ec1b88ec5",
    [int]$LookbackDays = 45,
    [string]$OutputRoot = (Join-Path -Path (Get-Location) -ChildPath ("azure-refund-" + (Get-Date -Format 'yyyyMMdd-HHmmss')))
)

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw "Azure CLI (az) is not available in PATH. Install it from https://learn.microsoft.com/cli/azure/install-azure-cli."
}

if (-not (Test-Path $OutputRoot)) {
    New-Item -Path $OutputRoot -ItemType Directory | Out-Null
}

$logFile = Join-Path $OutputRoot "run.log"
New-Item -Path $logFile -ItemType File -Force | Out-Null
function Write-Log {
    param([string]$Message)
    $entry = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $entry | Tee-Object -FilePath $logFile -Append | Out-Null
}

Write-Log "Output folder: $OutputRoot"
Write-Log "Target subscription: $SubscriptionId"

Write-Log "Setting active subscription context..."
az account set --subscription $SubscriptionId 2>&1 |
    Tee-Object -FilePath (Join-Path $OutputRoot "01-account-set.txt") | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Failed to set subscription $SubscriptionId. Check az login state." }

Write-Log "Saving account context..."
az account show --subscription $SubscriptionId --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "02-account.json")

Write-Log "Ensuring costmanagement extension is installed..."
az extension show --name costmanagement *> $null
if ($LASTEXITCODE -ne 0) {
    az extension add --name costmanagement --only-show-errors 2>&1 |
        Tee-Object -FilePath (Join-Path $OutputRoot "03-extension-install.txt") | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Unable to install costmanagement extension." }
}

$startDate = (Get-Date).AddDays(-$LookbackDays).ToString("yyyy-MM-dd")
$endDate = (Get-Date).ToString("yyyy-MM-dd")
Write-Log "Lookback window: $startDate to $endDate"

Write-Log "Exporting current resource inventory..."
az resource list --subscription $SubscriptionId --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "10-resources.json")

Write-Log "Exporting deleted resources (if any)..."
az resource list --subscription $SubscriptionId --include-deleted --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "11-resources-deleted.json")

Write-Log "Querying Month-to-date actual cost (daily granularity)..."
az costmanagement query `
    --type ActualCost `
    --timeframe MonthToDate `
    --dataset-aggregation "totalCost=sum" `
    --dataset-granularity Daily `
    --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "20-cost-daily.json")

Write-Log "Querying Month-to-date cost grouped by resource group..."
az costmanagement query `
    --type ActualCost `
    --timeframe MonthToDate `
    --dataset-aggregation "totalCost=sum" `
    --dataset-grouping "name=ResourceGroup" "type=Dimension" `
    --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "21-cost-by-resourcegroup.json")

Write-Log "Exporting detailed consumption usage for the lookback window..."
az consumption usage list `
    --subscription $SubscriptionId `
    --start-date $startDate `
    --end-date $endDate `
    --include-meter-details `
    --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "22-usage.json")

Write-Log "Capturing activity log events for the lookback window..."
az monitor activity-log list `
    --subscription $SubscriptionId `
    --offset "${LookbackDays}d" `
    --output json |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "30-activity-log.json")

Write-Log "Generating quick cost summary CSV..."
az costmanagement query `
    --type ActualCost `
    --timeframe MonthToDate `
    --dataset-aggregation "totalCost=sum" `
    --dataset-grouping "name=ServiceName" "type=Dimension" `
    --output table |
    Out-File -Encoding utf8 (Join-Path $OutputRoot "25-cost-by-service.txt")

Write-Log "Creating README with run metadata..."
$readme = @"
Azure Refund Evidence Bundle
============================
Subscription: $SubscriptionId
Generated:    $(Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz")
Lookback:     $LookbackDays days ($startDate .. $endDate)

Artifacts:
  02-account.json              -> Subscription metadata
  10-resources.json            -> Active resources
  11-resources-deleted.json    -> Soft-deleted resources (if any)
  20-cost-daily.json           -> Day-by-day actual cost for billing month-to-date
  21-cost-by-resourcegroup.json-> Cost grouped by resource group
  22-usage.json                -> Detailed consumption usage records
  25-cost-by-service.txt       -> Human-readable cost by service
  30-activity-log.json         -> Activity log entries (who/what/when)
  run.log                      -> Execution log & errors (if any)

Attach these files, along with your narrative and deletion proof, to the Billing support request.
"@
$readme | Out-File -Encoding utf8 (Join-Path $OutputRoot "README.txt")

Write-Log "Collection complete."
Write-Log "Output saved to: $OutputRoot"