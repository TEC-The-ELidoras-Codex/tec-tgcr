# Arcadia Translation Template

Purpose: mapping rules and examples to translate raw narrative/field material into the Experience Layer (ritual_script, soundtrack_descriptor, visual_prompts) suitable for a Resonance Bundle.

1) Input types
- Field notes (free text)
- Interview snippets (quotes)
- Short audio clips (wav/mp3)
- Photos or sketches

2) Translation steps (Arcadia)
- Extract motifs: identify 3 repeating motifs/phrases or emotional anchors.
- Define tone: map to a mood token (e.g., "wistful", "urgent", "savage") and BPM range.
- Ritual skeleton: 3 breath phases — opener (5–15s), core action (30–90s), close (5–15s).
- Visual prompts: 3 tokens that describe color, texture, and focal object (e.g., "cold-brass, matte-glass, humming-lamp").

3) Output template (example)
```
ritual_script: |
  1) Breathe soft: read the claim out loud, eyes closed.
  2) Play looped sound for 45s at 85 BPM.
  3) Place the emblem on the table and take two steps away.

soundtrack_descriptor:
  mood: "wistful"
  bpm: 85
  loop_seconds: 45
  audio_hint_files:
    - "sound/loop-85bpm.wav"

visual_prompts:
  - "cold-brass"
  - "matte-glass"
  - "humming-lamp"
```

4) Arcadia rules of thumb
- Keep scripts short and actionable (90–150 words for public digest)
- Frontload emotional claim, then one verifiable fact, then a single action
- Prefer single-sentence imperatives for ritual actions
- Encode TGCR tokens (phi_T, psi_R, Phi_E) in meta.yaml for Ely to record

5) Examples
- See `data/digital_assets/pilot-pizza` for a starter bundle sample.
