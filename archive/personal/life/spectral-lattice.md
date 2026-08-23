# Spectral Lattice — Two-Channel Processing

## Design

Each lattice site carries two coupled oscillatory channels:

- **Channel 0 (Fast)** — Signal / Carrier: Responds quickly to external gradients
- **Channel 1 (Slow)** — Memory / Modulator: Accumulates history and gates the fast channel

## Cross-Gating Rule

$$
G(C) = 0.2 + 0.8 \cdot C^2
$$

Coupling strength of the fast channel increases nonlinearly when the slow channel is coherent.

## Emergent Capabilities

- Context-dependent signal propagation
- Hysteresis and rudimentary learning
- Adaptation: repeated stimuli alter gating behavior
- Distributed processing via defect-line mixing

This provides the mechanical seed for memory, attention, and simple adaptation entirely within φ.
