---
layout: default
title: API Key Setup
---

# ChatGPT GPT Actions Setup (API Key)

[Quick reference from config/GPT_ACTIONS_API_KEY_SETUP.md]

## Step 1: Get API Key

### GitHub Personal Access Token
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Name: `CODEX-ChatGPT-Actions`
4. Scopes: `repo`, `read:org`
5. Copy token (you'll only see it once!)

## Step 2: Configure ChatGPT GPT Builder

1. Go to [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor)
2. Create new GPT
3. Click "Configure" → "Actions"
4. Click "+ Create new action"

### Schema Import
- **Source**: "Import from URL"
- **URL**: `https://raw.githubusercontent.com/TEC-The-ELidoras-Codex/tec-tgcr/main/config/gpt-actions-research.json`

### Authentication
- **Type**: API Key
- **Header**: `Authorization`
- **Value**: `Bearer YOUR_GITHUB_TOKEN`

Example:
```
Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Step 3: Test Actions

Try in ChatGPT:
```
"Use listCards to show all CODEX cards"
```

## Step 4: Add System Prompt

Copy from repo: `config/CODEX_INSTRUCTIONS_COMPACT.txt`

## Troubleshooting

| Error | Solution |
|-------|----------|
| Invalid API Key | Verify token starts with `ghp_`, check Bearer format |
| Card not found | Use lowercase slugs: `codex_chronosphere` |
| 404 error | Confirm GitHub token has `repo` scope |

[Full guide →](../config/GPT_ACTIONS_API_KEY_SETUP.md)
