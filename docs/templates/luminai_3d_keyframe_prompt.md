# LuminAI — 3D Keyframe Storyboard Prompt

Objective: Block three canonical animation beats tied to TGCR states for rigging and shader linking (Blender, Unity, or WebGL).

Global rig notes:

- Base mesh: soft blob with blendshapes: elongate, compress, wobble, horn_scale, gill_splay.
- Material: subsurface gel with emissive core layer; maskable blush overlay; rim highlights.
- Attachments: horn crystals (separate mesh), aurora gill cards (alpha planes), eye sprites.

Keyframes (pose + timing):

1. Blushing Protocol (High OXY)

   - Time: 0–24f (1s @24fps)
   - Pose: compact/rounded, cheeks blush mask from 0.0→0.7; horn glow low→mid.
   - Eyes: blue softens; red/gold diffuses. Micro head tilt.
   - Notes: easeOut on blush; add subtle body wobble.

2. Gills Extended / Sparkle (High DOP)

   - Time: 24–60f (1.5s)
   - Pose: mild elongation (elongate=0.25), gill_splay=0.8; horn glow mid; aurora tips emit Cyber Gold.
   - Eyes: sparkle overlay; quick glance sweep.
   - Notes: corePulseRate up; constellation rim flicker.

3. ADR Tremor / Core Glitch (High ADR)
   - Time: 60–100f (1.7s)
   - Pose: angular silhouette (elongate=0.35 + slight sharpness), horn_scale=1.2; micro jitter.
   - Core: emissive hue shifts toward Nexus Purple; brief chromatic aberration.
   - Notes: camera shake lite; return to neutral by 100f.

Export guidance:

- Provide stepped and spline versions of keyframes.
- Name actions “OXY_blush”, “DOP_flare”, “ADR_tremor”.
- Include preview turntable @ 12s (idle → OXY → DOP → ADR → idle).

Unity/Three hooks:

- Expose blendshape names and material params (see resonance driver JSON).
- Trigger map: key ‘O’, ‘P’, ‘A’ for OXY/DOP/ADR demos.
