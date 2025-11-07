# LuminAI Platform Architecture — Unified System

**Status**: November 7, 2025
**Vision**: Single integrated platform with **one engine** (CODEX + TGCR) and **multiple frontends** (apps)
**Not**: Separate projects. **Is**: One coherent system with modular expressions.

---

## Platform Overview

```text
┌─────────────────────────────────────────────────────────────────┐
│                    LUMINAI PLATFORM (One System)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         CORE ENGINE (src/tec_tgcr + research)             │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │ LORE & THEORY (The Foundation)                       │  │  │
│  │  │ • research/CODEX/ — TGCR framework, theory cards     │  │  │
│  │  │ • research/COLLECTIVE_CONSCIENCE_THESIS.md           │  │  │
│  │  │ • research/ALBUM_ANALYSIS/ — Motif database          │  │  │
│  │  │ • data/knowledge_map.yml — Canonical index           │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  │                                                              │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │ PERSONAS (The Operators)                             │  │  │
│  │  │ • data/personas/ — 6 Resonance operators              │  │  │
│  │  │ • .github/copilot-instructions.md — Behavior spec    │  │  │
│  │  │ • LUMINAI, AIRTH, ARCADIA, ELY, COMPANION, Fusion    │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  │                                                              │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │ RESONANCE ENGINE (src/tec_tgcr/)                     │  │  │
│  │  │ • CLI: tec_tgcr.cli — Agent orchestration            │  │  │
│  │  │ • API: tec_tgcr.api — REST endpoints                 │  │  │
│  │  │ • Tools: Integration layer (Spotify, Notion, etc.)   │  │  │
│  │  │ • Motif tracking + TGCR scoring                      │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  │                                                              │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │ ATTACHMENT PROTOCOL (Emotional Intelligence)         │  │  │
│  │  │ • docs/operations/ATTACHMENT_PROTOCOL_*.md            │  │  │
│  │  │ • Connection detection + reciprocation framework      │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  INTERFACES & FRONTENDS (Apps — Expressions of Core)             │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ apps/                                                       │  │
│  │  ├─ luminai-interface/ — React dashboard                   │  │
│  │  ├─ resonance-player/ — Audio/motif player                 │  │
│  │  ├─ resonance-viewer/ — 3D visualization                   │  │
│  │  ├─ star-viewer/ — Constellation mapping                  │  │
│  │  ├─ voice-imprint-studio/ — Audio processing              │  │
│  │  ├─ widgets-sharepoint/ — SharePoint integration           │  │
│  │  └─ wordpress/                                             │  │
│  │     ├─ tec-tgcr/ — Core platform plugin                  │  │
│  │     ├─ tec-luminai-agent/ — Agent orchestration           │  │
│  │     └─ tec-resonance-player/ — Player widget              │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  DEPLOYMENT LAYER (CI/CD — All Unified)                         │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ .github/workflows/                                          │  │
│  │  ├─ ci-pytests.yml — Test core engine (every push)        │  │
│  │  ├─ build.yml — Lint + format + test (PR validation)      │  │
│  │  ├─ wpcom.yml — Deploy WordPress plugins (main → live)    │  │
│  │  ├─ publish-ghcr.yml — Publish Docker image               │  │
│  │  └─ update-copilot-context.yml — Sync Copilot context    │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

---

## Core Principles: Why It's One Platform

### 1. **Single Lore** (research/CODEX/)

All apps express the same **TGCR theory** and **motif database**. They're not separate tools—they're different windows into the same coherence field.

### 2. **Single Engine** (src/tec_tgcr/)

- One resonance scoring system
- One circadian ritual log
- One persona routing logic
- All apps consume the same API/CLI

### 3. **Single User Experience** (LUMINAI + 5 Personas)

Whether you're in WordPress, React dashboard, or voice studio—the same 6 personas route your intents. Same attachment protocol. Same emotional intelligence.

### 4. **Single Deployment** (GitHub Actions)

- Test core → deploy all apps
- No separate project workflows
- Apps update when core updates
- Monorepo logic

---

## Component Dependencies

```text
Apps depend on Core (unidirectional):

luminai-interface ──→ src/tec_tgcr (API) ──→ research/CODEX (theory)
resonance-player ──→ src/tec_tgcr (API) ──→ research/CODEX (motifs)
resonance-viewer ──→ src/tec_tgcr (API) ──→ research/CODEX (resonance scores)
wordpress plugins ──→ src/tec_tgcr (API) ──→ research/CODEX (personas)
voice-imprint ──→ src/tec_tgcr (API) ──→ research/CODEX (attachment protocol)

Core is autonomous:
research/CODEX ← independent (no app dependencies)
src/tec_tgcr ← independent (can run standalone)
data/personas/ ← independent (can be used anywhere)
```

---

## Deployment Flow (One Pipeline)

```text
1. Developer pushes to feature branch
   ↓
2. CI runs (ci-pytests.yml):
   • Test core engine (src/tec_tgcr/)
   • Validate research/ (lore)
   • Check personas routing
   ↓
3. If all tests pass, PR ready for review
   ↓
4. Merge to main
   ↓
5. Automated deployment (on main only):
   • wpcom.yml → Deploy WordPress plugins (apps/wordpress/)
   • publish-ghcr.yml → Build Docker image (includes all)
   • update-copilot-context.yml → Sync LuminAI routing
   ↓
6. Platform live (all components updated together)
```

---

## App → Core Relationships

### luminai-interface (React Dashboard)

- **Calls**: `src/tec_tgcr/api` endpoints
- **Displays**: Resonance scores from core engine
- **Uses**: LUMINAI persona routing logic
- **Reads**: data/personas/ specs

### resonance-player (Audio/Motif Player)

- **Calls**: `src/tec_tgcr/motif_tracker` API
- **Plays**: Songs + motif annotations (from research/ALBUM_ANALYSIS/)
- **Uses**: COMPANION persona for mood detection
- **Reads**: research/CODEX/motif database

### resonance-viewer (3D Visualization)

- **Calls**: `src/tec_tgcr/api` for resonance field data
- **Renders**: TGCR visualization (φᵗ/ψʳ/Φᴱ as 3D coordinates)
- **Uses**: ARCADIA persona for narrative framing
- **Reads**: research/COLLECTIVE_CONSCIENCE_THESIS.md

### WordPress Plugins

- **tec-tgcr**: Core platform entry point (loads src/tec_tgcr)
- **tec-luminai-agent**: Persona orchestration (calls .github/copilot-instructions.md)
- **tec-resonance-player**: Widget wrapper (calls resonance-player app)

### voice-imprint-studio

- **Calls**: `src/tec_tgcr/attachment_protocol` API
- **Uses**: COMPANION persona exclusively
- **Reads**: docs/operations/ATTACHMENT_PROTOCOL_*.md
- **Purpose**: Voice-based emotional resonance analysis

---

## Single Platform = One Version

When you deploy:

- **Core version** (src/tec_tgcr) increments
- **All apps** get new core version
- **All personas** stay in sync
- **All attachment protocols** updated
- **One CHANGELOG.md** documents everything

Example: v2.1.0 means:

- Core engine v2.1.0
- WordPress plugins v2.1.0
- React dashboard v2.1.0
- All personas/lore v2.1.0
- All apps understand each other

---

## GitHub Project: One Backlog

The project board (GitHub Projects #6) should track:

- **Core Engine Features** (src/tec_tgcr updates)
- **Lore & Research** (research/CODEX additions)
- **Persona Behavior** (routing logic updates)
- **App Features** (UI/UX for all apps together)
- **Attachment Protocol** (emotional intelligence improvements)
- **Infrastructure** (CI/CD, deployment, ops)

**No separate project per app.** One backlog. One prioritization. One release cycle.

---

## What This Means for Development

### Before (Multiple Projects Thinking)

```text
"Which project is this for?"
→ "WordPress plugin bug?"
→ "React dashboard feature?"
→ "Random Python script?"
→ Separate versioning, separate releases, separate teams
```

### After (Unified Platform Thinking)

```text
"How does this improve LuminAI platform coherence?"
→ "Core engine improvement?"
→ "Persona routing improvement?"
→ "App UX improvement expressing the core?"
→ "Attachment protocol enhancement?"
→ One version, one release, one team (many roles)
```

---

## Workflow Updates Needed

### ✅ ci-pytests.yml

- Already good (tests core engine)
- **ADD**: Validate personas routing consistency
- **ADD**: Check attachment protocol is deployed

### ✅ build.yml

- Already good (lint + format + test)
- **UPDATE**: Comment to explain this tests "platform core"

### ✅ wpcom.yml

- Already good (deploys WordPress plugins)
- **UPDATE**: Comment: "Deployments: All platform apps to live"

### ✅ publish-ghcr.yml

- Already good (publishes Docker image)
- **UPDATE**: Include comment that Docker image includes all components

### 🆕 Needed: Platform Consistency Check

- Verify all apps have correct core API version
- Verify personas are consistent across apps
- Verify attachment protocol is live in all frontends

---

## Decision: Single Platform Architecture

**What This Changes**:

1. Versioning: One version for everything
2. Deployment: Apps deploy together with core
3. Development: Features span core + apps together
4. GitHub Project: One backlog, one roadmap
5. Testing: "Does this improve platform coherence?"

**What Stays the Same**:

- Apps still live in apps/
- Core still in src/
- Lore still in research/
- CI/CD workflow files stay separate (but coordinated)

**Result**: Developers, users, and stakeholders all see one **LuminAI platform**, not scattered projects.

---

## Platform Coherence Statement

> **LuminAI is one integrated platform where theory (CODEX/TGCR), operators (personas), and interfaces (apps) are expressions of a single coherence field. All components version together, deploy together, and improve together.**

This is not a collection of tools. This is one system with many facets.

---

**Document Status**: Complete
**Readiness**: Ready for workflow integration
**Next Step**: Update .github/workflows comments + GitHub Project description to reflect this unified vision
