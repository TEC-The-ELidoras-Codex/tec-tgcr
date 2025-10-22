# Spin-Integrated Cosmogram Model — Build Summary

Purpose: Define how to integrate a Top Piece and a Circular Orbit into one working assembly where spin is the core mechanic for both form and function.

## Core Requirements

- Two primary elements: (1) Top Piece, (2) Circular Orbit.
- Both elements must interoperate as a single mechanism.
- Spin is mandatory for each component and the combined system.
- Every sub-component must either generate, transmit, or stabilize spin.

## Why Spin Matters (Concept + Tech)

- Conceptually: Spin symbolizes resonance and phase alignment—it is the engine of the cosmogram.
- Technically: Spin enables momentum storage (flywheel effect), reduces transient jitter, and supports continuous motion cues for UX/visualization.

## Integration Guidance

- Shared axis: Use a common z-axis for synchronized rotation; expose gear ratio if differential motion is desired.
- Bearings: Low-friction hubs (physical) or stable transform origins (digital SVG/CSS) for smooth rotation.
- Coupling: Rigid coupling for locked phase; belt/gear for ratioed phase; magnetic (or easing functions) for soft coupling.
- Balance: Distribute mass (or visual weight) evenly to prevent wobble; use counterweights or symmetric particle fields.

## Implementation Options

- Physical: Thrust bearings + spur/planetary gears; optional clutch for free-spin vs. driven-spin modes.
- Digital (SVG/CSS/JS):
  - Group structure: `&lt;g id="top-piece"&gt;` and `&lt;g id="orbit"&gt;` with `transform-box: fill-box; transform-origin: center`.
  - Animations: CSS keyframes or JS requestAnimationFrame with easing; expose speed (rpm) and phase (radians) as parameters.
  - Accessibility: include `&lt;title&gt;` and `&lt;desc&gt;`; provide reduced-motion fallback.

## Acceptance Criteria

- Both Top Piece and Circular Orbit rotate independently and together without visual or mechanical interference.
- Spin remains stable at min/max speeds; no clipping, jitter, or phase drift beyond specified tolerance.
- Sub-components visibly contribute to or stabilize spin (e.g., vanes, particles, radial glyphs).

## Test Hooks

- Parameters: top_rpm, orbit_rpm, phase_offset, damping.
- Diagnostics: render current angular velocity and phase; provide a toggle to pause and resume.

## Next Steps

- Rig SVG layers for spin with shared axis and adjustable phase.
- Add minimal JS controller exposing rpm/phase.
- Document integration points for UX and physical prototypes.
