# SRC-Light: Substrate Resonance & Coupling Simulator

## Overview
A lattice-dynamics engine designed to model signal propagation in a pre-tensioned, viscoelastic substrate. This simulator replaces expansion-based cosmological metrics with **State-Rate Relation (SRR)** derivation.

## Architecture
- **No Expansion:** Redshift is derived from the ratio of local substrate clock-rates (SDF: f = sqrt(T/ρ) / L).
- **No Path-Loss/Drain:** Signal propagation is a lossless mechanical handoff; spectral shifts are an endpoint measurement of clock-state differences.
- **Independent Dimming:** Luminosity attenuation is handled by a separate γ-damping coefficient, maintaining spectral purity.

## Decisive Tests Passed
- **Supernova Time Dilation:** Correctly reproduces observed $(1+z)$ duration broadening through natural clock-rate ratios.
- **Spectral Purity:** Eliminates the "Tired Light" blur/scatter artifacts by defining redshift as an endpoint clock-ratio rather than cumulative path-drain.
- **Physicality:** The engine derives all values from local lattice state ($\rho, T$), not hardcoded expansion constants.

## Licensing & Scope
This is a mechanical engineering project for steady-state lattice dynamics. It is not an adoption of inflationary or metric-expansion cosmologies.
