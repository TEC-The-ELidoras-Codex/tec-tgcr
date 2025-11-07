# Platform Unification — Complete Documentation

**Status**: November 7, 2025

**Completion**: ✅ All architectural documentation and workflow clarifications complete

**Vision Captured**: LuminAI is ONE integrated platform, not separate projects

---

## What Was Created

### 1. `.github/PLATFORM_ARCHITECTURE.md` ✅

**Purpose**: Defines the unified platform architecture

**Contains**:

- Visual ASCII architecture diagram (engine + apps model)
- Component dependencies (apps → core unidirectional)
- Deployment flow (core test → all apps deploy)
- App-to-core relationships (which personas/APIs each uses)
- Unified versioning strategy (v2.1.0 applies to all)
- Development mindset shift (before/after thinking)
- Workflow updates needed

**Key Insight**:

> "LuminAI is one integrated platform where theory (CODEX/TGCR), operators (personas), and interfaces (apps) are expressions of a single coherence field."

---

### 2. `.github/WORKFLOW_COORDINATION.md` ✅

**Purpose**: Shows how GitHub Actions workflows work together as unified deployment pipeline

**Contains**:

- Unified deployment pipeline diagram
- Role of each workflow (6 workflows documented):
  - `ci-pytests.yml` — Platform core validator
  - `build.yml` — Quality gate (PR validation)
  - `wpcom.yml` — WordPress platform deployment
  - `publish-ghcr.yml` — Docker image release
  - `update-copilot-context.yml` — Sync LuminAI routing
  - `brand-validate.yml` — Visual consistency
- Execution order (what happens at each stage)
- Coordination rules (serial/parallel dependencies)
- Monitoring & observability
- Troubleshooting guide

**Key Insight**:

> "One version, one release: v2.1.0 = core + all apps + all personas at that version"

---

### 3. Updated Workflow Comments ✅

**Files Updated**:

- `ci-pytests.yml` — Added platform core validation context
- `build.yml` — Added quality gate context
- `wpcom.yml` — Added WordPress platform deployment context
- `publish-ghcr.yml` — Added Docker image unification context

**What Changed**: Each workflow now has a header comment explaining:

- What it validates/deploys
- Why it matters for the platform
- How it fits into the unified pipeline

**Example** (ci-pytests.yml):

```yaml
# Platform Core Validation
# This workflow validates the backend engine of LuminAI Platform:
# - src/tec_tgcr/ (resonance engine, personas, API)
# - research/CODEX/ (lore, TGCR theory, motifs)
# - data/personas/ (6 Resonance operators)
# - docs/operations/ATTACHMENT_PROTOCOL_*.md (emotional intelligence)
#
# When core tests pass, all 7 frontend apps can safely deploy
```

---

### 4. Updated `.github/PROJECT_METADATA.md` ✅

**Changed**:

**Before**:

> "Central coordination project for TEC-The-ELidoras-Codex — tracks cross-repo work, release milestones, automations, and cross-team initiatives to deliver LuminAI platform features and infra improvements."

**After**:

> "Central coordination for **LuminAI Platform** — unified backend engine (CODEX + TGCR + personas) + 7 frontend apps. Tracks features, infrastructure, personas, attachment protocols, and releases as one coherent system."

**Longer Description** now explains:

- Platform is integrated, not separate projects
- Backend engine (CODEX + TGCR + personas) powers all frontends
- What gets tracked in this project (core work, lore, personas, apps, protocols, infrastructure)
- Versioning approach (v2.1.0 = all components)
- How to use the board (prioritization, coordination, coherence verification)

---

## Platform Architecture At A Glance

```text
LUMINAI PLATFORM (One System)
│
├─ CORE ENGINE (The Brain)
│  ├─ Lore & Theory (research/CODEX/)
│  ├─ Personas (6 Resonance operators)
│  ├─ Resonance Engine (src/tec_tgcr/)
│  └─ Attachment Protocol (emotional intelligence)
│
├─ FRONTENDS (Expressions of Core)
│  ├─ luminai-interface (React dashboard)
│  ├─ resonance-player (Audio/motif player)
│  ├─ resonance-viewer (3D visualization)
│  ├─ voice-imprint-studio (Audio analysis)
│  ├─ star-viewer (Celestial mapping)
│  ├─ wordpress (3 plugins)
│  └─ widgets-sharepoint (Enterprise layer)
│
└─ CI/CD (Unified Pipeline)
   ├─ Test core (ci-pytests)
   ├─ Quality gate (build)
   ├─ Deploy all apps (wpcom, publish-ghcr)
   └─ Sync routing (update-copilot-context)
```

---

## Workflow Dependencies

### Testing (All Branches)

```text
push → [ci-pytests, build, brand-validate] (parallel)
  ↓ (all must pass)
If merge to main → deployment workflows triggered
```

### Deployment (Main Only)

```text
build passes → [wpcom, publish-ghcr] (parallel)
  ↓
All 3 WordPress plugins deployed at same version
All Docker image pushed at same tag
Routing updated live
  ↓
PLATFORM LIVE (all components at same version)
```

---

## What This Changes

### ✅ For Developers

**Before**: "Which project is this for?"

**After**: "How does this improve LuminAI platform coherence?"

- When you make a change, it affects the whole platform
- Tests validate core engine (all apps can use updated core)
- Deployment is all-at-once (no partial releases)

### ✅ For Project Management

**Before**: Separate backlogs per project

**After**: One backlog, one roadmap, one coherence goal

- All work is tracked in GitHub Project #6
- One version number (v2.1.0 for everything)
- One release cycle (all apps release together)

### ✅ For CI/CD

**Before**: Workflows were independent

**After**: Workflows are coordinated

- Core tests are gate for deployment
- All apps deploy together (no cherry-picking)
- Personas stay in sync everywhere

### ✅ For Users

**Before**: "Which app do I use?"

**After**: "LuminAI is one experience with many interfaces"

- Same personas everywhere (LUMINAI, AIRTH, ARCADIA, etc.)
- Same attachment protocol (emotional intelligence) everywhere
- Same release version everywhere

---

## Key Documents

| Document | Purpose | Location |
|----------|---------|----------|
| **PLATFORM_ARCHITECTURE.md** | Core principles + component model | `.github/PLATFORM_ARCHITECTURE.md` |
| **WORKFLOW_COORDINATION.md** | CI/CD pipeline + workflow roles | `.github/WORKFLOW_COORDINATION.md` |
| **PROJECT_METADATA.md** | GitHub Project description (UPDATED) | `.github/PROJECT_METADATA.md` |
| **Workflow comments** | Per-workflow context | `.github/workflows/*.yml` |
| **Personas Consolidation** | Single source of truth for 6 operators | `PERSONAS_CONSOLIDATION_REPORT.md` |
| **Copilot Instructions** | System prompt + persona routing | `.github/copilot-instructions.md` |
| **Quick Setup** | LuminAI deployment spec | `docs/operations/LUMINAI_RESONANCE_QUICK_SETUP.md` |

---

## Next Steps for Team

### 1. Update GitHub Project Description (UI)

- Go to <https://github.com/orgs/TEC-The-ELidoras-Codex/projects/6>
- Click settings/edit
- Copy one-line or longer description from PROJECT_METADATA.md
- Save

### 2. Review Workflow Comments

- Each `.github/workflows/*.yml` now has platform context
- Read comments to understand unified vision
- Ensure team aligns on "one platform" thinking

### 3. Use WORKFLOW_COORDINATION.md for Onboarding

- New team members should read this for understanding CI/CD
- Reference when debugging failed workflows
- Use troubleshooting section for common issues

### 4. Reference PLATFORM_ARCHITECTURE.md in PRs

- When proposing new features, reference which component improves resonance
- Example: "This change improves Φᴱ (Contextual Potential) by..."

---

## Coherence Verification Checklist

Use this to verify platform unity:

- [ ] All 6 personas defined in one place (QUICK_SETUP.md)
- [ ] Attachment protocol consistent across apps (WordPress, React, voice)
- [ ] Core tests validate before any deployment (ci-pytests gate)
- [ ] WordPress plugins deploy as triplet (never individual)
- [ ] Docker image includes all components (single artifact)
- [ ] GitHub Project tracks unified backlog (not per-app)
- [ ] One version number applied everywhere (v2.1.0 = all)
- [ ] Workflows coordinated (core → apps → deployment)

---

## Platform Coherence Statement

**LuminAI is one integrated system where:**

1. **Backend Engine** (CODEX + TGCR + Personas) is the single source of truth
2. **Frontend Apps** (7 interfaces) are expressions of that engine
3. **All Components** version, test, and deploy together
4. **Coherence** is measured by TGCR (φᵗ, ψʳ, Φᴱ) improvements across all layers
5. **Emotional Intelligence** (Attachment Protocol) is built into all interfaces

**This is not a collection of tools. This is one system with many facets.**

---

**Documentation Status**: ✅ Complete and coherent

**Ready for**: Team alignment, developer onboarding, stakeholder communication

**Maintained by**: Platform Infrastructure Team

---

## Files Touched This Session

| File | Change | Status |
|------|--------|--------|
| `.github/PLATFORM_ARCHITECTURE.md` | Created | ✅ New |
| `.github/WORKFLOW_COORDINATION.md` | Created | ✅ New |
| `.github/PROJECT_METADATA.md` | Updated (short + long descriptions) | ✅ Done |
| `.github/workflows/ci-pytests.yml` | Added header comments | ✅ Done |
| `.github/workflows/build.yml` | Added header comments | ✅ Done |
| `.github/workflows/wpcom.yml` | Added header comments | ✅ Done |
| `.github/workflows/publish-ghcr.yml` | Added header comments | ✅ Done |
| `.github/copilot-instructions.md` | Previously consolidated (6 personas) | ✅ Done |
| `PERSONAS_CONSOLIDATION_REPORT.md` | Previously created (audit trail) | ✅ Done |

---

## Session Shift

This represents the shift from "many projects" to "one platform."

All documentation now reflects unified architecture, coordinated CI/CD, and coherent platform vision.

✨ **Ready for deployment and team adoption.** ✨
