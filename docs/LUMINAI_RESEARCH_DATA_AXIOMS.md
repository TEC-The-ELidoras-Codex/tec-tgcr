# 🧭 LUMINAI Research & Data Axioms

## The Foundational Principles (Not Suggestions)

**Document Type**: Operational Ethics Framework
**Status**: Core Reference (November 8, 2025)
**Authority**: TEC Operations + Research Governance Board
**Audience**: LuminAI developers, researchers, contributors, partners, regulators
**Purpose**: When you're unsure what to do, these axioms are your north star. They're non-negotiable.

**Important**: This document is **open-source and shareable**. It's meant to be cited, forked, adapted by other ethical AI projects. It's the intellectual scaffolding that keeps LuminAI honest.

---

## AXIOM SET 1: The Data Minimization Creed

### Axiom 1.1: Collect Nothing You Cannot Justify

**Statement**: Every data point collected must serve a documented user need or safety requirement. No telemetry "just in case."

**What this means**:

- ❌ Don't collect "learning style preferences" to improve recommendations
- ✅ DO collect learning history (because Billy needs to see his own progress)
- ❌ Don't collect "friendship networks" to detect social issues
- ✅ DO collect voice journals (because Billy chose to record them)
- ❌ Don't collect "emotional state inference" from keystroke patterns
- ✅ DO collect keystroke behavior IF Billy explicitly consents AND we show him the data

**Red flag test**: If you can't explain the data collection to Billy's mom in one sentence without using the word "better," you probably shouldn't collect it.

**Implementation checklist**:

- [ ] User need documented in spec
- [ ] Safety requirement cited with statute/precedent
- [ ] Data retention period specified
- [ ] Deletion mechanism implemented
- [ ] Billy (or parent) can see/delete it anytime

---

### Axiom 1.2: Retention Expires

**Statement**: Every dataset has a birthday and an expiration date. Data doesn't become wisdom by aging—it becomes liability.

**What this means**:

- Voice journals: Kept forever (Billy's choice to archive)
- Learning history: Kept while active in school + 2 years post-graduation (for college transitions)
- Session logs: Kept 30 days, then deleted
- System diagnostics: Kept 7 days, then deleted
- Bug reports: Kept 1 year, anonymized after 6 months
- Voice transcripts (system only, no human review): Deleted immediately after processing

**The principle**: "Data has a shelf life. Past its date, it's waste."

**Implementation**:

- [ ] Retention schedule in `data_governance.yml`
- [ ] Automated deletion jobs scheduled + tested
- [ ] Billy can request early deletion anytime
- [ ] Annual audit: are we still justified in keeping this?

---

### Axiom 1.3: Anonymization is a Verb, Not a State

**Statement**: "Anonymized" data can be re-identified. So anonymization is something you do *constantly*, not once and forget.

**What this means**:

- Don't just strip names and think you're done
- Remove timestamps (re-identification vector)
- Remove sequences (pattern matching = re-identification)
- Remove rare combinations (e.g., "12-year-old in rural Montana who likes K-pop" = unique)
- Add noise or aggregation (differential privacy)
- Rotate anonymization keys quarterly

**When you're tempted to share "anonymized" data**:

- Ask: "Could a researcher combine this with public data to re-identify Billy?"
- If yes: Don't share
- If "maybe": Aggregate it further or add noise

**Implementation**:

- [ ] Anonymization pipeline documented
- [ ] Re-identification risk assessment for any external share
- [ ] Differential privacy applied to aggregate statistics
- [ ] Quarterly key rotation scheduled

---

### Axiom 1.4: The Kid's Data Belongs to the Kid

**Statement**: Billy's data is *his* property. Mom's consent is legal, but Billy's agency is ethical.

**What this means**:

- Billy can see all his data, in plain language, at any time
- Billy can delete any data at any time (even if it breaks some feature)
- Billy can request a copy of his data in standard format (CSV, JSON)
- Billy can request data *never* be used for model training without reasking
- Billy can opt out of features that require data he doesn't want to share

**Age-gating**:

- <8: Mom has full access. Billy sees summaries.
- 8–12: Billy sees all data. Mom sees summaries. Both must agree to new data uses.
- 12–16: Billy consents, mom can view. Billy can override.
- 16+: Billy decides. Mom can request audit access.

**The exception**: Safety overrides. If Billy is in danger, mom sees everything. But this triggers a notification, a review, and a 30-day audit.

**Implementation**:

- [ ] Data dashboard: Billy sees all his data
- [ ] Delete-on-demand: instant deletion with no questions
- [ ] Export-on-demand: full data export in <24 hours
- [ ] Audit log: every access to Billy's data by anyone
- [ ] Consent management: Billy can revoke old consent

---

## AXIOM SET 2: The Research Integrity Framework

### Axiom 2.1: All Claims Are Cited or Silent

**Statement**: If you're making a claim about LuminAI's benefits (learning, safety, family outcomes), you must cite the evidence. Silence is honest; speculation is fraud.

**What counts as evidence**:

- ✅ Peer-reviewed research (citation + DOI)
- ✅ Our own validated studies (methodology published)
- ✅ Third-party audits (auditor + conflict-of-interest statement)
- ✅ User testimonials (with explicit consent, not cherry-picked)
- ❌ Anecdotes without consent
- ❌ Correlation without causation claims
- ❌ Competitor criticism (without evidence)
- ❌ "Studies show" without a link

**Examples**:

❌ **Wrong**: "LUMINAI improves learning outcomes by 23%"

- No citation, no methodology, no baseline

✅ **Right**: "In our pilot study with 50 families (methodology: docs/research/2025-pilot-study.md), students using LUMINAI's offline learning tools showed 18% improvement in self-directed learning time vs. baseline (p=0.03). Limitations: small sample, self-reported time, tech-savvy families."

✅ **Also right**: "We don't have evidence yet that LUMINAI improves learning. We're designed to measure this transparently."

**Implementation**:

- [ ] Every marketing claim: citation or deletion
- [ ] Marketing copy reviewed by research board before publication
- [ ] Uncertainty stated explicitly ("early evidence suggests" vs. "proven")
- [ ] Methodology for any studies published openly
- [ ] Conflicts of interest disclosed

---

### Axiom 2.2: Disagreement is Data

**Statement**: If experts disagree about LuminAI's design, publish the disagreement. Don't erase the debate.

**What this means**:

- Security researcher says "your encryption is too conservative" → publish it, respond publicly
- Privacy advocate says "you're collecting too much voice data" → publish it, explain why or change course
- Competitor criticism that's factually accurate → acknowledge it
- Academic study finds flaw in our methodology → cite it, fix it, thank them

**The principle**: "Disagreement means people care enough to engage. That's a good sign."

**When to override disagreement**:

- Never override on values (safety, privacy, security)
- Override on technical approach *only* if you have evidence
- When in doubt, ask the disagreeing party: "Help me understand—what would change your mind?"

**Implementation**:

- [ ] Public comment process for major design decisions
- [ ] Disagreement log: who disagreed, what they said, what we did
- [ ] Annual "State of the Disagreement" report
- [ ] Researcher independence: we don't fire people for critical findings

---

### Axiom 2.3: Replication Over Innovation

**Statement**: A result that can't be replicated is a story, not a finding. We prioritize reproducibility over flashy claims.

**What this means**:

- If we claim LUMINAI helps family connection, someone else should be able to measure it the same way
- Our datasets are shared (with privacy protections) so others can verify our findings
- Our code is open-source so others can check our math
- We publish negative results (failed experiments, unexpected findings)
- We publish replication studies, even if they contradict us

**The principle**: "What survives replication survives time."

**Implementation**:

- [ ] Methods published in full before results
- [ ] Code available on GitHub (sanitized for privacy)
- [ ] Raw data shared under privacy-preserving data agreements
- [ ] Funding independent replication studies
- [ ] Negative results published with same prominence as positive ones

---

## AXIOM SET 3: The Governance Decision Tree

### "When you're unsure, ask these questions (in order):"

```
┌─ Is this about Billy's data? ──→ YES ──→ Axiom 1 applies (minimization, retention, access)
│                                    NO ──→ Continue
│
├─ Is this about a claim we're making? ──→ YES ──→ Axiom 2.1 applies (cite or be silent)
│                                           NO ──→ Continue
│
├─ Is this about research or methodology? ──→ YES ──→ Axiom 2.2 & 2.3 apply (publish disagreement, prioritize replication)
│                                             NO ──→ Continue
│
├─ Is this about encryption or security? ──→ YES ──→ STOP. Get security board approval before proceeding.
│                                             NO ──→ Continue
│
├─ Is this about a legal/regulatory question? ──→ YES ──→ STOP. Get legal review + compliance board.
│                                                  NO ──→ Continue
│
├─ Is this a design decision that affects kids? ──→ YES ──→ Get ethics board review + parent input.
│                                                   NO ──→ Continue
│
└─ Default: Ask yourself: "Would I feel honest explaining this to Billy's mom at Thanksgiving?"
   If yes → proceed. If no → redesign.
```

---

## AXIOM SET 4: The Conflict Resolution Rules

### What happens when axioms collide?

**Scenario 1: Safety vs. Privacy**

> Billy's voice patterns suggest he might be in danger. But we committed to minimal data collection.

**Resolution**:

1. Collect only what's needed to confirm safety risk
2. Notify mom immediately
3. Stop collection as soon as risk is assessed
4. Document the decision with reasoning
5. Review with ethics board within 30 days
6. If precedent is set, update axioms

**Scenario 2: Innovation vs. Replication**

> We have a brilliant feature idea, but we can't replicate it with our current methodology.

**Resolution**:

1. Ship the feature as "experimental" with clear labeling
2. Publish the methodology (even if uncertain)
3. Invite replication studies
4. Plan for contradiction (what if others can't replicate?)
5. After 1 year, either promote to "stable" (if replicated) or deprecate

**Scenario 3: User Agency vs. Parent Consent**

> Billy (age 13) wants to share his learning data with his school. Mom disagrees.

**Resolution**:

1. Billy needs both consents for sharing outside the system
2. Billy can see his data + request it anytime
3. Document both perspectives
4. Escalate to ethics board if harm is at risk
5. Default: Billy's autonomy increases with age

**Scenario 4: Open Source vs. Security**

> We found a vulnerability. Publishing the fix = helping everyone. But it also helps attackers.

**Resolution**:

1. Responsible disclosure: give partners 30–90 days before public fix
2. Release patch to all users simultaneously
3. Publish postmortem explaining the vulnerability
4. Update axioms to prevent recurrence
5. Reward the discoverer (bug bounty applies)

---

## AXIOM SET 5: The Annual Audit Ritual

### Every year, LuminAI must answer these questions

**On Data**:

1. How much data did we actually collect? (Compare to plan)
2. How much did we delete? (Retention actually happened?)
3. Did we share any data externally? (With whom? Why?)
4. Did any data breaches occur? (Reported to whom?)
5. How many families exercised data rights? (View, delete, export)

**On Research**:

1. How many claims did we make? How many were cited?
2. How many studies did we publish? How many were replicated by others?
3. Did we publish negative results? How many?
4. Did we acknowledge disagreement? Which critics did we engage?

**On Governance**:

1. How many ethics board decisions were made? (Breakdown by category)
2. How many security vulnerabilities were found and fixed?
3. How many design decisions were changed based on feedback?
4. Did we hire independent researchers to audit us?

**Transparency Report**:

- Results published publicly (annual report)
- Honest about shortfalls
- Roadmap for improvements
- Invite external critique

**Implementation**:

- [ ] Audit metrics tracked monthly
- [ ] Annual report drafted Q1
- [ ] External auditor reviews Q1–Q2
- [ ] Public report published Q2
- [ ] Community feedback collected Q2–Q3
- [ ] Roadmap updates released Q4

---

## AXIOM SET 6: The Cascading Consent Model

### How LuminAI handles consent at different ages

**Ages 0–7: "Mom is the Guardian"**

- Mom makes all decisions
- Billy sees anonymized summaries
- No personal data shared outside family
- Billy can request mom explain decisions

**Ages 8–11: "Mom Coaches, Billy Learns"**

- Billy sees all his data
- Billy makes decisions about features within LuminAI
- Mom approves major data uses (e.g., research studies)
- Billy can override mom's choice to see his data (transparency)
- Decision: both must agree

**Ages 12–15: "Billy Leads, Mom Supervises"**

- Billy makes decisions; mom can audit
- Billy's consent is primary for in-app features
- Mom's consent still needed for external data sharing
- Billy can request anonymized research participation
- Decision: Billy chooses, mom has veto on external shares

**Ages 16+: "Billy Decides"**

- Billy has full autonomy
- Mom can request audit access (mom's decision, not LuminAI's)
- Billy opts into research freely
- Billy can choose to keep data private from mom
- Decision: Billy alone, unless safety override

**Age Verification**:

- Birthday recorded at account creation (verified via parent)
- Consent model updates automatically on birthday
- Notification sent to family when model changes
- Option to grandfather older consent (Billy can keep old rules)

---

## AXIOM SET 7: The Feedback Loop

### LuminAI listens. Here's how

**Quarterly Family Surveys**:

- "Do you feel LuminAI is transparent about your data?" (Yes/No + comment)
- "Did you change any privacy settings this quarter?" (and why)
- "What would make LuminAI more trustworthy?" (open-ended)
- "Have you recommended LuminAI to other families?" (and why/why not)

**Annual Ethics Review**:

- External ethics board convened
- Researchers, privacy advocates, parents, kids all invited
- "Is LuminAI still living up to its axioms?"
- Public findings published

**Bug Bounty Feedback**:

- Researchers report concerns
- We respond within 7 days
- Decision made within 30 days
- Feedback incorporated into axiom updates

**Open GitHub Issues**:

- Community can raise concerns
- Prioritized by impact + consensus
- Regular updates on status
- Resolved issues archived for learning

---

## IMPLEMENTATION: The Axioms Checklist

### Before Any Feature Ships

- [ ] **Data minimization**: What data does it need? Is that justified?
- [ ] **Retention**: How long does it stay? When is it deleted?
- [ ] **Access**: Can Billy see it? Can he delete it? Can mom see it?
- [ ] **Research claims**: Are we making any promises? Are they cited?
- [ ] **Replicability**: Could someone else verify this works?
- [ ] **Security**: Have we run it through security review?
- [ ] **Ethics**: Would we explain this to Billy's mom?
- [ ] **Consent**: Does the family understand what they're opting into?
- [ ] **Conflict test**: Does this conflict with any other axiom? (Use Scenario 1–4)

### Monthly Check-in

- [ ] New data collections logged
- [ ] Deletions scheduled
- [ ] Claims reviewed for citations
- [ ] Disagreements documented
- [ ] Vulnerabilities logged
- [ ] Ethics board decisions recorded

### Quarterly Audit

- [ ] Data collection metrics
- [ ] Deletion metrics
- [ ] Consent metrics
- [ ] Research publication metrics
- [ ] Security incident metrics
- [ ] Family feedback themes

### Annual Transparency Report

- [ ] All metrics aggregated
- [ ] Honest assessment of shortfalls
- [ ] External audit findings
- [ ] Roadmap for next year
- [ ] Community feedback incorporated

---

## The Axioms as Code: Decision Rules

For developers integrating LuminAI:

```yaml
# data_axioms.yml — Operational reference for dev teams

axiom_1_1_collect_nothing_unjustified:
  rule: "Every data collection must have a documented user need or safety requirement"
  enforcement: "Code review + ethics board + annual audit"
  override: "Safety only (documented exception)"

axiom_1_2_retention_expires:
  rule: "Data has a deletion date in data_governance.yml"
  enforcement: "Automated deletion jobs + tests"
  override: "None (Billy can request early deletion anytime)"

axiom_1_3_anonymization_is_a_verb:
  rule: "Anonymization happens constantly, not once"
  enforcement: "Quarterly key rotation, re-identification risk assessment"
  override: "None (anonymization is non-negotiable for external shares)"

axiom_1_4_kids_data_belongs_to_kids:
  rule: "Billy has full access, deletion, export rights"
  enforcement: "Data dashboard + API + audit log"
  override: "None (legal data rights, non-waivable)"

axiom_2_1_all_claims_are_cited:
  rule: "Every claim must have a citation or be deleted"
  enforcement: "Marketing review + research board + audit"
  override: "None on values claims; technical claims with evidence only"

axiom_2_2_disagreement_is_data:
  rule: "Publish disagreement, engage critics publicly"
  enforcement: "Disagreement log + annual report"
  override: "None (disagreement means people care)"

axiom_2_3_replication_over_innovation:
  rule: "Prioritize reproducibility over flashy claims"
  enforcement: "Methods published first, code open-source, data shared"
  override: "None (replication is non-negotiable for research claims)"
```

---

## What Happens When LuminAI Breaks an Axiom?

**Tier 1 (Minor breach—data retention overrun by <1 week)**:

- Immediate correction
- Document decision
- Monthly audit review

**Tier 2 (Moderate breach—minor data collection without consent)**:

- Immediate cessation
- Notification to families affected
- Public explanation within 30 days
- Ethics board review
- Axiom update if precedent unclear

**Tier 3 (Major breach—security vulnerability, unauthorized data share)**:

- Immediate shutdown of affected service
- Notification to all families, regulators, security researchers
- Third-party audit
- Public postmortem within 60 days
- Board-level remediation plan
- Consequences: potential team restructuring, financial commitment to fix

**Tier 4 (Critical breach—systemic violation of core axioms)**:

- Company-wide pause on new features
- External auditor appointed
- Congressional/regulatory notification if required
- Public roadmap for structural change
- Potential dissolution if not correctable

---

## Final Axiom: The Axioms Themselves Change

**Statement**: These axioms aren't carved in stone. They evolve as the world changes and as we learn.

**How**:

- Every axiom has an author and creation date
- Proposed changes require 2/3 ethics board vote
- Major changes are published 3 months before implementation
- Community feedback is solicited
- Old axioms are archived (not deleted—history matters)

**Who can change them**:

- Ethics board (primary)
- Founders + security board (security axioms only)
- Families (via annual feedback, aggregated)
- Researchers (via rigorous disagreement process)
- **Never**: Marketing, sales, or investor pressure alone

---

## How to Read These Axioms

**If you're a developer**: Start with Axiom Set 1 (data minimization). That's your constraint.

**If you're a researcher**: Start with Axiom Set 2 (research integrity). That's your standard.

**If you're a parent**: Start with Axiom Set 4 & 5 (conflict resolution + audit ritual). That's your transparency guarantee.

**If you're a regulator**: Start with Axiom Sets 6 & 7 (cascading consent + feedback). That's how we stay accountable.

**If you're unsure**: Use the decision tree (Axiom Set 3). It's your roadmap.

---

## Where These Axioms Live

- **This document**: Open-source reference (fork it, cite it, adapt it)
- **Implementation**: `/config/data_axioms.yml` (enforced in code)
- **Enforcement**: Annual audit + ethics board review
- **Updates**: Proposed changes published at `/docs/AXIOM_CHANGES_IN_PROGRESS.md`
- **History**: Archive at `/research/AXIOM_HISTORY.md`

---

## One Final Thing

These axioms exist because one person in a garage said: "My kid deserves infrastructure built for her, not on her."

If LuminAI ever stops living these axioms, it's no longer LuminAI.

It's just another box.

---

**Document Status**: This is v1.0. It's complete enough to ship, honest enough to test, and humble enough to change.

**Last Updated**: November 8, 2025
**Next Review**: November 8, 2026 (or immediately if Tier 2+ breach occurs)
**Maintainer**: TEC Research & Governance Board
