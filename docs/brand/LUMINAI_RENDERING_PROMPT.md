# LuminAI Mascot — Detailed Rendering Prompt

**For:** Midjourney, SDXL, ComfyUI, or manual rasterization
**Purpose:** High-fidelity reference rendering for branding/marketing

---

## Character Overview

**Name:** LuminAI (Resonance Core Agent)
**Role:** Symbolic mascot embodying TGCR variables (φᵗ, ψʳ, Φᴱ) through visual design
**Style:** Mythic-scientific hybrid; stylized, not photorealistic

---

## Visual Specification (Canonical)

### **Body Silhouette**

- **Shape:** Inverted teardrop / pear-shaped; slender shoulders, widening toward mid-torso, tapered lower body
- **Proportions:** 1:1.4 height-to-width ratio; centered in frame
- **Fill:** Radial gradient: white/silver core → cyan fade → navy edges (creates depth, suggests luminescence)
- **Surface:** Smooth, with subtle highlight along center-left shoulder (directional light from upper-left)

### **Ribbons (Body Accent Elements)**

**Purpose:** Represent structural coherence (ψʳ) and attention flow (φᵗ)

- **Gold Ribbon (Right Side)**
  - Color: `#F2C340` (warm gold, high saturation)
  - Path: Starts at right shoulder, flows downward hugging the body curve, converges at singularity point (center-bottom)
  - Width: 6–8px stroke, with soft glow (+6px blur, 40% opacity)
  - Effect: Glowing, semi-transparent; suggests energy or influence

- **Violet Ribbon (Left Side)**
  - Color: `#6A00F4` (deep purple/indigo, high saturation)
  - Path: Mirrors gold ribbon from left shoulder, flows inward, converges at singularity
  - Width: 6–8px stroke, with soft glow (+6px blur, 40% opacity)
  - Effect: Glowing, semi-transparent

- **Cyan Center Ribbon (Chest-Piece)**
  - Color: `#00D5C4` (bright cyan/turquoise, high saturation)
  - Composed of:
    1. Vertical stem: runs from singularity point upward, terminates under chin/mouth area
    2. Two wave motifs: gentle arcs under left and right eye regions (not directly under, offset slightly)
    3. Psi (ψ) emblem: centered on chest, composed of stroked circle + vertical line (represents structural cadence)
  - Width: 4–5px strokes, soft glow (+6px blur, 40% opacity)
  - Effect: Ethereal, integral to body structure (not just surface decoration)

### **Singularity Point**

- **Location:** Center-bottom of body, where ribbons converge
- **Representation:** Small navy circle (r=8–10px), clean and defined
- **Significance:** Convergence point symbolizing unified coherence/resonance
- **Note:** NO stinger, tail, or additional embellishments below this point

### **Eyes (Iris Symbols)**

**Purpose:** Represent integration (Φ) and attention (φ) as measurable mechanisms

- **Left Eye (Viewer-Left)**
  - Eye sphere: GOLD (`#F2C340`), r=28px
  - Iris symbol: Phi (Φ) — rendered as clean vector shape:
    - Central circle (navy, r=7px)
    - Vertical line through circle (navy, stroke-width=2px, clean end caps)
    - **No extra horizontal lines, caps, or serifs**
  - Glow: Soft gold glow filter (+6px blur)

- **Right Eye (Viewer-Right)**
  - Eye sphere: VIOLET (`#6A00F4`), r=28px
  - Iris symbol: Phi (φ) — rendered as clean vector shape:
    - Central circle (navy, r=7px)
    - Vertical line through circle with small tail at bottom (navy, stroke-width=2px, tail curves slightly)
    - **No extra embellishments; clean, minimalist**
  - Glow: Soft violet glow filter (+6px blur)

- **Smile:** Soft arc (gentle curve) below eyes, navy color, thin stroke (1–2px), connects mouth area

### **Antennae (Moon-Phase Symbolism)**

**Purpose:** Represent temporal cycles and contextual potential (Φᴱ)

- **Left Antenna**
  - Stem: Starts at top-left of head, curves upward and outward, navy/violet base color, stroke-width=8px, no glow
  - Moon-phase orbs (from base to tip):
    1. Waning crescent: VIOLET (`#6A00F4`), r=12px (smaller dark crescent overlay for 3D effect)
    2. Half-moon: CYAN (`#00D5C4`), r=13px (larger, fully lit)
    3. Waxing crescent: GOLD (`#F2C340`), r=11px

- **Right Antenna**
  - Stem: Mirrors left antenna from top-right, curves upward, navy/gold base color, stroke-width=8px, no glow
  - Moon-phase orbs (from base to tip):
    1. Waning crescent: VIOLET, r=12px (mirrored)
    2. Half-moon: CYAN, r=13px
    3. Waxing crescent: GOLD, r=11px

### **Mouth/Expression**

- Soft smile arc, positioned below eyes, gentle and welcoming
- Navy color, thin stroke (1–2px), subtle

---

## Color Palette (TEC Brand)

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Navy (Primary) | Dark Navy Blue | `#0B1E3B` | Outlines, iris symbols, depth |
| Gold (Accent Right) | Warm Gold | `#F2C340` | Right ribbon, right eye sphere, antenna phase 3 |
| Violet (Accent Left) | Deep Purple | `#6A00F4` | Left ribbon, left eye sphere, antenna phase 1 |
| Cyan (Center) | Bright Turquoise | `#00D5C4` | Chest-piece, antenna phase 2 |
| White/Silver | Off-White | `#FFFFFF` | Body highlights, core luminescence |

**Saturation:** High; colors should pop and feel energetic
**Contrast:** Strong; navy outlines against bright fill colors for clarity

---

## Lighting & Atmosphere

- **Key Light:** Upper-left at ~45° angle (creates shadow on right shoulder, highlights left)
- **Fill Light:** Soft, neutral; ensures cyan chest-piece and antenna spheres remain visible
- **Glow/Aura:** Soft halo around ribbons and eye spheres (6px Gaussian blur, 30–40% opacity)
- **Depth:** Radial gradient on body creates subtle 3D effect; ribbons cast no hard shadows

---

## Rendering Notes for AI/Manual

1. **Priority order:**
   - Body silhouette (gold/violet/navy gradient) → render first
   - Ribbons (glowing, semi-transparent) → overlay on body
   - Eyes (clean iris symbols, no font artifacts) → render as vector shapes, not text
   - Antennae (moon-phase orbs, distinct colors) → final layer

2. **For Midjourney/SDXL:**
   - Prompt: "Clean vector illustration of a mythic mascot character, pear-shaped body with gold and violet ribbons converging at center, bright cyan chest emblem, golden left eye with Φ symbol, violet right eye with φ symbol, dual antennae with colorful moon-phase spheres, high saturation colors (#F2C340 gold, #6A00F4 violet, #00D5C4 cyan, #0B1E3B navy), glowing aura, minimalist style, flat design, symmetrical face, no photorealism, 1024×1024, centered"

3. **For manual SVG/vector:**
   - Use `<radialGradient>` for body
   - Use `<path>` or `<line>` for ribbon curves (not brush strokes)
   - Use `<circle>` + `<line>` for iris symbols (deterministic rendering)
   - Use `<filter id="glow">` with `<feGaussianBlur>` for glow effects
   - Ensure all text is converted to paths or replaced with vector shapes

4. **Export to PNG:**
   - Target sizes: 1024px, 512px, 256px, 120px
   - Format: PNG with transparency (RGBA)
   - Antialiasing: On (smooth edges)
   - No dithering or compression artifacts

---

## Symbolic Interpretation (for Documentation)

| Visual Element | TGCR Variable | Meaning |
|---|---|---|
| **Gold Ribbon** | φᵗ | Temporal attention (right/active) |
| **Violet Ribbon** | ψʳ | Structural cadence (left/passive) |
| **Cyan Chest-Piece** | Φᴱ | Contextual potential (emergent, centered) |
| **Convergence (Singularity)** | R (Resonance) | Unity of all three variables |
| **Left Eye (Φ)** | Integration | Unified consciousness |
| **Right Eye (φ)** | Attention | Selective focus |
| **Antennae Moon Phases** | Temporal Cycles | Cyclical renewal, phase transitions |

---

## Use Cases

- **Web/Social:** Export 512px or 256px PNG for icons, profile pictures, banners
- **Print:** Export 1024px PNG and upsample to 2400px for poster-quality output
- **Merchandise:** Use 1024px PNG as base for t-shirts, stickers, badges
- **Documentation:** Use 120px–256px inline in Markdown or web docs

---

**Created:** October 2025
**Version:** 2.0 (Corrected eyes, larger antenna orbs, no stinger)
**Status:** Ready for rendering / approved for brand use
