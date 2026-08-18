# A8 — Early-time Dynamics of the η-Seeded Phase

**Archive:** USM-Archive / 03-MERGE-BRIDGE  
**Tier:** 1 (native)  
**Status:** Locked v1.0 (set-up)  
**Depends on:** A7 (late-time overdamped solution), 03.4 (structural ω(φ)), 03.4b (null-path set-up), 03.5g (geometric conversion + structural limitation)  
**Feeds into:** globally consistent \(d(z)\), numerical confrontation with SN Ia Hubble diagram, 03.6 (CMB), 03.7 (light-curve stretch)  
**Scope:** Sets up the early-time problem, states the matching condition onto the late-time solution, and identifies what must be solved. Does **not** yet deliver a finished early-time solution or a finished Hubble diagram.

---

## 1. Why this document is required

The late-time overdamped ansatz of A7 produces a logarithmic \(d(z)\) whose derivative diverges at \(z=0\). That is incompatible with the observed finite Hubble constant \(H_0\).  

A finite slope at low redshift can be obtained only if the early, high-amplitude evolution of \(\phi\) (the phase seeded by \(\eta\)) is solved and then matched onto the late-time exponential relaxation already locked in A7.  

A8 therefore addresses the early-time regime of the same reduced equation used throughout the geometric series.

---

## 2. The equation in the early-time regime

The background evolution remains the reduced ordinary differential equation

$$
\frac{1}{c^2}\ddot\phi + \gamma(\phi,\dot\phi)\,\dot\phi + V'(\phi) = 0,
$$

with the double-well potential

$$
V(\phi)=\frac{\lambda}{4}(\phi^2-\phi_0^2)^2.
$$

In the early-time, high-amplitude regime the inertial term \(\ddot\phi/c^2\) is **not** negligible. The equation must be treated as a full second-order non-linear oscillator with damping. The overdamped reduction used in A7 is valid only after the field has entered the immediate neighbourhood of a minimum.

---

## 3. Initial-condition constraint (already required by A7)

The \(\eta\)-seeding must place the initial field value on the **high-curvature side** of the minimum:

$$
|\phi_{\rm seed}| > \frac{\phi_0}{\sqrt{3}}.
$$

Only then is \(V''(\phi_{\rm seed}) > V''(\phi_0)\) and the redshift direction \(\omega(t_{\rm s}) > \omega(t_{\rm o})\) preserved. This is a constraint on the initial data, not a free choice.

---

## 4. Matching condition onto the late-time solution

The early-time solution \(\phi_{\rm early}(t)\) must join smoothly onto the late-time overdamped solution of A7:

$$
\phi_{\rm late}(t)=\phi_0+(\phi_{\rm match}-\phi_0)\,e^{-\Gamma(t-t_{\rm match})},
$$

where \(t_{\rm match}\) is the time at which the field has entered the linear neighbourhood of the minimum and the inertial term has become negligible. Continuity of \(\phi\) and \(\dot\phi\) at \(t_{\rm match}\) fixes the matching amplitude \(\phi_{\rm match}\).

---

## 5. What must be delivered by the full solution

A successful early-time solution must provide:

1. A concrete function \(\phi(t)\) from the \(\eta\)-seeded initial condition through the non-linear phase.  
2. A smooth match onto the late-time exponential.  
3. The resulting clock function \(\omega(t)=\sqrt{V''(\phi(t))/\rho(\phi(t))}\).  
4. A low-redshift expansion of the light-travel distance \(d(z)=c(t_{\rm o}-t_{\rm s}(z))\) that yields a **finite, non-zero slope** at \(z=0\) (i.e., a finite \(H_0\)).

**Dynamical condition for a finite \(H_0\):**  
A finite, non-zero \(H_0\) requires that the local clock is still changing at the present epoch (\(\dot\omega(t_{\rm o})\neq 0\)). The matched early-time + late-time solution must therefore leave a residual \(\dot\phi\) (or residual \(\dot\rho\)) today. If the field has already reached a static minimum, the Hubble slope cannot be finite and non-zero.

Only after these four items exist can a globally consistent distance–redshift relation be written and compared with the SN Ia data.

---

## 6. Honest limitations of the present set-up

- No explicit analytic or numeric solution of the early-time ODE is given here.  
- The precise form of the \(\eta\)-seeded initial condition (beyond the high-curvature constraint) remains free and must be fixed by consistency with the CMB or other early-universe observables.  
- Branch A versus Branch B is still undecided; the early-time solution may force or exclude one of them.  
- No claim is made that a finite-\(H_0\) solution is already known to exist. That is the open question A8 is intended to answer.

---

## 7. Immediate next action inside A8

Solve (analytically by matched asymptotics or numerically) the full second-order equation from a high-curvature initial condition, impose the matching conditions of §4, extract \(\omega(t)\), and test whether the resulting low-\(z\) slope is finite and of the observed order of magnitude once the laboratory anchors are inserted.

---

**End of A8 (Locked v1.0 — set-up only)**
