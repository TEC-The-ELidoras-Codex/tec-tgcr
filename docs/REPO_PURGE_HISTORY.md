# Purging Secrets from Git History (TEC-TGCR)

This guide removes accidentally committed secrets (e.g., `.env`, SSH keys) from the entire repository history. Do this only after rotating all affected credentials.

## 0) Rotate credentials FIRST

Rotate and update in `.env.local`/GitHub Secrets:

- OpenAI, Anthropic, Civitai, WorldAnvil
- Spotify Client ID/Secret
- CoinDesk, CoinMarketCap (if used)
- WordPress.com App Password
- SSH private key (generate a new one)

## 1) Remove sensitive files from the working tree

- Delete the files locally (e.g., `.env`, any `*.key`, `*.pem`). Commit the removal before rewriting history.
  - Root `.gitignore` already ignores `.env*`, secrets, keys, and export artifacts to prevent repeat incidents.

## 2) Choose a rewriter

You can use either BFG Repo-Cleaner (fast) or `git filter-repo` (flexible, official).

### Option A — BFG Repo-Cleaner

1. Clone mirror

```powershell
git clone --mirror https://github.com/Elidorascodex/tec-tgcr.git tec-tgcr.git
cd tec-tgcr.git
```

1. Delete files by name/pattern

```powershell
java -jar ..\bfg.jar --delete-files ".env" --delete-files "*.pem" --delete-files "*.key"
```

1. Replace literal secrets (edit `..\secrets.txt`; one old token per line)

```powershell
# secrets.txt content example (do not commit this file)
sk-proj-OLDOPENAI...
-----BEGIN OPENSSH PRIVATE KEY-----
```

```powershell
java -jar ..\bfg.jar --replace-text ..\secrets.txt
```

1. Cleanup and force push

```powershell
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

### Option B — git filter-repo

1. Fresh clone to rewrite

```powershell
git clone --no-local https://github.com/Elidorascodex/tec-tgcr.git tec-tgcr-clean
cd tec-tgcr-clean
```

1. Remove files historically

```powershell
git filter-repo --path .env --invert-paths
git filter-repo --path-glob "*.pem" --invert-paths
git filter-repo --path-glob "*.key" --invert-paths
```

1. Replace secret patterns (repeat per token)

```powershell
# file: replace.txt
sk-proj-[A-Za-z0-9_\-]+==>***REDACTED***
```

```powershell
git filter-repo --replace-text replace.txt
```

1. Force push

```powershell
git push --force
```

## 3) Notify collaborators

Ask everyone to hard reset onto the rewritten history:

```powershell
git fetch --all
git reset --hard origin/main
```

## 4) Validate

- Check GitHub code search for prior tokens.
- Ensure CI still passes.
- Run: `python -m tec_tgcr.scripts.env_check`.

## Notes

- Secrets remain in clones until collaborators reset.
- Prefer `WPCOM_SSH_PRIVATE_KEY_PATH` over inline key content.
- `.env.example` is the only env template to keep in git.
