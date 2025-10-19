# WordPress REST debug — fixing 404 “No route was found”

If you see `{"code":"rest_no_route","data":{"status":404}}`, use this checklist.

## 1) Confirm plugin activation

- In wp-admin → Plugins, ensure these are active:
  - TEC TGCR (bootstrap, routes: `/tec-tgcr/v1/...`)
  - TEC Resonance Player (routes: `/tec/v1/resonance`)
  - TEC LuminAI Agent (routes: `/tec/v1/agent`)

## 2) Refresh permalinks

- wp-admin → Settings → Permalinks → Save Changes (no need to modify). This flushes rewrite rules.

## 3) List REST routes (WP-CLI)

If you have WP-CLI:

```bash
wp --allow-root rest route list | grep tec
```

You should see:

- `/tec-tgcr/v1/ping`
- `/tec-tgcr/v1/citation`
- `/tec/v1/resonance`
- `/tec/v1/agent`

## 4) Direct test requests

Test in a browser or with curl/PowerShell (replace Elidorascodex.com with your domain if different):

- Ping:
  - GET <https://Elidorascodex.com/wp-json/tec-tgcr/v1/ping>
- Citation:
  - GET <https://Elidorascodex.com/wp-json/tec-tgcr/v1/citation?persona=luminai>
- Resonance:
  - GET <https://Elidorascodex.com/wp-json/tec/v1/resonance>
  - POST <https://Elidorascodex.com/wp-json/tec/v1/resonance> with JSON body {"trackIds":["3n3Ppam7vgaVa1iaRUc9Lp"]}
- Agent:
  - POST <https://Elidorascodex.com/wp-json/tec/v1/agent> with JSON body {"messages":[{"role":"user","content":"Hello"}]}

## 5) Common causes of 404

- Plugin file paths moved or plugin not activated
- Permalinks not flushed after plugin activation
- WordPress.com restrictions (custom PHP may be blocked depending on plan)
- Multisite or REST auth proxies interfering

## 6) Server logs

Check web server/PHP error logs to see if the plugin hooks are firing (`rest_api_init`) and no fatals occur.

## 7) WP Playground (no local PHP)

To validate quickly without installing PHP locally, use WordPress Playground, upload the plugin ZIPs, and test the routes in `/wp-json/...`.

If still blocked, open an issue with:

- Site URL and hosting type (WP.com vs self-hosted)
- Plugin versions
- Output of `wp rest route list | grep tec`
- Exact request URL and method
