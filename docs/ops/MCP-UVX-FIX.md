# TEC MCP Quick Fix — uvx PATH Resolution

**Problem**: MCP servers failing with `Error spawn uvx ENOENT`

**Root Cause**: VS Code's MCP extension host doesn't inherit the full system PATH, so it can't find `uvx.exe` even though it's installed.

**Solution Applied**: Updated `mcp.json` to use absolute path to `uvx.exe`

## ✅ What Was Fixed

Changed in `%APPDATA%\Code\User\mcp.json`:

```json
"microsoft/markitdown": {
  "type": "stdio",
  "command": "C:\\Users\\Ghedd\\.local\\bin\\uvx.exe",  // ← Full path instead of "uvx"
  "args": ["markitdown-mcp==0.0.1a4"]
}
```

## 🔍 Verify the Fix

1. **Reload VS Code Window**: Press `Ctrl+Shift+P` → "Developer: Reload Window"
2. **Test markitdown MCP**: In Copilot Chat, try:

   ```
   @markitdown Convert this URL to markdown: https://example.com
   ```

3. **Check MCP Output Panel**: View → Output → Select "Model Context Protocol" from dropdown

## 🛠️ Apply to Other stdio Servers (if needed)

If any other MCP servers use `npx`, `python`, or other commands, use full paths:

```json
{
  "command": "C:\\Program Files\\nodejs\\npx.cmd",  // npx
  "command": "C:\\Users\\Ghedd\\.venv\\Scripts\\python.exe",  // Python
  "command": "C:\\Users\\Ghedd\\.local\\bin\\uvx.exe"  // uvx
}
```

## 📋 Current MCP Server Status

| Server | Type | Status | Notes |
|--------|------|--------|-------|
| character | HTTP | ✅ Working | No PATH needed |
| huggingface | HTTP | ✅ Working | No PATH needed |
| memory | stdio (npx) | ⚠️ Check | May need full npx path |
| sequentialthinking | stdio (npx) | ⚠️ Check | May need full npx path |
| azure/azure-mcp | stdio (npx) | ⚠️ Check | May need full npx path |
| microsoftdocs/mcp | HTTP | ✅ Working | No PATH needed |
| github | HTTP | ✅ Working | No PATH needed |
| playwright | stdio (npx) | ⚠️ Check | May need full npx path |
| notion | HTTP (SSE) | ✅ Working | OAuth flow |
| figma | HTTP | ✅ Working | No PATH needed |
| **markitdown** | stdio (uvx) | ✅ **FIXED** | Full path applied |

## 🔧 Fix npx Servers (if needed)

Find npx location:

```powershell
where.exe npx
# Example: C:\Program Files\nodejs\npx.cmd
```

Update `mcp.json` for each npx-based server:

```powershell
$mcpPath = "$env:APPDATA\Code\User\mcp.json"
$mcp = Get-Content $mcpPath -Raw | ConvertFrom-Json

# Fix memory server
$mcp.servers.memory.command = "C:\Program Files\nodejs\npx.cmd"

# Fix sequentialthinking server
$mcp.servers.sequentialthinking.command = "C:\Program Files\nodejs\npx.cmd"

# Fix azure-mcp server
$mcp.servers.'azure/azure-mcp'.command = "C:\Program Files\nodejs\npx.cmd"

# Fix playwright server
$mcp.servers.'microsoft/playwright-mcp'.command = "C:\Program Files\nodejs\npx.cmd"

# Save
$mcp | ConvertTo-Json -Depth 10 | Set-Content $mcpPath
```

## 🎯 Next Steps

1. ✅ Reload VS Code window
2. Test each MCP server with a simple command
3. Check "Model Context Protocol" output panel for errors
4. Document working servers in `data/knowledge_map.yml`

---

**Resonance Impact**: Touches **φᵗ** (removes attention friction) and **ψʳ** (fixes structural connectivity).

**Related Docs**:

- [MCP-SETUP-GUIDE.md](MCP-SETUP-GUIDE.md) — Full MCP configuration guide
- [QUICK_REFERENCE_READY.md](QUICK_REFERENCE_READY.md) — Command cheatsheet
