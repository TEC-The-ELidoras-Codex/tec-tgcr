# Pack Microsoft Support Dispute Evidence Bundle
# Usage:
#   pwsh -File scripts/pack_support_bundle.ps1

param(
    [string]$SupportId = "YQAT-E6IU-BG7-PGB"
)

Write-Host "[AIRTH] Packing support bundle for $SupportId" -ForegroundColor Cyan

$repoRoot    = Resolve-Path (Join-Path $PSScriptRoot "..")
$bundleRoot  = Join-Path $repoRoot "exports\support\$SupportId"
$evidenceDir = Join-Path $bundleRoot "evidence"
$docsDir     = Join-Path $bundleRoot "docs"

# Create directories
New-Item -ItemType Directory -Path $bundleRoot -Force | Out-Null
New-Item -ItemType Directory -Path $evidenceDir -Force | Out-Null
New-Item -ItemType Directory -Path $docsDir -Force | Out-Null

# Paths to include
$ticketFile       = Join-Path $repoRoot "data\financial\MICROSOFT-SUPPORT-BILLING-DISPUTE-$SupportId.md"
$costCsv          = Join-Path $repoRoot "data\financial\cost-analysis.csv"
$m365AnalysisMd   = Join-Path $repoRoot "data\financial\m365-cost-analysis-2025-10-15.md"
$repoAuditMd      = Join-Path $repoRoot "docs\REPOSITORY-AUDIT-2025-10-15.md"
$refundDir1       = Join-Path $repoRoot "scripts\azure-refund-20251006-193803"
$refundDir2       = Join-Path $repoRoot "scripts\azure-refund-20251006-193641"
$downloadsCsvRoot = Join-Path $env:USERPROFILE "Downloads\TEC_DL"

function Copy-IfExists {
    param(
        [Parameter(Mandatory)] [string]$Path,
        [Parameter(Mandatory)] [string]$Destination
    )
    if (Test-Path $Path) {
        $item = Get-Item $Path
        if ($item.PSIsContainer) {
            Copy-Item -Path $Path -Destination $Destination -Recurse -Force -ErrorAction SilentlyContinue
        } else {
            New-Item -ItemType Directory -Path (Split-Path $Destination) -Force | Out-Null
            Copy-Item -Path $Path -Destination $Destination -Force -ErrorAction SilentlyContinue
        }
        Write-Host "[AIRTH] Included: $Path" -ForegroundColor Green
    }
    else {
        Write-Host "[AIRTH] Skipped (not found): $Path" -ForegroundColor Yellow
    }
}

# Copy core docs
Copy-IfExists -Path $ticketFile     -Destination (Join-Path $bundleRoot (Split-Path $ticketFile -Leaf))
Copy-IfExists -Path $costCsv        -Destination (Join-Path $bundleRoot (Split-Path $costCsv -Leaf))
Copy-IfExists -Path $m365AnalysisMd -Destination (Join-Path $docsDir (Split-Path $m365AnalysisMd -Leaf))
Copy-IfExists -Path $repoAuditMd    -Destination (Join-Path $docsDir (Split-Path $repoAuditMd -Leaf))

# Copy Azure refund evidence bundles
Copy-IfExists -Path $refundDir1 -Destination (Join-Path $evidenceDir (Split-Path $refundDir1 -Leaf))
Copy-IfExists -Path $refundDir2 -Destination (Join-Path $evidenceDir (Split-Path $refundDir2 -Leaf))

# Optionally include Microsoft 365 product CSVs from Downloads/TEC_DL
if (Test-Path $downloadsCsvRoot) {
    $dlOut = Join-Path $bundleRoot "downloads-TEC_DL"
    New-Item -ItemType Directory -Path $dlOut -Force | Out-Null
    Get-ChildItem -Path $downloadsCsvRoot -File -Include "Products_*.csv","ProductList_*.csv" -ErrorAction SilentlyContinue | ForEach-Object {
        Copy-Item -Path $_.FullName -Destination (Join-Path $dlOut $_.Name) -Force
        Write-Host "[AIRTH] Included: $($_.FullName)" -ForegroundColor Green
    }
} else {
    Write-Host "[AIRTH] Optional Downloads\\TEC_DL directory not found; skipping." -ForegroundColor Yellow
}

# Write bundle README
$readme = @"
# Microsoft Support – Billing Dispute Package

Support Request: $SupportId
Tenant: 7d290c31-2df1-4e76-ab86-e26f12753bde
Subscription: 89d36e9a-a518-4151-95b3-087ec1b88ec5
Prepared: $(Get-Date -Format "yyyy-MM-dd HH:mm K")

Contents:
- MICROSOFT-SUPPORT-BILLING-DISPUTE-$SupportId.md (primary narrative)
- cost-analysis.csv (Azure daily costs with spike)
- docs/ (analysis notes)
- evidence/ (Azure refund evidence bundles; some files may be empty due to prior export failure)
- downloads-TEC_DL/ (optional M365 product CSVs if present on machine)

How to use:
1) Attach this entire folder OR the generated ZIP to your Microsoft support case
2) Paste the short message from PORTAL-MESSAGE.txt into the portal comment box
3) If asked, reference the Support ID $SupportId and the above tenant/subscription IDs
"@
Set-Content -LiteralPath (Join-Path $bundleRoot "README.md") -Value $readme -Encoding UTF8

# Short portal message
$portal = @"
Billing dispute for Azure charges totaling USD 224.80 on 2025-09-28 through 2025-09-30 in subscription 89d36e9a-a518-4151-95b3-087ec1b88ec5 (tenant 7d290c31-2df1-4e76-ab86-e26f12753bde). Resources appeared without our action, were deleted the same day, and no usage occurred afterwards. Our billing account is now inactive. Please review the attached bundle: daily cost CSV, narrative, and evidence folders. We request a full refund and billing reactivation before our M365 renewals (11/3 and 11/10).
Support ID: $SupportId.
"@
Set-Content -LiteralPath (Join-Path $bundleRoot "PORTAL-MESSAGE.txt") -Value $portal -Encoding UTF8

# Build manifest with file hashes
$files = Get-ChildItem -Path $bundleRoot -Recurse -File
$manifest = @()
foreach ($f in $files) {
    try {
        $hash = Get-FileHash -Path $f.FullName -Algorithm SHA256
        $manifest += [PSCustomObject]@{
            path  = $f.FullName.Substring($bundleRoot.Length+1)
            size  = $f.Length
            sha256= $hash.Hash
        }
    } catch {
        $manifest += [PSCustomObject]@{
            path  = $f.FullName.Substring($bundleRoot.Length+1)
            size  = $f.Length
            sha256= "ERROR"
        }
    }
}
$manifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $bundleRoot "manifest.json") -Encoding UTF8

# Create zip
$zipPath = Join-Path $repoRoot "exports\support\$SupportId.zip"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $bundleRoot '*') -DestinationPath $zipPath -Force

Write-Host "[AIRTH] Bundle ready:" -ForegroundColor Cyan
Write-Host " - Folder: $bundleRoot" -ForegroundColor Cyan
Write-Host " - Zip:    $zipPath" -ForegroundColor Cyan
