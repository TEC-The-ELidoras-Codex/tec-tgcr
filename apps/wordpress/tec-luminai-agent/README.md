# TEC LuminAI Agent (WordPress Plugin)

Server-side agent proxy and lightweight chat UI for TEC sites.

- REST endpoint: `POST /wp-json/tec/v1/agent`
- Shortcode UI: `[tec_luminai_agent]`
- Keys live in `wp-config.php` (never in themes or the DB)

## Install

1. Copy the `tec-luminai-agent/` folder into your WordPress `/wp-content/plugins/` directory.
2. Activate “TEC LuminAI Agent” in WP Admin → Plugins.
3. Add API keys to `wp-config.php` (see below).

## Configure (wp-config.php)

Use OpenAI (default):

```php
// OpenAI
define('TEC_OPENAI_API_KEY', 'sk-...');
// Optional overrides
// define('TEC_OPENAI_API_BASE', 'https://api.openai.com/v1');
// define('TEC_OPENAI_MODEL', 'gpt-4o-mini');
```

Or Azure OpenAI (takes precedence when set):

```php
// Azure OpenAI
define('AZURE_OPENAI_ENDPOINT', 'https://<your-endpoint>.openai.azure.com');
define('AZURE_OPENAI_KEY', '...');
define('AZURE_OPENAI_VERSION', '2024-05-01-preview');
define('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o-mini');
```

Security toggles:

```php
// Public access to /wp-json/tec/v1/agent (default true)
// Set to false to require logged-in users
define('TEC_LUMINAI_AGENT_PUBLIC', true);

// Basic rate limit per 10 minutes (default 30 requests/IP)
define('TEC_LUMINAI_RATE_LIMIT', 30);
```

## Use

- Place the shortcode on any page:

```text
[tec_luminai_agent]
```

- Or call the REST endpoint directly (local test):

```powershell
# PowerShell example
$body = @{ messages = @(@{ role = 'user'; content = 'Hello Lumina' }) } | ConvertTo-Json
Invoke-RestMethod -Method Post -ContentType 'application/json' -Uri 'https://your-site.com/wp-json/tec/v1/agent' -Body $body
```

## CI/CD mapping (optional)

If your front-end reads an API URL from environment:

- Set a secret `LUMINAI_API_URL=https://your-site.com/wp-json/tec/v1/agent`
- Use it in your build workflow to point the web app at this site-side proxy.

## Security notes

- The default route is open. For production, toggle `TEC_LUMINAI_AGENT_PUBLIC` to `false` to require logged-in users.
- Basic per-IP rate limiting is enabled via WordPress transients. Adjust `TEC_LUMINAI_RATE_LIMIT` as needed.
- Do not expose API keys to the browser. Keep them in `wp-config.php`.

## Troubleshooting

- If `/wp-json/tec/v1/agent` returns 404, ensure permalinks are enabled and the plugin is active.
- If you see 401/403 from OpenAI/Azure, re-check keys and endpoint.
