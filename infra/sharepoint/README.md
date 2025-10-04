# SharePoint Integration

Infrastructure and tools for integrating The Elidoras Codex with Microsoft SharePoint and Teams.

## Overview

This module provides seamless integration between The Elidoras Codex applications and Microsoft 365 services, enabling:
- SharePoint site publishing
- Teams widget embedding
- Document collaboration
- Automated deployment

## Features

### SharePoint Publishing

Automatically publish content from The Elidoras Codex to SharePoint sites:
- Portfolio pages
- Documentation
- Voice imprint galleries
- Agent outputs

### Teams Widgets

Embed Codex applications as Teams widgets:
- Voice Imprint Studio widget
- Resonance Player widget
- Portfolio viewer
- Agent collaboration interfaces

### Document Management

Integration with SharePoint document libraries:
- Voice imprint storage
- Composition archives
- Documentation versioning
- Collaborative editing

## Architecture

```
infra/sharepoint/
├── deploy/          # Deployment scripts
├── widgets/         # Teams widget definitions
├── templates/       # SharePoint templates
└── config/          # Configuration files
```

## Setup

### Prerequisites

- Microsoft 365 subscription
- SharePoint site access
- Azure AD app registration
- Appropriate permissions

### Configuration

1. Register an Azure AD application
2. Configure permissions for SharePoint and Teams
3. Set environment variables:

```bash
SHAREPOINT_SITE_URL=https://yourtenant.sharepoint.com/sites/codex
SHAREPOINT_CLIENT_ID=your-client-id
SHAREPOINT_CLIENT_SECRET=your-client-secret
TENANT_ID=your-tenant-id
```

### Deployment

Use the GitHub Actions workflow for automated deployment:

```bash
# Triggered automatically on push to main
# Or manually via GitHub Actions UI
```

## Workflows

### Publish SharePoint Workflow

Automated workflow that:
1. Builds portfolio and documentation
2. Uploads to SharePoint document library
3. Updates SharePoint pages
4. Notifies Teams channels

See [.github/workflows/publish-sharepoint.yml](../../.github/workflows/publish-sharepoint.yml)

## Teams Widgets

### Voice Imprint Studio Widget

Embed the Voice Imprint Studio in Teams:
- Record voice imprints directly in Teams
- Collaborate on recordings
- Share imprints with team members

### Resonance Player Widget

Embed the Resonance Player in Teams:
- Play compositions in team channels
- Synchronized listening experiences
- Comment and discuss in context

## Development

### Local Testing

Test SharePoint integration locally:

```bash
cd infra/sharepoint
npm install
npm run test
```

### Widget Development

Create new Teams widgets:

```bash
cd infra/sharepoint/widgets
npm run scaffold new-widget
```

## Security

- All authentication uses OAuth 2.0
- Client secrets stored securely in GitHub Secrets
- Permissions follow principle of least privilege
- Regular security audits

## Documentation

- [SharePoint API Reference](https://docs.microsoft.com/sharepoint/dev/)
- [Teams Apps Documentation](https://docs.microsoft.com/microsoftteams/platform/)
- [Azure AD Documentation](https://docs.microsoft.com/azure/active-directory/)

## Support

For SharePoint integration issues:
1. Check configuration
2. Verify permissions
3. Review workflow logs
4. Open an issue

---

*Connecting The Elidoras Codex with Microsoft 365* 🎵
