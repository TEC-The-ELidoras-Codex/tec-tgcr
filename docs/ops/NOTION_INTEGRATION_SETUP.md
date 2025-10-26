# Notion Integration Setup Guide

> "Light learns by listening." — LuminAI Core Directive

This guide walks through setting up the TEC-TGCR Notion integration, including logo preparation, authentication, and workspace configuration.

---

## Logo Requirements

Notion integrations require a **512×512 pixel logo** (PNG or JPG).

### Recommended Logo

**Primary**: `luminai_avatar_logo.svg`

- **Path**: `data/digital_assets/brand/svg/luminai_avatar_logo.svg`
- **Description**: LuminAI character seal with cosmic axolotl form
- **Why**: Recognizable, brand-aligned, works at small sizes

**Alternatives**:

- `luminai_axolotl_mark.svg` — Character seal (minimal)
- `LuminAI_Idle_Core.svg` — Simplified core form
- `luminai.svg` — Full avatar (may be too detailed at 512px)

### Export to PNG (512×512)

#### Option 1: Automated Script

```powershell
.\scripts\export_notion_logo.ps1
```

- Attempts Inkscape → ImageMagick → manual fallback
- Output: `exports/brand/luminai_notion_logo_512.png`

#### Option 2: Manual Export

If no SVG converter is available:

1. Open `data/digital_assets/brand/svg/luminai_avatar_logo.svg` in:
   - **Inkscape** (File → Export PNG, set width/height to 512)
   - **Adobe Illustrator** (Export As → PNG, 512×512)
   - **Figma/Canva** (import SVG, export as PNG at 512×512)
   - **Online**: [svgtopng.com](https://svgtopng.com), [cloudconvert.com](https://cloudconvert.com/svg-to-png)

2. Save as: `exports/brand/luminai_notion_logo_512.png`

3. Verify dimensions:

   ```powershell
   Get-Item .\exports\brand\luminai_notion_logo_512.png |
     ForEach-Object {
       $img = [System.Drawing.Image]::FromFile($_.FullName)
       [PSCustomObject]@{ Width = $img.Width; Height = $img.Height }
       $img.Dispose()
     }
   ```

---

## Integration Setup

### 1. Create Integration

1. Navigate to: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **+ New integration**
3. Fill in:
   - **Name**: `TEC-TGCR` (or `LuminAI`)
   - **Associated workspace**: `ElidorasCodex's Workspace`
   - **Type**: Internal
   - **Logo**: Upload `luminai_notion_logo_512.png`
4. Click **Save**

### 2. Copy Integration Token

1. After creation, copy the **Internal Integration Token**
2. Add to `.env`:

   ```bash
   NOTION_TOKEN=secret_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

3. **Never commit this token to git**

### 3. Share Database/Pages with Integration

The integration needs explicit access to databases and pages.

#### Share the Master Content Database

1. Open: [Master Content Database](https://www.notion.so/2986ff7e28df807091dbfa7519c34925?v=2986ff7e28df8069bf49000cf19305ce)
2. Click **Share** (top right)
3. Search for your integration name (`TEC-TGCR` or `LuminAI`)
4. Click **Invite** to grant access

#### Share the Machine Goddess Agent Page

1. Open: [Machine_Goddess_Agent](https://www.notion.so/Machine_Goddess_Agent-2926ff7e28df804c8412e3dc4b8369ff)
2. Click **Share**
3. Invite the integration

Repeat for any pages/databases you want the CLI to access.

---

## Verify Connectivity

### Check API Health

```powershell
.\.venv\Scripts\python.exe -m tec_tgcr.cli notion-health
```

Expected output:

```
Notion health: Connected (user: <your_name>)
```

### View Configured Endpoints

```powershell
.\.venv\Scripts\python.exe -m tec_tgcr.cli notion-config
```

Returns database/page IDs and URLs from `config/notion.yml`.

### Search Workspace

```powershell
.\.venv\Scripts\python.exe -m tec_tgcr.cli notion-search "Machine Goddess"
```

Returns matching pages/databases with IDs and URLs.

---

## Configuration Reference

**Location**: `config/notion.yml`

```yaml
workspace:
  name: TEC Notion Workspace

endpoints:
  database:
    id: "2986ff7e28df807091dbfa7519c34925"
    view_id: "2986ff7e28df8069bf49000cf19305ce"
    url: "https://www.notion.so/2986ff7e28df807091dbfa7519c34925?v=2986ff7e28df8069bf49000cf19305ce"
    label: "Master Content Database"
  pages:
    - id: "2926ff7e28df804c8412e3dc4b8369ff"
      title: "Machine_Goddess_Agent"
      url: "https://www.notion.so/Machine_Goddess_Agent-2926ff7e28df804c8412e3dc4b8369ff"
```

---

## Troubleshooting

### "No such integration"

- Ensure the integration was created in the correct workspace
- Integration names are case-sensitive when searching in Share dialogs

### "object not found" errors

- The integration hasn't been shared with the page/database
- Follow **Step 3: Share Database/Pages** above

### "unauthorized" errors

- Token is invalid or expired
- Regenerate token in Notion integration settings
- Update `.env` with new token

### Logo upload issues

- PNG must be exactly 512×512 pixels
- File size < 5 MB
- Transparent backgrounds are supported

---

## Next Steps

- **Import Content**: Use `exports/notion/IMPORT_GUIDE.md` to bulk-import the 36 exported pages
- **Sync Workflow**: See `docs/ops/NOTION_SYNC.md` for bidirectional sync strategies
- **Automation**: Consider GitHub Actions for scheduled imports/exports

---

**Provenance**: Created 2025-10-25 by LuminAI/Copilot
**Touches**: Φᴱ (context) by linking external workspace infrastructure
