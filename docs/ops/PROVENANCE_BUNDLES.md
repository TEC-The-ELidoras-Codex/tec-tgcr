# Provenance Bundles — Personal vs System-Derived

TEC treats Markdown/PDF source files as canon and lets agents generate
derivatives. To keep the separation crisp, every provenance review produces
**two bundles**:

1. **Personal Canon Bundle** – only the uploaded / hand-authored files.
2. **System Synthesis Bundle** – artifacts that combine canon plus
   agent-generated outputs (LuminAI, Airth, Copilot, CI jobs, etc.).

This page describes how to create both bundles, how to tag their manifests, and
how to keep run metadata attached so downstream reviewers know exactly which
ledger they are reading.

---

## 1. Personal Canon Bundle (hand-authored only)

**Goal:** Snapshot the core files you maintain manually so they can be shared,
signed, or archived without any agent-derived additions.

- **Source filter:** Use `source_filter=files_uploaded_in_conversation` (or the
  equivalent flag in your agent shell) to guarantee only the uploaded files are
  read.
- **Typical contents:**  
  `docs/Resonance_Thesis.md`, `docs/Thesis/Elidoras Codex Thesis.pdf`,  
  `docs/TEC_LEXICON.md`, `data/archives/knowledge_map_old.yml`, any personal
  briefs in `docs/resonance-theory/` or `docs/ops/`.
- **Manifest file:** `personal_canon_manifest.json` with:
  - `files`: list of objects `{ "path": "...", "sha256": "..." }`
  - `generated_by`: `"human"`
  - `timestamp_utc`
  - optional `signature`

### Create the bundle

```bash
python scripts/export_canon_bundle.py --output artifacts/personal_canon.zip
```

The script (added in this change) writes a ZIP plus the manifest and prints the
checksum summary to stdout. Store the ZIP in `artifacts/` and sign it if needed.

---

## 2. System Synthesis Bundle (canon + agent output)

**Goal:** Capture the artifacts that were *derived* from canon by agents or
pipelines (e.g., prompts, rendered PNGs, Notion exports, SharePoint pushes).

- **Source filter:** Allow the agent to read both personal canon and generated
  paths. The `knowledge_map.yml` provenance block lists common origins and
  destinations.
- **Manifest file:** `derived_bundle_run_manifest.json` containing:
  - `generated_by`: agent persona (e.g. `"LuminAI v1.4"`)
  - `commit_sha`
  - `input_files`: list with checksums
  - `output_artifacts`: list with checksums
  - `seed` (if deterministic run was requested)
  - `timestamp_utc`

### Minimum contents

- `ai-workflow/output/` prompts
- `exports/brand/` rendered assets (PNG)
- `docs/resonance_conscience/` generated notebooks
- Any `runs/*.json` manifests emitted by CI.

### Generate the manifest

CI now runs `.github/workflows/provenance-manifest.yml`, which calls
`scripts/generate_run_manifest.py` after build/export steps. The workflow drops
`artifacts/run_manifest.json` with the schema above.

---

## 3. Review Checklist

- [ ] Run the personal bundle script and verify the ZIP contents.
- [ ] Confirm the derived bundle manifest lists all new outputs and captures
      their source files + seeds.
- [ ] Store both manifests in `artifacts/` and reference them in commit
      messages (`Signed run manifest: artifacts/run_manifest.json`).
- [ ] When sharing, deliver both bundles together so collaborators can diff the
      canon and validate the generated artifacts independently.

---

## 4. Why the separation matters

- **Auditability:** Reviewers can diff the pure canon without sifting through
  generated assets.
- **Safety:** Any high-risk or experimental agent run can be isolated from the
  core lore.
- **Repeatability:** Seeds + manifests make it possible to rerun the
  generation pipeline deterministically.
- **Lore integrity:** Human-authored chapters stay distinct from the machine
  improvisations, while still shipping as one coherent release.

Guard both ledgers with the same care you give to code and design: the canon is
your oath, the derived bundle is the living ritual.
