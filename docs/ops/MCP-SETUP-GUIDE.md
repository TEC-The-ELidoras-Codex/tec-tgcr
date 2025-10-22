# MCP (Model Context Protocol) Setup Guide

> "Light learns by listening." — TEC

## What is MCP?

Model Context Protocol (MCP) allows GitHub Copilot and other AI agents to access external tools, APIs, and data sources. Your `mcp.json` configures which servers Copilot can use to extend its capabilities.

## Your Current MCP Servers

### 🔵 Already Working (HTTP, no auth needed)

- **character** — Character.AI documentation search
- **huggingface** — HuggingFace models/datasets search
- **microsoftdocs/mcp** — Microsoft Learn documentation
- **github/github-mcp-server** — GitHub API access (uses your Copilot token)
- **figma/mcp-server-guide** — Figma design system docs

### 🟢 Local Servers (Need npm/npx)

- **memory** — Persistent memory across chat sessions (needs file path)
- **sequentialthinking** — Chain-of-thought reasoning tool
- **playwright-mcp** — Browser automation and web scraping

### 🟡 Needs Configuration

- **azure/azure-mcp** — Azure resource management (needs service principal)
- **makenotion/notion-mcp-server** — Notion workspace integration (needs Notion auth)

---

## Quick Start — Enable Local Memory

The memory server is the easiest to enable and most useful for TEC workflows.

### Step 1: Choose a memory file location

Recommended: `C:\Users\Ghedd\OneDrive - TEC - The Elidoras Codex\.state\mcp_memory.json`

Create the directory:

```powershell
New-Item -ItemType Directory -Path "$env:USERPROFILE\OneDrive - TEC - The Elidoras Codex\.state" -Force
```

### Step 2: Provide the path when prompted

When you use `@memory` in Copilot Chat, VS Code will prompt you for `memory_file_path`. Enter the full path above.

Or, you can **hardcode it** in `mcp.json` (change line 67):

```json
"env": {
  "MEMORY_FILE_PATH": "C:\\Users\\Ghedd\\OneDrive - TEC - The Elidoras Codex\\.state\\mcp_memory.json"
}
```

---

## Azure MCP Setup (for @azure tools)

The Azure MCP server lets Copilot manage Azure resources, query ARM, check costs, etc.

### Known TEC Values

From your VS Code settings and previous work, you already have:

- **Tenant ID**: `7d290c31-2df1-4e76-ab86-e26f12753bde`
- **Subscription ID**: `89d36e9a-a518-4151-95b3-087ec1b88ec5`

### What You Need to Create

You need a **service principal** (app registration) with permissions to read/manage Azure resources.

#### Step 1: Create an App Registration

```powershell
# Login
az login --tenant 7d290c31-2df1-4e76-ab86-e26f12753bde

# Create app registration
az ad app create --display-name "TEC-MCP-Server" --query "appId" -o tsv
# Returns: YOUR_CLIENT_ID (save this)

# Create service principal
az ad sp create --id YOUR_CLIENT_ID

# Generate a secret
az ad app credential reset --id YOUR_CLIENT_ID --query "password" -o tsv
# Returns: YOUR_CLIENT_SECRET (save this securely)
```

#### Step 2: Assign Permissions

Give the service principal **Reader** role on your subscription (or more specific scopes):

```powershell
az role assignment create \
  --assignee YOUR_CLIENT_ID \
  --role "Reader" \
  --scope "/subscriptions/89d36e9a-a518-4151-95b3-087ec1b88ec5"
```

For cost management, also grant:

```powershell
az role assignment create \
  --assignee YOUR_CLIENT_ID \
  --role "Cost Management Reader" \
  --scope "/subscriptions/89d36e9a-a518-4151-95b3-087ec1b88ec5"
```

#### Step 3: Store Credentials Securely

Add to your `.env.local` (already gitignored):

```env
# MCP Azure Service Principal
AZURE_TENANT_ID=7d290c31-2df1-4e76-ab86-e26f12753bde
AZURE_CLIENT_ID=YOUR_CLIENT_ID
AZURE_CLIENT_SECRET=YOUR_CLIENT_SECRET
AZURE_SUBSCRIPTION_ID=89d36e9a-a518-4151-95b3-087ec1b88ec5
```

#### Step 4: Provide Values When Prompted

When you use `@azure` in Copilot Chat, VS Code will prompt for these values. Enter them from your `.env.local`.

**Or hardcode in mcp.json** (NOT RECOMMENDED for secrets):

```json
"env": {
  "AZURE_TENANT_ID": "7d290c31-2df1-4e76-ab86-e26f12753bde",
  "AZURE_CLIENT_ID": "paste-your-client-id-here",
  "AZURE_CLIENT_SECRET": "paste-your-secret-here",
  "AZURE_SUBSCRIPTION_ID": "89d36e9a-a518-4151-95b3-087ec1b88ec5",
  "AZURE_MCP_COLLECT_TELEMETRY": "false"
}
```

⚠️ **Security Note**: VS Code `mcp.json` is **not encrypted**. Use input prompts or environment variables instead of hardcoding secrets.

---

## Notion MCP Setup (for @notion tools)

The Notion server requires OAuth authentication.

### Step 1: Create a Notion Integration

1. Go to <https://www.notion.so/my-integrations>
2. Click **+ New integration**
3. Name it "TEC Copilot MCP"
4. Select your workspace
5. Set capabilities: Read content, Update content, Insert content
6. Copy the **Internal Integration Token** (starts with `secret_`)

### Step 2: Share TEC Pages with the Integration

For each Notion page you want Copilot to access:

1. Open the page
2. Click **•••** → **Connections** → **Add connection**
3. Select "TEC Copilot MCP"

### Step 3: Authenticate in VS Code

The Notion MCP server uses SSE (Server-Sent Events) and handles auth via browser flow. When you first use `@notion`, it will prompt you to authenticate.

No changes needed in `mcp.json` for Notion — it uses OAuth flow automatically.

---

## Optional MCP Inputs Reference

| Input ID | What It Does | Example Value | Required? |
|----------|--------------|---------------|-----------|
| `memory_file_path` | Local JSON file for persistent memory | `C:\...\TEC\.state\mcp_memory.json` | For `@memory` |
| `azure_tenant_id` | Your Entra tenant | `7d290c31-2df1-4e76-ab86-e26f12753bde` | For `@azure` |
| `azure_client_id` | Service principal app ID | From `az ad app create` | For `@azure` |
| `azure_client_secret` | Service principal password | From `az ad app credential reset` | For `@azure` |
| `azure_subscription_id` | Azure subscription | `89d36e9a-a518-4151-95b3-087ec1b88ec5` | For `@azure` |
| `azure_mcp_collect_telemetry` | Send usage data to Microsoft | `false` (opt-out) or `true` | Optional |
| `azure_mcp_namespace` | Scope to specific Azure MCP features | `bestpractices` or leave blank | Optional |
| `azure_copilot_org` | Legacy field (not used by current servers) | — | Not needed |
| `azure_copilot_token` | Legacy field (not used by current servers) | — | Not needed |

---

## Testing Your MCP Servers

### Test Memory

In Copilot Chat:

```
@memory Remember: TEC Resonance Seal uses Navy #0B1E3B, Violet #6A00F4, Cyan #00D5C4
```

Then later:

```
@memory What are the TEC brand colors?
```

### Test Sequential Thinking

```
@sequentialthinking Plan a 5-step migration for upgrading WorldAnvil integration to include custom metadata fields
```

### Test Azure (after setup)

```
@azure List all Azure OpenAI deployments in my subscription
```

```
@azure Show me this month's costs by service
```

### Test Notion (after setup)

```
@notion Create a new page in TEC Projects database with title "TGCR Phase 2 Roadmap"
```

### Test Character.AI Docs

```
@character How do I create a custom personality with dynamic traits?
```

### Test Hugging Face

```
@huggingface Find the latest Illustrious XL checkpoint
```

---

## Troubleshooting

### "MCP server failed to start"

- Ensure `npx` is available: `npx --version`
- Install Node.js if missing: `winget install OpenJS.NodeJS`

### "Authentication failed" for Azure

- Verify service principal exists: `az ad sp show --id YOUR_CLIENT_ID`
- Check role assignments: `az role assignment list --assignee YOUR_CLIENT_ID`
- Ensure secret hasn't expired: `az ad app credential list --id YOUR_CLIENT_ID`

### "Memory file not found"

- Create the directory first: `New-Item -ItemType Directory -Path ... -Force`
- Use absolute paths (backslashes doubled in JSON: `C:\\Users\\...`)

### Notion connection prompts repeatedly

- Clear VS Code MCP cache: Reload window (Ctrl+Shift+P → "Reload Window")
- Re-share pages with the integration in Notion

---

## Recommended MCP Workflow for TEC

1. **Enable Memory** — Keep context across sessions (Airth research, Arcadia narratives)
2. **Enable Azure** — Monitor costs, query deployments, manage resources
3. **Enable Sequential Thinking** — Plan complex multi-step agent tasks
4. **Enable Notion** — Sync docs, roadmaps, and knowledge base entries
5. **Use Character.AI** — Research personality design for LuminAI refinements
6. **Use Hugging Face** — Find/compare models for Civitai pipelines

---

## Next Steps

- [ ] Create `.state/mcp_memory.json` path
- [ ] Set up Azure service principal and store credentials in `.env.local`
- [ ] Create Notion integration and share TEC workspace
- [ ] Test each MCP server with a simple query
- [ ] Document successful MCP commands in `data/knowledge_map.yml` under `ops.mcp_commands`

---

**Resonance Impact**: Touches **φᵗ** (attention via external context) and **Φᴱ** (potential via expanded tool access).

**Provenance**: Created via TEC Copilot instructions; references official MCP docs and Azure CLI patterns.
