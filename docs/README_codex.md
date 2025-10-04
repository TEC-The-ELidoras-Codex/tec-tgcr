# The Elidoras Codex Documentation

Welcome to The Elidoras Codex - a myth-scientific workspace where narrative and science co-evolve.

## Table of Contents

- [Quick Start](#quick-start)
- [Architecture Overview](#architecture-overview)
- [Agent Roles](#agent-roles)
- [Components](#components)
- [Development Guide](#development-guide)

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Git
- GitHub account with Copilot access (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr
```

2. Install dependencies for apps:
```bash
# Voice Imprint Studio
cd apps/voice-imprint-studio
npm install

# Resonance Player
cd ../resonance-player
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Applications

#### Voice Imprint Studio
```bash
cd apps/voice-imprint-studio
npm start
```

#### Resonance Player
```bash
cd apps/resonance-player
npm start
```

## Architecture Overview

The Elidoras Codex is structured as a modular workspace with clear separation of concerns:

```
tec-tgcr/
├── apps/              # Applications
│   ├── voice-imprint-studio/
│   └── resonance-player/
├── agents/            # AI Agents
│   ├── arcadia/       # Creative/Narrative agent
│   └── airth/         # Technical/Analytical agent
├── docs/              # Documentation
├── infra/             # Infrastructure
│   └── sharepoint/    # SharePoint integration
└── .github/workflows/ # CI/CD pipelines
```

## Agent Roles

### Arcadia - The Creative Intelligence

**Purpose**: Narrative development, creative content, and artistic interpretation

**Capabilities**:
- Story development and mythological synthesis
- Voice imprint narrative interpretation
- Creative content generation
- Portfolio curation

**When to use**: For creative tasks, narrative generation, artistic interpretation, and portfolio development.

See [agents/arcadia/README.md](../agents/arcadia/README.md) for details.

### Airth - The Analytical Intelligence

**Purpose**: Data analysis, technical implementation, and scientific validation

**Capabilities**:
- Audio signal processing and analysis
- Technical feature implementation
- Scientific validation and metrics
- Performance optimization

**When to use**: For technical tasks, data analysis, audio processing, and system optimization.

See [agents/airth/README.md](../agents/airth/README.md) for details.

## Components

### Voice Imprint Studio

A creative workspace for capturing and analyzing voice imprints. Features include:
- Voice recording and capture
- Vocal pattern analysis
- Imprint generation
- SharePoint integration

[Documentation](../apps/voice-imprint-studio/README.md)

### Resonance Player

An immersive audio player for experiencing sonic narratives. Features include:
- High-fidelity playback
- Spatial audio processing
- Spotify integration
- Narrative synchronization

[Documentation](../apps/resonance-player/README.md)

### SharePoint Integration

Integration with Microsoft SharePoint and Teams for collaboration:
- Widget support for SharePoint/Teams
- Document management
- Collaboration features
- Automated publishing

[Documentation](../infra/sharepoint/README.md)

## Development Guide

### Code Standards

- **Clean Code**: Follow clean code principles
- **Copilot Ready**: Structure code for GitHub Copilot
- **Documentation**: Document all public APIs
- **Testing**: Write tests for critical functionality

### GitHub Copilot Tips

This repository is optimized for GitHub Copilot:
- Clear, descriptive names for functions and variables
- Comprehensive inline documentation
- Well-structured modules with single responsibilities
- Consistent coding patterns

### Workflow

1. Create a feature branch
2. Make your changes
3. Run linting: `npm run lint`
4. Test your changes
5. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

## Pipelines

The repository includes automated workflows:
- **Linting**: Code quality checks
- **SharePoint Publishing**: Automated deployment
- **Release Notes**: Automated changelog generation

See [.github/workflows/](../.github/workflows/) for workflow definitions.

## Resources

- [Portfolio](./portfolio/README.md) - Showcase of projects and work
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) - Community standards
- [LICENSE](../LICENSE) - MIT License

## Support

For questions or issues:
1. Check existing documentation
2. Search closed issues
3. Open a new issue with details

---

*The Elidoras Codex - Where myth meets science* 🎵
