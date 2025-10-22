# TEC Scripts — Automation & Deployment

> "Automate the ritual." — Ely's Ops Principle

This directory contains **all PowerShell scripts for automation, deployment, cleanup, and repository management**.

## Purpose

Provide **runnable automation** for:

- Repository consolidation and cleanup
- WordPress plugin packing and deployment
- Environment verification
- Azure resource control
- Blender 3D pipeline headless rendering
- Support bundle generation

**Distinction**:

- If it's **instructions** → `docs/ops/`
- If it's **runnable automation** → `scripts/` (you're here)

---

## Structure

```
scripts/
├─ consolidate_repo.ps1        # Repository structure consolidation
├─ cleanup_repo.ps1             # Cache cleanup (.pyc, __pycache__, etc.)
├─ pack_wp_plugin.ps1           # WordPress plugin ZIP creation
├─ deploy_wp_plugin.ps1         # WordPress.com SFTP deployment
├─ pack_support_bundle.ps1      # Generate support/audit bundle
├─ bootstrap.ps1                # Initial environment setup
├─ check_env.ps1                # Verify environment readiness
├─ azure_take_control.ps1       # Azure Entra takeover automation
├─ blender_headless_idle.py     # Blender idle scene headless render
├─ run_blender_idle.ps1         # PowerShell wrapper for Blender
├─ start_sd_api.ps1             # Stable Diffusion API server
├─ sanitize_spotify_url.ps1     # Spotify URL cleanup
├─ generate_prompts.py          # Batch prompt generation
├─ refresh_readme.py            # README regeneration
└─ README.md                    # This file
```

---

## Key Scripts

### Repository Management

**`consolidate_repo.ps1`**

- **Purpose**: Major repository structure consolidation
- **Actions**: Remove duplicates, move configs, clean archives
- **Flags**: `-DryRun` (preview changes), `-Force` (execute)
- **Usage**: `.\scripts\consolidate_repo.ps1 -DryRun`

**`cleanup_repo.ps1`**

- **Purpose**: Clean Python caches, temp files, build artifacts
- **Safe**: Always safe to run before commits/tests
- **Usage**: `.\scripts\cleanup_repo.ps1`

### WordPress Deployment

**`pack_wp_plugin.ps1`**

- **Purpose**: Create `tec-tgcr-x.x.x.zip` for WordPress.com deployment
- **Output**: `exports/wp-plugin/`
- **Usage**: `.\scripts\pack_wp_plugin.ps1`

**`deploy_wp_plugin.ps1`**

- **Purpose**: SFTP deploy to WordPress.com
- **Requires**: `WPCOM_SSH_PRIVATE_KEY_PATH` in `.env.local`
- **Usage**: `.\scripts\deploy_wp_plugin.ps1`

### Environment & Verification

**`bootstrap.ps1`**

- **Purpose**: Initial repo setup (create .venv, install deps)
- **Usage**: `.\scripts\bootstrap.ps1`

**`check_env.ps1`**

- **Purpose**: Verify Python, venv, secrets, paths
- **Usage**: `.\scripts\check_env.ps1`

### Azure Management

**`azure_take_control.ps1`**

- **Purpose**: Entra ID takeover (verify ownership, elevate access)
- **Requires**: Azure CLI (`az`) authenticated
- **Usage**: `.\scripts\azure_take_control.ps1`

### 3D Pipeline

**`blender_headless_idle.py`**

- **Purpose**: Render Blender scene headless (server-side)
- **Usage**: `python scripts/blender_headless_idle.py --scene idle --output renders/`

**`run_blender_idle.ps1`**

- **Purpose**: PowerShell wrapper for Blender headless execution
- **Usage**: `.\scripts\run_blender_idle.ps1`

### Utilities

**`pack_support_bundle.ps1`**

- **Purpose**: Generate support/audit bundle (docs, evidence, manifests)
- **Output**: `exports/support/`
- **Usage**: `.\scripts\pack_support_bundle.ps1`

**`generate_prompts.py`**

- **Purpose**: Batch generate AI prompts from templates
- **Output**: `ai-workflow/output/`
- **Usage**: `python scripts/generate_prompts.py`

**`sanitize_spotify_url.ps1`**

- **Purpose**: Clean Spotify share URLs (remove tracking params)
- **Usage**: `.\scripts\sanitize_spotify_url.ps1 -Url "https://..."`

---

## Execution Requirements

### PowerShell

- **Version**: PowerShell 7+ (`pwsh`)
- **Policy**: `-ExecutionPolicy Bypass` (use with caution)
- **Common Pattern**: `pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/<script>.ps1`

### Python Scripts

- **Environment**: Use repo `.venv` (activate first)
- **Common Pattern**: `python scripts/<script>.py`

---

## AI Context Guidelines

When referencing scripts for AI agents:

1. **Ops Automation**: Agents can *suggest* running scripts but should not execute without confirmation
2. **Read Scripts**: Always read script content before recommending execution
3. **Flags**: Prefer `-DryRun` for preview; require explicit `-Force` for changes
4. **Secrets**: Never log secrets; scripts handle via `.env.local`

---

## NotebookLM / MS Notebook Ready

**Not Applicable**: Scripts are executable code, not documentation. For AI ingestion, refer to:

- Script **purpose**: Documented above
- Script **instructions**: See `docs/ops/` for step-by-step guides
- Script **code**: Read `.ps1`/`.py` files directly if analyzing logic

---

## Related Directories

- **Operations Docs**: [`docs/ops/`](../docs/ops/README.md)
- **Technical Docs**: [`docs/technical/`](../docs/technical/README.md)
- **CI/CD Workflows**: [`.github/workflows/`](../.github/workflows/)

---

**Last Updated**: 2025-10-22
**Resonance**: Touches **ψʳ** (structural automation) and **φᵗ** (operational attention)
**Provenance**: Human-authored automation; AI-documented
