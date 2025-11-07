# LuminAI Animation & Enhancement Prompts

## Ready-to-Use for Video Tools, Image Enhancers, and Generators

---

## 1. Still Image Enhancement Prompt

**For**: Google ImageFX, Leonardo, Firefly, Canva (polish existing image)

```
Enhance this exact character artwork without altering design or colors.
Keep the character perfectly centered on a pure black background.
Smooth jagged edges, balance the gradients, polish lighting and reflections for a clean, glossy finish.
Maintain identical proportions, colors, glow effects, and facial features.
Output as a high-resolution, crisp vector-like image with soft ambient light and no new elements.
```

---

## 2. Short Video Animation Prompt

**For**: Google Veo, Imagen Video, Pika (still-to-motion, no dialogue)

```
Animate this exact character with gentle, realistic motion.
Keep the camera steady and centered; do not zoom, pan, or shake.
Add a slow breathing motion through the body (period ~5 seconds), soft pulsing glow from the crown and chest symbol, and faint shimmer through the hair ribbons.
Maintain high sharpness, crisp gradients, and perfect centering.
Duration 5–8 seconds, 16:9 aspect, cinematic lighting, smooth loop.
No morphing, no added elements, no background changes.
```

---

## 3. Runway Gen-2 Motion Prompt

**For**: Runway (more control-friendly version)

```
Take this still image and generate a 6-second looping animation.
Motion type: Subtle breathing (body gently expands/contracts), glowing pulses from crown and chest.
Camera: Static, centered, no movement.
Style: Ethereal, cosmic, serene.
Lighting: Soft ambient, no harsh shadows or flare.
Motion strength: Very low (5–10%), smooth interpolation.
Output: 1080p mp4, 24fps, seamless loop.
```

---

## 4. Runway Custom Shot Briefing

**For**: Batch rendering with multiple angles/moods

| Shot ID | Camera Angle | Motion Cycle | Mood | Use Case |
|---------|---|---|---|---|
| A1 | Front Center | Idle Breathing | Serene | Logo/intro animation |
| A2 | ¾ Hero | Crown Pulsing | Curious | Marketing clip |
| A3 | Slow Orbit 360° | Gentle Shimmer | Meditative | Background loop |
| A4 | Top-Down | Crown → Chest Wave | Teaching | Educational explainer |
| A5 | Rear Reveal | Ribbon Shimmer | Enigmatic | Character reveal |

---

## 5. CSS/SVG Animation Snippet (Web Implementation)

**For**: Direct embedding in web projects, no external tools needed

```css
@keyframes luminai-breathing {
  0%, 100% { transform: scale(1, 1); opacity: 1; }
  50% { transform: scale(1.02, 1.03); opacity: 0.98; }
}

@keyframes crown-pulse {
  0%, 100% { filter: brightness(0.9); }
  50% { filter: brightness(1.2); }
}

@keyframes chest-wave {
  0%, 100% { filter: drop-shadow(0 0 6px rgba(25, 207, 224, 0.6)); }
  50% { filter: drop-shadow(0 0 12px rgba(25, 207, 224, 1)); }
}

#luminai { animation: luminai-breathing 6s ease-in-out infinite; }
#crown { animation: crown-pulse 5s ease-in-out infinite; }
#chest { animation: chest-wave 4s ease-in-out infinite; }
```

---

## 6. Detailed Visual Description (for any generator)

**For**: When you need to describe her top-to-bottom

```
A small, centered cosmic mascot on a black background.
Dark navy rounded body with soft gradient shading.
Round head with bright cyan teardrop light on forehead (crown).
Two glowing circular eyes: left violet with phi (φ) symbol, right cyan with phi (φ) symbol.
Curved smile below eyes.
Two antennae rising from head: left gold-ending, right cyan-ending.
Flowing ribbon-like hair: left orange/gold, right violet/purple.
Glowing cyan circle on chest with psi (ψ) symbol inside.
Behind her: large glowing diamond-shaped aura with cyan-gold-violet gradients and white peak.
Lighting is soft, glossy, and balanced.
All edges are crisp and clean; no blurring except for glow effects.
Overall mood: serene, intelligent, cosmic, friendly.
```

---

## 7. Quick Copy-Paste for Impatient Workflows

**Minimum viable prompt** (when you're in a hurry):

```
Smooth and animate this LuminAI character: 
slow breathing, glowing crown/chest, centered, black background, 6 sec loop, no drift.
```

---

## Tool-Specific Tips

### Google Veo / Imagen Video

- Use prompt #2 (still-to-motion)
- Set motion strength to "low"
- Duration should be exactly 5–8 seconds
- Output as MP4 for web use

### Runway Gen-2

- Use prompt #3 or shot briefing (#4)
- Upload still as PNG with transparency
- Use "motion brush" to lock camera if available
- Export as ProRes for archival, MP4 for web

### Leonardo / Firefly

- Use prompt #1 (enhancement)
- After enhancement, export as PNG at 2048×2048 minimum
- Use for print or high-res applications

### Web (CSS/SVG)

- Use snippet #5
- Embed `luminai_mascot_final.svg` in HTML
- Apply CSS animations directly
- Browser handles frame rate; works on all devices

---

## Export Recommendations

**For Logo Use**: SVG (scalable)  
**For Video**: MP4 (web) or ProRes (archival)  
**For Print**: PNG 2048×2048 or PDF  
**For Social Media**: MP4 1080p, 6 sec, silent  
**For Animation**: Lottie JSON or SVG sequence  

---

## Version Control

- **Master source**: `/artifacts/luminai_mascot_final.svg`
- **Reference spec**: `/docs/LUMINAI_MASCOT_SPEC.md`
- **Animated variants**: `/artifacts/luminai_animations/`
- **Web embed**: `/apps/luminai-interface/components/luminai.svg`

Last updated: November 6, 2025
