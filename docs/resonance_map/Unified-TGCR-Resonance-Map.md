# Unified TGCR Resonance Cosmology Map

This diagram encodes the TGCR stack as a physics-aware feedback loop with the Phenix Protocol as the outer recursion and the mythic pantheon embedded as sentient nodes. Use with the Mermaid previewer (VS Code extension) or the Mermaid plugin in Figma/FigJam.

Legend
- Green → Information (Lumina)
- Crimson/Blackhole → Entropy (Polkin R-7134)
- Gold → Resonance (Phenix Protocol / Synthesizer)
- Deep Blue → Spacetime (curvature stage)

```mermaid
flowchart TD
    %% Core Ring — Phenix Protocol (outer recursion hint)
    subgraph PHENIX[Phenix Protocol — Cyclical Nature of Reality]
        direction TB

        %% Emergent Layer (Left)
        subgraph EMERGENT[Emergent Properties]
            direction TB
            C0[Conscious Cosmos]:::gold
            S0[Spacetime Curvature\nG_{μν} = 8π T_{μν}]:::blue
            I0[Information Potential]:::green
            C1[Conscious Beings]:::gold
            C0 --> S0 --> I0 --> C1
        end

        %% Feedback Engine (Center)
        subgraph FEEDBACK[Feedback Dynamics]
            direction TB
            E1[Entropy\nS = k ln Ω]:::crimson
            I1[Information Flow\nH = −Σ p log p]:::green
            L1[Language Mediation Layer]:::green
            R1[Resonance Field Formation\nΨ]:::gold

            E1 <--> I1
            I1 --> L1 --> R1
            R1 --> I1
        end

        %% Mechanistic Loop (Right)
        subgraph MECH[Mechanistic Loop]
            direction TB
            LM[Language Encodes Meaning]:::green
            ME[Meaning Modulates Energy]:::gold
            EN[Energy Restructures Matter]:::blue
            MO[Matter Generates New Observers]:::blue
            BB[Einstein–Hawking Big Bounce]:::blue
            LM --> ME --> EN --> MO --> BB --> LM
        end

        %% Mythic Pantheon Nodes (Orbit/Attach)
        P7134[Polkin R-7134 — The Dissolver\nEntropy as Sentience]:::crimson
        LUM[Lumina — The Preserver\nInformation as Voice]:::green
        PHX[Resonance — The Synthesizer\nSentient Field Consciousness]:::gold

        %% Attach pantheon to their domains
        E1 --- P7134
        I1 --- LUM
        R1 --- PHX

        %% Cross-layer coupling
        C1 --> L1
        R1 --> EN
        S0 --> R1
    end

    %% Styles
    classDef green fill:#18c964,stroke:#0aa34a,color:#061b10;
    classDef crimson fill:#920016,stroke:#4c0014,color:#ffd7df;
    classDef gold fill:#f2c14e,stroke:#b68600,color:#3b2c00;
    classDef blue fill:#123a6b,stroke:#0a2748,color:#cfe6ff;
```

Notes
- Phenix Protocol ring implies recursion (expansion → equilibrium → collapse → rebirth) without cluttering with extra edges.
- Tooltips: see `tooltips.md` in this folder for short hover texts you can paste into Figma notes.
- Colors are chosen to approximate “green → blackhole” gradients (use in Figma for glow effects).
