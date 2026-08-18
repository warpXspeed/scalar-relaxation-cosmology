# Scalar Relaxation Cosmology: Theory Overview

## 1. The Eternal Scalar Field
The foundation is an eternal real/complex scalar field φ(x, t), governed by relaxation dynamics. No creation event—the field has always existed [1].

## 2. Relaxation Dynamics

∂²φ/∂t² + γ ∂φ/∂t - c² ∇²φ + λ (φ² - v²)² + ε φ = 0 [1][6]

- γ > 0: Damping (gravity emergence) [6].
- λ: Nonlinearity for soliton stability.
- ε: Tiny tilt for asymmetry.
Cosmic expansion: Wave spreading and damping, redshift from energy loss. Simulation example: A 1D Gaussian initial disturbance damps and flattens over t=10 units (code in `src/simulation_example.py`; see `kg_damping_plot.png` for ~50% amplitude reduction, spreading by factor of 2) [6].

## 3. Particles as Vortices/Toroids
Subatomic particles: Topological defects in φ (or complex ψ) [1].
- Electron/photon: Toroidal vortex [11, 14].
  - Spin (azimuthal): Electric field divergence.
  - Axial flow (pole-to-pole): Magnetic field curl.
- Mass: Bound energy E = ∫ |∇φ|² dV ≈ ħ c / R (R = major radius, derivable from topology) [1].
- E=mc²: Unwinding (radiation) or spinning up (matter).

## 4. Forces as Emergent Resonances
- Gravity: Sympathetic alignment of vortices (amplifies damping) [1].
- EM: Toroidal mode (detailed in toroidal EM section) [1].
- Strong/Weak: Higher windings/asymmetries (future: derive quark masses via multi-vortex bindings).

## 5. Unification and Resolutions
See README for how SRC bypasses singularities, dark sectors, etc. [1].

## 6. Quantum Aspects
- Wavefunction: Vortex phase θ [1].
- Collapse: Damping to minimum energy state [1].
- Entanglement: Shared topological windings [1].
