## Mathematical substrate — DFM Finite-Gap Engine

Exact-algebraic realization of the Dynamic Fluid Medium (dark-aether) as finite-gap solutions on the Sato Grassmannian. No spatial grid: the state is a period matrix Ω, phase vector Z, and frequency matrix U; observables (potential, current, shear) are recovered from logarithmic derivatives of the Riemann theta function.

**Headline result.** A measured adiabatic validity condition

```
|Ω̇| / (|U| · |Im Ω|)  ≪  0.05
```

extracted from a path-dependent residual sweep against a counterfactual twin — the engine’s first falsifiable bound, not an assumed one.

**Run the demos** (pure NumPy / SciPy):

```bash
python -m dfm_engine.test_cnoidal       # unit test (periodicity ~1e-15)
python -m dfm_engine.demo_capture       # Terminal Capture + decay envelope
python -m dfm_engine.demo_adiabatic     # solar-driven Ω(t) drift
python -m dfm_engine.demo_interference  # capture interleaved with drift + ε sweep
python -m dfm_engine.demo_chart         # toroidal 3-D shear eigenvalues
```

Full geometry, measured numbers, honesty caveats, and API:  
→ [`dfm_engine/README.md`](dfm_engine/README.md)
