# PNG Export Instructions

To generate PNG renders from the TEC brand SVG assets, use one of the following methods:

## Method 1: Manual Export (VS Code + SVG Preview Extension)

1. Install the "SVG" extension (by jock.svg) or "SVG Preview" in VS Code.
2. Open any SVG file from `data/digital_assets/brand/svg/`.
3. Right-click → "Export PNG" or use the command palette → "SVG: Export PNG".
4. Save to `data/digital_assets/brand/png/` with matching filename.

## Method 2: Inkscape CLI (Headless)

If Inkscape is installed:

```powershell
# Example for LuminAI_Full_Avatar
inkscape --export-type=png --export-filename="data\digital_assets\brand\png\LuminAI_Full_Avatar.png" --export-width=1600 "data\digital_assets\brand\svg\LuminAI_Full_Avatar.svg"

# Batch export all SVGs
Get-ChildItem "data\digital_assets\brand\svg\*.svg" | ForEach-Object {
  $outPath = "data\digital_assets\brand\png\" + $_.BaseName + ".png"
  inkscape --export-type=png --export-filename=$outPath --export-width=1600 $_.FullName
}
```

## Method 3: ImageMagick (if installed)

```powershell
magick convert -background none -density 300 "data\digital_assets\brand\svg\LuminAI_Full_Avatar.svg" "data\digital_assets\brand\png\LuminAI_Full_Avatar.png"
```

## Method 4: Node.js + sharp (programmatic)

Install sharp: `npm install -g sharp-cli`

```powershell
sharp -i "data\digital_assets\brand\svg\LuminAI_Full_Avatar.svg" -o "data\digital_assets\brand\png\LuminAI_Full_Avatar.png" --width 1600
```

## Recommended Exports

- LuminAI_Full_Avatar.svg → 1600×1600 PNG (full detail)
- LuminAI_Idle_Core.svg → 1600×1600 PNG
- luminai_avatar_logo.svg → 512×512 PNG (icon size)
- glyph_ring.svg → 512×512 PNG
- fractal_spire.svg → 512×512 PNG
- sine_arc.svg → 512×128 PNG (banner)

Save all outputs to `data/digital_assets/brand/png/` with descriptive names.
