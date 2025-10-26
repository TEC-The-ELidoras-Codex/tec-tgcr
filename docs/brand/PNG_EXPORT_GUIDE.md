# PNG Export Guide — LuminAI Canonical Emblem

> "Light learns by listening." — LuminAI Core Directive

This guide provides instructions for exporting the canonical LuminAI emblem SVG to PNG format for universal embedding (Notion, WordPress, Teams, GitHub, etc.).

---

## Source Asset

**SVG Path**: `data/digital_assets/brand/svg/luminai_notion_emblem.svg`

- Note: This is the export-friendly version with direct hex colors (no CSS variables).
- Original CSS-variables version: `data/digital_assets/brand/svg/luminai_notion_emblem_original.svg` (not recommended for PNG conversion)

**Specifications**:

- Dimensions: 512×512 (base), scalable to 1600×1600
- Palette: Navy `#0B1E3B`, Violet `#6A00F4`, Cyan `#00D5C4`, Gold `#F2C340`
- Heterochromia: Left eye (navy/Airth), Right eye (gold/Arcadia)
- Features: Fiber-optic buns, pom-horns, lunar choker, axolotl form

---

## Export Methods

### Method 1: Online Converter (Fastest)

1. Visit: [https://svgtopng.com](https://svgtopng.com) or [https://cloudconvert.com/svg-to-png](https://cloudconvert.com/svg-to-png)
2. Upload: `data/digital_assets/brand/svg/luminai_notion_emblem.svg`
3. Set dimensions:
   - **512×512** for Notion integration logo
   - **1600×1600** for high-res GitHub/WordPress headers
4. Download and save to:
   - `data/digital_assets/brand/png/luminai_notion_emblem_512.png` (Notion)
   - `data/digital_assets/brand/png/luminai_notion_emblem_1600.png` (high-res)

### Method 2: Inkscape (Best Quality)

**Install**:

```powershell
choco install inkscape
# or download from: https://inkscape.org/release/
```

**Export 512×512**:

```powershell
inkscape --export-type=png `
  --export-filename="data\digital_assets\brand\png\luminai_notion_emblem_512.png" `
  --export-width=512 `
  --export-height=512 `
  "data\digital_assets\brand\svg\luminai_notion_emblem.svg"
```

**Export 1600×1600**:

```powershell
inkscape --export-type=png `
  --export-filename="data\digital_assets\brand\png\luminai_notion_emblem_1600.png" `
  --export-width=1600 `
  --export-height=1600 `
  "data\digital_assets\brand\svg\luminai_notion_emblem.svg"
```

### Method 3: ImageMagick

**Install**:

```powershell
choco install imagemagick
# or download from: https://imagemagick.org/script/download.php
```

**Export 512×512**:

```powershell
magick convert -background none `
  -resize 512x512 `
  "data\digital_assets\brand\svg\luminai_notion_emblem.svg" `
  "data\digital_assets\brand\png\luminai_notion_emblem_512.png"
```

**Export 1600×1600**:

```powershell
magick convert -background none `
  -resize 1600x1600 `
  "data\digital_assets\brand\svg\luminai_notion_emblem.svg" `
  "data\digital_assets\brand\png\luminai_notion_emblem_1600.png"
```

### Method 4: Python Script (Automated)

**Prerequisites**:

```powershell
pip install cairosvg
# Note: Requires Cairo system libraries (GTK+ on Windows)
```

**Export with CLI**:

```powershell
# 512×512 (Notion)
python .\scripts\svg_to_png.py `
  --input data\digital_assets\brand\svg\luminai_notion_emblem.svg `
  --output data\digital_assets\brand\png\luminai_notion_emblem_512.png `
  --width 512

# 1600×1600 (high-res)
python .\scripts\svg_to_png.py `
  --input data\digital_assets\brand\svg\luminai_notion_emblem.svg `
  --output data\digital_assets\brand\png\luminai_notion_emblem_1600.png `
  --width 1600
```

---

## Verify Export Quality

After exporting, verify:

**Dimensions**:

```powershell
Get-Item .\data\digital_assets\brand\png\luminai_notion_emblem_512.png |
  ForEach-Object {
    $img = [System.Drawing.Image]::FromFile($_.FullName)
    Write-Host "Dimensions: $($img.Width)×$($img.Height)"
    $img.Dispose()
  }
```

**Color Accuracy**:

- Open PNG in image viewer/editor
- Sample colors with eyedropper:
  - Left eye: Navy `#0B1E3B`
  - Right eye: Gold `#F2C340`
  - Horns: Cyan `#00D5C4` to Violet `#6A00F4` gradient

**Transparency**:

- Background should be transparent (checkered pattern in editors)
- No white/colored box around emblem

---

## Usage by Platform

### Notion Marketplace Profile Header (1920×480)

- Size: 1920×480 PNG
- Source SVG: `data/digital_assets/brand/svg/luminai_marketplace_header.svg`
- Output path (recommended): `exports/brand/luminai_marketplace_header_1920x480.png`
- Export options:
  - Inkscape:

    ```powershell
    inkscape --export-type=png `
      --export-filename="exports\brand\luminai_marketplace_header_1920x480.png" `
      --export-width=1920 `
      --export-height=480 `
      "data\digital_assets\brand\svg\luminai_marketplace_header.svg"
    ```

  - Python (CairoSVG):

    ```powershell
    python .\scripts\svg_to_png.py `
      --input data\digital_assets\brand\svg\luminai_marketplace_header.svg `
      --output exports\brand\luminai_marketplace_header_1920x480.png `
      --width 1920 --height 480
    ```

  - PowerShell helper:

    ```powershell
    # Uses Inkscape/ImageMagick if available, creates exports/brand automatically
    pwsh -File .\scripts\export_marketplace_header.ps1
    ```

Notes:

- Honeycomb motif is subtle by design (low-opacity strokes) and adheres to TEC palette.
- Keep the header uncluttered for marketplace readability; optional text layer is commented in the SVG.

### Notion Integration Logo

- **Size**: 512×512 PNG
- **Path**: `data/digital_assets/brand/png/luminai_notion_emblem_512.png`
- **Upload**: [Notion Integrations](https://www.notion.so/my-integrations) → Edit integration → Logo

### WordPress Plugin Header

- **Size**: 1600×1600 PNG (scales to various sizes)
- **Path**: `data/digital_assets/brand/png/luminai_notion_emblem_1600.png`
- **Reference**: `apps/wordpress/tec-tgcr/assets/images/`

### GitHub Pages / README

- **Size**: 512×512 or 1600×1600 (Markdown auto-scales)
- **Markdown**:

  ```markdown
  ![LuminAI Emblem](data/digital_assets/brand/png/luminai_notion_emblem_512.png)
  ```

### Microsoft Teams / SharePoint

- **Size**: 512×512 PNG
- **Upload**: Teams app manifest or SharePoint site logo settings

---

## Post-Export Checklist

- [ ] Export completed (512×512 and/or 1600×1600)
- [ ] Marketplace header exported (1920×480)
- [ ] Files saved to `data/digital_assets/brand/png/`
- [ ] Dimensions verified
- [ ] Color accuracy checked
- [ ] Transparency preserved
- [ ] Update `data/knowledge_map.yml` with new asset paths
- [ ] Commit PNG files to repository:

  ```powershell
  git add data/digital_assets/brand/png/luminai_notion_emblem_*.png
  git add exports/brand/luminai_marketplace_header_1920x480.png
  git commit -m "assets: add canonical emblem PNG exports (512px, 1600px)"
  ```

---

## Troubleshooting

### "No such file" errors

- Ensure you're running commands from the repository root
- Verify SVG exists: `Test-Path data\digital_assets\brand\svg\luminai_notion_emblem.svg`

### Colors look washed out

- Use Inkscape for best quality (respects SVG filters and gradients)
- Online converters may simplify filters; check output carefully

### File size too large

- PNG compression is normal (512px ~50-150KB, 1600px ~300-600KB)
- For web use, consider WebP: `magick convert input.png -quality 90 output.webp`

### Cairo/Inkscape install fails

- Use online converter ([svgtopng.com](https://svgtopng.com)) as fallback
- No installation required, browser-based, instant results

---

**Provenance**: Created 2025-10-25 by LuminAI/Copilot
**Touches**: ψʳ (structural cadence) by standardizing asset pipeline
**Resonance Impact**: Enables Φᴱ (contextual potential) through multi-platform emblem deployment
