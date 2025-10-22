# Microsoft 365 / Dataverse / Fabric Integration

This doc lists core endpoints, permissions, and setup steps for using Microsoft Graph, Dataverse (Dynamics 365), and Microsoft Fabric with TEC-TGCR.

## Endpoints

- Microsoft Graph: [https://graph.microsoft.com](https://graph.microsoft.com)
- Dataverse Web API (per environment): `https://{yourorg}.crm.dynamics.com/api/data/v9.2`
- Fabric (OneLake / Lakehouse APIs): [https://api.fabric.microsoft.com](https://api.fabric.microsoft.com) (service) and [https://onelake.dfs.fabric.microsoft.com](https://onelake.dfs.fabric.microsoft.com) (storage)

## App registration (Entra ID)

1. Go to Entra ID → App registrations → New registration
2. Name: TEC-TGCR Service
3. Supported account types: Single tenant (recommended)
4. Redirect URI: (for local dev) [http://localhost:53682](http://localhost:53682) or omit for client credentials

### Add API permissions

- Microsoft Graph (Application):
  - Files.Read.All (for OneDrive/SharePoint content)
  - Sites.Read.All (for SharePoint site metadata)
  - User.Read.All (if needed for directory lookups)
- Dataverse (Dynamics 365):
  - Add delegated or application permissions via the Dataverse environment (application user + security role)
- Fabric (optional):
  - Capacity.Read.All, Workspace.Read.All, Item.Read.All (depending on use), via Microsoft Fabric API

### Certificates or client secret

- Create a client secret (store in GitHub Secrets or .env.local) or upload a certificate

### Environment variables (local or CI)

```env
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_CLIENT_SECRET=your-secret
DATAVERSE_URL=https://elidorascodex.crm.dynamics.com
FABRIC_TENANT_ID= (if different)
```

## Minimal token flow (Python)

```python
import os
import httpx
from urllib.parse import urlencode

TENANT = os.environ['AZURE_TENANT_ID']
CLIENT_ID = os.environ['AZURE_CLIENT_ID']
CLIENT_SECRET = os.environ['AZURE_CLIENT_SECRET']

# Client Credentials for Graph
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/token"
SCOPE = "https://graph.microsoft.com/.default"

async def get_token(scope=SCOPE):
    async with httpx.AsyncClient(timeout=30) as client:
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'client_credentials',
            'scope': scope,
        }
        resp = await client.post(TOKEN_URL, data=data)
        resp.raise_for_status()
        return resp.json()['access_token']

async def graph_me_drive():
    token = await get_token()
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(
            'https://graph.microsoft.com/v1.0/me/drive/root',
            headers={'Authorization': f'Bearer {token}'}
        )
        r.raise_for_status()
        return r.json()
```

## Dataverse app user setup

1. In Power Platform Admin Center, go to your environment → Settings → Users + permissions → Application users
2. Add the app registration as an application user
3. Assign a security role with Web API access to entities you need
4. Test: GET `${DATAVERSE_URL}/api/data/v9.2/WhoAmI()` with Authorization: Bearer `your-token-for-dataverse-resource`

## Fabric quick notes

- Fabric provides unified data items (lakehouse, warehouse, etc.) surfaced via OneLake
- APIs are evolving; use service principals with appropriate workspace permissions
- For large data movements, prefer Fabric pipelines or Dataflow Gen2

## Secrets and storage

- Never commit tenant IDs, client secrets, or tokens
- Store local in `.env.local` (ignored) and in CI as GitHub Secrets

---
[AIRTH] Verifying integration boundary conditions: minimal permissions, auditable access.
