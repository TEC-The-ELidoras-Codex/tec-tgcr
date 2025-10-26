# Organization Update — 2025-10-26

> “Light learns by listening.” — LuminAI

This update strengthens ψʳ (structure) through a standardized marketplace/brand asset pipeline and improves Φᴱ (context) by aligning SharePoint/Notion publishing templates.

---

## What changed

- Brand asset: Added Notion Marketplace header SVG (1920×480) with subtle honeycomb motif
  - `data/digital_assets/brand/svg/luminai_marketplace_header.svg`
- Export workflow: Extended PNG export guide to include marketplace header
  - `docs/brand/PNG_EXPORT_GUIDE.md` (new section + checklist item)
- One-shot export helper: PowerShell script for 1920×480 PNG
  - `scripts/export_marketplace_header.ps1`
- Knowledge map: Registered header SVG and expected PNG output
  - `data/knowledge_map.yml`
- Publishing templates (recap):
  - Notion templates: `docs/templates/notion/Resonance_Brief.md`, `docs/templates/notion/Release_Summary.md`
  - SharePoint templates: `docs/templates/sharepoint/Landing_Template.html`, `docs/templates/sharepoint/Briefing_Pack.md`
  - SharePoint publish helper: `scripts/publish_sharepoint.ps1`

## Why it matters

- Consistent visuals: Marketplace presence matches TEC palette and motif without crowding UI
- Deterministic export: Single command path to generate header and emblem PNGs
- Cross-channel coherence: Notion + SharePoint templates keep φᵗ/ψʳ/Φᴱ front-and-center

## How to use

- Export marketplace header PNG (recommended)

  ```powershell
  pwsh -File .\scripts\export_marketplace_header.ps1
  ```

  Output: `exports/brand/luminai_marketplace_header_1920x480.png`

- Export emblem PNGs (see guide for more options)

  ```powershell
  # 512×512 and 1600×1600 via Inkscape (example)
  inkscape --export-type=png --export-width=512  data\digital_assets\brand\svg\luminai_notion_emblem.svg -o data\digital_assets\brand\png\luminai_notion_emblem_512.png
  inkscape --export-type=png --export-width=1600 data\digital_assets\brand\svg\luminai_notion_emblem.svg -o data\digital_assets\brand\png\luminai_notion_emblem_1600.png
  ```

- Publish SharePoint landing page (preview, then force)

  ```powershell
  pwsh -File .\scripts\publish_sharepoint.ps1
  pwsh -File .\scripts\publish_sharepoint.ps1 -Force
  ```

## Cleanup

- Repo reorg: moved top-level guides and configs into docs/ and config/; references auto-updated.
- Legacy folders: removed root 'archives/' (duplicate of data/archives) and 'assets/' (avatar duplicates); canonicalized to data/digital_assets/.
- Emblem variants: archived older 'luminai_notion_emblem_*' variants to data/archives/svg and updated docs/knowledge_map; keep 'luminai_notion_emblem.svg' as canonical.
- Knowledge map: pruned stale PNG entries and non-existent exports to prevent broken links.

## Status

- Tests: `pytest -q` — PASS
- Secrets: None added; follow `docs/ops/LOCAL_SECRETS.md` for local env
- Breaking changes: None

## Next steps

- Notion: Share the integration with “Master Content Database” and bulk-import the 36 docs (exports/notion)
- Assets: Export and upload marketplace header to Notion profile; verify fit/crop
- Optional: Provide alt header variants (denser/sparser hex lines) if needed

— LuminAI / Copilot
