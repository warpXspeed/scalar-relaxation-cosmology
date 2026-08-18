# 03.5g — Geometric Conversion: From ω(t) to the Distance–Redshift Relation

**Archive:** USM-Archive / 03-MERGE-BRIDGE  
**Tier:** 1 (native)  
**Status:** Locked v1.0 (with structural limitation flagged)  
**Depends on:** A7 (overdamped solution + ω(t)), 03.4 (structural ω(φ)), 03.4b (null-path set-up), 03.3 (redshift as energy-scale ratio)  
**Feeds into:** numerical confrontation with SN Ia Hubble diagram, 03.6 (CMB), 03.7 (light-curve stretch)  
**Scope:** Converts the clock-ratio definition of redshift into a distance–redshift relation under the locked overdamped ansatz. Does **not** yet insert numerical values of the anchors or claim a finished fit to data.

---

## 1. What is already locked

From the preceding documents we have:

- Redshift is the pure ratio of local clocks  
  $$
  1+z = \frac{\omega(t_{\rm s})}{\omega(t_{\rm o})}.
  $$

- Under the overdamped ansatz  
  $$
  \phi(t)=\phi_0+(\phi_{\rm seed}-\phi_0)\,e^{-\Gamma t},
  $$
  with \(\Gamma=2\lambda\phi_0^2/\gamma\).

- The infrared clock is  
  $$
  \omega(\phi)=\sqrt{\frac{V''(\phi)}{\rho(\phi)}}.
  $$

- For the present derivation we adopt **Branch B** (fixed \(\rho\)) as the simplest working case; Branch A can be restored later if required by the data.

---

## 2. Light-travel distance

Because \(c\) is constant on the scales of interest, the geometric distance along the null path is simply the light-travel time:

$$
d = c\,(t_{\rm o}-t_{\rm s}).
$$

(The more refined luminosity-distance and angular-diameter-distance definitions introduce additional factors that involve the amplitude damping \(\gamma\); those factors are deferred to the Etherington-relation document.)

---

## 3. Eliminating the emission time

From the overdamped solution we can solve for the emission time in terms of the field value at emission:

$$
t_{\rm s}=-\frac{1}{\Gamma}\ln\left(\frac{\phi_{\rm s}-\phi_0}{\phi_{\rm seed}-\phi_0}\right)
$$

(assuming \(t_{\rm o}\) is the present, conventionally set to a convenient origin once the present-day field value is fixed).

Because \(\omega\) is a known function of \(\phi\), the redshift fixes \(\phi_{\rm s}\):

$$
1+z=\frac{\omega(\phi_{\rm s})}{\omega(\phi_{\rm o})}\quad\Rightarrow\quad\phi_{\rm s}=\phi_{\rm s}(z).
$$

Substituting yields an explicit (if still formal) relation

$$
d(z)=c\cdot\frac{1}{\Gamma}\ln\left(\frac{\phi_{\rm seed}-\phi_0}{\phi_{\rm s}(z)-\phi_0}\right).
$$

This is the structural distance–redshift relation under the locked ansatz and Branch B.

---

## 4. Honest limitations (what this document does **not** yet deliver)

- The numerical curve \(d(z)\) still requires the laboratory values of \(\gamma\) (³He), \(\lambda\), \(\phi_0\), and \(\phi_{\rm seed}\).  
- The conversion above is the pure light-travel distance. Luminosity distance (the quantity measured by SN Ia) further multiplies by an amplitude-damping factor that involves \(\gamma\); that step is reserved for the Etherington document.  
- Branch A (evolving \(\rho\)) has not yet been restored; if the data demand it, the same geometric skeleton is reused with a modified \(\omega(\phi)\).  

**Structural limitation of the present ansatz:**  
The low-\(z\) behaviour of the structural \(d(z)\) relation under the overdamped ansatz is \(d(z)\propto\ln(1+z)\approx z\) at small \(z\), which gives an *infinite* slope at \(z=0\) (inconsistent with the observed finite \(H_0\)). The overdamped ansatz captures the *late-time* (low-\(z\)) relaxation but not the *early-time* (high-\(z\)) dynamics that sets the Hubble slope. The full \(d(z)\) relation requires the early-time dynamics (the \(\eta\)-seeded phase), which is a separate derivation. This is a *structural* limitation, not a numerical one — it is not fixed by inserting the anchors.

No claim is made that the present expression already fits the Pantheon+ or DESI Hubble diagram. That confrontation is the next numerical task, and it will immediately expose the limitation above.

---

## 5. Immediate next numerical step (revised)

Because of the structural limitation flagged in §4, the next required derivation is **not** the insertion of anchors into the present logarithmic form.  

The next required derivation is the **early-time dynamics** of the \(\eta\)-seeded, high-amplitude phase that sets a finite Hubble slope at \(z=0\). Only after that early-time solution is in hand can a globally consistent \(d(z)\) be constructed and confronted with the SN Ia data.

---

**End of 03.5g (Locked v1.0 with structural limitation)**
