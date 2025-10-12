# TEC Resonance Player — WordPress API Plugin

This plugin adds two things to your WordPress site:

- A public REST endpoint: `POST /wp-json/tec/v1/resonance` that computes OXY/DOP/ADR for Spotify track IDs using Spotify Client Credentials (no user login required). If you have an ARCADIA backend, set `TEC_ARCADIA_URL` and calls will proxy to it.
- A pretty route: `/spotify/callback` — a landing page for Spotify Authorization Code (PKCE) flows. It simply shows the `code` and `state` query params so you can verify redirects.

## Install

1. Copy the `tec-resonance-player` folder into `wp-content/plugins/` on your server.
2. In `wp-config.php`, set your Spotify credentials (never put secrets in the theme or public files):

```php
define('TEC_SPOTIFY_CLIENT_ID', 'YOUR_CLIENT_ID');
define('TEC_SPOTIFY_CLIENT_SECRET', 'YOUR_CLIENT_SECRET');
// Optional: forward to ARCADIA if you already run a backend
// define('TEC_ARCADIA_URL', 'https://api.example.com/resonance');
```
3. Activate the plugin in WordPress Admin → Plugins.
4. Visit Settings → Permalinks or run `wp rewrite flush` to ensure `/spotify/callback` works.
5. In the Spotify dashboard, add both redirect URIs:
   - `https://elidorascodex.com/spotify/callback`
   - `http://localhost:3000/callback` (for local dev, if needed)

## Usage

- Frontend player will auto-detect prod and call: `https://elidorascodex.com/wp-json/tec/v1/resonance`.
- POST body:

```json
{"trackIds":["0hHzFiG0FLRJ7N4GwJZzzk"]}
```

- Example curl:

```sh
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"trackIds":["0hHzFiG0FLRJ7N4GwJZzzk"]}' \
  https://elidorascodex.com/wp-json/tec/v1/resonance
```

## Security notes

- Secrets stay server-side in `wp-config.php`.
- The endpoint only returns computed features; no user tokens are stored.
- If you later need playback control, implement Authorization Code with PKCE and use `/spotify/callback` as the redirect page.

## Shortcode

`[tec_resonance_player_hint]` — renders a small block showing the REST URL for debugging.

## Troubleshooting

- After activation, if `/spotify/callback` 404s: go to Settings → Permalinks, click Save to flush rewrites.
- If the REST route 404s, ensure permalinks are enabled and check `Site Address (URL)` in Settings → General.
- For CORS issues when calling from other origins, use the site origin or add proper CORS headers via a microplugin or server config.

---
Made for TEC • The Elidoras Codex.