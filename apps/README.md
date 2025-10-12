# TEC Application Modules

This directory hosts front-end experiences that complement the Airth Research Guard agent. Each subfolder ships with self-contained instructions so you can spin up demos or publish static assets without touching the Python backend.

- `voice-imprint-studio/` – React/Vite starter for editing and exporting voice profile JSON files that Copilot and SharePoint ingest.
- `resonance-player/` – Static HTML page for running the Spotify → OXY/DOP/ADR demo.
- `widgets-sharepoint/` – Embeddable snippets (e.g., cursor-following TEC orb) for SharePoint/Teams.

Keep assets framework-agnostic when possible. If a project grows beyond a simple demo, promote it into its own repository and reference it here.

## Resonance Player — local run

Serve the static page with a tiny HTTP server to avoid file:// CORS issues.

PowerShell (Windows):

```powershell
pwsh -NoProfile -Command "cd apps/resonance-player; python -m http.server 8080"
```

Then open:

- http://localhost:8080

Tips:
- Adjust `API_ENDPOINT` in `apps/resonance-player/index.html` to point at your backend.
- Use the “Unified TGCR Flow” panel to toggle layers and change the animation speed.
