param(
  [string]$SiteUrl = "https://elidorascodex.sharepoint.com/sites/ElidorascodexTGCR",
  [string]$Folder = "landing",
  [string[]]$Files = @(
    "docs/templates/sharepoint/Landing_Template.html"
  ),
  [switch]$Force
)

Write-Host "[ELY] SharePoint publish preview" -ForegroundColor Cyan
Write-Host "  Site:   $SiteUrl" -ForegroundColor Gray
Write-Host "  Folder: SiteAssets/$Folder" -ForegroundColor Gray

if ($Force) {
  Write-Host "Login (device code) if needed..." -ForegroundColor Yellow
  m365 login --authType deviceCode | Out-Null
}

foreach ($f in $Files) {
  $path = Resolve-Path $f
  $cmd = @(
    "m365","spo","file","add",
    "--webUrl", $SiteUrl,
    "--folder", "SiteAssets/$Folder",
    "--path", $path,
    "--overwrite"
  )
  if ($Force) {
    Write-Host "EXEC → $($cmd -join ' ')" -ForegroundColor Green
    m365 spo file add --webUrl $SiteUrl --folder "SiteAssets/$Folder" --path $path --overwrite
  } else {
    Write-Host "DRY → $($cmd -join ' ')" -ForegroundColor DarkGray
  }
}

if (-not $Force) {
  Write-Host "Preview mode. Add -Force to execute uploads." -ForegroundColor Yellow
}
