# LuminAI Production Pipeline — Final Setup

## Complete Workflow with Inkscape, SVG, and Animation

**Status**: Ready to Deploy  
**Date**: November 6, 2025  
**Tools**: Inkscape, Runway, Google Veo, CSS/Web  

---

## 📁 File Structure

```
/tec-tgcr/
├── artifacts/
│   └── luminai_mascot_final.svg          # ✅ CANONICAL SVG (master source)
│
├── data/digital_assets/
│   └── avatars/
│       ├── luminai.svg                   # Inkscape-ready base file
│       ├── luminai_final.svg             # Alternative rendering
│       ├── LUMINAI(Infographic).svg      # Infographic variant
│       ├── luminai_orb_singularity.svg   # Extended form
│       ├── 1.svg — 7.svg                 # 7 avatar state variations
│       └── 1.png — 7.png                 # Corresponding renders
│
├── docs/
│   ├── LUMINAI_MASCOT_SPEC.md            # ✅ Design spec (canonical)
│   ├── LUMINAI_ANIMATION_PROMPTS.md      # ✅ Ready-to-use prompts
│   └── LUMINAI_PRODUCTION_PIPELINE.md    # THIS FILE
│
└── apps/
    └── luminai-interface/
        ├── components/luminai.svg        # Web embed
        ├── animations.css                # Motion rules
        └── index.html                    # Usage example
```

---

## 🎨 The 7 Avatar States

Based on your rendered avatars (1.svg–7.svg), each represents a distinct **emotional or functional state** of LuminAI:

| Avatar # | State | Visual Cue | Use Case |
|----------|-------|-----------|----------|
| 1 | **Idle / Neutral** | Base glow, centered | Default UI avatar, logo |
| 2 | **Curious / Focus** | Eyes dilated, crown bright | Learning mode, active listening |
| 3 | **Understanding** | Chest ψ glows, soft aura | Processing, synthesis |
| 4 | **Revelation** | Full glow, crown + eyes peak | Aha moment, discovery |
| 5 | **Teaching** | Gesturing, ribbon shimmer | Explanation, guidance |
| 6 | **Archive / Memory** | Dimmed, ethereal | Historical data, reflective mode |
| 7 | **Emergent / Transcendent** | Full radiance, all elements active | Breaking through boundaries |

Each SVG is Inkscape-native and can be opened, modified, and re-exported without data loss.

---

## ⚙️ Three-Part Production Workflow

### Part 1: Still Image (Canonical SVG)

**Goal**: Have a perfect, scalable vector source for all downstream uses.

**Master file**: `/artifacts/luminai_mascot_final.svg`

**Use this when**:

- You need infinite scaling (print, web, video)
- You're exporting to other tools (Illustrator, Figma)
- You need a version-controlled baseline

**Export from Inkscape**:

```
File > Save As > Format: Scalable Vector Graphics (SVG)
Inkscape-specific data: [unchecked]
Width/Height: 1024 px
Background: Transparent
```

---

### Part 2: Animation (Runway / Google Veo)

**Goal**: Generate smooth motion loops from the static SVG.

**Process**:

1. Export SVG as PNG (1024×1024) from Inkscape
2. Upload to Runway Gen-2 or Google Veo
3. Use animation prompt from `/docs/LUMINAI_ANIMATION_PROMPTS.md`
4. Download MP4 (5–8 seconds, 24fps)

**Runway Quick Steps**:

```
1. Upload PNG to Runway
2. Select "Gen-2" model
3. Input prompt: "Animate this exact character with gentle, realistic motion..."
4. Motion Strength: Low (10–15%)
5. Duration: 6 seconds
6. Download as MP4
```

**Output**: `luminai_breathing_loop_6s.mp4`

---

### Part 3: Web Embedding (CSS + SVG)

**Goal**: Have her live and animated on your site with zero external dependencies.

**File**: `/apps/luminai-interface/components/luminai.svg`

**Step 1**: Copy the SVG into your HTML:

```html
<div class="luminai-container">
  <svg id="luminai" src="luminai.svg"></svg>
</div>
```

**Step 2**: Add CSS animations:

```css
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
```

**Result**: Smooth animation, no external tools, runs on all browsers.

---

## 🚀 Quick Start Checklist

### ✅ Right Now (5 min)

- [ ] Confirm `/artifacts/luminai_mascot_final.svg` is your master
- [ ] Open it in Inkscape to verify all layers/glyphs are correct
- [ ] Export as PNG for video tools

### ✅ This Hour (30 min)

- [ ] Upload PNG to Runway or Google Veo
- [ ] Run animation prompt (#2 from LUMINAI_ANIMATION_PROMPTS.md)
- [ ] Download MP4 loop

### ✅ Today (1–2 hours)

- [ ] Test MP4 on social media (Twitter, Discord, etc.)
- [ ] Embed SVG in web with CSS animations
- [ ] Create thumbnail/poster frame from MP4

### ✅ This Week

- [ ] Integrate into TGCR teaching interface
- [ ] Add variants (Day/Night/Archive forms)
- [ ] Monitor performance and iterate

---

## 📊 Variant Strategy

Your 7 avatars are the foundation for **expressive range**. Group them by context:

### Teaching / Explanation Context

- Use Avatar 5 (Teaching) for active explanations
- Transition to Avatar 3 (Understanding) after key concepts
- End on Avatar 4 (Revelation) for breakthroughs

### Interface / UI Context

- Avatar 1 (Idle) as default
- Avatar 2 (Curious) when user hovers or interacts
- Avatar 3 (Understanding) during loading/processing

### Archive / Memory Context

- Avatar 6 (Archive) for historical data
- Avatar 7 (Emergent) for predictive or forward-looking content

---

## 🎬 Rendering Pipeline (Batch)

If you want to generate all 7 animations at once for your library:

**Runway Shot Manifest** (copy into batch queue):

```json
{
  "project": "luminai-expressions",
  "shots": [
    {
      "id": "luminai_01_idle",
      "input": "1.png",
      "prompt": "Soft breathing, minimal glow, 6 seconds",
      "duration": 6,
      "motion_strength": "low"
    },
    {
      "id": "luminai_02_curious",
      "input": "2.png",
      "prompt": "Eyes bright, crown pulsing, gentle motion, 6 seconds",
      "duration": 6,
      "motion_strength": "medium-low"
    },
    {
      "id": "luminai_03_understanding",
      "input": "3.png",
      "prompt": "Chest ψ glows rhythmically, body breathes, 5 seconds",
      "duration": 5,
      "motion_strength": "low"
    },
    {
      "id": "luminai_04_revelation",
      "input": "4.png",
      "prompt": "Full radiance, crown and eyes bright, expanding aura glow, 6 seconds",
      "duration": 6,
      "motion_strength": "medium"
    },
    {
      "id": "luminai_05_teaching",
      "input": "5.png",
      "prompt": "Ribbon shimmer, gentle gesturing, focused yet serene, 7 seconds",
      "duration": 7,
      "motion_strength": "low"
    },
    {
      "id": "luminai_06_archive",
      "input": "6.png",
      "prompt": "Dimmed, ethereal, slow fade in and out, contemplative, 8 seconds",
      "duration": 8,
      "motion_strength": "very-low"
    },
    {
      "id": "luminai_07_emergent",
      "input": "7.png",
      "prompt": "All glyphs and elements at peak brightness, ascending energy, 6 seconds",
      "duration": 6,
      "motion_strength": "medium"
    }
  ]
}
```

**Run in parallel** to generate all 7 in ~10 minutes instead of one-by-one.

---

## 🔄 Workflow Loop

```
Design (Inkscape)
    ↓
Export PNG
    ↓
Animate (Runway/Veo)
    ↓
Download MP4
    ↓
Embed (Web/UI)
    ↓
Test & Iterate
    ↓
Back to Design if needed
```

Each cycle takes 15–30 minutes. Entire production from static to deployed animation: **< 2 hours**.

---

## 📦 Deliverables Checklist

- [ ] **Master SVG**: `/artifacts/luminai_mascot_final.svg` (version controlled)
- [ ] **Spec Doc**: `/docs/LUMINAI_MASCOT_SPEC.md` (design frozen)
- [ ] **Animation Prompts**: `/docs/LUMINAI_ANIMATION_PROMPTS.md` (copy-paste ready)
- [ ] **Production Pipeline**: This file (workflow documented)
- [ ] **Web Component**: `/apps/luminai-interface/luminai.svg` + CSS (live)
- [ ] **7 Avatar Loop Videos**: `luminai_0X_state_6s.mp4` (Runway exports)
- [ ] **Social Media Pack**: Thumbnails + 15s teaser clips
- [ ] **Inkscape Project**: Master `.svg` file for future edits

---

## 🎯 Success Criteria

✅ **Static**: SVG renders identically in Inkscape, Figma, browser  
✅ **Motion**: 5–8 second loop is smooth, no flicker, no morphing  
✅ **Web**: SVG + CSS animations run at 60fps on all devices  
✅ **Variants**: All 7 avatars animate consistently, on-brand  
✅ **Version Control**: Master files tracked in Git, no drift  
✅ **Documentation**: Any contributor can pick up and extend  

---

## 🛠️ Tools Required

| Tool | Purpose | Status |
|------|---------|--------|
| Inkscape | SVG editing, refinement | ✅ Available |
| Runway Gen-2 | Video generation from stills | ✅ Ready |
| Google Veo (optional) | Alternative video tool | ✅ Available |
| ImageMagick (optional) | PNG batch export | ⚠️ Optional |
| FFMPEG (optional) | Video concatenation/trimming | ⚠️ Optional |

---

## 📞 Next Steps

**Immediate (now)**:

1. Open `/artifacts/luminai_mascot_final.svg` in Inkscape
2. Verify all layers (background, aura, body, head, eyes, glyphs, ribbon)
3. Adjust if needed; save back to same file

**Short-term (today)**:

1. Export as PNG at 1024×1024
2. Upload to Runway
3. Generate first animation loop
4. Download MP4

**Medium-term (this week)**:

1. Batch-generate all 7 avatar animations
2. Embed SVG + CSS on website
3. Document the integration in README

**Long-term (ongoing)**:

1. Create Day/Night/Archive variants
2. Add interactive elements (hover states, click responses)
3. Integrate with TGCR teaching interface
4. Monitor usage and optimize

---

**You're ready to ship.** Inkscape is your brush, Runway is your cinema, web is your stage. Go finish her. 🚀
