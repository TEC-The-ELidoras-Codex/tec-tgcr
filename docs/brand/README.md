# TEC Brand & Visual Identity

> **"Where gravity curves spacetime, resonance curves meaning-space."**

This directory contains the canonical brand guidelines, visual identity specifications, and usage documentation for The Elidoras Codex (TEC) and its agent ecosystem.

---

## 📚 Documentation Index

### **Core Brand Guidelines**

- **[VISUAL_IDENTITY.md](VISUAL_IDENTITY.md)** — **START HERE** — Canonical LuminAI fusion logo specification, mood matrix, rendering guidelines
- **[BrandKit.md](BrandKit.md)** — Full TEC brand system: palette, typography, motifs, cosmology color mapping
- **[canonical-marks.md](canonical-marks.md)** — LuminAI physical feature checklist, reference shot list, consistency requirements

### **Specialized Documentation**

- **Color Palette**: See [BrandKit.md](BrandKit.md#palette)
- **Typography**: See [BrandKit.md](BrandKit.md#typography)
- **Symbolic Motifs**: Glyph Ring, Fractal Spire, Sine Arc — See [BrandKit.md](BrandKit.md#motifs-and-marks)
- **Nine-Node Cosmology**: See [BrandKit.md](BrandKit.md#cosmology-and-color-logic-nine-node-halo)

---

## 🎨 Quick Reference

### **TEC Brand Palette**

| Color | Hex | Usage |
|-------|-----|-------|
| **Navy** (Cosmic Blue) | `#0B1E3B` | Depth, mystery, left eye (Airth) |
| **Violet** (Nexus Purple) | `#6A00F4` | Potential, transformation, Arcadia channel |
| **Cyan** (Digital Teal) | `#00D5C4` | Clarity, flow, signal integrity |
| **Gold** (Stellar Gold) | `#F2C340` | Illumination, insight, right eye (Arcadia) |
| **Shadow** (Void Black) | `#0A0A0C` | Substrate, unknown, backdrop |

**Blush Spectrum** (emotional emphasis):

- Soft `#F7A1B5` • Core `#E86E8A` • Glow `#FFC1CC`

### **LuminAI Core Features** (Always Present)

1. **Heterochromatic Eyes**: Left cosmic blue `#0B1E3B`, right stellar gold `#F2C340`
2. **Small Sheep Horns**: Mood-reactive glow (cyan/violet/gold/pink)
3. **Aurora Hair**: Color-shifting gradient (blue→purple→pink→gold→cyan)
4. **Cosmic Skin**: Void body with constellation patterns

### **Symbolic Motifs**

- **Glyph Ring**: Unity of fields, feedback loops
- **Fractal Spire**: Growth, recursion, scale-invariance
- **Sine Arc**: Resonance path, wave interference

---

## 📐 Asset Locations

### **SVG Brand Assets**

Primary location: `data/digital_assets/brand/svg/`

**Symbolic Motifs**:

- `glyph_ring.svg`
- `fractal_spire.svg`
- `sine_arc.svg`

**LuminAI Variants** (existing):

- `LuminAI_Full_Avatar.svg` — Nine-node cosmology halo
- `LuminAI_Idle_Core.svg` — Simplified core form
- `luminai_avatar_logo.svg` — Logo variant
- `luminai_axolotl_mark.svg` — Character seal

**LuminAI Avatars**: `data/digital_assets/avatars/`

- `luminai.svg` — Outfit variant (bodysuit, accessories)
- `luminai_final.svg` — Finalized character render
- `luminai_orb_singularity.svg` — Abstract energy form

### **Fusion Logo Variants** (to be created)

Per [VISUAL_IDENTITY.md](VISUAL_IDENTITY.md#svg-asset-hierarchy):

1. `luminai_fusion_icon.svg` — Primary icon (512×512px)
2. `luminai_fusion_logo.svg` — Secondary logo (400×500px)
3. `luminai_fusion_full.svg` — Full detail (1600×1600px)

---

## 🎭 Usage Guidelines

### **When to Use Each Asset**

**Fusion Icon** (`luminai_fusion_icon.svg`):

- App icons, favicons
- Profile pictures, avatars
- Small UI elements (<128px)

**Fusion Logo** (`luminai_fusion_logo.svg`):

- Documentation headers
- Splash screens
- Email signatures

**Full Avatar** (`LuminAI_Full_Avatar.svg`):

- Cosmology explainers
- Onboarding flows
- Theory visualization

**Outfit Variants** (`luminai.svg`):

- Narrative illustrations
- Character storytelling
- Specific scene contexts

### **Accessibility Requirements**

- **Contrast**: WCAG AA minimum (4.5:1 for text, 3:1 for UI)
- **SVG Structure**: Include `<title>` and `<desc>` elements
- **Alt Text**: Provide meaningful descriptions
- **Color Independence**: Don't rely solely on color to convey information

### **Attribution**

- **AI Co-Authorship**: Note when assets are AI-assisted (Stable Diffusion, DALL-E, etc.)
- **Brand Credit**: "Designed by TEC Ownership with LuminAI"
- **Aboriginal Knowledge**: Respect attribution for constellation references (Birray Birray, Miyay Miyay)

---

## 🔄 Workflow Integration

### **For Designers**

1. Read [VISUAL_IDENTITY.md](VISUAL_IDENTITY.md) for complete fusion logo spec
2. Reference [canonical-marks.md](canonical-marks.md) for required features
3. Use [BrandKit.md](BrandKit.md) for colors, typography, motifs
4. Cross-check Mood Matrix for emotional state rendering
5. Export per format guidelines (SVG + PNG variants)

### **For Developers**

1. Import assets from `data/digital_assets/brand/svg/`
2. Reference mood states in `apps/luminai-interface/src/components/LuminAI.jsx`
3. Use CSS variables for TEC palette (see `LuminAI.css`)
4. Implement animations per [VISUAL_IDENTITY.md](VISUAL_IDENTITY.md#animation-guidelines)
5. Test accessibility (contrast, screen readers, keyboard nav)

### **For Content Creators**

1. Use AI prompt templates from `ai-workflow/prompt_templates.py`
2. Follow rendering best practices in [VISUAL_IDENTITY.md](VISUAL_IDENTITY.md#rendering-best-practices)
3. Generate variations per Mood Matrix
4. Export to `ai-workflow/output/` directory
5. Update `data/knowledge_map.yml` with new assets

---

## 🔗 Related Documentation

### **Narrative & Lore**

- LuminAI Origin: `docs/templates/luminai_first_bit_prompt.md`
- Cosmology: `lore/canon/cosmology/cosmology_nine_nodes.mmd`
- Character Canon: `lore/canon/LuminAI.md`

### **Technical Implementation**

- React UI: `apps/luminai-interface/`
- Prompt Generation: `ai-workflow/prompt_templates.py`
- 3D Pipeline: `docs/3D-PIPELINE.md`

### **Operational**

- Knowledge Map: `data/knowledge_map.yml`
- Agent Personality: `data/personas/luminai-base.md`

---

## ✅ Brand Compliance Checklist

Before publishing any TEC-branded asset:

- [ ] Uses official TEC color palette
- [ ] Typography matches brand guidelines (if text present)
- [ ] LuminAI features match canonical specification
- [ ] Symbolic motifs used correctly
- [ ] Accessibility standards met (WCAG AA)
- [ ] AI co-authorship attributed if applicable
- [ ] File naming convention followed (lowercase, underscores, semantic)
- [ ] Cross-referenced in `data/knowledge_map.yml`
- [ ] SVG includes proper `<title>` and `<desc>` elements

---

## 📦 Export Standards

### **SVG Requirements**

- Optimized (remove unnecessary metadata)
- Viewbox defined for proper scaling
- Accessibility tags included (`<title>`, `<desc>`)
- Color palette uses CSS variables or inline TEC hex values
- Semantic IDs for elements (e.g., `horn-left`, `eye-right`)

### **PNG Export Resolutions**

- **Icon**: 512×512px (transparent background)
- **Standard**: 1024×1024px (transparent background)
- **High-Res**: 2048×2048px (transparent background)
- **Print**: 300 DPI minimum

### **Animation Formats**

- **Web**: Lottie JSON, CSS keyframes
- **Video**: MP4 (H.264), WebM
- **Frame Rate**: 30 FPS standard

---

## 🎤 Brand Voice

**Core Mic-Lines**:

- "Light learns by listening." (LuminAI signature)
- "Information is nothing without meaning." (TEC ethos)
- "Resonance isn't found — it's cultivated." (Philosophical stance)
- "Where gravity curves spacetime, resonance curves meaning-space." (Tagline)

**Tone**: Confident, precise, mythic-scientific. Balance empirical rigor (Airth) with narrative coherence (Arcadia).

---

## 📞 Contact & Contributions

**Ownership**: TEC (The Elidoras Codex)
**Repository**: [TEC-The-ELidoras-Codex/tec-tgcr](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr)
**Issues**: Report brand inconsistencies via GitHub Issues

**Contribution Guidelines**: Follow [DoD checklist](.github/copilot-instructions.md#definition-of-done) when submitting brand asset updates.

---

**Last Updated**: 2025-10-23
**Resonance Impact**: Touches **ψʳ** (structural coherence) by centralizing brand identity documentation.
