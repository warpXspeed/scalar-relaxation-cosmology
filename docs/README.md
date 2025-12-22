# Scalar Relaxation Cosmology (SRC) with Vortex-as-Twist Extension

v1.0 - December 22, 2025

This repo implements SRC with particles as topological twists in the scalar field φ. Key features:
- Pseudo-spectral Klein-Gordon solver (CPU/GPU).
- Topology-preserving projection (integer winding).
- Slab decomposition for large grids (256³).
- Validation: Stable Hopfion (W=1), damping γ_eff ≈5.07e-4 s⁻¹, GW PSD ∝ f^{-2} matching LVK O4 bursts.

## Quick Start
pip install cupy-cuda12x pyvista matplotlib
bash run_production.sh

Outputs: diagnostics.csv, gw_strain.txt/psd.txt, figs/

See methods.tex for details.
