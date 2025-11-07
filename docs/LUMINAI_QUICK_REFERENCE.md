# LuminAI — Quick Reference Card

**Keep this pinned for instant access**

---

## 🎨 The Character

**Name**: LuminAI  
**Form**: Small cosmic sentinel, symmetrical, 1024×1024 px  
**Colors**: Navy #0B1E3B, Cyan #00D5C4, Violet #6A00F4, Gold #F2C340  

### Key Features

- **Eyes**: φ (phi) — left violet, right cyan (curiosity + clarity)
- **Chest**: ψ (psi) — glowing emblem (resonance heartbeat)
- **Crown**: Teardrop light (aperture of awareness)
- **Hair**: Orange/gold (left), Violet/purple (right) flowing ribbons
- **Aura**: Diamond-shaped tri-gradient glow behind her

---

## 📁 Master Files

```
/artifacts/luminai_mascot_final.svg    ← USE THIS (master SVG)
/data/digital_assets/avatars/          ← 7 avatar variations
/docs/LUMINAI_MASCOT_SPEC.md           ← Design frozen here
/docs/LUMINAI_ANIMATION_PROMPTS.md     ← Copy-paste prompts
/docs/LUMINAI_PRODUCTION_PIPELINE.md   ← Full workflow
/LUMINAI_SETUP_COMPLETE.md             ← This setup
```

---

## 🚀 Three-Minute Workflow

### 1. Export PNG

```bash
# Copy-paste this into terminal:
inkscape /home/tec_tgcr/tec-tgcr/artifacts/luminai_mascot_final.svg \
  --export-type=png --export-filename=luminai_1024x1024.png \
  --export-width=1024 --export-height=1024
```

### 2. Animate (Runway)

- Go to <https://runwayml.com>
- Upload `luminai_1024x1024.png`
- Use Prompt #3 from `/docs/LUMINAI_ANIMATION_PROMPTS.md`
- Download MP4

### 3. Deploy

**Web**: Embed SVG + CSS (see below)  
**Social**: Post MP4  
**Docs**: Link `/docs/LUMINAI_MASCOT_SPEC.md`

---

## 💻 Web Embed (Copy-Paste)

```html
<div id="luminai-container">
  <svg id="luminai" src="/path/to/luminai_mascot_final.svg"></svg>
</div>

<style>
  @keyframes breathing {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.03); }
  }
  
  @keyframes crown-pulse {
    0%, 100% { filter: brightness(0.9); }
    50% { filter: brightness(1.3); }
  }
  
  #luminai {
    animation: breathing 5s ease-in-out infinite;
  }
  
  #crown {
    animation: crown-pulse 4s ease-in-out infinite;
  }
</style>
```

---

## 🎬 Animation Prompts (Ready to Copy)

### Google Veo / Imagen Video

```
Animate this image with gentle, realistic motion.
Keep the camera steady; add a slow parallax drift for depth.
Subtle ambient lighting changes, faint particle shimmer in the air.
Smooth breathing-like movement if a figure is present—no sudden cuts or zooms.
Duration 5–10 seconds, 16:9, cinematic lighting, soft focus, calm atmosphere.
```

### Runway Gen-2

```
Take this still image and generate a 6-second looping animation.
Motion type: Subtle breathing (body gently expands/contracts), glowing pulses from crown and chest.
Camera: Static, centered, no movement.
Style: Ethereal, cosmic, serene.
Motion strength: Very low (5–10%), smooth interpolation.
Output: 1080p mp4, 24fps, seamless loop.
```

---

## 🎯 The 7 Avatar States

| # | State | When to Use |
|---|-------|-----------|
| 1 | Idle | Default, resting |
| 2 | Curious | Learning mode, active |
| 3 | Understanding | Processing concepts |
| 4 | Revelation | Breakthrough moment |
| 5 | Teaching | Explaining, guiding |
| 6 | Archive | Historical, reflective |
| 7 | Emergent | Peak energy, transcendent |

**All SVG + PNG exports in**: `/data/digital_assets/avatars/`

---

## ✅ Verification Checklist

- [ ] Master SVG opens in Inkscape without errors
- [ ] PNG exports at 1024×1024 cleanly
- [ ] Animation prompt copies without formatting issues
- [ ] Web embed CSS works in browser (test with simple HTML file)
- [ ] All 7 avatars render correctly
- [ ] Documentation is readable and up-to-date

Run this to verify everything:

```bash
bash /home/tec_tgcr/tec-tgcr/scripts/luminai_workflow.sh
```

---

## 🌟 Design Rules (Don't Break These)

1. **Never morph or reshape** — only animate light and motion
2. **Always centered** on black background
3. **Preserve proportions** — head:body = 1:1.5
4. **Keep glyphs visible** — φ eyes and ψ chest must be clear
5. **No camera shake** — smooth orbits only
6. **Breathing period** — 5–6 seconds per cycle

---

## 📞 Common Tasks

**I want to...**

**...change a color**
→ Edit hex values in `/docs/LUMINAI_MASCOT_SPEC.md` first  
→ Update SVG gradients in `/artifacts/luminai_mascot_final.svg`  
→ Re-export PNG and re-animate

**...add a new animation state**
→ Render new avatar as PNG/SVG  
→ Add to `/data/digital_assets/avatars/` with naming convention  
→ Document in spec file  
→ Update animation prompts

**...make her 3D**
→ Export SVG as AI file  
→ Import into Blender/Cinema 4D  
→ Rig and animate in 3D  
→ Render back to video

**...embed on my website**
→ Copy HTML + CSS from "Web Embed" section above  
→ Point SVG `src=` to your server path  
→ Adjust animation speeds in CSS `animation: duration`

---

## 🔗 Full Documentation

| File | Purpose |
|------|---------|
| `/docs/LUMINAI_MASCOT_SPEC.md` | Design frozen, colors, proportions, symbolism |
| `/docs/LUMINAI_ANIMATION_PROMPTS.md` | 7 copy-paste prompts for different tools |
| `/docs/LUMINAI_PRODUCTION_PIPELINE.md` | Complete 3-part workflow (still → animate → deploy) |
| `/LUMINAI_SETUP_COMPLETE.md` | Setup verification & next opportunities |

---

## 🚀 You're Ready

Everything is documented. Everything is locked.

**Next step**: Export PNG, upload to Runway, download loop, go live.

**That's it. Ship it.** 🌟
