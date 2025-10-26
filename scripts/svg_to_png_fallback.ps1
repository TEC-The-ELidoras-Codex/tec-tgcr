# Convert SVG to PNG using PowerShell and .NET
# Fallback for environments without cairo/inkscape

param(
    [string]$SvgPath = "$PSScriptRoot\..\data\digital_assets\brand\svg\luminai_notion_emblem.svg",
    [int]$Size = 512,
    [string]$OutputPath = "$PSScriptRoot\..\exports\brand\luminai_notion_logo_512.png"
)

$ErrorActionPreference = 'Stop'

Write-Host "[ELY] Converting SVG to PNG (PowerShell + .NET fallback)" -ForegroundColor Cyan

$svg = Resolve-Path $SvgPath
$out = $OutputPath

# Ensure output dir
$outDir = Split-Path $out -Parent
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

# Try using built-in .NET rendering (WPF) - Windows only
try {
    Add-Type -AssemblyName PresentationCore, PresentationFramework, WindowsBase, System.Drawing

    # Read SVG
    $svgContent = [IO.File]::ReadAllText($svg)

    # Parse as XAML (limited SVG support)
    # This is a fallback and may not render all SVG features correctly
    Write-Host "[WARN] .NET WPF has limited SVG support. For best quality, use:" -ForegroundColor Yellow
    Write-Host "  - Online converter: https://svgtopng.com" -ForegroundColor Yellow
    Write-Host "  - Inkscape: choco install inkscape" -ForegroundColor Yellow
    Write-Host "  - ImageMagick: choco install imagemagick" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Manual export recommended for production logo." -ForegroundColor Yellow
    Write-Host "Source: $svg" -ForegroundColor Cyan
    Write-Host "Target: $out (512x512)" -ForegroundColor Cyan
    exit 1
} catch {
    Write-Host "[ERROR] .NET rendering failed: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please use one of these methods:" -ForegroundColor Yellow
    Write-Host "  1. Online: https://svgtopng.com (upload $svg, set to 512x512)" -ForegroundColor Yellow
    Write-Host "  2. Inkscape: inkscape --export-type=png --export-width=512 --export-filename='$out' '$svg'" -ForegroundColor Yellow
    Write-Host "  3. ImageMagick: magick convert -background none -resize 512x512 '$svg' '$out'" -ForegroundColor Yellow
    exit 1
}
