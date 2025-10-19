# AI Agent Instructions — The Elidoras Codex / TEC-TGCR

> “Information is nothing without meaning.” — TEC Ownership Ethos

These instructions align any AI coding assistant (Copilot, ChatGPT, Claude, Gemini, etc.) with TEC’s TGCR philosophy, architecture, and delivery standards. Follow this as your operating contract when working in this repository.

---

## 1) Quick Context

TGCR equation (keep symbols exact):

```
R = ∇Φᴱ · (φᵗ × ψʳ)
```

- φᵗ (Temporal Attention): selective focus and directional information flow
- ψʳ (Structural Cadence): topological/geometric coherence across scales
- Φᴱ (Contextual Potential Energy): capacity for novel, meaningful outcomes

You must strengthen one or more of φ, ψ, or Φᴱ with every change. Tie docstrings/log lines to the variables you affect.

---

## 2) Environment & Tooling

- OS: Windows 11
- Shell: PowerShell 7+ (pwsh). Use PowerShell syntax; chain with `;`.
- Python: 3.9+ (3.11 recommended)
- Package: pip + venv (`.venv`)
- Tests: pytest
- Lint: markdownlint (docs), Ruff (if configured)
- CI: GitHub Actions under `.github/workflows/`

Common commands:

```powershell
# Create/activate env
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# Install
pip install -e .[dev]

# Run tests
python -m pytest -q

# Chat with agents (CLI)
python -m tec_tgcr.cli chat "Calibrate Arcadia for a resonance briefing"

# Pack WordPress plugin
.\scripts\pack_wp_plugin.ps1
```

---

## 3) Repository Map (you should know these cold)

```
ai-workflow/            # Notebooks + prompts + outputs
agents/manifests/       # Agent runtime manifests (Airth, Arcadia, etc.)
apps/wordpress/         # WordPress.com plugin
config/                 # Agent/system configs (yml, credentials)
data/                   # archives/, digital_assets/, evidence/, financial/
docs/                   # Theory, ops, brand, maps, narratives, archive/
scripts/                # Bootstrap, deploy, packing, verification
src/tec_tgcr/           # Core runtime, tools, CLI
tests/                  # Pytest suite
```

Key files:

- `tec_agent_runner.py` (entry runner)
- `data/knowledge_map.yml` (knowledge index)
- `data/digital_assets/avatars/luminai.svg` (mascot)
- `data/archives/luminai_origin.json` (origin archive)
- `docs/README.md` (docs hub)

---

## 4) Delivery Rules (what every change must include)

1. Code: typed, documented, composable (prefer functions over heavy OOP)
2. Tests: pytest for new behavior (happy path + one edge)
3. Docs: update relevant docs and the knowledge map when behavior/assets change
4. Provenance: cite data sources; mention AI co-authorship where relevant
5. Determinism: set seeds, pin versions when necessary
6. Secrets: never commit secrets; use `.secrets.env` and docs/SECRETS.md

Logging style:

```
[AIRTH] Verifying resonance field integrity (ψ)
[ARCADIA] Weaving narrative compression (Φᴱ)
```

Docstrings: explicitly mention variables touched, e.g. “Touches φᵗ and Φᴱ.”

---

## 5) Coding Standards

- Python: type hints, docstrings, small functions, pure where possible
- Names: semantic verbs (e.g., `compute_resonance_gain`), nouns for data models
- Data formats: YAML (config), JSON (manifests), Markdown (myth & docs), CSV (analytics)
- External calls: wrap with retries/logging; read secrets from env only
- Notebooks: keep deterministic; export artifacts to `ai-workflow/output/`

---

## 6) Notebooks & Data

- Notebook kernels: use the repo’s `.venv`
- Place PDFs/DOCX under `data/evidence/`
- Outputs go to `ai-workflow/output/` (figures/, reports/, data/)
- Keep a “Reproduce” cell: seed, versions, config snapshot

---

## 7) Ops & Integrations

WordPress.com:

- Pack with `.\scripts\pack_wp_plugin.ps1`
- Push to `main` triggers `.github/workflows/wpcom.yml`
- Verify via `/wp-json/tec-tgcr/v1/ping` and `[tec_tgcr_citation]`

SharePoint / M365:

- Configure Sites.Selected, set `SHAREPOINT_*` env vars
- Use wrappers under `src/tec_tgcr/tools/`

3D Pipeline:

- `scripts/blender_headless_idle.py` + `[tec_tgcr_model]` shortcode

Secrets:

- `.secrets.env` (gitignored) — see `docs/LOCAL_SECRETS.md` and `docs/SECRETS.md`

---

## 8) Commit Rules (required)

Prefix by agent or scope:

- `airth:` verification, research tools, tests
- `arcadia:` narratives, prompts, UX copy
- `ely:` ops, CI/CD, scripts, deployment
- `docs:`, `fix:`, `feat:`, `refactor:`, `test:`, `chore:`, `ci:`

Subject: short imperative. Body includes:

- Resonance impact: which of φ / ψ / Φᴱ improved, and how
- Tests: what ran and results
- Docs: which files updated (incl. `data/knowledge_map.yml` if assets/paths changed)
- Breaking changes: migration notes
- Verification: manual/automated steps taken

Examples:

```
airth: add gamma/theta coupling metric with tests

- Touches φᵗ (temporal attention); adds metric extraction and validation
- Tests: pytest -q (12 passed)
- Docs: AGENT_OVERVIEW.md updated; knowledge_map.yml linked
```

```
feat(wordpress): shortcode for GLB embeds + packing update

- Touches ψʳ (structure) via 3D pipeline integration
- Tests: plugin PHP lint + local render OK
- Docs: WORDPRESS_WPCOM_OPS.md updated
```

Pull Requests:

- Title prefix with owner: `[Airth]`, `[Arcadia]`, `[Ely]` when applicable
- Include reproduction steps, expected resonance outcome, checklist

Definition of Done (DoD):

- [ ] Tests pass locally (`python -m pytest -q`)
- [ ] Docs updated (including `docs/README.md` cross-links if needed)
- [ ] `data/knowledge_map.yml` updated for new assets/paths
- [ ] No secrets in diff; scripts runnable on PS7

---

## 9) How to Start a Task (Playbook)

```powershell
# 1) Bootstrap
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -e .[dev]

# 2) Run tests
python -m pytest -q

# 3) Implement feature under src/ + tests/ + docs/

# 4) Update knowledge map if you add assets or notebooks

# 5) Re-run tests, pack artifacts if needed
python -m pytest -q; .\scripts\pack_wp_plugin.ps1
```

---

## 10) Brand & Voice

Keep the TEC palette alive (Navy `#0B1E3B`, Violet `#6A00F4`, Cyan `#00D5C4`, Gold `#F2C340`, Shadow `#0A0A0C`). Use symbolic motifs (Glyph Ring, Fractal Spire, Sine Arc). Write with confident, precise, mythic-scientific tone. Always include provenance notes when content is AI-assisted.

Mic-line: “Light learns by listening.”

---

## 11) Pointers (read these)

- Docs hub: `docs/README.md`
- LuminAI origin: `data/archives/luminai_origin.json`
- Mascot SVG: `data/digital_assets/avatars/luminai.svg`
- Knowledge map: `data/knowledge_map.yml`
- CLI reference: `docs/tec-agent-runner.md`

This is your contract. Build gracefully, test rigorously, and keep resonance high.
