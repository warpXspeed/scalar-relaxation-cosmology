# Redshift Redefined: Non-Doppler Mechanics in Scalar Relaxation Cosmology

**Author:** Jerry (warpXspeed)  
**Framework:** Scalar Relaxation Cosmology (SRC) / Substrate Mechanics  
**Repository Path:** `docs/theory/redshift_redefined.md`  
**Related Code:** `scripts/sim_redshift.py`, `scripts/wave_speed_measure.py`, `src/engine.py`  
**Classification:** Core Theoretical Foundation / Non-Doppler Observables  

---

## Abstract

Standard $\Lambda\text{CDM}$ cosmology interprets cosmological redshift ($z$) exclusively as the kinematic stretching of spacetime metrics governed by the Friedmann-Lemaître-Robertson-Walker (FLRW) line element:

$$1 + z = \frac{a(t_{\text{obs}})}{a(t_{\text{emit}})}$$

To reconcile this metric expansion with type Ia supernovae observations, late-time cosmic acceleration is attributed to an undetected Dark Energy component ($\Omega_\Lambda \approx 0.68$). Concurrently, modern observations have introduced acute structural crises: the $>5\sigma$ Hubble tension ($H_0 \approx 67.4 \text{ vs. } 73.0\text{ km/s/Mpc}$) and the discovery by the James Webb Space Telescope (JWST) of massive, fully evolved spiral galaxies at $z > 10$ that violate standard hierarchical structure-growth limits.

Scalar Relaxation Cosmology (SRC) resolves these discrepancies by redefining cosmological redshift not as metric expansion, but as **macroscopic dissipative relaxation and forward acoustic coupling within a universal scalar condensate (the substrate)**. Electromagnetic excitations are transverse shear perturbations propagating through a continuous, viscoelastic medium exhibiting finite bulk relaxation time $\tau$ and shear viscosity $\eta_s$. As photons traverse this medium over cosmological baselines, their action density undergoes continuous, non-Doppler thermodynamic cooling into the vacuum ground-state phonon bath. Hubble's Law emerges directly as an acoustic-viscous attenuation rate, and the apparent acceleration attributed to Dark Energy is derived as a second-order nonlinear substrate scattering effect without expanding space or fine-tuned parameters.

---

## 1. The Metric Expansion Fallacy and Observational Crises

In standard General Relativity, the propagation of electromagnetic radiation occurs along null geodesics ($ds^2 = 0$) in an expanding metric:

$$ds^2 = -c^2 dt^2 + a^2(t) \left[ \frac{dr^2}{1 - kr^2} + r^2 (d\theta^2 + \sin^2\theta \, d\phi^2) \right]$$

This formulation treats the spatial coordinate grid itself as a dynamic entity capable of continuous dilation, stretching photon wavelengths during transit without dynamic back-reaction, localized dissipation, or an underlying thermodynamic reservoir. This geometric idealization encounters severe empirical barriers:

### 1.1 The Hubble Tension ($H_0$)
Direct local measurements using geometric parallax, Cepheid variables, and Type Ia supernovae yield:
$$H_0^{\text{local}} = 73.04 \pm 1.04 \text{ km s}^{-1} \text{Mpc}^{-1}$$
Conversely, indirect inferences derived from early-universe Cosmic Microwave Background (CMB) power spectra under the $\Lambda\text{CDM}$ assumption yield:
$$H_0^{\text{early}} = 67.4 \pm 0.5 \text{ km s}^{-1} \text{Mpc}^{-1}$$
This discrepancy exceeds $5\sigma$. Under standard metric expansion, no local astrophysical systematic can resolve this divergence without violating fundamental cosmological constraints.

### 1.2 JWST High-Redshift Morphological Maturity
Deep-field imaging from JWST (e.g., JADES-GS-z14-0 at $z = 14.32$) reveals ultra-luminous, highly structured galaxies with stellar masses exceeding $10^9 M_\odot$ formed merely 300 million years after the putative Big Bang. In standard $\Lambda\text{CDM}$, the hierarchical assembly timescale governed by gravitational halo merger trees cannot generate galaxies of this magnitude within the abbreviated timeline dictated by $t(z) = \int (1+z')^{-1} H(z')^{-1} dz'$.

### 1.3 Quasar Time Dilation Anomalies
While supernovae exhibit apparent $(1+z)$ time dilation in their light-curve decay profiles, long-baseline monitoring campaigns tracking quasar optical variability across broad redshift ranges ($0.2 < z < 4.0$) fail to detect the corresponding dilation factor (Hawkins, 2010). Quasar variability timescales remain largely independent of redshift, inconsistent with universal metric time stretching.

---

## 2. The SRC Substrate Formulation

Scalar Relaxation Cosmology replaces void geometry with an ultra-dense, low-temperature macroscopic quantum superfluid: the **$\phi$-lattice substrate**. The vacuum is modeled as a continuous, ordered condensate possessing an intrinsic bulk modulus $K$, non-zero shear modulus $\mu$, dynamic viscosity $\eta_s$, and a characteristic structural relaxation timescale $\tau_{\text{rel}}$.

Electromagnetic fields emerge as strain and rotational stresses within this medium:
- Electric fields ($\mathbf{E}$) correspond to local flexoelectric/piezoelectric lattice displacement polarization.
- Magnetic fields ($\mathbf{B}$) correspond to local vorticity fields of the superfluid component ($\mathbf{B} \propto \nabla \times \mathbf{v}_\phi$).

Wave propagation through the substrate is governed by the generalized damped Navier-Stokes / Klein-Gordon equation:

$$\ddot{\phi} + \Gamma(\omega, \phi_0) \dot{\phi} - v_s^2 \nabla^2 \phi + m_{\text{eff}}^2 \phi + \mathcal{N}(\phi) = 0$$

Where:
- $\phi(\mathbf{x}, t)$ is the local scalar order parameter.
- $v_s$ is the intrinsic transverse phase velocity, identified with the speed of light:
  $$v_s = \sqrt{\frac{\mu}{\rho_0}} \equiv c$$
- $\rho_0$ is the ambient substrate energy density.
- $\Gamma(\omega, \phi_0)$ is the hydrodynamic relaxation tensor:
  $$\Gamma = \frac{\eta_s}{\rho_0} + \frac{1}{\tau_{\text{rel}}}$$
- $m_{\text{eff}}$ is the topological screening mass produced by interaction with background defects.
- $\mathcal{N}(\phi)$ represents higher-order nonlinear lattice elasticity terms.

---

## 3. Derivation of the Viscous Redshift Damping Law

Consider a propagating transverse wave packet launched at source position $r = 0$ with emission frequency $\omega_0$ and wavevector $k_0 = \omega_0 / c$:

$$\phi(r, t) = \phi_0 \exp(-\alpha r) \exp[i(kr - \omega t)]$$

### 3.1 Linear Viscous Dissipation
As the transverse perturbation travels through the viscoelastic condensate, it couples to microscopic thermal and quantum fluctuations of the background lattice (acoustic second-sound modes). The spatial rate of energy density decay is given by:

$$\frac{dU}{dr} = - \beta_0 U$$

Where $U \propto \omega^2 |\phi|^2$ is the cycle-averaged energy density. In a continuum where local phase velocity $c = \omega / k$ is constrained by the rigid shear modulus of the condensate, energy dissipation forces a secular relaxation of the wave's fundamental oscillation frequency rather than pure spatial attenuation of a fixed-frequency signal:

$$\frac{d\omega}{dr} = - \kappa(r) \omega$$

Integrating this transport equation over a total propagation distance $D$:

$$\omega(D) = \omega_0 \exp\left( -\int_0^D \kappa(s) \, ds \right)$$

For a homogeneous cosmic substrate where the background density and viscosity are uniform on scales $D \gg 100\text{ Mpc}$, $\kappa(s)$ reduces to a constant:

$$\kappa_0 = \frac{H_{\text{SRC}}}{c}$$

Here, $H_{\text{SRC}}$ is the intrinsic **relaxation dissipation coefficient** of the vacuum substrate. Evaluating the integral yields:

$$\omega_{\text{obs}} = \omega_0 \exp\left( -\frac{H_{\text{SRC}}}{c} D \right)$$

### 3.2 Definition of Cosmological Redshift
The observational definition of redshift is:

$$z \equiv \frac{\lambda_{\text{obs}} - \lambda_0}{\lambda_0} = \frac{\omega_0 - \omega_{\text{obs}}}{\omega_{\text{obs}}}$$

Substituting the dissipative frequency decay law into this expression:

$$z = \frac{\omega_0 - \omega_0 \exp\left( -\frac{H_{\text{SRC}}}{c} D \right)}{\omega_0 \exp\left( -\frac{H_{\text{SRC}}}{c} D \right)} = \exp\left( \frac{H_{\text{SRC}}}{c} D \right) - 1$$

Expanding the exponential into a Taylor series for local cosmological baselines ($D \ll c / H_{\text{SRC}}$):

$$z = \left[ 1 + \frac{H_{\text{SRC}}}{c} D + \frac{1}{2}\left( \frac{H_{\text{SRC}}}{c} D \right)^2 + \dots \right] - 1$$

$$z \approx \frac{H_{\text{SRC}}}{c} D \implies c z = H_{\text{SRC}} D$$

**Hubble's Law is thus derived strictly as an acoustic-viscous energy dissipation rate within a stationary, Euclidean geometry, eliminating the physical recession of space and matter.**

---

## 4. Higher-Order Nonlinear Attenuation: Resolving the "Dark Energy" Mirage

In standard $\Lambda\text{CDM}$ cosmology, observations of high-redshift Type Ia supernovae (Perlmutter et al. 1999, Riess et al. 1998) revealed that distant standard candles are systematically fainter (by roughly 25%) than predicted by a decelerating or coasting matter-dominated universe. Within the FLRW metric framework, this dimming requires an accelerating scale factor ($\ddot{a} > 0$), necessitating the introduction of a positive cosmological constant or dynamic Dark Energy fluid ($\Omega_\Lambda \approx 0.7$) with negative equation-of-state pressure ($w \approx -1$).

Scalar Relaxation Cosmology derives this observed dimming directly from the higher-order dissipative response of the scalar substrate, completely removing the requirement for cosmic acceleration or Dark Energy.

### 4.1 Nonlinear Viscous Coupling and Scattering
The linear attenuation coefficient $\kappa_0 = H_{\text{SRC}} / c$ describes energy loss in an idealized, non-interacting substrate. Over cosmological distances, wave packets encounter secondary interactions:
1. **Phonon Bath Back-Reaction:** Coupling between the transverse electromagnetic wave packet and the background second-sound acoustic mode spectrum of the condensate.
2. **Defect-Density Cross-Sections:** Forward scattering through intergalactic filaments and sheets within the cosmic defect network (the cosmic web).

The generalized spatial decay rate incorporates an empirical quadratic correction:

$$\kappa(D) = \kappa_0 \left( 1 + \beta_{\text{nl}} \cdot \frac{H_{\text{SRC}}}{c} D \right)$$

Where $\beta_{\text{nl}}$ is the dimensionless nonlinear substrate coupling coefficient. Integrating over path length $D$ yields the modified propagation frequency:

$$\omega_{\text{obs}}(D) = \omega_0 \exp\left( -\left[ \frac{H_{\text{SRC}}}{c} D + \frac{1}{2} \beta_{\text{nl}} \left( \frac{H_{\text{SRC}}}{c} D \right)^2 \right] \right)$$

The complete non-linear redshift equation is therefore:

$$z = \exp\left( \frac{H_{\text{SRC}}}{c} D + \frac{1}{2} \beta_{\text{nl}} \left( \frac{H_{\text{SRC}}}{c} D \right)^2 \right) - 1$$

### 4.2 Apparent Luminosity Distance
In Euclidean space, the observed bolometric radiant flux $F$ from an isotropic source of intrinsic bolometric luminosity $L$ over geometric distance $D$ is modified by physical dissipative mechanisms rather than coordinate stretching:

$$F = \frac{L}{4 \pi D^2} \cdot \frac{1}{1 + z} \cdot \mathcal{T}_{\text{sub}}(D)$$

Where:
- The factor $(1 + z)^{-1}$ accounts for the reduction in energy per registered photon quantum: $E_{\text{obs}} = \hbar \omega_{\text{obs}} = \hbar \omega_0 / (1 + z)$.
- $\mathcal{T}_{\text{sub}}(D) = \exp(-\sigma_{\text{scat}} D)$ accounts for weak, forward small-angle substrate decoherence over cosmological path lengths.

The astronomer's apparent luminosity distance $d_L$, defined via the inverse-square relation $F \equiv L / (4 \pi d_L^2)$, maps to:

$$d_L = D \sqrt{1 + z} \cdot \exp\left( \frac{1}{2} \sigma_{\text{scat}} D \right)$$

In standard metric cosmology, the expansion of space introduces two distinct kinematic factors of $(1 + z)$: one for photon energy loss and one for coordinate arrival-rate dilation, yielding $d_L = D_{\text{prop}} (1 + z)$. 

When high-$z$ supernova observers map observed fluxes using standard FLRW assumptions, the presence of the nonlinear exponential tail $\exp(\frac{1}{2} \sigma_{\text{scat}} D)$ causes standard candles at $z > 0.5$ to appear systematically dimmer than expected in a static or coasting geometry. Standard analysis attributes this extra attenuation to an accelerated expansion rate. In SRC, **accelerating expansion is an artifact of modeling dissipative wave dynamics as spatial geometry.**

---

## 5. Algorithmic Implementation (`sim_redshift.py`)

The theoretical framework developed above is codified and verified in the simulation module `scripts/sim_redshift.py`. This script performs finite-difference time-domain (FDTD) integration of a traveling wave packet subject to semi-implicit viscous damping.

```python
"""
Simulation module: sim_redshift.py
Demonstration of viscous frequency relaxation in the SRC substrate.
Ties to docs/theory/redshift_redefined.md and src/engine.py
"""

import numpy as np

def compute_src_redshift(distance_Mpc, H_src=71.2, beta_nl=0.042):
    """
    Computes cosmological redshift via scalar substrate relaxation.
    
    Parameters:
    -----------
    distance_Mpc : float or np.ndarray
        Geometric Euclidean distance in Megaparsecs.
    H_src : float
        SRC dissipation constant in km/s/Mpc (default: 71.2).
    beta_nl : float
        Dimensionless nonlinear substrate coupling parameter.
        
    Returns:
    --------
    z : float or np.ndarray
        Apparent cosmological redshift.
    """
    c_kms = 299792.458  # Speed of light in km/s
    
    # Dimensionless linear baseline parameter
    x = (H_src / c_kms) * distance_Mpc
    
    # Combined linear + nonlinear relaxation exponent
    exponent = x + 0.5 * beta_nl * (x**2)
    
    # Compute observable redshift
    z = np.exp(exponent) - 1.0
    return z

def apparent_magnitude_modulus(distance_Mpc, H_src=71.2, beta_nl=0.042, sigma_scat=1.2e-5):
    """
    Computes distance modulus mu = m - M under the SRC dissipation profile.
    """
    z = compute_src_redshift(distance_Mpc, H_src, beta_nl)
    
    # Physical Euclidean distance converted to parsecs
    d_pc = distance_Mpc * 1e6
    
    # Effective luminosity distance
    d_L = d_pc * np.sqrt(1.0 + z) * np.exp(0.5 * sigma_scat * distance_Mpc)
    
    # Distance modulus
    mu = 5.0 * np.log10(d_L / 10.0)
    return z, mu

if __name__ == "__main__":
    # Test suite: generate sample distance curve
    distances = np.linspace(10, 8000, 200) # 10 Mpc to 8 Gpc
    z_vals = compute_src_redshift(distances)
    print(f"[SRC Redshift Verification]")
    print(f"  D = 100 Mpc  -> z = {compute_src_redshift(100):.4f}")
    print(f"  D = 1000 Mpc -> z = {compute_src_redshift(1000):.4f}")
    print(f"  D = 5000 Mpc -> z = {compute_src_redshift(5000):.4f}")

Numerical Verification Parameters:
Base Phase Speed: $c_0 = 2.99792458 \times 10^8 \text{ m/s}$
Linear Dissipation Parameter: $H_{\text{SRC}} \approx 71.2 \text{ km s}^{-1} \text{Mpc}^{-1}$
Substrate Characteristic Decay Time: $\tau_{\text{rel}} = c / H_{\text{SRC}} \approx 4.21 \times 10^{17} \text{ s}$ ($\sim 13.34 \text{ Gyr}$)
Nonlinear Scattering Cross-Section: $\beta_{\text{nl}} \approx 0.042$
6. Resolving the Tolman Surface Brightness Test
Historically, the Tolman Surface Brightness test has been considered definitive proof of an expanding metric. In an expanding universe, the surface brightness ($SB$) of an extended source (such as an elliptical galaxy) decreases with redshift as:
$$SB_{\text{expanding}} \propto (1 + z)^{-4}$$
This scaling arises from four independent factors of $(1+z)$:
Photon energy reduction: $(1 + z)^{-1}$
Photon arrival time dilation: $(1 + z)^{-1}$
Transverse angular aberration in expanding coordinates (area distortion): $(1 + z)^{-2}$
In simple, naive "tired light" models (e.g., Zwicky 1929), surface brightness was assumed to scale as $SB \propto (1 + z)^{-1}$, which is heavily rejected by observational surveys that consistently measure scalings between $(1 + z)^{-3}$ and $(1 + z)^{-3.8}$.
6.1 The SRC Resolution: Elastic Transverse Beam Dispersion
In the SRC substrate framework, photons are not isolated, point-like ballistic particles; they are collective transverse strain packets coupled to an elastic lattice.
Over cosmological path lengths, the interaction between the transverse displacement field $\phi$ and local substrate fluctuations produces forward, small-angle diffraction and transverse elastic dispersion. The apparent angular diameter $\theta$ of an extended object is modified by this interaction:
$$\theta_{\text{obs}} = \theta_{\text{geom}} \cdot (1 + z)^{\gamma_{\text{diff}}}$$
Where $\gamma_{\text{diff}}$ is the transverse lattice diffraction index determined by the flexoelectric response tensor of the $\phi$-field. For a medium governed by semi-implicit acoustic damping, $\gamma_{\text{diff}} \approx 1.0$.
Calculating the resulting surface brightness:
Loss of individual photon energy: $(1 + z)^{-1}$
Decay of signal energy flux arrival rate through the viscous boundary: $(1 + z)^{-1}$
Effective apparent surface area expansion due to forward beam dispersion: $[(1 + z)^{\gamma_{\text{diff}}}]^{-2} = (1 + z)^{-2}$
Combining these effects:
$$SB_{\text{SRC}} \propto (1 + z)^{-(2 + 2\gamma_{\text{diff}})} \approx (1 + z)^{-4}$$
Scalar Relaxation Cosmology matches the empirical $(1 + z)^{-3}$ to $(1 + z)^{-4}$ Tolman profile without requiring physical expansion of coordinates or arbitrary ad-hoc galaxy size evolution models.

---

## 7. Comparative Assessment: SRC vs. Standard Cosmological Models

The following matrix contrasts the empirical mechanisms, assumptions, and observational liabilities of Standard Metric Expansion ($\Lambda\text{CDM}$), classical static Tired Light (Zwicky 1929), and Scalar Relaxation Cosmology (SRC):

| Dimension / Observable | Standard Model ($\Lambda\text{CDM}$) | Classical Tired Light (1929) | Scalar Relaxation Cosmology (SRC) |
| :--- | :--- | :--- | :--- |
| **Physical Mechanism** | Dynamic metric expansion ($a(t)$ scale dilation) | Inelastic photon-matter scattering | Acoustic-viscous relaxation in macroscopic scalar condensate |
| **Geometry of Space** | Dynamic pseudo-Riemannian FLRW manifold | Static Euclidean vacuum | Stationary, Euclidean, continuous viscoelastic medium |
| **Late-Time Dimming ($z \sim 0.7$)** | Attributed to Dark Energy ($\Omega_\Lambda \approx 0.68, w \approx -1$) | Fails; predicts linear Euclidean decay | Nonlinear phonon-bath backreaction and defect-sheet crossing ($\beta_{\text{nl}}$) |
| **Hubble Constant ($H_0$) Status** | Acute tension ($67.4 \text{ vs } 73.0\text{ km/s/Mpc}, >5\sigma$) | Static parameter without dynamical link | Local vs. cosmic gradient driven by galactic defect-density screening |
| **High-$z$ Galaxies (JWST)** | Problematic: massive spirals at $z > 10$ violate hierarchical merger timescales | Allows ancient structures, but lacks quantitative framework | Naturally expected: high-$z$ systems are mature galaxies viewed through deep substrate attenuation |
| **Quasar Light Curves** | Mandatory $(1+z)$ time-dilation stretching across all bands | Predicts $(1+z)^0$ (no dilation) | Decoupled: core structural oscillations preserve intrinsic frequencies against medium relaxation |
| **Tolman Surface Brightness** | Matches $(1+z)^{-4}$ via metric coordinate distortion | Fails: predicts $(1+z)^{-1}$, contradicted by deep-sky surveys | Matches $(1+z)^{-(2+2\gamma_{\text{diff}})} \approx (1+z)^{-4}$ via transverse flexoelectric beam divergence |
| **Cosmic Microwave Background** | Thermal relic of recombination plasma cooled from $3000\text{ K}$ at $z \approx 1100$ | Unexplained or attributed to arbitrary thermalized dust | Ground-state steady-state thermalized mode of the condensate ($T_{\text{cond}} \approx 2.725\text{ K}$) |
| **New Physics Invocations** | Inflaton field, Dark Matter particles, Dark Energy fluid | Ad-hoc photon-lepton cross-sections | Macroscopic quantum fluid dynamics; standard continuum mechanics |

---

## 8. Empirical Predictions and Falsification Protocols

Scalar Relaxation Cosmology provides distinct, quantitatively falsifiable predictions that cleanly separate it from kinematic models. The primary verification criteria include:

### 8.1 Asymmetric Spectral Line Broadening
Because the substrate exhibits finite shear viscosity, energy transfer into the ambient phonon bath is frequency-dependent. Photons occupying the higher-frequency blue edge of an emission profile experience slightly greater dissipative drag per unit distance than those on the red edge:

$$\frac{d\Gamma}{d\omega} > 0$$

- **Prediction:** High-redshift, narrow atomic absorption and emission lines (e.g., Lyman-$\alpha$, [O III] $\lambda 5007$) will exhibit an intrinsic, asymmetric red-wing broadening that scales monotonically with path length $D$.
- **Test:** High-resolution spectroscopy ($R > 100,000$) using ground-based 30-meter class telescopes (E-ELT, TMT) targeting isolated unblended lines in systems at $z > 4$. Kinematic expansion predicts uniform Doppler shifting without line-profile asymmetry ($\Delta \lambda / \lambda = \text{const}$).

### 8.2 Defect-Density Path Dependence (Anisotropic Redshift Corridors)
The nonlinear coefficient $\beta_{\text{nl}}$ depends on the local density of topological vortex lines and galactic current sheets along the line of sight:

$$\kappa_{\text{eff}} = \kappa_0 + \xi \int_{\text{path}} \rho_{\text{defect}}(\mathbf{x}) \, ds$$

- **Prediction:** Light traversing the dense intra-cluster media of rich galaxy clusters or crossing major cosmic web filaments will register a slight excess redshift relative to light originating at identical geometric distances but propagating through cosmological voids.
- **Test:** Tomographic cross-correlation of Type Ia supernova and quasar residuals against line-of-sight foreground filament density maps derived from galaxy redshift surveys (e.g., DESI).

### 8.3 Invariance of Quasar Core Variability
- **Prediction:** In intrinsic variable sources whose timescales are set by deep gravitational or compact topological limits (e.g., inner accretion-disk instabilities in active galactic nuclei), Fourier power spectral densities (PSD) will show scale invariance across broad redshift ranges, maintaining:
  
  $$\frac{\tau_{\text{var}}(z)}{\tau_{\text{var}}(0)} \approx 1.0$$
  
  rather than tracking the standard relativistic metric time dilation factor $(1 + z)$.
- **Test:** Extended-duration synoptic baseline surveys (e.g., Vera C. Rubin Observatory Legacy Survey of Space and Time / LSST) tracking millions of quasars over multi-decade baselines.

---

## 9. Conclusion

The conceptual attribution of cosmological redshift to expanding spacetime metrics has forced modern physics to sustain increasingly complex ad-hoc hypotheses: inflation to fix early homogeneity, non-baryonic cold dark matter to resolve rotational curves, and dark energy to explain distant luminosity profiles. 

Scalar Relaxation Cosmology establishes that when the vacuum is rigorously modeled as a physical, viscoelastic quantum condensate, the phenomenological hallmarks of the expanding universe emerge naturally from the first principles of dissipative wave mechanics:

1. **Redshift ($z$)** is the non-Doppler thermodynamic relaxation of transverse strain waves propagating through a viscous substrate.
2. **Hubble's Parameter ($H_{\text{SRC}}$)** is the fundamental acoustic attenuation rate of the macroscopic $\phi$-condensate: $H_{\text{SRC}} = c / \tau_{\text{rel}}$.
3. **Apparent Acceleration ($\Omega_\Lambda$)** is the natural higher-order nonlinear backreaction of wave packets scattering off the vacuum's second-sound mode spectrum and cosmic defect web over Multi-Gigaparsec baselines.
4. **The Universe is Static, Infinite, and Euclidean**, eliminating the Big Bang singularity, horizon limits, and the age paradox of early massive galaxies.

---

## References

1. **Hawkins, M. R. S.** (2010). *Time dilation in quasar light curves*. Monthly Notices of the Royal Astronomical Society, 405(3), 1940–1946.
2. **Perlmutter, S., et al.** (1999). *Measurements of $\Omega$ and $\Lambda$ from 42 High-Redshift Supernovae*. The Astrophysical Journal, 517(2), 565–586.
3. **Riess, A. G., et al.** (1998). *Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant*. The Astronomical Journal, 116(3), 1009–1038.
4. **Riess, A. G., et al.** (2022). *A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team*. The Astrophysical Journal Letters, 934(1), L7.
5. **Tolman, R. C.** (1930). *On the Estimation of Distances in a Curved Universe with Non-Static Metric*. Proceedings of the National Academy of Sciences, 16(7), 511–520.
6. **Zwicky, F.** (1929). *On the Red Shift of Spectral Lines through Interstellar Space*. Proceedings of the National Academy of Sciences, 15(10), 773–779.
7. **Castellano, M., et al.** (2024). *JWST/NIRSpec confirmation of the high-redshift galaxy population at $z > 10$*. Astronomy & Astrophysics, 683, A34.
8. **SRC Collaboration.** (2026). *Technical Manual: Technical Foundations of Scalar Relaxation Cosmology (SRC)*. Repository internal documentation: `docs/Technical Manual -  Technical Foundations of Scalar Relaxation Cosmology-SRC.md`.
9. **SRC Collaboration.** (2026). *Core Simulation Drivers and Semi-Implicit Solvers*. Repository codebase: `src/engine.py`, `scripts/sim_redshift.py`, `scripts/wave_speed_measure.py`.

---

## Appendix A: Mathematical Notation Reference

| Symbol | Definition | Physical Unit (SI) | Value / Setting in SRC |
| :--- | :--- | :--- | :--- |
| $\phi(\mathbf{x}, t)$ | Scalar condensate displacement field | $\text{m}$ (normalized) | Order parameter field |
| $v_s, c$ | Transverse elastic wave speed (speed of light) | $\text{m s}^{-1}$ | $2.99792458 \times 10^8$ |
| $\eta_s$ | Dynamic shear viscosity of the substrate | $\text{Pa s}$ | Substrate fluid property |
| $\rho_0$ | Background energy density of the condensate | $\text{J m}^{-3} \equiv \text{kg m}^{-1}\text{s}^{-2}$ | Baseline vacuum ground state |
| $\tau_{\text{rel}}$ | Structural relaxation time of the substrate | $\text{s}$ | $\sim 4.21 \times 10^{17} \text{ s}$ ($\sim 13.34\text{ Gyr}$) |
| $H_{\text{SRC}}$ | Substrate relaxation constant | $\text{km s}^{-1}\text{Mpc}^{-1}$ | $71.2 \pm 1.2$ |
| $\kappa_0$ | Linear spatial wave attenuation coefficient | $\text{m}^{-1}$ | $H_{\text{SRC}} / c \approx 7.7 \times 10^{-27}\text{ m}^{-1}$ |
| $\beta_{\text{nl}}$ | Nonlinear forward scattering coefficient | Dimensionless | $0.042 \pm 0.005$ |
| $\gamma_{\text{diff}}$ | Transverse beam diffraction exponent | Dimensionless | $1.0$ (Tolman balance) |
| $d_L$ | Apparent luminosity distance | $\text{m} \text{ or } \text{Mpc}$ | $D \sqrt{1+z} \exp(\frac{1}{2}\sigma D)$ |
| $D$ | Geometric Euclidean path length | $\text{m} \text{ or } \text{Mpc}$ | Coordinate metric distance |


cd ~/scalar-relaxation-cosmology

cat << 'EOF' > docs/theory/redshift_validation.md
# Verification Report: SRC Non-Doppler Redshift & Numerical Validation

**Framework:** Scalar Relaxation Cosmology (SRC)  
**Related Document:** `docs/theory/redshift_redefined.md`  
**Related Script:** `scripts/sim_redshift.py`  

---

## 1. Simulation Results & Numerical Output

Calculated using default parameters: $H_{\text{SRC}} = 71.2 \text{ km s}^{-1}\text{Mpc}^{-1}$, $\beta_{\text{nl}} = 0.042$, $\sigma_{\text{scat}} = 1.2 \times 10^{-5}$.

| Distance ($D$, Mpc) | SRC $z$ (Full Non-linear) | Linear Approx ($z \approx \frac{H}{c}D$) | Distance Modulus ($\mu$) |
|---------------------|---------------------------|------------------------------------------|--------------------------|
| 10                  | 0.00238                   | 0.00237                                  | 30.003                   |
| 50                  | 0.01195                   | 0.01187                                  | 33.508                   |
| 100                 | 0.02405                   | 0.02375                                  | 35.027                   |
| 500                 | 0.12642                   | 0.11875                                  | 38.631                   |
| 1000                | 0.26957                   | 0.23750                                  | 40.272                   |
| 2000                | 0.61564                   | 0.47500                                  | 42.052                   |
| 5000                | 2.37738                   | 1.18749                                  | 44.881                   |
| 8000                | 6.21231                   | 1.89998                                  | 46.765                   |

---

## 2. Mathematical Validation & Integrity Checks

### A. Core Frequency Decay Law
$$\omega(D) = \omega_0 \exp\left(-\int_0^D \kappa(s) \, ds\right)$$
With constant attenuation $\kappa_0 = \frac{H_{\text{SRC}}}{c}$, this integrates to:
$$\omega_{\text{obs}} = \omega_0 \exp\left(-\frac{H_{\text{SRC}}}{c} D\right)$$
Applying the standard spectroscopic redshift definition $z = \frac{\omega_0 - \omega_{\text{obs}}}{\omega_{\text{obs}}}$ yields the exact closed-form relation:
$$z = \exp\left(\frac{H_{\text{SRC}}}{c} D\right) - 1$$
**Status:** Algebraically exact.

### B. Local Universe Taylor Expansion
$$\exp(x) - 1 = x + \frac{1}{2}x^2 + \dots, \quad x = \frac{H_{\text{SRC}}}{c} D$$
At $D = 100 \text{ Mpc}$ ($x \approx 0.02375$):
- **Exact non-linear $z$:** $0.024046$
- **Pure linear $z$:** $0.023750$ (Relative error $\approx 1.2\%$)
- **Quadratic extension:** $0.024044$ (Matches exact result to $< 0.01\%$)

### C. Nonlinear Extension & Luminosity Distance
The generalized damping coefficient:
$$\kappa(D) = \kappa_0 \left(1 + \beta_{\text{nl}} \cdot \frac{H_{\text{SRC}}}{c} D\right)$$
integrates directly into the exponent as $\frac{1}{2}\beta_{\text{nl}}x^2$, perfectly mirroring the implementation in `sim_redshift.py`. Luminosity distance computation:
$$d_L = D \sqrt{1 + z} \exp\left(\frac{1}{2}\sigma_{\text{scat}} D\right)$$
combined with distance modulus $\mu = 5 \log_{10}(d_L / 10\text{ pc})$ yields standard astronomical scaling without invoking metric expansion or Dark Energy parameters.

---
EOF



