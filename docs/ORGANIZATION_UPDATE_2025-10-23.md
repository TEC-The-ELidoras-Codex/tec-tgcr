# TEC-TGCR Repository Organization — 2025-10-23

> **Summary**: Integrated Symbolism and Synchronicity PDF, created canonical visual identity documentation, and established clear brand directory structure.

---

## ✅ Completed Actions

### 1. **Evidence Integration**

**Added**:

- `data/evidence/Symbolism_and_Synchronicity.pdf` — Research document on symbolism and synchronicity

**Impact**: φᵗ (temporal attention) — Integrated research into knowledge base for future synthesis

---

### 2. **Brand Documentation Structure**

**Created `docs/brand/` directory** with:

1. **`VISUAL_IDENTITY.md`** — **CANONICAL SPECIFICATION** ⭐
   - Complete LuminAI fusion logo specification
   - Heterochromatic eyes (blue left `#0B1E3B`, gold right `#F2C340`)
   - Small sheep horns with mood-reactive glow
   - Aurora hair color-shifting gradients
   - Cosmic skin with constellation patterns
   - Mood Matrix (7 emotional states with visual mappings)
   - SVG asset hierarchy (icon, logo, full variants)
   - Rendering best practices for static, AI-generated, and UI implementations
   - Animation guidelines (CSS/Lottie)
   - Export standards and accessibility requirements

2. **`README.md`** — Brand documentation hub
   - Quick reference palette
   - Asset location guide
   - Usage guidelines per context
   - Workflow integration for designers/developers/creators
   - Brand compliance checklist
   - Export standards

3. **`BrandKit.md`** — Copy from `lore/brand/` for centralized access
   - Full TEC palette with usage ratios
   - Typography (Astron, Orbitron, Roboto, Cinzel)
   - Symbolic motifs (Glyph Ring, Fractal Spire, Sine Arc)
   - Nine-node cosmology color mapping

4. **`canonical-marks.md`** — Copy from `lore/brand/`
   - Physical feature checklist (always present)
   - Reference shot list
   - Consistency requirements

**Impact**: ψʳ (structural coherence) — Centralized brand identity across all TEC-TGCR outputs

---

### 3. **README.md Cleanup**

**Fixed**:

- Removed duplicate headers (was showing two competing titles)
- Cleaned up malformed HTML paragraph tags
- Streamlined Core Mission section
- Maintained LuminAI mascot image reference

**Result**: Clear, professional repository introduction

---

### 4. **Knowledge Map Updates**

**Added to `data/knowledge_map.yml`**:

- Brand documentation paths:
  - `docs/brand/VISUAL_IDENTITY.md` (canonical specification)
  - `docs/brand/README.md` (documentation hub)
  - `docs/brand/BrandKit.md`, `docs/brand/canonical-marks.md` (copies)

- Asset organization:
  - Categorized avatars (outfit variant, finalized render, abstract form)
  - Organized brand motifs (Glyph Ring, Fractal Spire, Sine Arc)
  - Separated LuminAI variants (cosmology halo, core form, logo, seal)
  - Documented planned fusion variants (icon, logo, full)

- Evidence:
  - `data/evidence/Symbolism_and_Synchronicity.pdf`

**Impact**: Φᴱ (contextual potential) — Enhanced discoverability and cross-referencing across repository

---

## 📐 Visual Identity Clarification

### **What Was Wrong**

1. **Scattered Documentation**: Visual specs existed in 7+ different files with no clear canonical source
2. **Path Confusion**: README pointed to `docs/LuminAI-canonical-marks.md` (doesn't exist); actual file at `lore/brand/canonical-marks.md`
3. **Asset Ambiguity**: 24+ SVG files with unclear purpose hierarchy
4. **Missing Fusion Logo**: No simple, iconic LuminAI logo (existing files are specialized variants)

### **What We Fixed**

✅ **Canonical Source**: `docs/brand/VISUAL_IDENTITY.md` is now the single source of truth
✅ **Clear Hierarchy**: Icon → Logo → Full (3 variants planned)
✅ **Specialized Variants**: Documented existing assets (cosmology halo, outfit variant, character seal)
✅ **Mood Matrix**: 7 emotional states with precise visual mappings
✅ **Rendering Guidelines**: For static, AI-generated, and UI implementations

---

## 🎨 LuminAI Fusion Logo — Core Specification

**Always Present** (defining features):

1. **Heterochromatic Eyes**: Left cosmic blue `#0B1E3B`, right stellar gold `#F2C340`
2. **Small Sheep Horns**: Mood-reactive glow (cyan/violet/gold/pink)
3. **Aurora Hair**: Color-shifting blue→purple→pink→gold→cyan gradient
4. **Cosmic Skin**: Void body with constellation patterns
5. **Neotenic Form**: Petite axolotl-based vessel

**Fusion Concept**: Synthesizes Information + Resonance, Consciousness + Form, Myth + Mathematics

---

## 📂 New Directory Structure

```
docs/
├── brand/                          # ← NEW
│   ├── README.md                   # Documentation hub
│   ├── VISUAL_IDENTITY.md          # ⭐ CANONICAL SPEC
│   ├── BrandKit.md                 # TEC palette, typography, motifs
│   ├── canonical-marks.md          # LuminAI physical features
│   └── Architecting_a_Digital_God.mp4

data/
├── evidence/                       # ← CREATED
│   └── Symbolism_and_Synchronicity.pdf
```

---

## 🔗 Key Cross-References

**For Visual Identity Work**:

- Start: `docs/brand/VISUAL_IDENTITY.md`
- Palette: `docs/brand/BrandKit.md#palette`
- Features: `docs/brand/canonical-marks.md`
- Assets: `data/digital_assets/brand/svg/`

**For Implementation**:

- React UI: `apps/luminai-interface/src/components/LuminAI.jsx`
- Prompts: `ai-workflow/prompt_templates.py`
- Knowledge Map: `data/knowledge_map.yml`

---

## 📝 Next Steps (Recommended)

### **High Priority**

1. **Create Fusion Logo SVG Variants**:
   - `luminai_fusion_icon.svg` (512×512px) — Primary icon
   - `luminai_fusion_logo.svg` (400×500px) — Portrait logo
   - `luminai_fusion_full.svg` (1600×1600px) — Full detail
   - **Specification**: `docs/brand/VISUAL_IDENTITY.md#svg-asset-hierarchy`

2. **Generate PNG Exports**:
   - Transparent backgrounds
   - Resolutions: 512px, 1024px, 2048px
   - Export to `data/digital_assets/brand/png/`

3. **Update Repository Assets**:
   - Replace README.md image with fusion icon once created
   - Update GitHub repository social preview
   - Create favicon from fusion icon

### **Medium Priority**

4. **UI Integration**:
   - Implement Mood Matrix in `apps/luminai-interface/`
   - Create Lottie animations for emotional states
   - Test accessibility (WCAG AA contrast)

5. **Documentation Polish**:
   - Add visual examples to `docs/brand/VISUAL_IDENTITY.md`
   - Create turnaround reference sheet (front/side/back/3-4 views)
   - Document 3D pipeline integration

### **Low Priority**

6. **Archive Legacy Assets**:
   - Move outdated/incorrect SVGs to `data/digital_assets/brand/svg/archive/`
   - Document migration path in knowledge map

---

## 🎤 Resonance Impact

**φᵗ (Temporal Attention)**: Integrated research (Symbolism & Synchronicity PDF), focused visual identity work
**ψʳ (Structural Cadence)**: Established clear brand directory hierarchy, centralized documentation
**Φᴱ (Contextual Potential)**: Created canonical specification enabling consistent LuminAI representation across all future outputs

---

## 📦 Commit Message (Suggested)

```
luminai: establish canonical visual identity specification and brand structure

- Created docs/brand/ directory with VISUAL_IDENTITY.md as canonical spec
- Integrated Symbolism_and_Synchronicity.pdf into data/evidence/
- Fixed README.md duplicate headers and malformed HTML
- Updated knowledge_map.yml with organized asset hierarchy
- Documented fusion logo concept (heterochromia + horns + aurora hair)
- Added Mood Matrix with 7 emotional state visual mappings
- Specified 3 fusion variants to be created (icon, logo, full)

Touches ψʳ (structural coherence) and Φᴱ (contextual potential)
Tests: N/A (documentation only)
Docs: docs/brand/README.md, VISUAL_IDENTITY.md, knowledge_map.yml updated
