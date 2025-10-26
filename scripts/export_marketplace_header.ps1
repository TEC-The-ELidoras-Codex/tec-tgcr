<#
 .SYNOPSIS
  Export the Notion Marketplace profile header PNG (1920×480) from the canonical SVG.

 .DESCRIPTION
  Prefers Inkscape, falls back to ImageMagick. Creates exports/brand if needed.
  Touches ψʳ (structure) by standardizing marketplace asset generation.

 .PARAMETER SourceSVG
  Path to the source SVG header.

 .PARAMETER Width
  Output width (default 1920).

 .PARAMETER Height
  Output height (default 480).

 .PARAMETER OutputDir
  Directory to place the exported PNG.

 .PARAMETER OutputName
  File name for the exported PNG.
#>
param(
    [string]$SourceSVG = "$PSScriptRoot\..\data\digital_assets\brand\svg\luminai_marketplace_header.svg",
    [int]$Width = 1920,
    [int]$Height = 480,
    [string]$OutputDir = "$PSScriptRoot\..\exports\brand",
    [string]$OutputName = "luminai_marketplace_header_1920x480.png"
)

$ErrorActionPreference = 'Stop'

Write-Host "[ELY] Exporting Notion marketplace header - ${Width}x${Height}" -ForegroundColor Cyan

if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

$source = Resolve-Path $SourceSVG
$output = Join-Path $OutputDir $OutputName

Write-Host "Source: $source" -ForegroundColor DarkGray
Write-Host "Output: $output" -ForegroundColor DarkGray

$inkscape = Get-Command inkscape -ErrorAction SilentlyContinue
if ($inkscape) {
    Write-Host "Using Inkscape..." -ForegroundColor Green
    & inkscape `
        --export-type=png `
        --export-filename="$output" `
        --export-width=$Width `
        --export-height=$Height `
        "$source"

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Export complete: $output" -ForegroundColor Green
        Get-Item $output | Select-Object Name, Length, LastWriteTime
        exit 0
    } else {
        Write-Host "Inkscape export failed (exit $LASTEXITCODE)" -ForegroundColor Yellow
    }
}

$magick = Get-Command magick -ErrorAction SilentlyContinue
if ($magick) {
    Write-Host "Using ImageMagick..." -ForegroundColor Green
    & magick convert `
        -background none `
        -resize "${Width}x${Height}!" `
        "$source" `
        "$output"

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Export complete: $output" -ForegroundColor Green
        Get-Item $output | Select-Object Name, Length, LastWriteTime
        exit 0
    } else {
        Write-Host "ImageMagick export failed (exit $LASTEXITCODE)" -ForegroundColor Yellow
    }
}

Write-Host "[ELY] No SVG→PNG converter found." -ForegroundColor Red
Write-Host "Options:" -ForegroundColor Yellow
Write-Host "  1. Install Inkscape: https://inkscape.org/release/" -ForegroundColor Yellow
Write-Host "  2. Install ImageMagick: https://imagemagick.org/script/download.php" -ForegroundColor Yellow
Write-Host "  3. Manual export: Open $source in a design tool and export as ${Width}x${Height} PNG" -ForegroundColor Yellow
Write-Host ""
Write-Host "Expected output path: $output" -ForegroundColor Cyan
exit 1
