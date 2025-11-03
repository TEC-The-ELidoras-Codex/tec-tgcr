# Resonance Bundle (RB) — README

This document introduces the Resonance Bundle (RB) artifact format and how to create, validate, and publish bundles using the tec-tgcr tooling.

Quick summary

- RB is a single, versioned artifact containing an Experience Layer (ritual-first content) and an Evidence Layer (immutable metadata, provenance, verification).
- Use the CLI `tec_tgcr.cli bundle create --source <folder> --target <publish>` to build and publish bundles.
- The RB schema lives at `specs/resonance_bundle_schema.json`.

RB structure

- `id` (string): unique id (UUID)
- `title` (string)
- `created_at` (datetime)
- `experience` (object): ritual_script, soundtrack_descriptor, visual_prompts
- `evidence` (object): evidence_hash, verification_checks, provenance_git, observer_context
- `phi_T`, `psi_R`, `Phi_E` (numbers): TGCR tokens for analytics

Creating a bundle (example)

1. Prepare a source folder with:
   - `ritual.md` (the ritual script)
   - `sound/` (optional audio files)
   - `visuals/` (image assets)
   - `meta.yaml` (minimal manifest with title, tags, phi_T, psi_R, Phi_E)

2. Run the CLI (skeleton provided in `scripts/tec_bundle_cli.sh`):

```bash
bash scripts/tec_bundle_cli.sh create --source ./data/digital_assets/pilot-pizza --output ./artifacts/pilot-pizza-rb.zip --validate
```

3. The CLI will:
   - Validate `meta.yaml` against the RB schema
   - Package files into a ZIP
   - Compute `evidence_hash` (SHA256 of ZIP)
   - Run Airth smoke-tests (if configured)
   - Write `rb.json` (manifest) alongside zipped artifact

Publishing

- Publishing targets are configured in `meta.yaml` or CLI flags (e.g., wordpress, sharepoint, resonance-player).
- Publishing step will call publisher hooks; see `docs/ops/PUBLISHER_HOOKS.md` for specifics.

Verification

- Airth runs a set of automated checks (schema compliance, minimal falsifiability tests).
- Ely records phi_T/psi_R/Phi_E tokens and basic resonance metrics (dwell time, recurrence count).

Development notes

- Schema: `specs/resonance_bundle_schema.json`
- CLI skeleton: `scripts/tec_bundle_cli.sh`
- Templates: `templates/arcadia_translation.md`, `templates/observer_amplification.yaml`

Next: implement CLI flags for publish targets and integrate Airth/Ely hooks.
