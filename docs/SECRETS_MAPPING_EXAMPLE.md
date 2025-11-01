# Secrets mapping example

This file contains a tracked, safe example of the mapping used by the repository's secrets helper scripts.
It is intentionally non-sensitive and intended for collaborators to copy into their local ignored store at `secrets-local/bw/mapping.json`.

Usage:

- Copy the JSON below into `secrets-local/bw/mapping.json` on your machine.
- Keep real secrets in `secrets-local/bw/` — that folder is ignored by Git and will not be committed.
- The repository also includes `secrets/mapping.example.json` for quick reference.

Example mapping (placeholder values):

```json
{
  "OPENAI_API_KEY": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "OPENAI_ORG_ID": "REPLACE_WITH_ITEM_NAME_OR_CONFIG_VALUE",
  "PROJECTS_TOKEN": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "PROJECT_ID": "REPLACE_WITH_PROJECT_CLASSIC_ID_OR_LEAVE_BLANK",
  "PROJECT_NUMBER": "REPLACE_WITH_PROJECTV2_NUMBER",
  "TEC_WPCOM_API_PASS": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "WPCOM_SSH_SECRET_KEY": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "WORLDANVIL_API_KEY": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "CIVITAI_API_KEY": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "SPOTIFY_CLIENT_SECRET": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "GITLAB_PAT": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "TEC_OLLAMA_API_KEY": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "TEC_RUNWAY_API_KEY": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID",
  "NOTION_TOKEN": "REPLACE_WITH_BITWARDEN_ITEM_NAME_OR_SECRET_ID"
}
```

Security note: Never commit secrets. Keep them in `secrets-local/bw/` (ignored) or in your organization secret manager.
