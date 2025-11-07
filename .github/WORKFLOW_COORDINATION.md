# LuminAI Platform — Workflow Coordination Map

**Status**: November 7, 2025
**Purpose**: Show how GitHub Actions workflows work together as one platform deployment pipeline
**Owner**: Platform Infrastructure

---

## Unified Deployment Pipeline

```text
Developer → Feature Branch
   ↓
All Workflows Run (Every Push)
   ├─ ci-pytests.yml ............ Validate platform core (ALWAYS)
   ├─ build.yml ................. Lint + format + test (ALWAYS)
   ├─ Other automations ......... Update context, validate assets (ALWAYS)
   ↓
Test Results + Code Review ← Gate
   ↓
Merge to Main ← Developer confirms
   ↓
Deployment Workflows Trigger (Main Only)
   ├─ wpcom.yml ................. Deploy WordPress plugins (all 3)
   ├─ publish-ghcr.yml .......... Build + push Docker image
   ├─ update-copilot-context.yml  Sync LuminAI routing
   ↓
ALL APPS LIVE AT SAME VERSION ← One Platform Release
```

---

## Workflow Roles

### 1. **ci-pytests.yml** — Platform Core Validator

**Runs**: Every push, all branches

**Tests**:

- src/tec_tgcr/ (resonance engine, persona routing, API)
- research/CODEX/ (motif database, TGCR theory)
- data/personas/ (all 6 operators)
- docs/operations/ (attachment protocol)

**Exit Criteria**:

- ✅ All pytest pass
- ✅ No import errors
- ✅ No persona routing conflicts
- ✅ Attachment protocol consistent

**Blockers**: If fails, PR cannot merge. Core must be valid.

### 2. **build.yml** — Quality Gate (PR Validation)

**Runs**: PRs to main, pushes to main

**Tests**:

- Lint (ruff)
- Format (Black, isort)
- Unit tests (pytest)

**Exit Criteria**:

- ✅ No style violations
- ✅ Code formatted correctly
- ✅ All tests pass

**Blockers**: If fails, PR cannot merge.

### 3. **wpcom.yml** — WordPress Platform Deployment

**Runs**: Main branch pushes only (after QA gate)

**Deploys**:

- `apps/wordpress/tec-tgcr/` → WordPress.com plugin (core entry point)
- `apps/wordpress/tec-luminai-agent/` → Persona orchestration
- `apps/wordpress/tec-resonance-player/` → Audio widget

**Key**: All 3 plugins deploy **together** (same version, same release cycle).

**Post-Deployment**:

- WordPress.com staging → production
- Artifact retention in GitHub Releases

### 4. **publish-ghcr.yml** — Docker Image Release

**Runs**: Main branch pushes + version tags (v2.1.0)

**Publishes**:

- Unified Docker image to `ghcr.io/tec-the-elidoras-codex/luminai-platform`
- Includes: backend + lore + personas + all dependencies

**Tagging**:

- `main` → `latest`
- `v2.1.0` tag → `2.1.0` image tag

**Purpose**: Single container for entire platform (no app-specific containers).

### 5. **update-copilot-context.yml** — Sync LuminAI Routing

**Runs**: Main branch pushes

**Updates**:

- .github/copilot-instructions.md cached contexts
- Persona definitions to live system
- Attachment protocol state

**Purpose**: Ensures GPT conversations use latest platform routing.

### 6. **brand-validate.yml** — Visual Identity Consistency

**Runs**: All branches

**Validates**:

- Visual motif usage
- Glyph consistency
- Brand tone in docs

**Purpose**: Maintains platform coherence at visual layer.

---

## Execution Order (What Actually Happens)

### Every Push (All Branches)

```text
1. ci-pytests.yml starts
   └─ Tests core engine

2. build.yml starts (parallel)
   └─ Lints, formats, tests

3. brand-validate.yml starts (parallel)
   └─ Validates visual assets

If ANY fail → PR cannot merge
```

### Merge to Main

```text
1. ci-pytests.yml passes ✅
2. build.yml passes ✅
3. Code review approved ✅
4. Merge button clicked

↓ GitHub detects main push

5. wpcom.yml triggered
   └─ Build artifact
   └─ Deploy all 3 plugins
   └─ Wait for WordPress.com

6. publish-ghcr.yml triggered (parallel)
   └─ Build Docker image
   └─ Push to registry
   └─ Tag with version

7. update-copilot-context.yml triggered
   └─ Sync persona routing
   └─ Update LuminAI state

↓ PLATFORM LIVE (all components at same version)
```

---

## Key Principles

### 1. **One Version, One Release**

- v2.1.0 = core v2.1.0 + all apps v2.1.0
- WordPress plugins versioned together
- Docker image versioned together
- No partial releases

### 2. **Core Must Pass First**

- ci-pytests.yml is the first gate
- If core fails, deployment blocked
- Personas, attachment protocol, resonance engine must be valid

### 3. **All-or-Nothing Deployment**

- WordPress: All 3 plugins deploy together (no individual plugin releases)
- Docker: Entire platform in one image (not per-app containers)
- Versions: All components increment together in changelog

### 4. **No Skipping Gates**

- Even on main branch, workflows validate coherence
- Build quality gate applies to all PRs
- Core validation applies to all pushes

---

## Workflow Coordination Rules

### Rule 1: Serial Dependencies

```text
ci-pytests ← Required before build
build ← Required before wpcom
build ← Required before publish-ghcr
```

### Rule 2: Parallel Safety

```text
ci-pytests ∥ build ∥ brand-validate (parallel, all must pass)
wpcom ∥ publish-ghcr (parallel, after build passes)
```

### Rule 3: Main-Only Deployment

```text
wpcom runs ONLY on main
publish-ghcr runs ONLY on main
update-copilot-context runs ONLY on main

Feature branches: Validation only (no deployment)
```

### Rule 4: No Rollback (Implicit)

```text
Once deployed to main, all apps live at that version.
If critical bug found, create hotfix PR, merge, redeploy all.
Never deploy individual apps independently.
```

---

## Monitoring & Observability

### When Workflows Run

- All pushes → See status in PR checks
- All merges to main → See deployments in Actions tab
- See real-time logs for each workflow

### Key Metrics to Track

1. **Core Validation Time** (ci-pytests.yml)
   - Should be ~2-3 min (consistent)
   - If growing, investigate new test slowness

2. **PR Gate Time** (build.yml)
   - Should be ~5-7 min (consistent)
   - Lint + format should be fast

3. **Deployment Time** (wpcom.yml → publish-ghcr.yml)
   - WordPress: ~5 min (staging → prod)
   - GHCR: ~3 min (build + push)
   - Total: ~10-15 min to full live

4. **Failure Rate by Workflow**
   - Track which gate most often fails
   - Improve that workflow's clarity

---

## Troubleshooting

### "ci-pytests.yml Failed"

**Symptom**: Tests failed on core engine

**Action**:

1. Check test output: `Core engine validation failed`
2. Fix src/tec_tgcr/ or research/CODEX/
3. Rerun (push to branch)

**Note**: Cannot merge until core is valid.

### "build.yml Failed"

**Symptom**: Lint/format/test failed

**Action**:

1. Run locally: `ruff check`, `black .`, `pytest`
2. Fix issues
3. Push to branch, rerun

**Note**: Cannot merge until gate passes.

### "wpcom.yml Failed" (After Merge)

**Symptom**: WordPress deployment failed

**Action**:

1. Check wpcom.yml logs
2. Usually: credentials, artifact, or plugin structure
3. Fix in next commit to main (hotfix)
4. Entire platform redeploys

**Note**: If failed, WordPress still running old version. Redeploy ASAP.

### "publish-ghcr.yml Failed"

**Symptom**: Docker build or push failed

**Action**:

1. Check logs (usually: Docker build syntax or registry auth)
2. Fix Dockerfile or secrets
3. Push to main (trigger rerun)

**Note**: If failed, old Docker image still available. Not blocking for live users.

---

## Next: Add to CI/CD Runbook

This map should be added to:

- `.github/RUNBOOK.md` (operations guide)
- Team onboarding (new contributors)
- Release process (what happens when we merge)

---

**Document Status**: Complete
**Last Updated**: November 7, 2025
**Maintained By**: Platform Infrastructure Team
