# Export LuminAI logo to PNG for Notion integration
# Touches ψʳ (structure) by producing deployment-ready visual assets
# Requires: Inkscape or ImageMagick for SVG→PNG conversion

param(
    [string]$SourceSVG = "$PSScriptRoot\..\data\digital_assets\brand\svg\luminai_avatar_logo.svg",
    [int]$Size = 512,
    [string]$OutputDir = "$PSScriptRoot\..\exports\brand",
    [string]$OutputName = "luminai_notion_logo_512.png"
)

$ErrorActionPreference = 'Stop'

Write-Host "[ELY] Exporting Notion integration logo - $Size x $Size" -ForegroundColor Cyan

# Ensure output directory
if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

$source = Resolve-Path $SourceSVG
$output = Join-Path $OutputDir $OutputName

Write-Host "Source: $source" -ForegroundColor DarkGray
Write-Host "Output: $output" -ForegroundColor DarkGray

# Try Inkscape first (preferred for high-quality SVG conversion)
$inkscape = Get-Command inkscape -ErrorAction SilentlyContinue

if ($inkscape) {
    Write-Host "Using Inkscape..." -ForegroundColor Green
    & inkscape `
        --export-type=png `
        --export-filename="$output" `
        --export-width=$Size `
        --export-height=$Size `
        "$source"

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Export complete: $output" -ForegroundColor Green
        Get-Item $output | Select-Object Name, Length, LastWriteTime
        exit 0
    } else {
        Write-Host "Inkscape export failed (exit $LASTEXITCODE)" -ForegroundColor Yellow
    }
}

# Fallback: ImageMagick (magick convert)
$magick = Get-Command magick -ErrorAction SilentlyContinue

if ($magick) {
    Write-Host "Using ImageMagick..." -ForegroundColor Green
    & magick convert `
        -background none `
        -resize "${Size}x${Size}" `
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

# Manual fallback instructions
Write-Host "[ELY] No SVG→PNG converter found." -ForegroundColor Red
Write-Host "Options:" -ForegroundColor Yellow
Write-Host "  1. Install Inkscape: https://inkscape.org/release/" -ForegroundColor Yellow
Write-Host "  2. Install ImageMagick: https://imagemagick.org/script/download.php" -ForegroundColor Yellow
Write-Host "  3. Manual export: Open $source in a design tool and export as 512x512 PNG" -ForegroundColor Yellow
Write-Host ""
Write-Host "Expected output path: $output" -ForegroundColor Cyan
exit 1
