# VS Code Settings Guide — Secure & Organized

> Keep your project settings synchronized across Windows, Linux, and CI environments.

## Three Layers of Settings

### 1. **Project Settings** (`.vscode/settings.json`)
**This is where team-wide, reproducible settings live.** Committed to git.

✓ Python interpreter path  
✓ Testing configuration  
✓ Formatting rules (Prettier, Markdown, YAML)  
✓ File exclusions (build artifacts, cache, `.venv`)  
✓ Git behavior  
✓ Debugging settings  

**Why:** All team members get the same setup. CI/CD also uses these.

**Location:** `/home/tec_tgcr/tec-tgcr/.vscode/settings.json`

---

### 2. **User Settings** (VS Code User Settings)
**This is for YOUR machine only.** Not committed.

- Theme preferences
- Font/editor appearance
- Extensions you personally use
- Keyboard shortcuts
- Shell preferences (PowerShell vs bash)
- GitHub Copilot settings

**Why:** Personal preferences shouldn't impose on teammates.

**Location:** 
- **Windows:** `C:\Users\Ghedd\AppData\Roaming\Code\User\settings.json`
- **Linux/Mac:** `~/.config/Code/User/settings.json`

**Current Issue:** Your user settings had PHP paths and personal extensions mixed with project config. We've moved the project stuff to `.vscode/settings.json`.

---

### 3. **Environment Variables** (`.env.local`, `.secrets.env`)
**This is for secrets and machine-specific values.** Never committed.

✓ API keys  
✓ Database URLs  
✓ Authentication tokens  
✓ Local paths that differ per machine  

**Why:** Secrets stay out of git. Different machines have different paths.

**Files:**
- `.env.example` — Template showing what vars are needed
- `.env.local` — Your actual values (gitignored)
- `.secrets.env` — Additional secrets (also gitignored)

---

## Setup Checklist

### ✓ Done
- Fixed `.vscode/settings.json` to use project-level config
- Configured `.venv` interpreter auto-detection
- Set up test discovery with pytest
- Excluded build artifacts from search

### ✓ Next Steps

**1. Clean Up Your User Settings**

Your user settings now contain too much project-specific stuff. Keep only:
- Theme (`workbench.colorTheme`)
- Font / editor appearance
- Personal extensions
- Keyboard shortcuts
- GitHub Copilot preferences

**2. Use `.env.local` for Local Overrides**

If you need machine-specific values, put them in `.env.local`:
```bash
# .env.local (never committed)
PYTHON_PATH=/custom/path/to/python
WORKSPACE_ROOT=/home/tec_tgcr/tec-tgcr
```

**3. Pull Project Settings Automatically**

When you open the workspace, VS Code will:
1. Load your **user settings**
2. Override with **project settings** from `.vscode/settings.json`
3. Read **environment variables** from `.env` files

---

## Cross-Platform Compatibility

### Python Interpreter
```jsonc
// ✓ Works on Windows & Linux
"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
```

Not:
```jsonc
// ✗ Windows-only
"python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe"
```

The `.venv/bin/python` path is universal; VS Code translates it on Windows.

---

## CI/CD and Secrets

**GitHub Actions & other CI:**
- Reads `.vscode/settings.json` ✓
- Does NOT read `.env.local` ✓
- Uses repository secrets (via GitHub Settings) ✓

**Your Local Machine:**
- Reads `.vscode/settings.json` ✓
- Reads `.env.local` ✓
- Reads user settings ✓

---

## Workflow

### When You Change Project Settings

```bash
# 1. Edit .vscode/settings.json
# 2. Test locally
# 3. Commit & push
git add .vscode/settings.json
git commit -m "project: update python test discovery"
git push

# All teammates get the update automatically.
```

### When You Need Local Overrides

```bash
# Edit .env.local (already gitignored)
# Don't commit it!
echo "MY_LOCAL_VAR=value" >> .env.local

# Verify it's not staged:
git status  # should NOT show .env.local
```

### When You Need Secrets

Use GitHub Secrets or `.secrets.env`:
```bash
# .secrets.env (gitignored, local only)
API_KEY=your-secret-key
DB_PASSWORD=your-password

# Load it in scripts/CI:
source .secrets.env
echo $API_KEY
```

---

## Troubleshooting

### "Settings Keep Getting Mixed Up"

→ Separate by layer:
- **Team/project logic** → `.vscode/settings.json`
- **Your personal preferences** → User settings
- **Secrets & local paths** → `.env.local`

### "Python Interpreter Won't Update"

→ Restart VS Code: `Ctrl+Shift+P` → "Developer: Reload Window"

Or reload Python extension:
```
Ctrl+Shift+P → Python: Select Interpreter
Choose ./.venv/bin/python
```

### "CI Tests Fail But Local Tests Pass"

→ Check `.vscode/settings.json` is committed:
```bash
git log --oneline -- .vscode/settings.json
```

If it's not in git, CI won't see it. Add it:
```bash
git add .vscode/settings.json
git commit -m "chore: add vscode project settings"
```

---

## Summary

| Layer | File | Committed? | Use For |
|-------|------|-----------|---------|
| **Project** | `.vscode/settings.json` | ✓ Yes | Team config, testing, formatting |
| **User** | `~/.config/Code/User/settings.json` | ✗ No | Personal theme, font, extensions |
| **Local Override** | `.env.local` | ✗ No | Local paths, development values |
| **Secrets** | `.secrets.env` | ✗ No | API keys, passwords, tokens |

Your settings are now **secure, organized, and consistent**. 🎯
