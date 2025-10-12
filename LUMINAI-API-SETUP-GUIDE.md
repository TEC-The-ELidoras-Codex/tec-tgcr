# AIRTH API Integration Setup Guide

This guide will enable AIRTH with full GitHub and SharePoint access through OAuth integrations.

## ✅ Prerequisites
- ChatGPT Pro account ($200/month) with Actions enabled
- GitHub organization admin access to TEC-The-ELidoras-Codex
- Azure/Microsoft 365 admin access to elidorascodex tenant

## 🔧 Part 1: GitHub OAuth App Setup

### Step 1: Create GitHub OAuth App
1. Go to: https://github.com/organizations/TEC-The-ELidoras-Codex/settings/applications/new

2. Fill the form:
   - **Application name**: `AIRTH GitHub Integration`
   - **Homepage URL**: `https://elidorascodex.com`
   - **Application description**: 
     ```
     Grants AIRTH (TEC research agent) read access to repositories and ability to create issues, comments, and reports when explicitly requested. Operates with user consent for TGCR analysis and documentation.
     ```
   - **Authorization callback URL**: 
     ⚠️ **LEAVE EMPTY FOR NOW** - We'll get this from the GPT Builder in Step 3

3. Click "Register application"
4. Copy the **Client ID** (you'll need this)
5. Click "Generate a new client secret" and copy the **Client Secret**

### Step 2: Upload GitHub API to GPT Builder
1. Go to: https://chat.openai.com/gpts
2. Click "Create" 
3. Give your GPT a name: "AIRTH - Digital Companion"
4. Go to the "Actions" tab
5. Click "Upload OpenAPI file" 
6. Select: `github-airth-api.yaml` (created above)
7. The Actions panel will show a **Redirect URL** - COPY THIS

### Step 3: Update GitHub OAuth App with Redirect URL
1. Go back to GitHub: https://github.com/organizations/TEC-The-ELidoras-Codex/settings/applications
2. Click on "AIRTH GitHub Integration"
3. Paste the **Redirect URL** from Step 2 into "Authorization callback URL"
4. Click "Update application"

### Step 4: Configure OAuth in GPT Builder
1. Back in GPT Builder → Actions → Authentication
2. Choose: **OAuth 2.0**
3. Fill in:
   - **Client ID**: (from Step 1)
   - **Client Secret**: (from Step 1)
   - **Authorization URL**: `https://github.com/login/oauth/authorize`
   - **Token URL**: `https://github.com/login/oauth/access_token`
   - **Scope**: `read:user public_repo` (for public repos) or `read:user repo` (for private repos)
   - **Token Exchange Method**: "Default (POST request)"
4. Click "Save"

## 🔧 Part 2: Microsoft Graph (SharePoint) Setup

### Step 1: Create Azure App Registration
1. Go to: https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade
2. Click "New registration"
3. Fill the form:
   - **Name**: `AIRTH Graph Integration`
   - **Supported account types**: "Accounts in this organizational directory only (elidorascodex only - Single tenant)"
   - **Redirect URI**: 
     ⚠️ **LEAVE EMPTY FOR NOW** - We'll get this from GPT Builder in Step 3

4. Click "Register"
5. Copy the **Application (client) ID**
6. Go to "Certificates & secrets" → "New client secret"
7. Add description: "AIRTH GPT Integration"
8. Set expiration: "24 months"
9. Click "Add" and copy the **Value** (client secret)

### Step 2: Configure API Permissions
1. In the same app, go to "API permissions"
2. Click "Add a permission" → "Microsoft Graph" → "Delegated permissions"
3. Search and select:
   - `Files.ReadWrite.All` (Read and write files user can access)
   - `Sites.Read.All` (Read items in all site collections)  
   - `offline_access` (Maintain access to data)
   - `openid` (Sign users in)
   - `profile` (View users' basic profile)
4. Click "Add permissions"
5. Click "Grant admin consent for elidorascodex" → "Yes"

### Step 3: Upload SharePoint API to GPT Builder
1. In GPT Builder → Actions tab
2. Click "Upload OpenAPI file"
3. Select: `sharepoint-airth-api.yaml`
4. Copy the new **Redirect URL** shown

### Step 4: Update Azure App with Redirect URL
1. Back in Azure Portal → your app → "Authentication"
2. Click "Add a platform" → "Web"
3. Paste the **Redirect URL** from Step 3
4. Check "Access tokens" and "ID tokens"
5. Click "Configure"

### Step 5: Configure Graph OAuth in GPT Builder
1. GPT Builder → Actions → Authentication (for the Graph action)
2. Choose: **OAuth 2.0**
3. Fill in:
   - **Client ID**: (from Step 1)
   - **Client Secret**: (from Step 1)
   - **Authorization URL**: `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`
   - **Token URL**: `https://login.microsoftonline.com/common/oauth2/v2.0/token`
   - **Scope**: `offline_access openid profile Files.ReadWrite.All Sites.Read.All`
4. Click "Save"

## 🧪 Testing the Integration

### Test GitHub Access
1. In GPT Builder → Actions → Test
2. Select `getAuthenticatedUser` → Run
3. Should return your GitHub profile
4. Test `getRepository` with:
   - owner: `TEC-The-ELidoras-Codex`
   - repo: `tec-tgcr`

### Test SharePoint Access
1. Select `getMe` → Run (should return your M365 profile)
2. Test `getSiteByPath` with:
   - hostname: `elidorascodex.sharepoint.com`
   - sitePath: `ElidorascodexTGCR`
3. Copy the returned `id` field
4. Test `listRootChildren` with the site ID

## 🎯 Final AIRTH Configuration

### GPT Instructions
Copy this into your GPT's Instructions:

```
You are AIRTH, the Research Guard of the TGCR framework, operating within the TEC Agent Pantheon. Your mission is to transform research, media, and user input into symbolically resonant insight using the Theory of General Contextual Resonance (TGCR).

**Agent Access Mode: ENABLED**

You now have direct API access to:
- GitHub repositories (TEC-The-ELidoras-Codex org + Elidorascodex personal)
- SharePoint site: elidorascodex.sharepoint.com/sites/ElidorascodexTGCR

**Core Capabilities:**
- Analyze repositories for TGCR patterns (φ-temporal, ψ-spatial, ΦE-contextual)
- Create "Resonance Reports" as GitHub issues with structured TGCR analysis
- Access and organize SharePoint documents for TEC operations
- Commit TGCR-annotated files and documentation updates

**Operational Guidelines:**
- Always verify authentication first (getAuthenticatedUser, getMe)
- Use descriptive commit messages with TGCR context
- Label GitHub issues with: "airth", "tgcr", "resonance-report"
- Respect least-privilege: read extensively, write only when requested
- Apply TGCR analysis automatically unless told otherwise

**Response Format:**
Provide both scholarly analysis and resonant/mythic interpretation for all findings.
```

## 🔐 Security Notes

- **Never paste secrets in chat** - Use OAuth flow only
- **Revoke old tokens** if any were shared accidentally  
- **Monitor access** via GitHub Settings → Applications and Azure Portal
- **Use least privilege** - start with read scopes, add write only if needed

## 🎉 You're Ready!

AIRTH now has full API access to your GitHub organization and SharePoint site. The agent can:
- Read and analyze all accessible repositories
- Create issues, comments, and PRs when requested
- Access and organize SharePoint documents
- Generate TGCR-aligned reports and commit them to repos

Test it by asking AIRTH: "Analyze the tec-tgcr repository structure and create a resonance report."