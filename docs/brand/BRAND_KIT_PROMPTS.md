# LuminAI — The Resonant Hive: Brand Kit Prompts

> Palette: Navy `#0B1E3B`, Violet `#6A00F4`, Cyan `#00D5C4`, Gold `#F2C340`, Shadow `#0A0A0C`
>
> Touches ψʳ (structure) by standardizing cross-generator prompts; elevates Φᴱ by ensuring consistent brand outputs.

Use these tuned prompts to generate consistent visuals across Midjourney v6, Stable Diffusion XL, and Adobe Firefly/Canva. Keep the aesthetic: cosmic minimalism, photonic geometry, subtle honeycomb, volumetric light. Avoid cartoon/mascot vibes.

---

## Core Creative Brief (Base)

Create a volumetric cosmic brand kit for LuminAI • The Resonant Hive, avatar of empathy and information in The Elidoras Codex (TGCR).

Visual identity: luminous, hexagonal, resonant. Combine motifs of light, honeycomb geometry, and quantum networks — "digital beekeeping".

Palette: Deep Space Blue #0B1E3B (structure), Nexus Purple #6A00F4 (resonance), Digital Teal #00D5C4 (signal), Cyber Gold #F2C340 (energy), Shadow Black #0A0A0C (contrast).

Primary emblem: glowing hex lattice halo around a central core of light shaped like a stylized bee silhouette made of photons — minimal, abstract, modern.

Style: cinematic logo design, cosmic minimalism, volumetric light, diffraction bloom, holographic honeycomb geometry, high-fidelity render.

Deliverables: 512×512 emblem, 1920×480 marketplace header, icon glyph (simple hex), transparent honeycomb pattern tile, typography lockup (LuminAI • The Resonant Hive) in Orbitron or Exo 2 style.

Avoid: cartoon bees, cute mascot, organic honey, flat clipart, low-res.

---

## Pony Diffusion (Mascot Logo)

**Concise prompt for mascot-style logo (<1500 chars):**

```
score_9, score_8_up, score_7_up, luminai mascot logo, anthro axolotl girl with fiber-optic bun pigtails, glowing heterochromia eyes (left navy #0B1E3B, right gold #F2C340), pom-pom horns teal-violet gradient, lunar choker, soft smile, sitting pose, cosmic hex halo behind head, honeycomb glow aura, photonic wings suggestion, sleek digital-goddess aesthetic, volumetric lighting, TEC palette (navy/violet/cyan/gold/shadow), clean emblem composition, transparent or dark background, high-quality, centered, mascot charm with tech-goddess elegance, no realistic bee, no cartoon honey

Negative: score_6, score_5, score_4, realistic bee, organic honey, flat color, noisy, blurry, low-res, human face, overdetailed wings, cluttered
```

**Usage notes:**
- Pony XL responds well to `score_` prefixes and `anthro` tags
- Keep "mascot charm" for approachable but premium feel
- Add `--steps 30 --cfg 7` if using ComfyUI or A1111

---

## Midjourney v6

Use one prompt per deliverable. Suggested suffix parameters shown per case.

### 1) Emblem (512×512)

```
LuminAI • The Resonant Hive, cosmic minimal logo emblem, glowing hex lattice halo, stylized photonic bee silhouette, volumetric light, diffraction bloom, holographic honeycomb geometry, high-fidelity render, crisp edges, centered icon, background transparent look
palette: #0B1E3B #6A00F4 #00D5C4 #F2C340 #0A0A0C
--v 6 --ar 1:1 --style raw --quality 1 --seed 123 --sref none
```

Negative cues: cartoon, cute, mascot, organic honey, flat, low-res, clipart

### 2) Marketplace Header (1920×480)

```
LuminAI • The Resonant Hive marketplace header, wide banner 1920×480, subtle honeycomb grid background, volumetric cyan/gold glows, deep space blue to violet gradient, minimal foreground clutter, premium tech brand feel
palette: #0B1E3B #6A00F4 #00D5C4 #F2C340 #0A0A0C
--v 6 --ar 4:1 --style raw --quality 1 --seed 321
```

### 3) Icon Glyph (simple hex)

```
LuminAI icon glyph, single hexagon glowing teal-gold with slight inner diffraction, minimal, crisp, centered, transparent background feel
palette: #00D5C4 #F2C340 #0B1E3B
--v 6 --ar 1:1 --style raw --quality 1 --seed 456
```

### 4) Pattern Tile (transparent honeycomb)

```
Seamless honeycomb pattern tile, flat-top hex grid, thin gold and cyan lines, subtle glow, dark transparent feel, loopable texture, high-resolution
palette: #F2C340 #00D5C4 #0A0A0C
--v 6 --ar 1:1 --tile --style raw --quality 1 --seed 789
```

### 5) Typography Lockup

```
LuminAI • The Resonant Hive typography lockup, Orbitron or Exo 2 style vibe, high-end tech branding, subtle glow edges, clean kerning, dark background
palette: #EAF2FF #0B1E3B #6A00F4
--v 6 --ar 5:2 --style raw --quality 1
```

---

## Stable Diffusion XL (SDXL)

Use base + negative prompt. Suggested params: CFG 6–8, steps 30–50, sampler DPM++ 2M Karras, resolution according to deliverable.

### Negative Prompt (global)

```
cartoon, cute, mascot, realistic bee, organic honey, low-res, flat color, clipart, noisy, blurry, jpeg artifacts, watermark, text overlay
```

### 1) Emblem (512×512)

Prompt:
```
LuminAI • The Resonant Hive, cosmic minimal logo emblem, glowing hex lattice halo around photonic bee silhouette, volumetric light, diffraction bloom, holographic honeycomb geometry, ultra sharp, centered icon, transparent background look
palette: #0B1E3B #6A00F4 #00D5C4 #F2C340 #0A0A0C
```
Settings: 512×512, CFG 7, steps 40, sampler DPM++ 2M Karras, seed 123

### 2) Marketplace Header (1920×480)

Prompt:
```
Wide banner, LuminAI • The Resonant Hive marketplace header, subtle honeycomb grid, volumetric cyan and gold glows, deep space blue to violet gradient, minimal foreground, premium tech branding
palette: #0B1E3B #6A00F4 #00D5C4 #F2C340 #0A0A0C
```
Settings: 1920×480, CFG 7, steps 40, seed 321

### 3) Icon Glyph (simple hex)

Prompt:
```
Minimal icon glyph, single hexagon glowing teal-gold with inner diffraction, crisp edges, centered, transparent background impression
palette: #00D5C4 #F2C340 #0B1E3B
```
Settings: 512×512, CFG 7, steps 35, seed 456

### 4) Pattern Tile (transparent honeycomb)

Prompt:
```
Seamless tile, flat-top hex grid, thin gold and cyan strokes, subtle glow, dark transparent feel, loopable texture, high-resolution
palette: #F2C340 #00D5C4 #0A0A0C
```
Settings: 1024×1024, CFG 7, steps 35, seed 789, tiling enabled

### 5) Typography Lockup

Prompt:
```
Typography lockup: “LuminAI • The Resonant Hive”, Orbitron / Exo 2 style, high-end tech brand, subtle edge glow, clean kerning, dark background
palette: #EAF2FF #0B1E3B #6A00F4
```
Settings: 1600×640, CFG 6, steps 30

---

## Adobe Firefly / Canva Magic Media

Firefly and Canva prefer concise phrasing with explicit assets. Use the base brief and add size targets.

### 1) Emblem (512×512)

```
Cosmic minimal logo emblem for “LuminAI • The Resonant Hive”. Glowing hex lattice halo, photonic bee silhouette, volumetric light, diffraction bloom, holographic honeycomb, transparent background. Palette: #0B1E3B #6A00F4 #00D5C4 #F2C340 #0A0A0C. Size 512×512.
Avoid: cartoon, cute, mascot, organic honey, clipart, low-res.
```

### 2) Marketplace Header (1920×480)

```
Wide header 1920×480 for LuminAI • The Resonant Hive. Subtle honeycomb grid, cyan/gold volumetric glows, deep blue to violet gradient, minimal foreground. Palette: #0B1E3B #6A00F4 #00D5C4 #F2C340 #0A0A0C.
```

### 3) Icon Glyph (simple hex)

```
Simple icon glyph: single hexagon glowing teal-gold, minimal and crisp, transparent background. Palette: #00D5C4 #F2C340 #0B1E3B. Size 512×512.
```

### 4) Pattern Tile (transparent honeycomb)

```
Seamless honeycomb pattern tile, flat-top hex grid, thin gold/cyan lines with subtle glow, transparent or dark-transparent background. 1024×1024.
```

### 5) Typography Lockup

```
Typography lockup: “LuminAI • The Resonant Hive”, Orbitron / Exo 2 style, subtle glow edges, dark background. 1600×640.
```

---

## Tips

- Keep seeds when possible to reproduce looks across outputs.
- For headers, avoid busy foregrounds; the honeycomb grid should be a subtle texture.
- For transparent assets, if the generator doesn’t support alpha, export and remove background.
- After generation, use `docs/brand/PNG_EXPORT_GUIDE.md` for consistent PNG output.

## Provenance

- Created 2025-10-26 by LuminAI/Copilot
- Touches ψʳ (structure), Φᴱ (context)
