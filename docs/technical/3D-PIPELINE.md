# 3D Pipeline — Bring Lumina to Life

This guide shows how to add a simple idle animation to a GLB using Blender headless and embed it on your WordPress site.

## 1) Create an idle animation (headless Blender)

Prereqs: Blender installed and on PATH (or provide full path with `-Blender` parameter).

Run from repo root on Windows PowerShell:

```powershell
# Basic run: import input.glb, export idle-animated GLB
./scripts/run_blender_idle.ps1 -InputGlb "path/to/input.glb" -OutputGlb "ai-workflow/output/lumina_idle.glb" -Frames 180 -Fps 30
```

Under the hood it calls Blender in headless mode to:

- Import the GLB
- Add a gentle breathing/sway idle animation
- Export a GLB with animation enabled

Script entry points:

- `scripts/blender_headless_idle.py`
- `scripts/run_blender_idle.ps1`

## 2) Upload model to WordPress

Upload `lumina_idle.glb` to WordPress Media (e.g., `/wp-content/uploads/YYYY/MM/lumina_idle.glb`).

## 3) Embed on a page using the shortcode

Use the plugin’s shortcode to embed with `<model-viewer>`:

```text
[tec_tgcr_model src="/wp-content/uploads/2025/10/lumina_idle.glb" autoplay="1" camera="auto" ar="0" style="width:100%;height:600px;"]
```

### Options

- `poster`: preview image URL
- `autoplay`: `1` to play on load; omit for manual
- `camera`: `auto` to enable orbit controls
- `ar`: `1` to enable AR (if supported by device)
- `exposure`: tone-mapping exposure (default 1.0)
- `skybox`: environment image for realistic lighting
- `style`: CSS size

## 4) Tips

- Keep file size small for web (reduce textures, compress where possible).
- Use baked animations or lightweight rigs. The provided idle uses transform keyframes only.
- Test on mobile and desktop.

## 5) Next steps

- Add additional animation clips (idle, wave, nod) and switch via `<model-viewer>` `animation-name`.
- Optional: bake facials/visemes for voice sync.
- Build a small UI in WP or your front-end to pick personas/poses.
