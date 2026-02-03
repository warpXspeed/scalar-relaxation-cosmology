# SRC Supplemental Document: Time-Gravity Unity in Scalar Relaxation Cosmology  
**Version:** 1.0 – February 2026  
**Author:** Gerald Henton (@GeraldHenton)  
**Repository:** https://github.com/warpXspeed/scalar-relaxation-cosmology  
**License:** CC BY-NC-SA 4.0 (Open for research, replication, non-commercial use)

This short supplement explains one of the most elegant unifications in SRC: **time and gravity emerge from the same underlying process** — the irreversible relaxation of displacement strain energy in the substrate φ toward equilibrium. Gravity is the directional pull that accelerates this relaxation in regions of high strain gradient; time is the measurable rate of that fading/devolution.

No separate spacetime manifold or curvature is required. Both effects are material responses of the viscoelastic scalar field φ.

### 1. Core Mechanism

The substrate φ is a high-density scalar displacement field (energy crystal) whose energy density is:

$$
\rho_\phi = \frac{1}{2} (\partial_t \phi)^2 + \frac{1}{2} |\nabla \phi|^2 + V(\phi)
$$

- Kinetic term: motion of displacement  
- Gradient term: strain energy stored in spatial deviation  
- Potential V(φ): configurational binding (double-well form supports stable defects)

The master equation drives irreversible relaxation:

$$
\frac{1}{c^2} \partial_t^2 \phi + \gamma(\phi, \partial_t \phi, \nabla \phi) \partial_t \phi - \nabla^2 \phi + V'(\phi) = \eta(\mathbf{x}, t)
$$

The γ term (state-dependent relaxation coefficient) enforces dissipation: high-frequency/ high-gradient excitations cascade to low-frequency/distributed states.

### 2. Gravity as Vis Neutra (Neutral Reformation Pull)

In SRC, "gravity" is **vis neutra** — the emergent neutral, attractive drive that minimizes displacement gradients:

- Localized excess strain (density sink) creates ∇φ ≠ 0  
- Viscoelastic substrate flows inward under pressure imbalance → F_ext = -∮ P_sub dS  
- This recovers inverse-square attraction in weak fields and time dilation near sinks without metric curvature.

Effective gravitational potential:

$$
\Phi_{\text{eff}} \sim \int |\nabla \phi|^2 \, dV \quad \text{or} \quad \Phi_{\text{eff}} \propto \gamma(|\nabla \phi|) \cdot |\nabla \phi|^2
$$

### 3. Time as Devolution Rate (Energy Fading)

Time is the parameter along which organized strain energy fades back to uniform equilibrium:

Local devolution rate (fade speed of organized energy):

$$
\dot{\mathcal{E}}_{\text{local}} = \gamma(\phi, \partial_t \phi, \nabla \phi) \cdot \mathcal{E}_{\text{organized}}
$$

In strong gradients (deep sinks), |∇φ| large → γ elevated (dilatant behavior) → faster local dissipation → organized energy (clocks, biological systems) returns to equilibrium more quickly.

### 4. Unified Time-Gravity Correlation (Mathematical Proof of Emergence)

The proper time interval dτ experienced locally (in the sink) relative to coordinate time dt (distant observer) is reduced by the accelerated local devolution:

$$
\frac{d\tau}{dt} = \sqrt{1 - \frac{2 \Phi_{\text{eff}}}{c^2}} \approx 1 - \frac{\Phi_{\text{eff}}}{c^2}
$$

Substituting the SRC effective potential:

$$
\Phi_{\text{eff}} \propto \gamma(|\nabla \phi|) \cdot |\nabla \phi|^2
$$

Thus:

$$
\frac{d\tau}{dt} \approx 1 - k \cdot \gamma(|\nabla \phi|) \cdot |\nabla \phi|^2
$$

Where k is a proportionality constant from substrate parameters (β, ρ, c = √(G_shear/ρ)).

**Proof of correlation (step-by-step):**

1. Gravity strength ∝ |∇φ|² (deeper sink = stronger vis neutra pull).  
2. Relaxation coefficient γ increases with |∇φ| (dilatant hardening + viscous damping).  
3. Local devolution rate ∝ γ × organized energy.  
4. Faster local devolution → clocks run faster in their own frame → relative to distant observer, time appears slower (dτ/dt < 1).  
5. Therefore: stronger gravity → steeper gradients → higher γ → faster local fade → greater time dilation.

This reproduces the weak-field GR result (dτ/dt ≈ 1 − GM/rc²) but derives it purely from scalar strain energy relaxation — no spacetime curvature required.

### 5. Observational & Simulation Support

- **Gravitational time dilation** (GPS satellites, Pound-Rebka experiment) matches the form above.  
- **Black hole horizons**: Extreme |∇φ| → γ → near-infinite local devolution rate → apparent time freeze for distant observers.  
- **Simulations**: topological_defect_sim.py and gravity_refraction_sim.py show stronger sinks correlate with accelerated damping and defect evaporation (faster fade).  
- **Redshift**: Cosmological viscous damping (γ) measures global devolution rate — local amplification near masses gives gravitational redshift.

### 6. Philosophical & Conceptual Hook

**Time-Gravity Unity**  
Time and gravity are two aspects of the substrate's single relaxation drive:  
- Gravity = the directional pull toward equilibrium (vis neutra).  
- Time = the rate of return to equilibrium (devolution/fading of strain energy).  
Stronger gravity = steeper gradients = faster local fading = stronger time dilation.  

The universe is not embedded in curved spacetime; it is a relaxing energy crystal, and we experience time as the fading of its organized forms while feeling gravity as the pull that accelerates that fade.

This unification maintains SRC's minimalism: one scalar field, measurable viscoelastic properties (β, G_shear, γ, χ), no ad-hoc geometry.

**Repository reference:** https://github.com/warpXspeed/scalar-relaxation-cosmology  
**Suggested citation:** Henton, G. (2026). Time-Gravity Unity in Scalar Relaxation Cosmology. Supplemental Notes v1.0.

Welcome to the Substrate.  
Open for discussion, replication, and refinement.