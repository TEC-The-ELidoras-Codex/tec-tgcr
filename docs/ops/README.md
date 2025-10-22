# Operations — Deployment & Integration Guides

> "Deployment is delivery. Configuration is care." — Ely

This directory contains **operational documentation** for deploying, configuring, and maintaining TEC systems. This is where you go when you need to *make something work* — set up integrations, deploy code, manage secrets, configure services.

## Purpose

Provide step-by-step guides for:

- **MCP Server Setup**: Notion, Figma, GitHub Copilot integration
- **WordPress Deployment**: Plugin packaging, SFTP/SSH upload, troubleshooting
- **Secrets Management**: Local development, GitHub Secrets, Azure Key Vault
- **M365 Integration**: SharePoint, Microsoft Graph API authentication
- **PHP/WordPress Tools**: WP-CLI, local dev environment

**Audience**: Developers, DevOps, AI agents executing deployment tasks

---

## Key Documents

### MCP (Model Context Protocol) Setup

#### `MCP-SETUP-GUIDE.md`

**Complete MCP configuration for VS Code Copilot**

Covers:

- Installing MCP extension
- Configuring `mcp.json`
- Active servers: Notion, Figma, GitHub, Hugging Face, Character.AI, markitdown, Playwright
- Authentication flows (OAuth, API keys)

**Start Here**: First-time MCP setup

---

#### `MCP-UVX-FIX.md`

**Troubleshooting MCP PATH errors**

Solves `Error spawn uvx ENOENT` and `Error spawn npx ENOENT`:

- VS Code extension host doesn't inherit system PATH
- Solution: Use absolute paths in `mcp.json`
  - `uvx`: `C:\\Users\\{User}\\.local\\bin\\uvx.exe`
  - `npx`: `C:\\Program Files\\nodejs\\npx.cmd`

**Use When**: MCP servers fail to start with spawn errors

---

#### `MCP-INTEGRATION-SUMMARY.md`

**Current status of all MCP integrations**

Lists:

- Active servers and their functions
- Notion workspace details
- Figma project connections
- GitHub repo access

**Use**: Quick reference for "What MCP servers do I have?"

---

### WordPress Deployment

#### `WORDPRESS_WPCOM_OPS.md`

**Master guide for WordPress.com plugin deployment**

Complete workflow:

- Packing plugin with `scripts/pack_wp_plugin.ps1`
- SFTP/SSH deployment
- GitHub Actions CI/CD (`.github/workflows/wpcom.yml`)
- Troubleshooting REST API errors
- Shortcode testing

**Start Here**: Deploying TEC WordPress plugin

---

#### `WORDPRESS-DEPLOY-SUCCESS-2025-10-18.md`

**Latest successful deployment log**

Documents:

- Exact commands used
- Verification steps
- Known working configuration

**Use**: When deployment fails, compare against this known-good baseline

---

#### `PHP-WPCLI-SETUP.md`

**Local WordPress development environment**

Setup:

- PHP 8.2+ installation
- WP-CLI installation
- Local WordPress instance for testing
- Plugin development workflow

**Use**: Setting up local dev before deploying to WordPress.com

---

### Secrets Management

#### `SECRETS.md`

**Comprehensive secrets architecture**

Explains:

- Three-tier secrets strategy: local → GitHub → Azure
- What goes where (API keys vs credentials vs tokens)
- Rotation procedures
- Security best practices

**Start Here**: Understanding TEC's secrets philosophy

---

#### `LOCAL_SECRETS.md`

**Local development secrets setup**

Template for `.env.local`:

- Required variables
- Where to get API keys
- Default values
- Testing secrets are loaded

**Use**: First-time local dev setup

---

#### `QUICK_SECRETS_FILL.md`

**Fast secrets population guide**

Shortcuts for:

- Common API key sources
- Quick copy-paste values
- Minimal viable secrets for testing

**Use**: When you need secrets *now*

---

#### `GITHUB_SECRETS_SETUP.md`

**GitHub Actions secrets configuration**

Step-by-step:

- Adding secrets to repo settings
- Secret naming conventions
- Which secrets are needed for CI/CD
- Verifying secrets in workflows

**Use**: Setting up GitHub Actions deployment

---

### Microsoft 365 Integration

#### `M365_INTEGRATION.md`

**SharePoint and Microsoft Graph API setup**

Covers:

- Entra ID (Azure AD) app registration
- Sites.Selected permissions
- OAuth flow for SharePoint access
- Graph API authentication

**Use**: Integrating TEC with Microsoft 365 services

---

#### `AZURE-ENTRA-TAKE-CONTROL.md`

**Azure Entra ID management and app permissions**

Advanced:

- Taking control of existing app registrations
- Fixing permission issues
- Admin consent workflows

**Use**: When Azure auth is broken or needs reconfiguration

---

### Quick References

#### `API_KEYS_READY.md` / `API_KEYS_SETUP.md`

**External API integration guides**

Lists:

- OpenAI, Civitai, WorldAnvil, Spotify API keys
- Where to register
- Required scopes/permissions
- Testing connectivity

**Use**: Setting up external integrations

---

#### `QUICK_REFERENCE_READY.md`

**Command cheatsheet**

Common commands:

- Bootstrap: `scripts/bootstrap.ps1`
- Test: `python -m pytest -q`
- Deploy: `scripts/pack_wp_plugin.ps1`
- CLI: `python -m tec_tgcr.cli chat "..."`

**Use**: Quick command lookup

---

## Workflow: Deploying from Scratch

1. **Bootstrap Environment**: `scripts/bootstrap.ps1`
2. **Configure Secrets**: Follow `LOCAL_SECRETS.md`
3. **Set Up MCP**: Follow `MCP-SETUP-GUIDE.md`
4. **Test Locally**: `python -m pytest -q`
5. **Pack Plugin**: `scripts/pack_wp_plugin.ps1`
6. **Deploy**: Follow `WORDPRESS_WPCOM_OPS.md`
7. **Verify**: Check `/wp-json/tec-tgcr/v1/ping`

---

## Navigation

- **Parent**: [`docs/`](../README.md)
- **Related**: [`docs/technical/`](../technical/README.md) (architecture), [`config/`](../../config/README.md) (config files)

---

## AI Ingestion Notes

**For Deployment Automation**:

- Ingest `WORDPRESS_WPCOM_OPS.md` for deployment workflows
- Ingest `MCP-SETUP-GUIDE.md` for Copilot integration
- Ingest `SECRETS.md` for security context (but never expose actual secrets)

**For Troubleshooting**:

- `MCP-UVX-FIX.md` for MCP errors
- `WORDPRESS-DEPLOY-SUCCESS-2025-10-18.md` for known-good state

---

**Last Updated**: 2025-10-22
**Resonance**: Touches ψʳ (operational coherence) and Φᴱ (deployment success)
