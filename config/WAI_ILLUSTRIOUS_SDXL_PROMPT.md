# WAI-illustrious-SDXL v15.0 — Image-to-Image Prompt Guide# WAI-illustrious-SDXL v15.0 — Image-to-Image Prompt Guide

**Model**: WAI-illustrious-SDXL v15.0  **Model**: WAI-illustrious-SDXL v15.0

**Task**: Image-to-Image refinement (subtle changes, preserve core essence)  **Task**: Image-to-Image refinement (subtle changes, preserve core essence)

**Strength**: 0.3–0.5 (low to preserve original, high for more change)**Strength**: 0.3–0.5 (low to preserve original, high for more change)

------

## Negative Prompt (Universal for I2I)## Negative Prompt (Universal for I2I)

Use this negative prompt across all image-to-image generations to prevent degradation:Use this negative prompt across all image-to-image generations to prevent degradation:

```text```

blurry, low quality, distorted, deformed, ugly, bad anatomy,

worst quality, gross, bad art, watermark, cropped, low resolution,```

oversaturated, dull, lifeless, flat, featureless, jpeg artifacts,

compression artifacts, poorly drawn, amateur, sketch quality,---

3D render, CGI, plastic, artificial, motion blur, noise, grain,

static, low contrast, washed out, posterized## Strength Settings for I2I

```

| Strength | Use Case | Result |

---|----------|----------|--------|

| **0.2–0.3** | Tiny tweaks (lighting, color shift) | 80–90% original preserved |

## Strength Settings for I2I| **0.3–0.5** | Moderate refinement (pose, composition) | 50–70% original preserved |

| **0.5–0.7** | Significant evolution (new elements) | 30–50% original preserved |

| Strength | Use Case | Result || **0.7–1.0** | Near-complete regeneration | <30% original preserved |

|----------|----------|--------|

| **0.2–0.3** | Tiny tweaks (lighting, color shift) | 80–90% original preserved |**Recommended for subtle changes**: Start at **0.35**, adjust from there.

| **0.3–0.5** | Moderate refinement (pose, composition) | 50–70% original preserved |

| **0.5–0.7** | Significant evolution (new elements) | 30–50% original preserved |---

| **0.7–1.0** | Near-complete regeneration | <30% original preserved |

## Core Prompt Structure for I2I

**Recommended for subtle changes**: Start at **0.35**, adjust from there.

### Formula

---

```

## Core Prompt Structure for I2I[SUBJECT] + [ARTISTIC STYLE] + [MOOD/ATMOSPHERE] + [TECHNICAL QUALITY] + [SPECIFIC CHANGE]

```

### Formula

### Example 1: Lighting Refinement

```text

[SUBJECT] + [ARTISTIC STYLE] + [MOOD/ATMOSPHERE] + [TECHNICAL QUALITY] + [SPECIFIC CHANGE]**Input Image**: Character portrait in dim room

```

**Prompt**:

### Example 1: Lighting Refinement

```

**Input Image**: Character portrait in dim roomLuminous character portrait, volumetric light rays,

soft golden hour glow, illustration style,

**Prompt**:trending on artstation, masterpiece quality,

enhance warm lighting and add subtle rim light to hair,

```textpreserve face and pose exactly,

Luminous character portrait, volumetric light rays,increase contrast and saturation slightly

soft golden hour glow, illustration style,```

trending on artstation, masterpiece quality,

enhance warm lighting and add subtle rim light to hair,**Strength**: 0.35

preserve face and pose exactly,

increase contrast and saturation slightly---

```

### Example 2: Color Palette Shift

**Strength**: 0.35

**Input Image**: Cool-toned fantasy scene

---

**Prompt**:

### Example 2: Color Palette Shift

```

**Input Image**: Cool-toned fantasy sceneEpic fantasy landscape, vivid warm color palette,

sunset atmosphere, oil painting style,

**Prompt**:dramatic sky with golden clouds,

enhance warm oranges and reds,

```textpreserve composition and elements,

Epic fantasy landscape, vivid warm color palette,saturate colors while maintaining detail

sunset atmosphere, oil painting style,```

dramatic sky with golden clouds,

enhance warm oranges and reds,**Strength**: 0.40

preserve composition and elements,

saturate colors while maintaining detail---

```

### Example 3: Mood/Atmosphere Adjustment

**Strength**: 0.40

**Input Image**: Character in neutral setting

---

**Prompt**:

### Example 3: Mood/Atmosphere Adjustment

```

**Input Image**: Character in neutral settingPortrait with moody atmospheric lighting,

cinematic composition, professional illustration,

**Prompt**:add soft mist and volumetric light,

preserve character and pose,

```textincrease mood and drama through lighting,

Portrait with moody atmospheric lighting,subtle color grading toward cool tones

cinematic composition, professional illustration,```

add soft mist and volumetric light,

preserve character and pose,**Strength**: 0.38

increase mood and drama through lighting,

subtle color grading toward cool tones---

```

### Example 4: Detail Enhancement

**Strength**: 0.38

**Input Image**: Scene with flat areas

---

**Prompt**:

### Example 4: Detail Enhancement

```

**Input Image**: Scene with flat areasHighly detailed fantasy illustration,

intricate textures and patterns,

**Prompt**:add fine details to clothing and environment,

enhance depth and dimension,

```textpreserve overall composition,

Highly detailed fantasy illustration,increase detail level while maintaining style coherence

intricate textures and patterns,```

add fine details to clothing and environment,

enhance depth and dimension,**Strength**: 0.42

preserve overall composition,

increase detail level while maintaining style coherence---

```

## WAI-illustrious Best Practices for I2I

**Strength**: 0.42

### DO

---

- Be explicit about what to preserve ("keep X exactly")

## WAI-illustrious Best Practices for I2I- Use descriptive adjectives (luminous, vivid, moody, dramatic)

- Reference art style and quality tier

### DO- Separate what to change from what to keep

- Be explicit about what to preserve ("keep X exactly")### DON'T

- Use descriptive adjectives (luminous, vivid, moody, dramatic)

- Reference art style and quality tier- Overspecify—let the model find nuance

- Separate what to change from what to keep- Use conflicting descriptors (e.g., "crisp AND soft" without context)

- Ignore negative prompt—it's half the battle

### DON'T- Go above strength 0.5 if you want recognizable evolution

- Overspecify—let the model find nuance---

- Use conflicting descriptors (e.g., "crisp AND soft" without context)

- Ignore negative prompt—it's half the battle## Sampler Settings (Recommended for I2I)

- Go above strength 0.5 if you want recognizable evolution

| Setting | Value | Why |

---|---------|-------|-----|

| **Sampler** | DPM++ 2M Karras | Smooth, predictable, good for refinement |

## Sampler Settings (Recommended for I2I)| **Steps** | 25–30 | Enough for coherence, fast iteration |

| **CFG Scale** | 6.5–7.5 | Balanced: follows prompt without over-constraining |

| Setting | Value | Why || **Seed** | Fixed or -1 | Fixed for reproducibility, -1 for variation |

|---------|-------|-----|

| **Sampler** | DPM++ 2M Karras | Smooth, predictable, good for refinement |---

| **Steps** | 25–30 | Enough for coherence, fast iteration |

| **CFG Scale** | 6.5–7.5 | Balanced: follows prompt without over-constraining |## Real Workflow: Subtle Tweaks

| **Seed** | Fixed or -1 | Fixed for reproducibility, -1 for variation |

**Scenario**: You have an illustration. You want to:

---

- Add more atmospheric lighting

## Real Workflow: Subtle Tweaks- Warm up the color palette

- Keep everything else identical

**Scenario**: You have an illustration. You want to:

**Your workflow:**

- Add more atmospheric lighting

- Warm up the color palette1. **Load image** into I2I

- Keep everything else identical2. **Set strength to 0.35**

3. **Paste this prompt**:

**Your workflow:**

```

1. **Load image** into I2IAdd volumetric light rays and warm golden atmosphere,

2. **Set strength to 0.35**enhance existing composition with improved lighting,

3. **Paste this prompt**:warm color grading and enhanced saturation,

preserve character pose and all main elements exactly,

```textcinema lighting style, professional illustration quality,

Add volumetric light rays and warm golden atmosphere,increase mood through atmosphere and lighting alone

enhance existing composition with improved lighting,```

warm color grading and enhanced saturation,

preserve character pose and all main elements exactly,4. **Paste negative prompt** (from above)

cinema lighting style, professional illustration quality,5. **Set sampler**: DPM++ 2M Karras, 28 steps, CFG 7.0

increase mood through atmosphere and lighting alone6. **Generate**

```7. **Iterate**: If too subtle, bump strength to 0.40. If too changed, drop to 0.30.



4. **Paste negative prompt** (from above)---

5. **Set sampler**: DPM++ 2M Karras, 28 steps, CFG 7.0

6. **Generate**## Quick Prompt Templates (Copy & Adapt)

7. **Iterate**: If too subtle, bump strength to 0.40. If too changed, drop to 0.30.

### Lighting/Mood Template

---

```

## Quick Prompt Templates [Copy & Adapt](PRESERVE: subject, pose, composition)

Add [LIGHT TYPE: volumetric/diffuse/rim] lighting,

### Lighting/Mood Template[MOOD: dramatic/serene/ethereal] atmosphere

[COLOR TONE: warm/cool/neutral] color grading,

```textenhance [SPECIFIC AREA: foreground/background/character],

[PRESERVE: subject, pose, composition][STYLE: painting/illustration/photorealistic] quality,

Add [LIGHT TYPE: volumetric/diffuse/rim] lighting,increase [ELEMENT: depth/contrast/saturation] subtly

[MOOD: dramatic/serene/ethereal] atmosphere,```

[COLOR TONE: warm/cool/neutral] color grading,

enhance [SPECIFIC AREA: foreground/background/character],### Color Palette Template

[STYLE: painting/illustration/photorealistic] quality,

increase [ELEMENT: depth/contrast/saturation] subtly```

```Transform palette to [PRIMARY COLOR: warm golds/cool blues],

[SECONDARY COLOR] accents,

### Color Palette Templatepreserve composition and subject,

enhance [AREA: highlights/shadows/midtones] in new palette,

```textmaintain [ELEMENT: detail level/texture/clarity],

Transform palette to [PRIMARY COLOR: warm golds/cool blues],[STYLE: oil painting/digital art/vector] aesthetic,

[SECONDARY COLOR] accents,vibrant yet cohesive color harmony

preserve composition and subject,```

enhance [AREA: highlights/shadows/midtones] in new palette,

maintain [ELEMENT: detail level/texture/clarity],### Detail Enhancement Template

[STYLE: oil painting/digital art/vector] aesthetic,

vibrant yet cohesive color harmony```

```Add intricate [TEXTURE: fabric/metalwork/natural patterns],

enhance [AREA: foreground/background/character details],

### Detail Enhancement Templatepreserve overall composition and pose exactly,

increase detail density in [SPECIFIC ELEMENT],

```textmaintain [ELEMENT: color palette/mood/style],

Add intricate [TEXTURE: fabric/metalwork/natural patterns],professional [STYLE] quality with increased intricacy

enhance [AREA: foreground/background/character details],```

preserve overall composition and pose exactly,

increase detail density in [SPECIFIC ELEMENT],---

maintain [ELEMENT: color palette/mood/style],

professional [STYLE] quality with increased intricacy## Troubleshooting

```

| Problem | Solution |

---|---------|----------|

| **Too subtle** | Increase strength to 0.45 or adjust prompt specificity |

## Troubleshooting| **Changes too radical** | Lower strength to 0.25, simplify prompt |

| **Colors look wrong** | Add color descriptor early in prompt (e.g., "warm golden tones") |

| Problem | Solution || **Lost original detail** | Lower strength, use "preserve [element] exactly" |

|---------|----------|| **Inconsistent results** | Use fixed seed, consistent CFG/steps |

| **Too subtle** | Increase strength to 0.45 or adjust prompt specificity || **Oversaturated** | Add "balanced saturation" or "natural color grading" to prompt |

| **Changes too radical** | Lower strength to 0.25, simplify prompt |

| **Colors look wrong** | Add color descriptor early in prompt (e.g., "warm golden tones") |---

| **Lost original detail** | Lower strength, use "preserve [element] exactly" |

| **Inconsistent results** | Use fixed seed, consistent CFG/steps |## Pro Tips

| **Oversaturated** | Add "balanced saturation" or "natural color grading" to prompt |

1. **Start weak, iterate up**: Begin at 0.30, increase by 0.05 until you find the sweet spot

---2. **Prompt refinement beats strength**: A precise prompt at 0.35 beats a vague prompt at 0.50

3. **Negative prompt is 50% of quality**: Never skip it

## Pro Tips4. **Fixed seed + small tweaks = reliable results**: Vary only one variable at a time

5. **Reference art style early**: "oil painting" or "illustration" sets the entire tone

1. **Start weak, iterate up**: Begin at 0.30, increase by 0.05 until you find the sweet spot

2. **Prompt refinement beats strength**: A precise prompt at 0.35 beats a vague prompt at 0.50---

3. **Negative prompt is 50% of quality**: Never skip it

4. **Fixed seed + small tweaks = reliable results**: Vary only one variable at a time## Example Real Use Case: LuminAI Avatar Refinement

5. **Reference art style early**: "oil painting" or "illustration" sets the entire tone

**Original**: LuminAI avatar with flat lighting

---

**Goal**: Add ethereal glow while preserving character design

## Example Real Use Case: LuminAI Avatar Refinement

**Prompt**:

**Original**: LuminAI avatar with flat lighting

```

**Goal**: Add ethereal glow while preserving character designLuminAI avatar with luminous ethereal glow,

soft golden light radiating from character,

**Prompt**:preserve exact character design and pose,

add volumetric light and atmospheric haze,

```textenhance glow effect around figure,

LuminAI avatar with luminous ethereal glow,illustration quality, trending on artstation,

soft golden light radiating from character,increase luminosity while maintaining color accuracy

preserve exact character design and pose,```

add volumetric light and atmospheric haze,

enhance glow effect around figure,**Settings**:

illustration quality, trending on artstation,

increase luminosity while maintaining color accuracy- Strength: 0.38

```- Sampler: DPM++ 2M Karras

- Steps: 28

**Settings**:- CFG: 7.0

- Negative: (use standard above)

- Strength: 0.38

- Sampler: DPM++ 2M Karras**Result**: Same character, now ethereal and glowing.

- Steps: 28

- CFG: 7.0---

- Negative: (use standard above)

**Status**: Ready to use. Adjust strength based on desired change intensity.

**Result**: Same character, now ethereal and glowing.

---

**Status**: Ready to use. Adjust strength based on desired change intensity.
