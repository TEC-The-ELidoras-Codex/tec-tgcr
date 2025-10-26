# PNG Asset Directory

This directory contains PNG exports of the canonical LuminAI emblem for universal embedding (Notion, WordPress, Teams, GitHub, etc.).

## Export Workflow

See: `exports/brand/PNG_EXPORT_GUIDE.md` for complete export instructions.

## Expected Assets

- `luminai_notion_emblem_512.png` — 512×512 PNG for Notion integration logo
- `luminai_notion_emblem_1600.png` — 1600×1600 PNG for high-res headers/banners

## Generation Commands

**Using online converter** (fastest):
1. Visit [https://svgtopng.com](https://svgtopng.com)
2. Upload `data/digital_assets/brand/svg/luminai_notion_emblem.svg`
3. Set dimensions (512 or 1600)
4. Download and save here

**Using Python script**:
```powershell
# 512×512
python .\scripts\svg_to_png.py `
  --input data\digital_assets\brand\svg\luminai_notion_emblem.svg `
  --output data\digital_assets\brand\png\luminai_notion_emblem_512.png `
  --width 512

# 1600×1600
python .\scripts\svg_to_png.py `
  --input data\digital_assets\brand\svg\luminai_notion_emblem.svg `
  --output data\digital_assets\brand\png\luminai_notion_emblem_1600.png `
  --width 1600
```

**Using Inkscape**:
```powershell
inkscape --export-type=png `
  --export-filename="data\digital_assets\brand\png\luminai_notion_emblem_512.png" `
  --export-width=512 `
  --export-height=512 `
  "data\digital_assets\brand\svg\luminai_notion_emblem.svg"
```

## Quality Standards

- Transparency: Preserved (no background)
- Colors: TEC palette (`#0B1E3B`, `#6A00F4`, `#00D5C4`, `#F2C340`)
- Filters: Cyan/gold glow effects must be visible
- Format: PNG with alpha channel

## Provenance

Created: 2025-10-25 by LuminAI/Copilot  
Touches: ψʳ (structure) via asset pipeline standardization
