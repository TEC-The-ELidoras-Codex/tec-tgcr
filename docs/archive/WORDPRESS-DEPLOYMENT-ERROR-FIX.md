# WordPress.com Deployment & REST 404 — Troubleshooting Guide

Date: October 16, 2025

This guide helps resolve the `{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}` error after deployment.

---

## What changed in this repo

- Workflow fix: The artifact now mirrors the site root so WordPress.com deploys into the correct location.
  - We stage the plugin under `wp-content/plugins/tec-tgcr/` inside the artifact.
  - Commit: `wpcom: stage plugin under wp-content/plugins/tec-tgcr for correct deploy` (SHA ends with `0b762a2`).
- Tests: Python test suite is still green (14/14).

---

## Why you see 404 rest_no_route

One or both of these are true:

- The plugin files were deployed to the wrong place (site root instead of `wp-content/plugins/tec-tgcr`), so WordPress never loaded the plugin.
- The plugin is present but not activated, so its `rest_api_init` hooks never ran.

With the new workflow, deployment now places files under the correct directory. You still need to ensure the plugin is Active on the site.

---

## Verify deployment success

1. Check deployment logs

- WordPress.com → Hosting → Deployments → Latest deployment
- Confirm it references the commit `0b762a2` and shows status Succeeded.

2. Check files on the server

- WordPress.com → Hosting → File Manager
- Navigate to `wp-content/plugins/tec-tgcr/`
- You should see `tec-tgcr.php` and other plugin files.

---

## Activate the plugin (critical)

- WordPress Admin → Plugins → Installed
- Find “TEC Agent Stack” v1.0.1
- If it’s Inactive, click Activate.
- If you don’t see it, the deployment hasn’t landed yet; wait a minute and refresh, or re-run the deployment.

---

## Validate routes are registered

1. List all REST routes

- Visit `https://your-site.com/wp-json/` (replace with your domain)
- Search for `tec-tgcr` and `tec_tgcr` in the JSON. You should see entries like:
  - `/tec-tgcr/v1/ping`
  - `/tec_tgcr/v1/ping`

1. Test endpoints directly

- `https://your-site.com/wp-json/tec-tgcr/v1/ping`
- `https://your-site.com/wp-json/tec_tgcr/v1/ping` (compat namespace)
- Optional: `https://your-site.com/wp-json/tec-tgcr/v1/debug`

If these return JSON with `ok: true`, the plugin is active and routes are working.

---

## WordPress.com deployment settings (reference)

- Mode: Advanced
- Workflow file: `wpcom.yml`
- Artifact name: `wpcom`
- Artifact content must mirror site root. For plugins, include: `wp-content/plugins/tec-tgcr/...`

We’ve updated `.github/workflows/wpcom.yml` to do exactly this.

---

## Common pitfalls and quick fixes

- Wrong site or domain: Ensure you’re testing the exact domain the deployment targets (production vs staging).
- Cache delay: Add a cache-buster to the URL, e.g., `?ts=1699999999` or try an incognito window.
- Plugin not activated: Activate it under Plugins. Routes are registered on activation via `rest_api_init`.
- Mixed workflow modes: If you previously used SSH/SFTP workflows, make sure WordPress.com is now pointing to the artifact workflow (`wpcom.yml`). Reconnect GitHub if needed.

---

## Advanced: validate via shortcode

- Add a page with `[tec_tgcr_ping]` and view it; the link should point to `/wp-json/tec-tgcr/v1/ping`.
- Add `[tec_tgcr_citation persona="luminai"]` to see a public-domain quote.

---

## If it’s still 404

- Confirm the plugin files exist at `wp-content/plugins/tec-tgcr/`.
- Deactivate and reactivate the plugin to force a fresh hook registration.
- Verify the REST base works at `/wp-json/` and that general endpoints (like `/wp-json/wp/v2/types`) return JSON.
- Try both namespaces: `tec-tgcr` and `tec_tgcr`.
- If the route appears under `/wp-json/` but direct hits 404, the domain may be fronted by a caching/CDN. Test from a different network or add `?ts=<unix>`.

---

## Artifact structure (current, correct)

```text
.wpcom-dist/
└── wp-content/
    └── plugins/
        └── tec-tgcr/
            ├── tec-tgcr.php
            └── ...
```

This mirrors the WordPress site root so WordPress.com places files correctly.

---

## Summary

- We corrected the artifact structure so deployments land in `wp-content/plugins/tec-tgcr`.
- After the next deployment, activate the plugin in WP Admin, then verify:
  - `/wp-json/tec-tgcr/v1/ping`
  - `/wp-json/tec_tgcr/v1/ping`
  - `/wp-json/tec-tgcr/v1/citation?persona=luminai`

Once these return JSON, the REST 404 is resolved.
