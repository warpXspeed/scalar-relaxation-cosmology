# Autocatalytic Molecular Overlay

## Species

- **S0**: Boundary stabilizer (lipid-like) — promotes compartmentalization
- **S1**: Catalyst — enhances resonant modes
- **S2**: Resource carrier — couples to external gradients

## Dynamics

Formation rate of species *s* is biased by local coherence:

$$
\frac{dM_s}{dt} = \kappa_s \cdot C_{k_s}^2 \cdot \left( \sum_r \alpha_{sr} M_r \right) - \delta_s (1 + \gamma D_{\rm total}) M_s
$$

Molecular concentrations feed back into lattice parameters (stiffness and nonlinearity), closing the loop:

**Coherence → Chemistry → Lattice modification → Coherence**

This creates heritable compositional states that bias future behavior.
