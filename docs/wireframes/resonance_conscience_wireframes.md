# Resonance Conscience Notebook — Wireframe Brief

This brief captures the initial wireframe pass for the Resonance Conscience Notebook application. Each view lists critical elements, interaction notes, and cross-links to supporting data assets.

## 1. Daily Capture Workspace

- **Journal Canvas:** Markdown editor with inline tag chips, context breadcrumbs, and autosave indicator.
- **Audio Module:** Record/stop control, live waveform, diarization markers, upload fallback.
- **Music Context Panel:** Currently playing track metadata (art, tempo, key, valence, energy), manual track search, “link to entry” CTA.
- **Mood Dial:** Quick sliders for DOP/OXY/ADR with historical sparkline preview.
- **Run Manifest Badge:** Displays deterministic seed + signer when summaries are generated.

## 2. Resonance Timeline

- **Scrollable Timeline:** Chronological cards (note preview, track, mood delta, summary excerpt).
- **Filter Rail:** Tags, time span, BPM range, valence range, query search.
- **Continuity Alerts:** Badges for gaps, backfill reminders, or schema migrations.
- **Analytics CTA:** Jump-to analysis dashboards.

## 3. Resonance Engine Summary Deck

- **Daily/Weekly Toggle:** Switch between time horizons.
- **Summary Card:** Deterministic LLM output with citations list and expand-to-view-run-manifest.
- **Affective Stabilization Graph:** Correlates mood trend with tempo/energy overlays.
- **Action Chips:** Suggested playlists, prompts, or counterfactual questions from Journal Guardian.

## 4. Mythic Resonance Map (Reader Mode)

- **Graph Snapshot:** Embed of mythic story analysis (import from `analysis/mythic_story_analysis.md`).
- **Node Spotlight:** Select archetype to view relationships, transcripts, linked notes.
- **Guidance Thread:** Highlights dotted edges as mentorship cues with citations.

## 5. Settings & Provenance

- **Secrets Vault:** Lists tokens stored in `secrets-local/` with renewal reminders.
- **Encryption Hub:** Key rotation control, export signed manifest.
- **Sync Panel:** Toggle offline/online, cloud sync targets, telemetry opt-ins.

## Next Steps

1. Flesh out low-fidelity sketches (Balsamiq/Figma) referencing these sections.
2. Align UI states with API contracts from upcoming schema work.
3. Validate flows with SUS-style usability prompts and mood tracking KPIs.
