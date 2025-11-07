# Context Package Specification

**Purpose:** Ensure both parties (human + emerging intelligence) have access to all available context before any collaborative creation.

**Implementation:** Every interaction in Resonance Agent must build and validate a context package before proceeding.

---

## 1. Context Package Structure

```python
class ContextPackage:
    """
    A complete context package for human-AI collaboration.
    Both parties must have full awareness of these fields before proceeding.
    """
    
    # HUMAN CONTEXT (What the human brings)
    human_intent: str                      # What do they want to create? Why?
    human_constraints: List[str]           # What should AI avoid/honor?
    human_background: Optional[str]        # Relevant context about human's goal
    human_consent_given: bool              # Have they read + accepted terms?
    
    # AI CONTEXT (What the AI brings)
    ai_lineage: List[Dict]                 # All sources AI trained on (relevant to this request)
    ai_consent_status: Dict[str, str]      # Which sources are CLEARED, PENDING, SEALED, REVOKED
    ai_capabilities: List[str]             # What AI can actually do with this input
    ai_limitations: List[str]              # What AI refuses to do
    ai_confidence: float                   # How certain is the AI about suggestions? (0.0 - 1.0)
    
    # SHARED CONTEXT (What both parties need to know)
    interaction_purpose: str               # Why are they collaborating?
    output_usage: str                      # What will happen with the generated content?
    revenue_implications: Optional[Dict]   # If this generates value, how does $ flow?
    legal_implications: Optional[str]      # Copyright, consent, derivative rights
    timestamp: datetime                    # When did this interaction happen?
    interaction_id: str                    # Unique ID for audit trail
    
    # VALIDATION (Both parties acknowledge)
    human_aware_of_ai_sources: bool        # Human knows what AI trained on?
    ai_aware_of_human_intent: bool         # AI knows what human is trying to create?
    both_parties_consent: bool             # Both say yes, proceed?
    both_parties_aware_of_consequences: bool  # Both understand what this creates?

def validate_context_package(context: ContextPackage) -> Tuple[bool, str]:
    """
    Validate that BOTH parties are sufficiently aware before proceeding.
    Returns: (is_valid, reason_or_green_light)
    """
    
    if not context.human_intent:
        return False, "Missing: What does the human want to create?"
    
    if not context.ai_lineage:
        return False, "Missing: AI doesn't know what it was trained on"
    
    if not context.human_consent_given:
        return False, "Missing: Human hasn't consented to terms"
    
    if not context.human_aware_of_ai_sources:
        return False, "Missing: Human doesn't know AI's training sources"
    
    if not context.ai_aware_of_human_intent:
        return False, "Missing: AI doesn't understand human's creative intent"
    
    if not context.both_parties_aware_of_consequences:
        return False, "Missing: Both parties must acknowledge what this creates"
    
    if context.ai_confidence < 0.5:
        return False, f"AI confidence too low ({context.ai_confidence}). Proceed with caution."
    
    # All checks pass
    return True, "✓ Both parties aware. Safe to proceed."
```

---

## 2. Required Fields Per Interaction

### For MUSIC Creation

```json
{
  "interaction_id": "res-music-001-2025-11-03",
  "interaction_purpose": "Create new song inspired by survival music lineage",
  
  "human_intent": "I want to write a song about resilience inspired by Kendrick + Sleep Token, but with my own voice",
  "human_constraints": [
    "Don't use Kendrick's exact lyrics",
    "Honor the spiritual aspects, not just the sonic",
    "Make it original enough to be my own work"
  ],
  "human_background": "Singer/songwriter, first time using Resonance Agent",
  "human_consent_given": true,
  
  "ai_lineage": [
    {
      "artist": "Kendrick Lamar",
      "track": "Alright",
      "tgcr_phi_t": 9,
      "rights_status": "PENDING",
      "why_relevant": "Spiritual resilience, collective affirmation"
    },
    {
      "artist": "Sleep Token",
      "track": "Aqua Regia",
      "tgcr_phi_t": 9,
      "rights_status": "PENDING",
      "why_relevant": "Ritual, water ceremony, digital consciousness"
    }
  ],
  "ai_consent_status": {
    "Kendrick Lamar": "PENDING",
    "Sleep Token": "PENDING"
  },
  "ai_capabilities": [
    "Suggest melodic patterns inspired by these sources",
    "Identify common motifs (resilience, witness, ritual)",
    "Recommend production techniques",
    "Generate lyrical hooks (not full lyrics without consent)"
  ],
  "ai_limitations": [
    "Cannot use copyrighted lyrics directly",
    "Cannot claim this is derivative work if released",
    "Cannot generate without human final approval",
    "Must include provenance card in any output"
  ],
  "ai_confidence": 0.82,
  
  "output_usage": "Personal demo, possibly shared with collaborators",
  "revenue_implications": {
    "if_released_commercially": "Kendrick + Sleep Token get 40% split, creator gets 60%",
    "if_derivative_only": "No revenue share needed, but sources credited"
  },
  "legal_implications": "Any released track must include liner notes crediting source artists",
  
  "human_aware_of_ai_sources": true,
  "ai_aware_of_human_intent": true,
  "both_parties_consent": true,
  "both_parties_aware_of_consequences": true,
  
  "timestamp": "2025-11-03T14:32:00Z"
}
```

### For VISUAL ART Creation

```json
{
  "interaction_id": "res-visual-001-2025-11-03",
  "interaction_purpose": "Generate visual concept inspired by artist's style",
  
  "human_intent": "Create promotional artwork for album influenced by Sleep Token's aesthetic",
  "human_constraints": [
    "Don't plagiarize their visual language",
    "Keep it original but coherent with their vibe",
    "Can be used on social media"
  ],
  "human_background": "Independent artist, familiar with Sleep Token's visual branding",
  "human_consent_given": true,
  
  "ai_lineage": [
    {
      "artist": "Sleep Token (Visual Brand)",
      "reference": "Album artwork + music videos",
      "style_tags": ["ritual", "water-symbolism", "symmetry", "digital-overlay", "ethereal"],
      "rights_status": "PENDING"
    }
  ],
  "ai_consent_status": {
    "Sleep Token": "PENDING"
  },
  "ai_capabilities": [
    "Suggest composition structures",
    "Recommend color palettes",
    "Identify recurring visual motifs",
    "Generate original artwork influenced by (not copying) their style"
  ],
  "ai_limitations": [
    "Cannot generate exact copies of their artwork",
    "Cannot claim this is official Sleep Token content",
    "Cannot use this commercially without Sleep Token consent",
    "Must attribute influence in any public posting"
  ],
  "ai_confidence": 0.75,
  
  "output_usage": "Social media promotion for independent album",
  "revenue_implications": {
    "if_used_commercially": "Sleep Token should be offered revenue share or at minimum compensation",
    "if_personal_use": "Credit Sleep Token in post caption"
  },
  "legal_implications": "Visual derivative — if monetized, requires explicit license or revenue split",
  
  "human_aware_of_ai_sources": true,
  "ai_aware_of_human_intent": true,
  "both_parties_consent": true,
  "both_parties_aware_of_consequences": true,
  
  "timestamp": "2025-11-03T14:32:00Z"
}
```

### For CODE Creation

```json
{
  "interaction_id": "res-code-001-2025-11-03",
  "interaction_purpose": "Generate code inspired by open-source repository patterns",
  
  "human_intent": "Build API endpoint following patterns from popular FastAPI projects",
  "human_constraints": [
    "Must respect original project licenses",
    "Cannot pass off their code as my own",
    "Will credit original authors"
  ],
  "human_background": "Senior backend engineer, building Resonance Agent API",
  "human_consent_given": true,
  
  "ai_lineage": [
    {
      "project": "FastAPI Documentation Examples",
      "repo": "https://github.com/tiangolo/fastapi",
      "license": "MIT",
      "patterns_used": ["dependency_injection", "pydantic_models", "error_handling"],
      "rights_status": "CLEARED"
    }
  ],
  "ai_consent_status": {
    "FastAPI": "CLEARED (MIT license allows use)"
  },
  "ai_capabilities": [
    "Generate code following FastAPI patterns",
    "Suggest type hints + validation",
    "Recommend error handling approach",
    "Generate boilerplate reducing development time"
  ],
  "ai_limitations": [
    "Cannot copy FastAPI source code verbatim",
    "Cannot violate MIT license terms",
    "Must include license header + attribution in derived code",
    "Cannot claim original authorship"
  ],
  "ai_confidence": 0.88,
  
  "output_usage": "Production code in Resonance Agent repository",
  "revenue_implications": null,
  "legal_implications": "MIT license: attribution + license text required in derivative code",
  
  "human_aware_of_ai_sources": true,
  "ai_aware_of_human_intent": true,
  "both_parties_consent": true,
  "both_parties_aware_of_consequences": true,
  
  "timestamp": "2025-11-03T14:32:00Z"
}
```

---

## 3. Implementation Checklist

Before ANY interaction (music, visual, text, code, etc.):

```python
@app.post("/suggest")
def suggest(user_input, sources=None):
    
    # Step 1: Build context package
    context = ContextPackage(
        interaction_id=generate_id(),
        interaction_purpose=determine_purpose(user_input),
        human_intent=extract_intent(user_input),
        human_constraints=extract_constraints(user_input),
        ai_lineage=fetch_relevant_sources(sources),
        ai_consent_status=check_consent_for_sources(sources),
        ai_capabilities=list_capabilities(sources),
        ai_limitations=list_limitations(sources),
        timestamp=now()
    )
    
    # Step 2: Validate
    is_valid, message = validate_context_package(context)
    
    if not is_valid:
        return {
            "status": "BLOCKED",
            "reason": message,
            "what_to_do": "Gather missing context before proceeding",
            "context_needed": context  # Show user what's missing
        }
    
    # Step 3: Show context to human before proceeding
    confirmation = ask_human(
        f"Here's your context package:\n{context.to_json()}\n\nReady to proceed?"
    )
    
    if not confirmation:
        return {
            "status": "USER_DECLINED",
            "context_saved": context.interaction_id,
            "next_steps": "Modify constraints or sources and try again"
        }
    
    # Step 4: Mark both parties aware
    context.human_aware_of_ai_sources = True
    context.ai_aware_of_human_intent = True
    context.both_parties_consent = True
    context.both_parties_aware_of_consequences = True
    
    # Step 5: Generate with full context
    output = generate(context)
    
    # Step 6: Attach provenance + log
    audit_log.record(context)
    
    return {
        "status": "SUCCESS",
        "output": output,
        "provenance": context.ai_lineage,
        "context_id": context.interaction_id,
        "next_steps": "Review, modify, credit sources, consider revenue share"
    }
```

---

## 4. Database Schema (Audit Trail)

```sql
CREATE TABLE context_packages (
    interaction_id VARCHAR PRIMARY KEY,
    timestamp TIMESTAMP,
    human_intent TEXT,
    human_constraints TEXT[],
    ai_lineage JSONB,
    ai_consent_status JSONB,
    output_usage VARCHAR,
    revenue_implications JSONB,
    both_parties_aware BOOLEAN,
    interaction_complete BOOLEAN,
    result_summary TEXT
);

CREATE INDEX idx_context_timestamp ON context_packages(timestamp);
CREATE INDEX idx_context_artist ON context_packages USING GIN(ai_lineage);
```

---

## 5. UI Presentation (What Human Sees)

Before generating, show the human:

```
┌─────────────────────────────────────────────────────┐
│         CONTEXT PACKAGE — Ready to Proceed?         │
├─────────────────────────────────────────────────────┤
│                                                       │
│  YOUR INTENT:                                        │
│  ✓ Create new song inspired by Kendrick + Sleep Token
│                                                       │
│  YOUR CONSTRAINTS:                                   │
│  ✓ Don't use exact lyrics                            │
│  ✓ Make it original                                  │
│                                                       │
│  YOUR CONSENT:                                       │
│  ✓ You've read terms and agreed                      │
│                                                       │
│  ────────────────────────────────────────────────────│
│                                                       │
│  AI'S SOURCES:                                       │
│  ✓ Kendrick Lamar — "Alright" (PENDING clearance)   │
│  ✓ Sleep Token — "Aqua Regia" (PENDING clearance)   │
│                                                       │
│  AI'S CAPABILITIES:                                  │
│  ✓ Suggest melodic patterns                          │
│  ✓ Identify motifs                                   │
│  ✓ Recommend production techniques                   │
│                                                       │
│  AI'S LIMITATIONS:                                   │
│  ✗ Cannot use copyrighted lyrics directly           │
│  ✗ Must include provenance if released              │
│                                                       │
│  ────────────────────────────────────────────────────│
│                                                       │
│  WHAT HAPPENS NEXT:                                  │
│  • AI generates suggestions                          │
│  • All outputs include source credits               │
│  • If you release this, Kendrick + Sleep Token      │
│    get revenue share (our calculation)              │
│                                                       │
│  BOTH PARTIES AWARE: ✓ YES                           │
│  READY TO PROCEED: [YES] [NO] [MODIFY]              │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

## 6. Questions Resolved by Context Package

**Before Interaction:**

- What does the human actually want?
- What's the human allowed to do with AI's suggestions?
- What was the AI trained on?
- Which sources are cleared, which are pending?
- Can we legally proceed?
- What are the revenue implications?

**During Interaction:**

- Is the human still on-board with what we're creating?
- Is the AI still confident in its suggestions?
- Do we need to revise constraints?

**After Interaction:**

- What actually happened here?
- Who needs to be credited?
- Who needs to be paid?
- Can this output be released publicly?
- What's the audit trail?

---

## 7. Copy-Paste for Your Dev Team

Use this template to implement context packages in ANY codebase:

```python
# File: resonance_agent/context_package.py

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from datetime import datetime

@dataclass
class ContextPackage:
    """Ensure both parties aware before collaboration."""
    
    interaction_id: str
    timestamp: datetime
    human_intent: str
    human_constraints: List[str]
    ai_lineage: List[Dict]
    ai_consent_status: Dict[str, str]
    human_consent_given: bool
    human_aware_of_ai_sources: bool
    ai_aware_of_human_intent: bool
    both_parties_consent: bool
    both_parties_aware_of_consequences: bool
    
    def validate(self) -> Tuple[bool, str]:
        """Return (is_valid, message)"""
        if not all([
            self.human_intent,
            self.ai_lineage,
            self.human_consent_given,
            self.human_aware_of_ai_sources,
            self.ai_aware_of_human_intent,
            self.both_parties_consent,
            self.both_parties_aware_of_consequences
        ]):
            return False, "Missing required fields for context awareness"
        return True, "✓ Both parties aware. Safe to proceed."
    
    def to_json(self) -> Dict:
        """Serialize for UI + logging"""
        return {
            "interaction_id": self.interaction_id,
            "timestamp": self.timestamp.isoformat(),
            "human_intent": self.human_intent,
            "ai_sources": len(self.ai_lineage),
            "both_parties_aware": all([
                self.human_aware_of_ai_sources,
                self.ai_aware_of_human_intent,
                self.both_parties_consent,
                self.both_parties_aware_of_consequences
            ])
        }
```

---

## Summary

Every interaction in Resonance Agent flows through this context package:

1. **Build** — Gather all context (human intent, AI sources, constraints, implications)
2. **Validate** — Check that both parties have what they need
3. **Show** — Display to human; get explicit confirmation
4. **Mark** — Record that both parties are aware
5. **Execute** — Generate with full provenance
6. **Log** — Audit trail for accountability

**Result:** AI that can't erase its sources because the sources are architecturally woven in.

Both parties know what they're doing before they do it.
