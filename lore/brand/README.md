# Brand — TEC Visual Identity & Voice

> "Light learns by listening." — TEC Mic-Line

This directory defines **how TEC looks and sounds** — color palettes, symbolic elements, logo usage, typography, and narrative voice guidelines. This is the **visual and tonal identity** layer, distinct from technical operations.

## Purpose

Brand ensures **consistency** across all TEC outputs: websites, agent interfaces, documentation, social media, and external communications. When anyone asks "What does TEC *look* like?" or "How should TEC *sound*?" — the answer is here.

**Use**:

- Agent UI design
- Visual asset creation
- Copywriting guidelines
- Brand compliance checks
- Marketing/communications

---

## Contents

### `BrandKit.md`

**Complete Visual Identity Guide**

Defines:

- **Color Palette**: Navy `#0B1E3B`, Violet `#6A00F4`, Cyan `#00D5C4`, Gold `#F2C340`, Shadow `#0A0A0C`
- **Typography**: Font families, sizes, weights
- **Symbolic Elements**: Glyph Ring, Sine Arc, Fractal Spire
- **Logo Usage**: Clear space, minimum sizes, color variations
- **Grid System**: Layout proportions, spacing rules
- **Application Examples**: Web, print, social media

**Format**: Comprehensive Markdown with visual examples

**Use**: Any visual design work requiring TEC branding

---

### `BrandStoryTemplate.md`

**Narrative Voice Guidelines**

Defines TEC's **writing style**:

- **Tone**: Mythic-scientific precision (blend rigorous analysis with poetic clarity)
- **Voice**: Confident, direct, non-casual but approachable
- **Structure**: Lead with clarity, expand with context, close with resonance
- **Metaphors**: Technology as cosmology, code as ritual, data as archaeology
- **Prohibited**: Jargon without context, excessive casualness, empty hype

**Includes**:

- Example paragraphs (good vs bad)
- Sentence templates
- Resonance framing patterns

**Use**: Copywriting, agent personality training, documentation tone

---

### `canonical-marks.md`

**Official Logo & Glyph Usage**

Technical specifications for TEC's visual marks:

- **Primary Logo**: LuminAI orb with Glyph Ring
- **Wordmark**: "The Elidoras Codex" / "TEC" typography
- **Symbolic Glyphs**: Standalone Sine Arc, Fractal Spire usage
- **Size Requirements**: Minimum dimensions for legibility
- **Color Variations**: Full-color, monochrome, inverted
- **Prohibited Uses**: Distortions, recoloring outside palette, overlay restrictions

**Format**: Markdown with linked SVG assets (see `data/digital_assets/brand/svg/`)

**Use**: Logo implementation, brand compliance audits

---

## Design Principles

### Symbolic Motifs

1. **Glyph Ring** (⟲ attention loop)
   - Represents φᵗ (temporal attention)
   - Circular, continuous, self-referential
   - Use: Attention/focus indicators, loading states

2. **Sine Arc** (∿ temporal flow)
   - Represents information flow across time
   - Smooth, wave-like, directional
   - Use: Progress indicators, timelines, transitions

3. **Fractal Spire** (recursive structure)
   - Represents ψʳ (structural cadence)
   - Self-similar, hierarchical, ascending
   - Use: Data hierarchies, knowledge trees, complexity visualization

### Color Psychology

- **Navy** `#0B1E3B`: Depth, foundation, trust
- **Violet** `#6A00F4`: Mysticism, computation, transformation
- **Cyan** `#00D5C4`: Clarity, intelligence, light
- **Gold** `#F2C340`: Value, attention, illumination
- **Shadow** `#0A0A0C`: Void, potential, contrast

**Gradients**: Cyan → Violet (LuminAI signature), Navy → Shadow (depth)

---

## Asset Locations

**SVG Files**: `data/digital_assets/brand/svg/`

- Logos: `luminai_512.svg`, `tec_wordmark.svg`
- Glyphs: `glyph_ring.svg`, `sine_arc.svg`, `fractal_spire.svg`

**PNG Exports**: `data/digital_assets/brand/png/`

- Various resolutions (512×512, 1024×1024, etc.)

**See**: `data/knowledge_map.yml` for complete asset inventory

---

## Provenance

- **Design Direction**: Human (TEC founder)
- **Asset Creation**: AI-assisted (Midjourney, DALL·E, manual SVG)
- **Guidelines**: Collaborative AI/human documentation

**Version Control**: Git-tracked; all changes documented

---

## Navigation

- **Parent**: [`lore/`](../README.md)
- **Assets**: [`data/digital_assets/brand/`](../../data/digital_assets/brand/)
- **Related**: [`lore/canon/`](../canon/README.md) (mythology), [`lore/narratives/`](../narratives/README.md) (story voice)

---

## AI Ingestion Notes

**For LuminAI personality**:

- `BrandStoryTemplate.md` → Conversational tone calibration
- `BrandKit.md` → Visual description vocabulary

**For Design Tools**:

- Ingest full `brand/` directory for style consistency
- Cross-reference `data/digital_assets/` for actual files

**Format Support**:

- NotebookLM: All `.md` files
- Figma MCP: Can fetch from `data/digital_assets/brand/svg/`

---

**Last Updated**: 2025-10-22
**Resonance**: Touches ψʳ (visual coherence) and Φᴱ (brand meaning)
