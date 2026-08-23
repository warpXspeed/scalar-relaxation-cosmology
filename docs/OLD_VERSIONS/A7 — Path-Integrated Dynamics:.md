# A7 — Path-Integrated Dynamics: Solution of the Reduced ODE & Extraction of ω(z)

**Archive:** USM-Archive / 03-MERGE-BRIDGE  
**Tier:** 1 (native)  
**Status:** Draft v0.1  
**Depends on:** 03.4 (structural ω(φ)), 03.4b (null-path set-up + extraction rule), §2 (master equation), 03.1 (SDF), 03.3 (redshift as energy-scale ratio)  
**Feeds into:** 03.5 (spectral-line constraint), 03.6 (CMB), 03.7 (light-curve stretch)  
**Scope:** Integrates the reduced ODE under an explicit overdamped ansatz, extracts the functional form of ω(t), and states how the z–d and T(z) relations are obtained. The final numerical match to data is flagged as requiring the laboratory anchors and the separate light-travel-time relation.

---

## 1. The equation being solved

From 03.4b the background evolution on the null path is the reduced ordinary differential equation

$$
\frac{1}{c^2}\ddot\phi + \gamma(\phi,\dot\phi)\,\dot\phi + V'(\phi) = 0,
$$

with the double-well potential of the source manual

$$
V(\phi)=\frac{\lambda}{4}(\phi^2-\phi_0^2)^2.
$$

The transverse speed \(c\) is held fixed by the spectral-line constraint. The coefficient \(\gamma\) is fixed in magnitude by the ³He second-sound anchor (\(\gamma\sim 1.2\times 10^{-18}\,{\rm s}^{-1}\)).

---

## 2. Physically motivated ansatz: overdamped relaxation

In the late-time, \(\gamma\)-dominated regime the inertial term is negligible compared with the frictional term. The equation reduces to the first-order balance

$$
\gamma\,\dot\phi + V'(\phi)\approx 0.
$$

For motion near a minimum the potential is locally harmonic, \(V'(\phi)\approx V''(\phi_0)\,(\phi-\phi_0)=2\lambda\phi_0^2\,(\phi-\phi_0)\). The solution is pure exponential relaxation:

$$
\phi(t)=\phi_0+(\phi_{\rm seed}-\phi_0)\,e^{-\Gamma t},
$$

where the effective rate is

$$
\Gamma=\frac{2\lambda\phi_0^2}{\gamma}.
$$

(The precise relation between \(\Gamma\) and the laboratory \(\gamma\) will be fixed once the numerical values of \(\lambda\) and \(\phi_0\) are taken from the source-manual calibration; the functional form is exponential.)

This is the explicit ansatz used throughout the remainder of the document. It corresponds to the physically expected behaviour once the early high-amplitude phase seeded by \(\eta\) has decayed and the field is settling into a minimum.

---

## 3. Local clock along the solution

From 03.4 the infrared clock is

$$
\omega(\phi)=\sqrt{\frac{V''(\phi)}{\rho(\phi)}}.
$$

Substituting the overdamped solution gives a concrete function of time:

$$
\omega(t)=\sqrt{\frac{V''\bigl(\phi(t)\bigr)}{\rho\bigl(\phi(t)\bigr)}}.
$$

Because \(\phi(t)\) is monotonic, \(\omega(t)\) is monotonic. The redshift between an emission event at time \(t_{\rm s}\) and an observation event at time \(t_{\rm o}\) is therefore

$$
1+z=\frac{\omega(t_{\rm s})}{\omega(t_{\rm o})}.
$$

This is still a pure ratio of local clocks; no cumulative integral of \(\gamma\) enters the frequency ratio.

---

## 4. Branch decision

Two structural possibilities remain open (03.4 §4):

- **Branch B (fixed \(\rho\))** — density is constant on the relevant scales. Then \(\omega(t)\) varies solely because \(V''(\phi(t))\) varies as \(\phi\) approaches the minimum.  
- **Branch A (compensated)** — both \(\rho(\phi)\) and \(G_{\rm shear}(\phi)\) evolve while their ratio (and therefore \(c\)) stays fixed. The redshift is still carried by the ratio \(V''(\phi)/\rho(\phi)\).

The overdamped solution itself does not yet force a choice; the choice is made by inspecting whether a consistent, observationally viable solution exists with fixed \(\rho\) or requires a compensating evolution of \(\rho\). That inspection is part of the numerical confrontation with data and is left open here.

---

## 5. From \(\omega(t)\) to the observed relations (honest scope)

The function \(\omega(t)\) supplies the redshift once the emission time \(t_{\rm s}\) is known. Converting redshift into a distance–redshift relation further requires the light-travel time along the null path:

$$
d_{\rm travel}=c\cdot(t_{\rm o}-t_{\rm s}).
$$

That conversion is a separate geometric step (the null-path length). Likewise, the temperature–redshift relation \(T(z)\) follows once the energy density of the photon gas is expressed in terms of the local clock, again using the same \(\omega(t)\).

**A7 therefore yields:**
- the functional form of \(\omega(t)\) under the overdamped ansatz,
- the explicit redshift formula \(1+z=\omega(t_{\rm s})/\omega(t_{\rm o})\),
- a clear statement of the additional geometric step needed for the \(z\)–\(d\) diagram,
- the laboratory anchors (\(\gamma\) from ³He, \(c\) from spectral lines, \(\phi_0\) and \(\lambda\) from the source-manual calibration) that must be inserted before numerical comparison with data.

It does **not** claim that the ODE integration alone already produces a finished Hubble diagram or a finished CMB spectrum. Those final numerical outputs remain contingent on the anchors and on the light-travel-time relation.

---

## 6. Summary

- The reduced dynamics are those of a damped oscillator in the double-well.  
- In the \(\gamma\)-dominated regime the solution is exponential relaxation toward the minimum.  
- The local clock \(\omega(t)\) follows at once from the structural formula of 03.4.  
- Redshift is the pure ratio of clocks at emission and observation.  
- The quantitative \(z\)–\(d\) and \(T(z)\) curves require one additional geometric ingredient (null-path length) and the laboratory values of the anchors.  
- Branch A versus Branch B is decided by whether a consistent solution exists with fixed or evolving \(\rho\).

---

**End of A7 (Draft v0.1)**
