## LuminAI — Mascot Visual Style (Author's notes captured)

This document captures the user's style directions for the LuminAI mascot (verbatim and refined). It is intentionally anchored to the live SVG at `data/digital_assets/brand/svg/luminai_mascot_logo.svg` and is intended to be the single source-of-truth for finalizing the vector before PNG export.

### Original (raw) text
>
> Yellow Eye Needs to be  φ The Yellow AND TEAL AND PURPLE curves Travel along her Geometry Traccing her Outer curveature as the Teal in Part of the Wave function psi THe Middle Line Extends from that giving the PSI Wave form a Abstract look on her Center And the Symbols In the EYES REPLACE THE WHITE circles inside of her Eye they are her Irises the purple is the Φ sybol its now the white circle or inside of the white circle and the yellow eye is φ again its the white circle in her eye the Teal Stripe at hthe Top of the 3 at her Bottom needs to just go Put the Golden on in its Place  then The Purple one at the Bottom needs to Curve with the Bottom of her giving that look as the Lines The yellow the Purple glowing one and the Center Teal all Meet into a POINT that Stretches making the Stinger look that way ran it btw its good the psha do i add the thing to "C:\Users\Ghedd\OneDrive\Projects\TEC\Secrets\tec-resonance-automation.2025-10-26.private-key .pem" or do i run ... (truncated)

> (Above is the user's original wording captured intact — see the SVG for current implementation.)

### Refined visual specification (interpreted and actionable)

- Eyes
  - Left eye (purple): iris is a white disk; the glyph inside the iris is a capital Φ (Phi). This replaces the previous hollow circle/white-dot.
  - Right eye (gold/yellow): iris is a white disk; the glyph inside the iris is a lowercase φ (phi). This replaces the previous white-dot.

- Antennae spheres
  - Each antenna tip has three stacked spheres (top / middle / bottom). Colors top→bottom: Violet, Teal, Gold. Each sphere has a gentle glow filter of its color.

- Tail ribbons and stinger
  - Three colored ribbon lines wrap along the tail/waist and trace the outer curveature of the body (they should follow the silhouette, not cut across it).
  - Order (top → center → bottom): Gold (top), Teal/Cyan (middle), Violet (bottom).
  - The middle teal line acts as part of an abstract ψ-wave: its central segment extends toward the chest center and suggests the ψ waveform.
  - All three ribbons converge at the bottom into a single stretched point that forms the stinger. The stinger should visually read as a continuation of the three lines (a tapered convergence), not an isolated dot.

- Abdomen banding
  - Three subtle bands (low opacity) aligned with the lower abdomen. Colors: Cyan (upper), Golden (middle, darker yellow), Dark Purple (lower). They should follow the body curve.

- Resonance core (chest)
  - A circular ring with a centered ψ glyph. The ring has cyan tint and a soft cyan glow filter.

- Geometry and line flow (important)
  - All colored curves (antenna stripes, mane/tail ribbons, abdomen bands) must trace the outer body geometry where possible — that is, their control points should be set so the path follows the body silhouette or inner contour rather than cutting straight lines.
  - The teal center line (wave) should extend from the ribbons inward to the resonance core, creating an abstract ψ wave that visually links the tail to the chest.

### File locations

- Vector source: `data/digital_assets/brand/svg/luminai_mascot_logo.svg` (canonical)
- Working exports (to create after approval): `data/digital_assets/brand/png/` (1024x1024, 512x512, 256x256, 120x120)

### Previewing locally

1. Open the SVG in a browser or vector editor (In Windows PowerShell):

```powershell
# open with default viewer (Windows)
Start-Process data/digital_assets/brand/svg/luminai_mascot_logo.svg
```

2. Or open in a design tool (Inkscape, Illustrator) for precise path editing.

### Next actionable steps (pick one)

1. Approve the current implementation and ask me to export PNGs and open a PR.
2. Ask me to finish the SVG so the ribbons strictly follow the body curveature — I will programmatically nudge the ribbon path control points to snap to the body silhouette and re-run a visual preview. (I can open a branch and commit the adjusted SVG.)
3. Request color/size/glyph refinements (supply hex values for colors if you want exact changes).

### Notes on the private key and token snippet

- Keep the PEM out of the repo; path `C:\Users\Ghedd\OneDrive\Projects\TEC\Secrets\...pem` is fine for local use if that folder is private and is in `.gitignore`.
- Use the existing Python helper (`scripts/get_github_app_installation_token.py`) for the installation token exchange; use the PowerShell JWT snippet only for ad-hoc verification if needed.

---
If you want, I can now (A) programmatically adjust the ribbon/curve paths so they hug the body silhouette (recommended), then export PNGs and open a PR; or (B) produce a branch with the current SVG + this markdown and a short README. Tell me which and I'll proceed.
