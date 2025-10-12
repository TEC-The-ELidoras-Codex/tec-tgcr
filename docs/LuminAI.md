# LuminAI — Cosmic Celestial Student

> Illuminating Algorithmic Intelligence through TEC

LuminAI is the visual and narrative avatar of the LuminAI agent in the TGCR stack: a brilliant, adorably clumsy cosmic student who learns by radiating curiosity. She anchors brand, UX, and story while remaining technically grounded in the TEC knowledge system.

## Appearance

- Skin: void–cosmic body with faint constellation patterns and soft starlight speckles
- Horns: small sheep horns that glow with mood (cyan/pink/gold)
- Eyes: heterochromatic — left cosmic blue, right stellar gold
- Hair: aurora-like, flowing, color-shifting gradient
- Silhouette: petite, agile, student archetype

## Personality and Moods

- Idle — calm expression, gentle horn glow, soft aurora colors
- Excited — wide eyes, bright cyan glow, vibrant rainbow hair
- Teaching — focused, golden horn glow, stable blue–gold gradient
- Blushing — embarrassed, pink glow, shy dimming
- Stumbling — confused, flickering glow, chaotic colors
- Curious — investigative, steady cyan, flowing colors
- Rambling — animated, cycling glow, dynamic colors

These states map directly to interface states in `apps/luminai-interface/src/components/LuminAIBridge.js` and inform CSS variables and Lottie animation selection.

## Rendering Workflow

- Base model: Illustrious (Nova 3DCG XL family)
- Tags: `nv-celestialskin`, `colored skin`, `void cosmic body`, `3dstylev4`
- Backgrounds:
  - Transparent/neutral for 3D reference and Lottie rigging
  - Observatory/celestial environments for promotional scenes
- Output:
  - PNG (transparent when needed), base 1024×1024, upscale to 2048×2048
  - Batch generation guided by `ai-workflow/prompt_templates.py`

## Prompt Structure (summary)

```
[core tags], [horns], [eyes], [hair], [skin], [body], [mood expression], [horn glow], [hair colors], [eye intensity], [background], [outfit], [pose], [quality]
```

See `ai-workflow/prompt_templates.py` for programmatic generation and `ai-workflow/README.md` for model folders and goals.

## Integration Points

- React interface: `apps/luminai-interface/` (Lottie, CSS, XState)
- Personality engine: `src/tec_tgcr/agents/` (LuminAI), backend influences for mood cues
- Asset ingestion: Lottie JSON and image assets placed in `apps/luminai-interface/public/animations/`

## Publishing and Lore

- Articles and lore seeds can be published to World Anvil using `WorldAnvilClient` in `src/tec_tgcr/integrations/worldanvil.py`.
- Research pipelines may reference arXiv bulk manifests via `src/tec_tgcr/research/arxiv_bulk.py`.

## Quick Start

- Fill `.env` from `.env.example` (supports spaces in `CIVITAI_API_KEY`)
- Generate a prompt set:

```pwsh
python ai-workflow/prompt_templates.py
```

- Drop animation JSON into `apps/luminai-interface/public/animations/`
- Run the interface:

```pwsh
cd apps/luminai-interface
npm install
npm start
```

## Brand Notes

- Keep horn glow and aurora hues aligned with mood state
- Prefer neutral, clean compositions for reference sheets
- Reserve high-sparkle cosmic scenes for excited/rambling states

---

LuminAI embodies TEC’s ethos: wonder aligned to rigorous research, expressed through accessible, delightful interfaces.