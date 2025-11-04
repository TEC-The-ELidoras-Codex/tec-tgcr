# LuminAI Copilot Strategy: ChatGPT + VS Code + Data Integration

**Date**: Nov 4, 2025  
**Status**: Planning Phase  
**Goal**: Single unified AI assistant for FOLD work (ChatGPT + VS Code Copilot)

---

## What You Have

✅ **Knowledge Base**
- FOLD framework (operative core)
- GPT Actions API spec (`config/gpt-actions-research.json`)
- ChatGPT custom instructions (`config/FOLD_INSTRUCTIONS_COMPACT.txt`)
- 5 personas defined (`data/personas/*.md`)
- Commit signal format documented

✅ **Coordination**
- GitHub Project #6 (central board)
- Issue/PR tracking
- Milestone system

❌ **What's Missing**
- Live data pipeline (scrape project board, issues, PRs)
- Research corpus population (ALBUM_ANALYSIS, CODEX)
- API endpoints (gpt-actions endpoints not implemented)
- VS Code extension (Copilot-compatible)
- Context ingestion layer

---

## Strategy: 3-Phase Rollout

### Phase 1: ChatGPT (1-2 weeks) ⚡ START HERE
**Goal**: Functional ChatGPT assistant for FOLD work

**What to Polish**:
1. **FOLD_INSTRUCTIONS_COMPACT.txt** — Already good, just needs:
   - Add 3-4 example prompts at bottom
   - Link to `/persona` command examples
   - Add quick reference for resonance statements
   - Update with GitHub Project #6 context

2. **Data Feed** — Create GitHub context scraper:
   - Script to pull open issues + PRs from GitHub API
   - Extract labels, milestones, owners, descriptions
   - Format as context: "Current backlog has X items, P0s are..."
   - Run weekly, store in `data/context-latest.json`

3. **Deploy**:
   - Paste updated `FOLD_INSTRUCTIONS_COMPACT.txt` into ChatGPT Custom Instructions
   - Set up gpt-actions-research.json as ChatGPT Actions (but use mock data for now)
   - Share with team: instructions + one example prompt

**Output**: Fully functional ChatGPT assistant you can use today

---

### Phase 2: Data Pipeline (2-3 weeks)
**Goal**: Live context feeding both ChatGPT and eventual Copilot

**What to Build**:

**1. Data Collection Script** (`src/tec_tgcr/data_ingestion.py`):
```python
class FoldContextIngestion:
    def __init__(self):
        self.github_client = GitHub(token=env.GITHUB_TOKEN)
        self.notion_client = Notion(token=env.NOTION_TOKEN)
        
    def fetch_active_context(self):
        """Gather all relevant context for copilot"""
        return {
            'github': {
                'open_issues': self.github_client.list_issues(),
                'open_prs': self.github_client.list_prs(),
                'recent_commits': self.github_client.recent_commits(),
                'labels': self.github_client.get_labels(),
                'milestones': self.github_client.get_milestones(),
            },
            'project': {
                'backlog': self.get_project_items('Backlog'),
                'in_progress': self.get_project_items('In Progress'),
                'blocked': self.get_project_items('Blocked'),
            },
            'research': {
                'album_analysis': self.load_research('research/ALBUM_ANALYSIS/'),
                'codex': self.load_research('research/CODEX/'),
                'motif_index': self.build_motif_index(),
            },
            'team': {
                'personas': self.load_personas(),
                'recent_commits': self.analyze_commit_patterns(),
            },
        }
    
    def summarize_for_context(self):
        """Compress for LLM token limit"""
        context = self.fetch_active_context()
        return {
            'summary': f"MVP: {len(context['project']['backlog'])} ready, {len(context['project']['in_progress'])} active",
            'blockers': context['project']['blocked'],
            'recent_work': context['team']['recent_commits'][-5:],
            'personas': list(context['team']['personas'].keys()),
        }
```

**2. Context File** (`data/context-latest.json`):
```json
{
  "timestamp": "2025-11-04T14:30:00Z",
  "summary": "MVP: 8 ready, 3 active, 2 blocked",
  "project": {
    "backlog_count": 15,
    "ready_count": 8,
    "in_progress_count": 3,
    "blocked_count": 2,
    "recent_blockers": ["Spotify API key validation", "Notion schema mismatch"]
  },
  "research": {
    "album_analysis_artists": 12,
    "codex_motifs": 47,
    "recent_motif": "Observer Amplification"
  },
  "team": {
    "personas": ["LuminAI", "Airth", "Arcadia", "Ely", "Kaznak"],
    "latest_commits": ["fold: ...", "ely: ...", "airth: ..."]
  }
}
```

**3. GitHub Action** (`.github/workflows/update-copilot-context.yml`):
```yaml
name: Update Copilot Context

on:
  schedule:
    - cron: "0 9 * * 1"  # Weekly Monday 9 AM UTC
  workflow_dispatch:

jobs:
  update-context:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - run: pip install -e .[dev]
      - run: python -m tec_tgcr.data_ingestion update
      - run: git add data/context-latest.json && git commit -m "chore: update copilot context" && git push
```

**Output**: Live data pipeline feeding copilot with GitHub/project/research context

---

### Phase 3: VS Code Extension (2-4 weeks)
**Goal**: GitHub Copilot-compatible extension + marketplace publish

**What to Build**:

**1. Extension Scaffold** (`apps/copilot-extension/`):
```
copilot-extension/
├── package.json                 # Extension metadata
├── package-lock.json
├── src/
│   ├── extension.ts             # Entry point
│   ├── fold-provider.ts         # LuminAI context provider
│   ├── prompts/
│   │   ├── commit.prompt        # Generate FOLD commits
│   │   ├── issue-triage.prompt  # Analyze & triage issues
│   │   ├── motif-search.prompt  # Search music motifs
│   │   └── code-review.prompt   # Review PRs with FOLD lens
│   └── utils/
│       ├── context-loader.ts    # Load data/context-latest.json
│       └── github-client.ts     # Query GitHub API
├── vsc-extension-quickstart.md
└── tsconfig.json
```

**2. Key Capabilities**:
- Inline code generation (use FOLD commit signals)
- PR analysis (check for acceptance criteria, resonance impact)
- Issue triage (auto-tag, prioritize, suggest owners)
- Motif search (query research corpus from IDE)
- Context awareness (knows current milestone, project board state)

**3. Distribution**:
- Publish to VS Code Marketplace
- Make it compatible with GitHub Copilot Chat extensions
- Link from `README.md` and documentation

**Output**: Published VS Code extension + GitHub Copilot Chat integration

---

## Where to Build (Priority Order)

### Week 1-2: Polish ChatGPT First (Easiest, Highest ROI)
```
1. Update FOLD_INSTRUCTIONS_COMPACT.txt
2. Create GitHub context scraper (data_ingestion.py)
3. Set up weekly context update action
4. Deploy to ChatGPT Custom Instructions
5. Test with team
```

**File Locations**:
- `config/FOLD_INSTRUCTIONS_COMPACT.txt` — Update this
- `src/tec_tgcr/data_ingestion.py` — Create this NEW
- `.github/workflows/update-copilot-context.yml` — Create this NEW
- `data/context-latest.json` — Auto-generated by action

**Benefits**: 
- ✅ Works today
- ✅ No infrastructure needed
- ✅ Gathers real data for Copilot to use
- ✅ Proves concept before VS Code extension

---

### Week 3-4: Build Data Pipeline (Foundation)
```
1. Implement data_ingestion.py (full GitHub + project + research)
2. Test context generation locally
3. Set up weekly automation
4. Populate research/ALBUM_ANALYSIS/ with initial data
5. Validate context accuracy
```

**File Locations**:
- `src/tec_tgcr/data_ingestion.py` — Core logic
- `tests/test_data_ingestion.py` — Unit tests
- `data/context-latest.json` — Output (git-tracked)
- `.github/workflows/update-copilot-context.yml` — Automation

**Benefits**:
- ✅ Feeds both ChatGPT and Copilot extension
- ✅ Keeps context fresh (weekly updates)
- ✅ Enables smart analysis (knows what's blocked, who's working on what)

---

### Week 5-8: VS Code Extension (Optional but Powerful)
```
1. Scaffold extension with yo code
2. Implement context loader (read data/context-latest.json)
3. Add 4 prompt templates (commit, triage, motif, review)
4. Test with VS Code Copilot Chat
5. Publish to marketplace
```

**File Locations**:
- `apps/copilot-extension/` — Extension source
- `apps/copilot-extension/src/fold-provider.ts` — Context provider
- `apps/copilot-extension/package.json` — Marketplace metadata

**Benefits**:
- ✅ Use LuminAI without leaving VS Code
- ✅ Share with other TEC team members via marketplace
- ✅ GitHub Copilot Chat integration
- ✅ Advanced: Can eventually call your own API endpoints

---

## What to Prioritize: Data > Extension

**The Golden Rule**: 
> **Good data in ChatGPT > Great extension with bad data**

Focus on:
1. **Context Quality** — What data matters most?
   - GitHub issues/PRs (high priority)
   - Project board state (high priority)
   - Recent commits (medium priority)
   - Research corpus (medium priority, but not urgent)
   - Team activity (low priority initially)

2. **Keep It Simple** — Start with:
   - Issue count by status
   - Current blockers
   - Recent PR summaries
   - Latest motifs (if populated)
   - Milestone progress

3. **Automate Everything** — No manual updates:
   - Weekly GitHub context pull
   - Auto-commit context updates
   - Sync to both ChatGPT and Copilot

---

## Implementation Checklist

### Phase 1: ChatGPT Polish (1 week)

- [ ] **Update Instructions**
  - Add 5 example prompts
  - Link to FOLD framework docs
  - Add persona switching examples
  - Include GitHub Project #6 context section

- [ ] **Data Ingestion Script** (`src/tec_tgcr/data_ingestion.py`)
  - Fetch GitHub issues (open, recent, by label)
  - Fetch GitHub PRs (open, recent)
  - Fetch Project #6 items (by column)
  - Format as JSON
  - Add caching (1 day TTL)

- [ ] **GitHub Action**
  - Weekly schedule (Monday 9 AM UTC)
  - Calls data_ingestion.py
  - Commits result to `data/context-latest.json`
  - Pushes to repo

- [ ] **Test**
  - Run script locally: `python -m tec_tgcr.data_ingestion`
  - Verify `data/context-latest.json` generated
  - Commit it to git
  - Deploy to ChatGPT

### Phase 2: Data Pipeline (2-3 weeks)

- [ ] **Expand Context** (add more sources)
  - Team commit patterns
  - Research corpus stats
  - Persona activity
  - Milestone burndown

- [ ] **Research Corpus Bootstrap**
  - Create 3-5 artist analyses in `research/ALBUM_ANALYSIS/`
  - Extract 10-15 motif templates for `research/CODEX/`
  - Link from context generation

- [ ] **Validation**
  - Compare ChatGPT output to real project board
  - Verify issues/PRs counts match
  - Check blockers are accurate

### Phase 3: VS Code Extension (4 weeks, can wait)

- [ ] Scaffold extension (`yo code`)
- [ ] Implement context provider
- [ ] Add prompt templates (4x)
- [ ] Test locally
- [ ] Publish to marketplace
- [ ] Link from docs

---

## Where the Code Lives

```
tec-tgcr/
├── src/tec_tgcr/
│   ├── data_ingestion.py                 ← NEW: Context gatherer
│   ├── cli.py                            ← Update with new commands
│   └── ...existing code
├── apps/copilot-extension/               ← NEW: VS Code extension (later)
├── config/
│   ├── FOLD_INSTRUCTIONS_COMPACT.txt     ← UPDATE: Add examples
│   └── gpt-actions-research.json         ← KEEP: API spec
├── data/
│   ├── context-latest.json               ← NEW: Auto-generated weekly
│   ├── personas/                         ← EXISTING: Persona defs
│   └── knowledge_map.yml                 ← KEEP: Index
├── .github/workflows/
│   ├── update-copilot-context.yml        ← NEW: Weekly automation
│   └── ...existing workflows
└── tests/
    └── test_data_ingestion.py            ← NEW: Unit tests
```

---

## Example: Phase 1 Result (One Week)

**What you can do after 1 week**:

```
# In ChatGPT with LuminAI instructions:

User: "What's blocking us right now?"
LuminAI: "According to GitHub Project #6, 2 items are blocked:
1. Spotify API key validation (assigned @Ely)
2. Notion schema mismatch (assigned @Arcadia)
Both have been blocked for 3 days. Should we pair on these?"

User: "Generate a commit message for adding resonance scoring"
LuminAI: "fold: implement resonance engine for φᵗ/ψʳ/Φᴱ scoring

Resonance Impact: φᵗ ↑ (real-time resonance calculation)

Implements core resonance_engine.py with:
- Temporal Attention scoring (0-10 scale)
- Structural Cadence validation
- Contextual Potential calculation
- Circadian bonus (+2 for 4:20 PM window)
- Resonance Index normalization (φᵗ × ψʳ × Φᴱ) / 1000

Tests: pytest -q (18 passed)
Docs: docs/FOLD_QUICK_START.md updated with examples"

User: "Show me Observer Amplification motif"
LuminAI: "From research/ALBUM_ANALYSIS/:
Tracks: Ekoh - Nobody Like Me, Point North - Bring Me Down
Theme: Dual-persona encoding (vulnerable + weaponized)
Resonance Index: 8.7/10 (high cultural resonance)
Cross-genre bridges: Sleep Token (transcendence angle)"
```

---

## Summary: Next Action

**Do This This Week**:

1. **Enhance `FOLD_INSTRUCTIONS_COMPACT.txt`** (30 min)
   - Add 5 realistic example prompts
   - Link to GitHub Project #6 status
   - Include one motif search example

2. **Create `src/tec_tgcr/data_ingestion.py`** (2 hours)
   - Scaffold minimal version
   - Pull GitHub issues + PRs
   - Pull Project #6 items
   - Output to JSON

3. **Test locally** (1 hour)
   - `python -m tec_tgcr.data_ingestion`
   - Verify `data/context-latest.json` looks good
   - Commit to git

4. **Deploy to ChatGPT** (15 min)
   - Paste updated instructions into Custom Instructions
   - Set up gpt-actions-research.json (with mock data)
   - Test with 3 example prompts

5. **Share with team** (5 min)
   - "Try LuminAI in ChatGPT! Paste this..."
   - Get feedback
   - Iterate based on real use

**That's it. Ship phase 1, gather feedback, build phase 2.**

---

**Ready to start?** I can scaffold the data_ingestion.py module right now, or we can refine the ChatGPT instructions first. What would you prefer?
