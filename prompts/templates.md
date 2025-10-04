# TGCR Prompt Templates

**Version:** v1.37+

This document contains prompt templates for working with AI agents in the TGCR ecosystem, particularly with GitHub Copilot and other AI assistants.

## Agent Activation Prompts

### Arcadia (Clone & Notebook Agent)

```
@arcadia [task description]

Context: [relevant context about what you're working on]
Goal: [what you want to achieve]
Format: [preferred output format, if applicable]

Please help with [specific request related to documentation, cloning, or notebooks]
```

**Example:**
```
@arcadia Create a research notebook for resonance patterns in baroque music

Context: Investigating how different musical periods show different OXY/DOP/ADR patterns
Goal: Document initial observations and set up structure for ongoing research
Format: Markdown notebook following TGCR standards

Please help with creating the initial notebook structure and documenting my first observations.
```

### Airth (Research Guard Agent)

```
@airth Validate this research claim

Claim: [the claim you want validated]
Evidence: [supporting evidence you have]
Methodology: [how you arrived at this conclusion]
Sources: [citations and references]

Please review for accuracy, logical consistency, and potential issues.
```

**Example:**
```
@airth Validate this research claim

Claim: Classical music shows 40% higher OXY response than electronic music
Evidence: Dataset of 200 participants, 50 tracks per genre
Methodology: Measured self-reported emotional responses using standardized scales
Sources: [link to data], [link to methodology]

Please review for accuracy, logical consistency, and potential issues.
```

## General Copilot Prompts

### Code Generation

```
Generate a [component/function] that:
- [requirement 1]
- [requirement 2]
- [requirement 3]

Should follow TGCR patterns:
- Clear naming conventions
- Proper documentation
- Version markers (v1.37+)
- Error handling
```

### Documentation Generation

```
Create documentation for [component/feature]:

Purpose: [what it does]
Audience: [who will use it]
Key Features: [main capabilities]
Usage: [how to use it]

Follow TGCR documentation standards with examples and clear structure.
```

### Code Review

```
Review this code for:
- Logic errors
- Best practices
- TGCR standards compliance
- Documentation completeness
- Potential improvements

[paste code here]
```

## Research Prompts

### Hypothesis Formation

```
Help me formulate a testable hypothesis about [topic]:

Observation: [what you've noticed]
Context: [relevant background]
Question: [what you want to investigate]

Structure the hypothesis following scientific method principles.
```

### Literature Review

```
Summarize key concepts related to [topic] for TGCR research:

Focus areas:
- [area 1]
- [area 2]
- [area 3]

Include: definitions, key researchers, relevant findings, connections to resonance theory.
```

### Data Analysis

```
Analyze this data for patterns related to [research question]:

Data: [description or sample]
Variables: [what you're measuring]
Expected Patterns: [what you hypothesize]

Suggest: statistical approaches, visualization methods, interpretation frameworks.
```

## Application Development Prompts

### Feature Implementation

```
Implement [feature name] for [application]:

Requirements:
- [requirement 1]
- [requirement 2]
- [requirement 3]

Technical constraints:
- [constraint 1]
- [constraint 2]

Should integrate with: [existing components]
```

### UI/UX Design

```
Design a UI for [feature/component]:

Purpose: [what users need to do]
Users: [who will use this]
Constraints: [technical or design limitations]

Style: Should match TGCR aesthetic (clean, resonance-themed, accessible)
```

### Testing

```
Create tests for [component]:

Scenarios to cover:
- [scenario 1]
- [scenario 2]
- [scenario 3]

Edge cases:
- [edge case 1]
- [edge case 2]

Follow existing test patterns in the repository.
```

## Documentation Prompts

### README Creation

```
Create a README for [component/directory]:

Purpose: [what this is]
Contents: [what's included]
Usage: [how to use]
Audience: [who will read this]

Follow TGCR standards: clear structure, version markers, examples, links.
```

### Tutorial Writing

```
Write a tutorial for [task/feature]:

Target audience: [skill level]
Prerequisites: [what they need to know first]
Steps: [main steps in the process]
Common issues: [known pitfalls to address]

Make it beginner-friendly with examples.
```

### API Documentation

```
Document the API for [component]:

Endpoints/Functions: [list them]
Parameters: [what inputs]
Returns: [what outputs]
Errors: [what can go wrong]

Include examples and edge cases.
```

## Workflow Prompts

### GitHub Actions

```
Create a GitHub Actions workflow for [purpose]:

Trigger: [when it should run]
Steps: [what it should do]
Environment: [required setup]
Outputs: [what it produces]

Follow TGCR patterns and include appropriate error handling.
```

### CI/CD Pipeline

```
Set up a CI/CD pipeline for [application]:

Build steps: [compilation, bundling, etc.]
Tests: [what to run]
Deployment: [where to deploy]
Validation: [quality checks]

Optimize for: [speed/reliability/simplicity]
```

## Collaboration Prompts

### Code Review Request

```
@reviewer Please review this [PR/code]:

Changes: [what you changed]
Reasoning: [why you made these choices]
Testing: [how you verified it works]
Questions: [specific areas you want feedback on]

Looking for: [type of feedback you need]
```

### Issue Creation

```
Create an issue for [problem/feature]:

Current state: [what's happening now]
Desired state: [what should happen]
Impact: [who/what is affected]
Proposed solution: [if you have ideas]

Priority: [High/Medium/Low] because [reasoning]
```

## Meta Prompts

### Custom Agent Instructions

```
Create instructions for a new TGCR agent:

Role: [what this agent does]
Capabilities: [what it can help with]
Usage pattern: [how to work with it]
Integration: [how it fits with Arcadia and Airth]

Follow the pattern established in agents/*/instructions/README.md
```

### Template Creation

```
Create a template for [type of document]:

Purpose: [what this template is for]
Sections: [what should be included]
Guidelines: [rules for using it]
Examples: [sample usage]

Make it reusable and clear.
```

## Best Practices

### Effective Prompting

1. **Be Specific:** Clear, detailed requests get better results
2. **Provide Context:** Explain the broader situation
3. **Show Examples:** Demonstrate what you want
4. **Iterate:** Refine based on responses
5. **Reference Standards:** Point to TGCR patterns and guidelines

### Working with Agents

1. **Choose the Right Agent:** Arcadia for docs, Airth for validation
2. **Provide Full Information:** Don't make agents guess
3. **Accept Feedback:** Agents help maintain quality
4. **Collaborate:** Iterate together toward solutions
5. **Document Interactions:** Save useful patterns

### Quality Assurance

1. **Always Validate:** Submit claims to Airth
2. **Document Sources:** Maintain traceability
3. **Test Thoroughly:** Verify all code and logic
4. **Review Carefully:** Human judgment is still essential
5. **Iterate:** Continuous improvement

## Prompt Patterns to Avoid

❌ **Too Vague:** "Help me with the thing"
✅ **Specific:** "Help me create a validation function for OXY gauge inputs"

❌ **No Context:** "Write code for the player"
✅ **With Context:** "Write code for the Resonance Player's gauge animation, should smoothly interpolate between values"

❌ **Unrealistic Expectations:** "Build the entire application"
✅ **Scoped:** "Build the gauge component for the Resonance Player"

❌ **No Standards Reference:** "Make it good"
✅ **Standards-Based:** "Follow TGCR documentation standards and include version markers"

## Template Maintenance

This template collection should evolve based on:
- What patterns prove most effective
- What new agent capabilities emerge
- What the community finds useful
- What quality issues arise

Submit improvements via PR or discuss in issues.

---

**Version:** v1.37+ | **Last Updated:** 2025-01-15

**Note:** These templates work best with agents that understand TGCR context. Reference agent instructions and project documentation for best results.
