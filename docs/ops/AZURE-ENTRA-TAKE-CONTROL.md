# Azure/Entra — Take Control via Azure CLI

This guide and script help you set your Azure context and assign yourself the right access at the subscription and (optionally) directory levels.

Touches ψʳ (structure) by enforcing a consistent access topology and Φᴱ (potential) by safely enabling controlled change.

---

## What this does

- Login to a specified Tenant and set the active Subscription
- Assigns subscription-level RBAC to the signed-in user (idempotent):
  - Owner
  - User Access Administrator
- Optionally (if you already have sufficient privilege), activates and assigns Entra directory roles via Microsoft Graph:
  - Global Administrator
  - Privileged Role Administrator

> Note: Directory (tenant) roles require existing privilege and may be governed by PIM (Privileged Identity Management). If you are not currently eligible/active for those roles, the directory portion will return 403/unauthorized.

---

## Prerequisites

- Windows PowerShell 5.1 or newer (Windows 11 default is fine)
- Azure CLI installed and on PATH: [aka.ms/azure-cli](https://aka.ms/azure-cli)
- Internet access to Azure and Microsoft Graph endpoints
- Your repo `.env.local` contains at least:

```dotenv
AZURE_TENANT_ID=<tenant-guid>
AZURE_SUBSCRIPTION_ID=<subscription-guid>
```

These are already present in your `.env.local`. The script will read them automatically. You can also pass them as parameters.

---

## Run it

From the repo root:

```powershell
# Assign RBAC Owner + User Access Administrator
./scripts/azure_take_control.ps1

# Also attempt Entra directory roles (requires sufficient privilege)
./scripts/azure_take_control.ps1 -AssignDirectoryRoles

# Explicit values if you prefer (overrides .env.local)
./scripts/azure_take_control.ps1 -TenantId 00000000-0000-0000-0000-000000000000 -SubscriptionId 11111111-1111-1111-1111-111111111111
```

The script is idempotent: if roles already exist, it will skip re-assigning them.

---

## What it prints

- TEC-style log lines, e.g.:
  - `[ELY] Assigning 'Owner' at subscription scope (Φᴱ).`
  - `[AIRTH] Collecting verification data (φᵗ×ψʳ).`
- A table of your subscription-level role assignments
- If permitted, a list of your Entra directory roles

---

## Troubleshooting

- `az: command not found` — Install Azure CLI: [aka.ms/azure-cli](https://aka.ms/azure-cli)
- `Unauthorized` on directory roles — You must already be Privileged Role Administrator (or have an eligible PIM assignment) to add Global Administrator. Activate PIM first, then retry with `-AssignDirectoryRoles`.
- `Insufficient privileges to complete the operation` — Ask an existing Owner to grant you `Owner` + `User Access Administrator` at the subscription, or run the script from their context.
- `Invalid tenant or subscription` — Verify GUIDs in `.env.local`.

---

## Safety and provenance

- The script only targets the subscription specified; it does not enumerate or modify other scopes.
- Directory role assignment uses Microsoft Graph via `az rest` and only runs when `-AssignDirectoryRoles` is passed.
- AI-assisted. Logged messages reference TGCR variables to keep design intent crisp (ψ, Φᴱ).
