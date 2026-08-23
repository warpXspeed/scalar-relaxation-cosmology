# Module K: Distance–Redshift Relation ($d(z)$) & Clock-Ratio Mechanics

**Document Ref:** SRC-MOD-COSMO-001  
**Category:** Observational Cosmology / Spectral Shift Mechanics  
**Ontology:** State-Rate Relation (SRR) & Overdamped Field Relaxation  

---

## 1. Foundational Axioms & Clock-Ratio Definition

In Scalar Relaxation Cosmology (SRC), spectral redshift ($z$) is not produced by metric expansion of space or path-loss energy dissipation ("tired light"). It is defined strictly as the **ratio of local clock rates** at the emission time ($t_s$) and observation time ($t_o$):

$$1+z = \frac{\omega(t_s)}{\omega(t_o)}$$

Where the local infrared clock rate $\omega(\phi)$ is determined by the scalar field potential $V''(\phi)$ and local lattice density $\rho(\phi)$:

$$\omega(\phi) = \sqrt{\frac{V''(\phi)}{\rho(\phi)}}$$

---

## 2. Overdamped Substrate Relaxation

Under the late-time overdamped relaxation solution, the scalar field evolves as:

$$\phi(t) = \phi_0 + (\phi_{\text{seed}} - \phi_0) e^{-\Gamma t}$$

where $\Gamma = \frac{2\lambda\phi_0^2}{\gamma}$ represents the global viscoelastic relaxation rate set by field viscosity $\gamma$ and self-interaction $\lambda$.

Solving for the emission time $t_s$ in terms of the local field value at emission $\phi_s$:

$$t_s = -\frac{1}{\Gamma} \ln\left(\frac{\phi_s - \phi_0}{\phi_{\text{seed}} - \phi_0}\right)$$

---

## 3. Geometric Light-Travel Distance

Because the shear-wave speed of light $c$ is constant across the pre-tensioned substrate, the geometric distance $d$ along the null path is:

$$d(z) = c \cdot (t_o - t_s)$$

Substituting the clock-ratio mapping $\phi_s(z)$ yields the closed-form structural distance-redshift relation:

$$d(z) = \frac{c}{\Gamma} \ln\left(\frac{\phi_{\text{seed}} - \phi_0}{\phi_s(z) - \phi_0}\right)$$


EMISSION NODE (tₛ)                                     OBSERVER NODE (tₒ)
High-Density State φₛ                                 Baseline State φₒ
Fast Local Clock ω(tₛ) ───[ Null Path: d = c(tₒ - tₛ) ]───> Slow Local Clock ω(tₒ)
Observed Redshift: 1+z = ω(tₛ) / ω(tₒ)  ===>  Pure Clock Ratio (Zero Path Loss)


---

## 4. Luminosity Distance & Supernova Ia Fits

For observational confrontation with Type Ia Supernovae (Pantheon+ / DESI Hubble diagrams), the luminosity distance $d_L(z)$ incorporates the amplitude damping parameter $\gamma$:

$$d_L(z) = (1+z) \cdot d(z) \cdot \exp\left(\frac{\gamma \cdot d(z)}{2c}\right)$$

This two-component structure separates spectral redshift (SRR clock ratio) from flux attenuation, satisfying supernova light-curve duration dilation without angular blurring or CMB distortion.


