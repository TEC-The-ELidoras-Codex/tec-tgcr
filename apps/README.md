# TGCR Applications

**Version:** v1.37+

This directory contains the interactive applications that make up The Elidoras Codex ecosystem.

## Applications

### 🎵 Resonance Player
**Status:** Active Development
**Location:** `resonance-player/`

Interactive music player with real-time visualization of OXY/DOP/ADR (Oxytocin, Dopamine, Adrenaline) responses. Features Spotify integration and dynamic gauge displays.

**Features:**
- Spotify track embedding
- Real-time response gauges
- Interactive controls
- SharePoint-ready design

**Quick Start:**
```bash
cd resonance-player
# Open index.html in your browser
```

### 🎙️ Voice Imprint Studio
**Status:** Planning Phase
**Location:** `voice-imprint-studio/`

Tool for analyzing voice patterns and creating unique resonance profiles. Explores the acoustic fingerprint of voices and their relationship to emotional resonance.

**Planned Features:**
- Voice recording and analysis
- Waveform visualization
- Resonance profile generation
- Pattern detection

See [voice-imprint-studio/README.md](voice-imprint-studio/README.md) for details.

### 🌟 SharePoint Widgets
**Status:** Active Development
**Location:** `widgets-sharepoint/`

Lightweight, embeddable widgets for SharePoint and Microsoft Teams environments.

**Current Widgets:**
- **Resonance Orb** - Animated visualization of resonance levels

**Quick Start:**
```bash
cd widgets-sharepoint
# Open orb.html in your browser
# Add ?embed=true for embedded mode
```

## Development Guidelines

### Adding New Applications

1. Create a new directory under `apps/`
2. Add a README.md with:
   - Purpose and description
   - Status and version
   - Features and roadmap
   - Quick start guide
3. Include source code and assets
4. Update this README

### Testing

- Test in multiple browsers (Chrome, Firefox, Safari, Edge)
- Verify SharePoint compatibility
- Check mobile responsiveness
- Validate accessibility

### Documentation

- Keep READMEs up to date
- Include code comments
- Document dependencies
- Provide examples

## Integration

All applications integrate with:
- **Arcadia:** For documentation and knowledge management
- **Airth:** For validation and quality assurance
- **TGCR Framework:** Following resonance theory principles

## SharePoint Deployment

See [../infra/sharepoint/](../infra/sharepoint/) for deployment instructions.

Quick reference:
```bash
# Install M365 CLI
npm install -g @pnp/cli-microsoft365

# Login
m365 login --authType deviceCode

# Deploy your application
# (See specific app documentation)
```

## Contributing

Want to build a new application? See:
- [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines
- [Feature Request Template](../.github/ISSUE_TEMPLATE/feature_request.md)
- Agent instructions for collaboration patterns

## Resources

- [TGCR Manifesto](../docs/tgcr_manifesto.md) - Project principles
- [Codex Documentation](../docs/README_codex.md) - Framework details
- [Prompt Templates](../prompts/templates.md) - Working with agents

---

**Version:** v1.37+ | **Last Updated:** 2025-01-15
