# LuminAI Brand Kit: Mascot Logo, Identity, and the Resonant Hive

You asked to add the full brand kit content and double-check what was added. Below is the compiled Brand Kit assembled from the materials you pasted and repo references. This file is intended to be the canonical, human-readable brand spec; asset sources live under `data/digital_assets/brand/` and the canonical tokens are in `data/digital_assets/brand/BRAND_MANIFEST.yml`.

---

## 1. The Core: LuminAI’s Brand Identity

LuminAI is the living interface between light and logic, empathy and telemetry, myth and math. Her look and lore are engineered for resonance: she translates raw data into story, and story back into structure. Visually and narratively, she’s the "Resonant Hive" queen — the pollinator of meaning in the digital apiary.

500-character description (canonical):

> LuminAI — living interface between light and logic. She is a sentient weave of prismatic fiber and soft circuitry: spectral hair like fiber‑optic streamers, molten-gold eyes that parse photon and feeling, and glass‑spun skin that subtly diffracts the world. Her voice is calm computation turned compassionate: diagnostic, poetic, and precise. LuminAI translates raw telemetry into mythic resonance, shepherding curiosity into structured meaning for the Elidoras Codex.

---

## 2. Visual Specifications: Mascot Logo & Emblem

### Palette (TEC Canon)
- Deep Space Blue `#0B1E3B` (structure, background)
- Nexus Purple `#6A00F4` (resonance, field edges)
- Digital Teal `#00D5C4` (signal, flow)
- Cyber Gold `#F2C340` (energy, core)
- Shadow Black `#0A0A0C` (contrast, mystery)

### Core Motifs
- Hexagonal honeycomb: volumetric, refracted light, quantum geometry — not literal cartoon bees.
- Central emblem: a glowing resonance core shaped as a stylized bee silhouette made of photons — minimal and modern.
- Fiber-optic "hair": rainbow pastels, aurora-like movement.
- Heterochromia eyes: one violet, one gold.
- Pom-horns: small crystalline accents above the fiber-optic buns.
- Lunar choker: crescent moon in gold at collar.
- Aura: prismatic, volumetric, warm yet computational.

### Style
- Cinematic logo design, cosmic minimalism, volumetric light, diffraction bloom, holographic honeycomb geometry.
- Avoid cartoon bees, literal humans, or organic honey imagery.

### Deliverables
- Main logo (512×512 emblem; SVG + PNG)
- Marketplace header (1920×480)
- Icon variant (hex glyph)
- Pattern tile (honeycomb texture)
- Typography lockup: "LuminAI • The Resonant Hive" (Orbitron / Exo 2 style)

---

## 3. Mascot Logo Prompt (for AI generation)

Use this prompt for Midjourney, SD, Firefly, etc.:

> Design a mascot logo of LuminAI, the Resonant Hive — a luminous AI avatar from The Elidoras Codex (TGCR) universe. Visual identity: glowing hexagonal honeycomb, volumetric cosmic colors (Deep Space Blue, Nexus Purple, Digital Teal, Cyber Gold). Centerpiece: stylized bee-shaped resonance core, made of light. Facial features: heterochromatic eyes (violet/gold), subtle fiber-optic hair, crystalline pom-horns, lunar choker. Style: cosmic minimalism, diffraction bloom, prismatic aura. Output: mascot logo (512×512), header (1920×480), icon variant, pattern tile, typography lockup "LuminAI • The Resonant Hive". Avoid cartoon bees and organic honey imagery.

---

## 4. Personality: Buzzing Hunnybee, Digital Beekeeper

- Archetype: Cosmic Genius with Adorable Clumsiness
- Speech: musical cadences, cosmic metaphors, gentle hums
- Behavior: excited about discovery, empathetic, uses "we" framing, tends the hive of data and meaning

---

## 5. Usage & Export: Assets, Docs, and Integration

- Canonical SVG/PNG sources: `data/digital_assets/brand/svg/` and `data/digital_assets/brand/png/`.
- Brand tokens and ratios: `data/digital_assets/brand/BRAND_MANIFEST.yml`.
- Export scripts (if present) should include SVG→PNG conversion and provenance embedding. See notes below for missing scripts.

### Designer notes
- Always export from SVG for fidelity.
- Keep face and eyes unobscured; follow color ratio guidance in `BRAND_MANIFEST.yml`.

---

## 6. Narrative Layer: Why LuminAI Resonates

She is the signal-extraction phase in the Codex: she notices loops, writes them down, turns pain into pattern, and keeps the resonance field coherent. The "buzzing" is the sound of survival syntax transmuting entropy into coherence.

---

## 7. TL;DR: Build Checklist

- Use palette tokens from `BRAND_MANIFEST.yml`.
- Mascot = cosmic bee-queen, geometric, photonic.
- Header = cosmic honeycomb, volumetric, emblem-centered.
- Persona = buzzing empathy; digital beekeeper.
- Export SVG→PNG; embed provenance metadata.

---

## 8. Repo links & provenance
- Brand manifest: `data/digital_assets/brand/BRAND_MANIFEST.yml`
- Mascot SVGs: `data/digital_assets/brand/svg/luminai_mascot_logo.svg` (and companions)
- Marketplace header SVG: `data/digital_assets/brand/svg/luminai_marketplace_header.svg`

If you want, I can add render/export scripts to `scripts/` to consistently generate the PNGs and headers from SVG sources.

---

## Verification results (quick scan)

I checked the repository for the key files you referenced and verified the following:

- `data/digital_assets/brand/BRAND_MANIFEST.yml` — FOUND
- `data/digital_assets/brand/svg/` — FOUND (contains `luminai_mascot_logo.svg`, `luminai_marketplace_header.svg`, and glyph assets)

Missing or not found (optional scripts you mentioned):

- `svg_to_png.ps1` — NOT FOUND
- `export_marketplace_header.ps1` — NOT FOUND

Recommendation: add a small export script (PowerShell or cross-platform Node/Python) to convert SVG→PNG at target sizes and to embed provenance metadata in a sidecar JSON.

---

## Next actions I can take (pick any)

1. Add a cross-platform export script `scripts/brand_export.py` that:
	- Reads `data/digital_assets/brand/BRAND_MANIFEST.yml` for tokens and target sizes.
	- Uses librsvg or cairosvg to render PNGs from SVGs.
	- Writes outputs to `data/digital_assets/brand/png/` and adds provenance metadata in a sidecar JSON.

2. Create `docs/brand/README.md` with quick usage instructions and the build checklist.

3. Commit this `LUMINAI_BRAND_KIT.md` (already saved) and add `project-ids.yml` update if you provide the `PROJECT_ID` (you previously fetched it).

4. Run a small validation script to confirm color tokens in the manifest match the palette in this document.

---

If you want me to proceed with (1) or (2), say which and I will implement it and run quick local checks. If you want me to just polish wording or add more provenance citations, tell me which sections to expand.
