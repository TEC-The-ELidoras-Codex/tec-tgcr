# The Elidoras Codex (TGCR)

**Version:** v1.37+

The Elidoras Codex is a myth-scientific workspace for TGCR (The Grand Codex of Resonance). This monorepo includes agents, applications, documentation, and infrastructure to automate a lab where narrative and science co-evolve.

## 🎭 What is TGCR?

TGCR is an experimental framework that bridges myth, science, and technology. It explores resonance theory through interactive applications, AI agents, and narrative-driven research.

## 📁 Repository Structure

```
tec-tgcr/
├── apps/                           # Applications
│   ├── voice-imprint-studio/       # Voice analysis and imprinting tool
│   ├── resonance-player/           # Music player with resonance gauges
│   └── widgets-sharepoint/         # SharePoint/Teams widgets
├── agents/                         # AI Agents
│   ├── arcadia/                    # Arcadia: Clone & Notebook agent
│   └── airth/                      # Airth: Research guard agent
├── docs/                           # Documentation
│   ├── portfolio/                  # Living résumé and case studies
│   ├── README_codex.md            # Codex overview
│   └── tgcr_manifesto.md          # Project manifesto
├── infra/                          # Infrastructure
│   └── sharepoint/                 # SharePoint deployment configs
├── prompts/                        # Agent prompt templates
└── .github/                        # GitHub workflows and templates
    └── workflows/
        ├── publish-sharepoint.yml
        ├── lint.yml
        └── release-notes.yml
```

## 🤖 Agent Roles

### Arcadia
The **Clone & Notebook** agent. Arcadia helps with documentation, knowledge cloning, and maintaining research notebooks. See [agents/arcadia/instructions/](agents/arcadia/instructions/) for details.

### Airth
The **Research Guard** agent. Airth validates research integrity, guards against hallucinations, and ensures scientific rigor. See [agents/airth/instructions/](agents/airth/instructions/) for details.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ (for apps)
- VS Code with GitHub Copilot (for agent collaboration)
- M365 CLI (for SharePoint deployment)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
   cd tec-tgcr
   ```

2. **Run the Resonance Player:**
   ```bash
   cd apps/resonance-player
   # Open index.html in your browser
   ```

3. **Work with Agents:**
   - Open the repo in VS Code
   - Use GitHub Copilot with agent instructions
   - See `agents/*/instructions/` for agent-specific guidance

### SharePoint Deployment

Deploy widgets to SharePoint using M365 CLI:

```bash
# Login with device code
m365 login --authType deviceCode

# Deploy to SharePoint
npm run deploy:sharepoint
```

See [infra/sharepoint/](infra/sharepoint/) for detailed deployment instructions.

## 📱 Applications

### Resonance Player
Interactive music player with OXY/DOP/ADR gauges that visualize emotional resonance in real-time. Integrates with Spotify.

### Voice Imprint Studio
Tool for analyzing voice patterns and creating resonance profiles.

### SharePoint Widgets
Lightweight widgets for embedding in SharePoint/Teams, including the orb visualization.

## 📚 Documentation

- [README_codex.md](docs/README_codex.md) - Overview of the codex framework
- [tgcr_manifesto.md](docs/tgcr_manifesto.md) - Project vision and principles
- [Portfolio](docs/portfolio/) - Living résumé and case studies

## 🛠️ VS Code Configuration

This repository includes VS Code settings optimized for agent-first development:
- GitHub Copilot integration
- Agent instruction highlighting
- Recommended extensions

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Apps](apps/) - Application code and demos
- [Agents](agents/) - AI agent instructions and configurations
- [Documentation](docs/) - Project documentation
- [Workflows](.github/workflows/) - CI/CD pipelines

---

**Note:** This is an experimental project exploring the intersection of myth, science, and technology. Contributions and feedback are welcome!
