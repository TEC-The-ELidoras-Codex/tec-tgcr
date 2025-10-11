# Voice Imprint Studio

A lightweight React/Vite starter that lets you load, edit, and export voice profile JSON files in the TEC house style. Use it to maintain persona manifests for Arcadia, Airth, or future agents before syncing them back into SharePoint or the repo.

## Quick start

```bash
npm create vite@latest voice-imprint-studio -- --template react-ts
cd voice-imprint-studio
npm install
npm run dev
```

After scaffolding the Vite app, copy the contents of `src/App.tsx` with the component provided in `templates/App.tsx` and drop any shared UI helpers in `src/components/`.

## TEC-specific guidance
- Keep the editable JSON schema aligned with `voice_profile_template.json` in the root of this repo.
- Surface copy-to-clipboard actions for `/agents/.../instructions/*.md` so Copilot can ingest the updates quickly.
- When exporting, generate Markdown notes alongside the JSON so SharePoint pages can render them directly.

## Deployment
- For SharePoint: build with `npm run build` and upload the `dist/` folder to `SiteAssets/apps/voice-imprint-studio`.
- For Azure Static Web Apps: connect this folder and enable CI/CD through GitHub Actions.

