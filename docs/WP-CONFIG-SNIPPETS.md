# WordPress wp-config snippets — TEC TGCR plugins

This page lists copy-ready constants to paste into `wp-config.php` for the TEC plugins. Use these on self‑hosted WordPress. For WordPress.com, see notes below.

Note: Do not commit secrets to git. Keep them server-side only.

## Resonance Player (Spotify)

Add server-side client credentials for the Spotify Web API. The plugin uses these to exchange a server token and render resonance safely.

```php
// TEC: Resonance Player — Spotify API credentials
define('TEC_SPOTIFY_CLIENT_ID',    'your_spotify_client_id');
define('TEC_SPOTIFY_CLIENT_SECRET','your_spotify_client_secret');
```

Optional: If you prefer not to store Spotify creds on WordPress, point the plugin to an external proxy you control.

```php
// TEC: Arcadia proxy URL (resonance via proxy) — the plugin will POST here instead of Spotify
define('TEC_ARCADIA_URL', 'https://your-api.example.com/resonance');
```

## LuminAI Agent (OpenAI / Azure OpenAI)

Provide either an OpenAI key or Azure OpenAI details. Use only one mode at a time.

OpenAI API (api.openai.com):

```php
// TEC: LuminAI Agent — OpenAI
define('TEC_OPENAI_API_KEY', 'sk-your-openai-key');
```

Azure OpenAI (preferred in enterprise):

```php
// TEC: LuminAI Agent — Azure OpenAI
define('AZURE_OPENAI_ENDPOINT', 'https://<your-name>.openai.azure.com');
define('AZURE_OPENAI_KEY',      'your-azure-openai-key');
// Use the API version your resource supports
define('AZURE_OPENAI_VERSION',  '2024-05-01-preview');
// The model deployment name in your Azure OpenAI resource (e.g., gpt-4o-mini)
define('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o-mini');
```

## WordPress.com vs self‑hosted

- WordPress.com often restricts direct edits to `wp-config.php`. If you cannot set constants there:
  - Prefer the proxy mode (`TEC_ARCADIA_URL`) so the site calls your backend, and keep secrets off WordPress.com.
  - Or migrate to a self‑hosted WordPress or a host that lets you edit `wp-config.php`.
- The current plugins read constants; they don’t yet provide an admin UI to store keys. If you need an options page, open an issue and we can add one.

## Quick verification

After adding constants and activating plugins:

- Resonance Player routes:
  - GET /wp-json/tec/v1/resonance (returns usage hint)
  - POST /wp-json/tec/v1/resonance (body: {"trackIds":["3n3Ppam7vgaVa1iaRUc9Lp"]})
- LuminAI Agent route:
  - POST /wp-json/tec/v1/agent (body: {"messages":[{"role":"user","content":"Hello"}]})

If these 404, see `docs/WORDPRESS-REST-DEBUG.md`.
