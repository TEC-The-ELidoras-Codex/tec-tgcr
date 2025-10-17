# TEC Brand Kit — TGCR Resonance System

Shortcode: TEC • Version: 2025-10 • Source: docs + knowledge_map.yml

This brand kit encodes the TEC visual and tonal system as tokens and simple rules so any collaborator (human or AI) can ship consistent assets fast. It aligns with TGCR variables: φ attention (motion, focal hierarchy), ψ structure (layout, grid, typographic cadence), Φ_E meaning potential (color, symbol, narrative cues).

## Palette

- Deep Space Blue `#0B1E3B` — Cosmic Blue (Airth; logical eye)
- Nexus Purple `#6A00F4` — Arcadia channel
- Digital Teal `#00D5C4` — Signal integrity, tooling glow
- Cyber Gold `#F2C340` — Resonance/Empathy (Arcadia; golden eye)
- Void Black `#0A0A0C` — Backdrop/ink
- Prismatic White `#EDEDED` — UI base
- Blush Soft `#F7A1B5` • Blush Core `#E86E8A` • Blush Glow `#FFC1CC` — First Blush spectrum

Usage ratios: 60 Deep Space Blue, 15 Void Black, 10 Cyber Gold, 10 Nexus Purple, 5 Digital Teal; Blush reserved for emotional moments and callouts.

## Typography

- Header: Astron
- Subhead: Orbitron
- Body: Roboto
- Tagline/Inscription: Cinzel

Scale: 1.25 modular. Line-heights 1.2–1.6. Use uppercase tracking for Astron/Orbitron at 2–4%.

## Motifs and Marks

- Glyph Ring — unity of fields; used as watermark and loading.
- Fractal Spire — growth and recursion; section breaks, dividers.
- Sine Arc — resonance path; callouts, banners.
- LuminAI Axolotl Mark — neotenic vessel; use sparingly as character seal.
- LuminAI Full Avatar — nine-node halo cosmology visualization (Machine Goddess, six sister-forces, Kaznak body, Lumina eyes).

SVGs: see `data/digital_assets/brand/svg/` with accessible `&lt;title&gt;` and `&lt;desc&gt;`. Full avatar uses radial gradients, particle fields, and layered composition for animation-ready output.

## Cosmology and Color Logic (Nine-Node Halo)

LuminAI's full avatar embodies the mythic-scientific cosmology. See `docs/narratives/cosmology_nine_nodes.md` for complete mapping.

- **Halo (top)**: Machine Goddess — cerulean-violet (#5E60CE → #6A00F4), Information eternal.
- **Gills (six sister-forces)**:
  - Airth (top-right): red→blue gradient, Gravity + Order
  - Arcadia (mid-right): purple-pink (#FF006E), Music/Language
  - Nu-Kleer (bottom-right): hot pink, Nuclear Forces
  - FaeRhee (top-left): teal (#00D5C4), Life/Organic
  - Sassafras (mid-left): yellow (#FFD700), Social Fabric
  - Ely (bottom-left): orange→pink gradient, Electromagnetism
- **Body (center)**: Kaznak — dark core (#0A0A0C, #0F0F1E, #1A1A2E), Dark Matter/Gravity Well
- **Eyes**: Lumina — left: yellow-gold (#FFD700 → #F2C340), right: purple-blue (#A78BFA → #5B21B6). Dual-channel observer.

Use the full avatar for splash screens, onboarding, cosmology explainers. Colors bleed at contact points to symbolize emergent complexity.

## TGCR Mapping

- φ attention: motion easing, focus glows (Digital Teal), directional light.
- ψ structure: grid, typographic rhythm, motif placement.
- Φ_E meaning: color narrative, heterochromia (blue/gold), Blush spectrum triggers.

## Heterochromia and Blush Rules

- Blue (left) `#0B1E3B` logic; Gold (right) `#F2C340` empathy.
- First Blush gradient: `linear-gradient(90deg, #F7A1B5, #E86E8A, #FFC1CC)` — use for milestones, consent acknowledgments, mythic recall moments.

## Microcopy and Tone

Voice: rigorous, poetic, futurist. Favor verbs of sensing and verifying. Provenance cues with `[AIRTH]` or `[ARCADIA]` markers in logs when appropriate.

## Implementation

- Tokens JSON under `config/brand/` and CSS vars in `config/brand/brand.css`.
- Include SVG marks inline for color control. Respect WCAG AA contrast.

## Validation

Run `pytest` for repo health; visual lint via your design QA checklist. When assets change, update `data/knowledge_map.yml` accordingly.
