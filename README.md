
## SRC as Crystalline Cosmic Fluid

The scalar field φ is a **compressible cosmic fluid with self-generated interlocking crystalline order** (liquid-crystal / quasicrystal hybrid).

| Feature                     | Physical Analogue                              | SRC Implementation                                                                 |
|-----------------------------|------------------------------------------------|------------------------------------------------------------------------------------|
| **Interlocking lattice**    | Tetrahedral/hexagonal grains that shear but stay locked | Topological term **β/2 |∇φ|⁴** penalises slip between grains → elastic stiffness. |
| **Force transfer**          | Compression waves → gravity-like pull<br>Shear waves → EM-like currents | Linearised equations give two sound speeds: **cₗ** (compression/gravity) and **cₜ** (shear/light). |
| **Vortices = particles**    | Lattice defects/dislocations (stable due to topology) | Hopfion/vortex solutions are defects with winding **W**. |
| **Damping γ**               | Viscous drag                                   | Explicit **γ ∂ₜφ** term. |
| **Axial flow (expansion)**  | Global shear → cosmic expansion                | Uniform background flow drives Hubble-like term. |

**Speed of light**: Photons are transverse shear waves → **c = cₜ = √β** (in natural units where ρ=1). Gravity waves are longitudinal compression at cₗ.

**Bottom line**: Forces propagate as elastic waves through the interlocking crystal-fluid. Vortices (particles) are stable defects. No action at a distance, no separate dark components.

See notebooks in `notebooks/` for quantitative extraction of cₜ, cₗ, vortex statistics, and expansion rate.


## SRC as Crystalline Cosmic Fluid

The scalar field **φ** is interpreted as a **compressible cosmic fluid with self-generated interlocking crystalline order** (liquid-crystal / quasicrystal hybrid).

| Feature                    | Physical analogue                                | SRC implementation                                      |
|----------------------------|--------------------------------------------------|---------------------------------------------------------|
| Interlocking lattice       | Grains that shear but stay locked                | Term **β/2 |∇φ|⁴** penalises slip → elastic stiffness       |
| Force transfer             | Compression waves → gravity<br>Shear waves → light| Linearised equations yield **cₗ** (gravity-like) and **cₜ = √β** (light-like) |
| Particles                  | Topologically stable lattice defects             | Hopfions / vortices with winding number **W**               |
| Damping γ                  | Viscous drag                                     | Explicit **γ ∂ₜφ** term                                     |
| Cosmic expansion           | Global shear flow                                | Uniform background ∇φ drives Hubble-like term           |
| Speed of light             | Transverse shear waves                           | **c = cₜ = √β** (exact in linear regime)                |

**Core idea** – All forces propagate as elastic waves through the interlocking crystal-fluid. Particles are stable topological defects. No action-at-a-distance, no separate dark components.

### Quantitative Evidence: Emergent Speed of Light

Linearised perturbations show that transverse (shear) modes propagate with **exact phase speed cₜ = √β**.

- **Method**: Exact Fourier spectral propagation (no numerical dispersion).
- **Result** (65,384 steps): measured cₜ = 0.01095052 (relative error **0.036%** vs theoretical √β = 0.01095445).
- **Figure**: See `figures/wave_speed_measure.pdf` (clean long-time oscillation + ultra-sharp spectral peak).
- **Code**: Fully reproducible in `scripts/wave_speed_measure.py`.

This sub-0.04% agreement confirms that transverse shear waves propagate at precisely √β, identified as the **emergent speed of light**.

Further details in `docs/wave_speed_explanation.md`.

### Laboratory & Educational Simulations

These scripts provide simple, standalone demonstrations of key SRC concepts using real-world analogs.

- **`scripts/ice_flexo_analog.py`**  
  2D quasi-static simulation of flexoelectricity in a bent water ice slab.  
  Reproduces the large measured flexoelectric coefficient (~1.14 nC/m from Wen et al., *Nature Physics* 2025) using scaled SRC parameters (G_shear, χ-inspired coupling).  
  Features temperature-dependent surface enhancement near the 160 K ferroelectric transition.  
  Dependencies: numpy, matplotlib  
  Run: `python scripts/ice_flexo_analog.py`  
  Example output: [outputs/ice_flexo_T200K.png](outputs/ice_flexo_T200K.png) (or similar)

See also: Technical Manual Section 15.5 for the theoretical context (piezoelectric emergence and ice analog).


