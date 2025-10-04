# TGCR AI Agents

**Version:** v1.37+

This directory contains the AI agents that power The Elidoras Codex. These agents are designed to work with GitHub Copilot and other AI assistants to provide specialized capabilities for documentation, validation, and research.

## Agent Overview

### 📚 Arcadia - Clone & Notebook Agent
**Location:** `arcadia/instructions/`

Arcadia specializes in documentation, knowledge management, and research notebooks. She helps maintain consistency, clone knowledge structures, and organize findings.

**Capabilities:**
- Documentation cloning and replication
- Research notebook creation and management
- Knowledge synthesis and organization
- Maintaining codex structure

**Usage:**
```
@arcadia Create a research notebook for [topic]
```

See [arcadia/instructions/README.md](arcadia/instructions/README.md) for full documentation.

### 🛡️ Airth - Research Guard Agent
**Location:** `airth/instructions/`

Airth is the quality assurance and validation specialist. He guards against hallucinations, validates research claims, and ensures scientific rigor across all TGCR work.

**Capabilities:**
- Research validation and fact-checking
- Hallucination detection
- Methodology review
- Quality assurance

**Usage:**
```
@airth Validate this research claim: [claim]
```

See [airth/instructions/README.md](airth/instructions/README.md) for full documentation.

## Working with Agents

### Prerequisites
- VS Code with GitHub Copilot
- Agent instructions loaded
- Understanding of TGCR context

### Best Practices

1. **Choose the Right Agent**
   - Use Arcadia for documentation tasks
   - Use Airth for validation and quality checks

2. **Provide Context**
   - Reference relevant files and documents
   - Explain the broader goal
   - Share existing work

3. **Be Specific**
   - Clear, detailed requests
   - Include examples when helpful
   - Specify output format

4. **Iterate**
   - Review agent output
   - Refine requests as needed
   - Build on previous work

5. **Validate**
   - Always submit research to Airth
   - Have Arcadia document important findings
   - Maintain quality standards

## Agent Instructions

Each agent has detailed instructions in their respective directories:

```
agents/
├── arcadia/
│   └── instructions/
│       ├── README.md                      # Main instructions
│       └── arcadia_clone_notebook.md      # Cloning template
└── airth/
    └── instructions/
        ├── README.md                      # Main instructions
        └── airth_research_guard_notebook.md  # Validation template
```

## Collaboration Patterns

### Documentation Workflow
```
1. Create content
2. @arcadia Document and structure this
3. @airth Validate the claims
4. Revise based on feedback
5. Finalize and publish
```

### Research Workflow
```
1. Formulate hypothesis
2. Collect data/evidence
3. @airth Validate methodology
4. Conduct investigation
5. @arcadia Create research notebook
6. @airth Final validation
7. Publish findings
```

### Development Workflow
```
1. Write code
2. Test functionality
3. @arcadia Document the code
4. @airth Review technical claims
5. Commit changes
```

## Creating New Agents

Want to add a new agent to TGCR? Follow these steps:

1. **Define Role**
   - What specific capability does this agent provide?
   - How does it complement existing agents?

2. **Create Directory Structure**
   ```
   agents/
   └── [agent-name]/
       └── instructions/
           └── README.md
   ```

3. **Write Instructions**
   - Clear role definition
   - Specific capabilities
   - Usage examples
   - Integration guidelines

4. **Test Integration**
   - Verify with GitHub Copilot
   - Test collaboration patterns
   - Document results

5. **Update Documentation**
   - Add to this README
   - Update root README
   - Create issue templates if needed

## Prompt Templates

For working with agents, see:
- [Prompt Templates](../prompts/templates.md)
- Agent-specific instructions in each directory
- Examples in research notebooks

## Integration with TGCR

Agents integrate with:
- **Applications:** Validate features, document APIs
- **Research:** Guard quality, maintain notebooks
- **Infrastructure:** Review workflows, ensure standards
- **Documentation:** Maintain consistency, clone content

## Support

For agent-related questions:
- Check agent instructions first
- Review prompt templates
- Open an issue with relevant label:
  - `agent:arcadia` for Arcadia questions
  - `agent:airth` for Airth questions
  - `agent:general` for agent system questions

## Resources

- [VS Code Settings](../.vscode/settings.json) - Optimized for agent work
- [TGCR Manifesto](../docs/tgcr_manifesto.md) - Agent philosophy
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute

---

**Version:** v1.37+ | **Last Updated:** 2025-01-15

*"Agents are partners in the pursuit of knowledge."*
