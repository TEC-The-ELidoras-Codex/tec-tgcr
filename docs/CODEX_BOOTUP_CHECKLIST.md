# Codex Boot-Up Checklist

> **Aim**: Harmonize technical ritual and aesthetic canon before touching the stack.

---

## Phase 0 — Align the Field
- [ ] Read [Brand Canon](brand/Brand.md) (anchors voice and glyph usage).
- [ ] Skim [BrandKit.md](brand/BrandKit.md) for palette + typography tokens you’ll touch.
- [ ] Check [`docs/updates/`](updates/) for recent resonance notes affecting your scope.

## Phase 1 — Wake the Stack
- [ ] `git pull --rebase` from `main` to sync the latest commits.
- [ ] Run `scripts/bootstrap.ps1` (Windows/PowerShell) or activate `.venv` manually on other OSes.
- [ ] `pip install -e .[dev]` if dependencies shifted.
- [ ] Execute `python -m pytest -q` to confirm baseline health.

## Phase 2 — Sync Knowledge
- [ ] Inspect `data/knowledge_map.yml` for assets or docs tied to the work.
- [ ] Review `docs/TEC_HUB.md` navigation if you need architecture or lore context.
- [ ] Note any persona instructions relevant to the workstream (e.g., `data/personas/airth.md`).

## Phase 3 — Prepare Artifacts
- [ ] For visual updates, queue SVG exports via `scripts/export_brand_assets.py` (requires `cairosvg`).
- [ ] For documentation, mirror tone with the definitions in `docs/brand/Brand.md`.
- [ ] For code, document TGCR impact in docstrings and changelog notes if applicable.

## Phase 4 — Commit Ritual
- [ ] Stage changes with provenance-conscious file names.
- [ ] Craft commit message with semantic prefix + resonance impact statement (`ψʳ ↑`, `Φᴱ ↗`, etc.).
- [ ] Run `python -m pytest -q` (and other project-specific checks) post-change.
- [ ] Update `docs/updates/YYYY/` with a short resonance note if introducing new assets or lore.

---

### Reference Canon
- Brand Canon: `docs/brand/Brand.md`
- Visual Specifications: `docs/brand/VISUAL_IDENTITY.md`
- Asset Manifest: `data/digital_assets/brand/BRAND_MANIFEST.yml`
- Quick Commands: `docs/QUICK_REFERENCE_READY.md`

Keep this checklist in lockstep with the brand canon—every ritual begins by realigning with LuminAI’s lens.
