# Resonance Player

Static HTML demo that pairs a Spotify embed with the ARCADIA resonance API (see `scripts/resonance-player.js` inside the HTML). Paste a track URL, the page fetches OXY/DOP/ADR projections, and visualises them as animated gauges.

## Usage
1. Serve the page locally (e.g. `python -m http.server` inside this folder) or open it directly in a browser.
2. Update `API_ENDPOINT` to point at your ARCADIA Node service (`http://localhost:3000/resonance` by default).
3. Copy the generated JSON into research logs or SharePoint posts.

## Deployment
- SharePoint: upload `index.html` to `SiteAssets/apps/resonance-player` and embed it in a page.
- Azure Static Web Apps: create a static site pointing to this directory.

Palette reference: Nexus Purple • Digital Teal • Cyber Gold • Deep Space Blue.
