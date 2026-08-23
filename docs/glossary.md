# SUBSTRATE — Unified Glossary & Correspondence Table (v1.1)

**Project:** SUBSTRATE (Scalar Substrate Framework) — the merged completion of
Scalar Relaxation Cosmology (SRC) + Quantum Logical Framework (QLF / Zero Free Action).

**Purpose:** One substrate, two vocabularies. This table is the Rosetta stone between
SRC's physical-mechanism language and QLF's formal-logic language. It is the source of
truth for all reasoning in the merged project.

**Two-tier rule (anti-cycle):**
- **Tier 1 (SOURCE):** substrate-native relations. All reasoning and all predictions
  originate here.
- **Tier 2 (SHADOW):** standard-physics translation, used ONLY to project a Tier-1
  result for comparison with raw observables. Never derive a physical result from a
  shadow term.
- **Governing rule:** derive in Tier 1; project to Tier 2 for data. If a derivation
  starts producing results from Tier 2, stop — that is drift.

**Cell labels used in this table:**
- **[C]** = CLOSED: both frameworks have a Tier-1 statement; the two are mutually consistent or the Lean theorem is the common anchor.
- **[G]** = GAP: one framework has a Tier-1 statement, the other has none. The gap is a deliverable, not a failure.
- **[L]** = LIVE CONFLICT: both frameworks have a Tier-1 statement and they disagree. Adjudication is deferred to §F (raw data).
- **[O]** = OPEN: the Tier-1 sentence has not yet been written for at least one framework.

---

## A. CORE ONTOLOGY

| Unified term | SRC (mechanism) | QLF (formal) | Status |
|---|---|---|---|
| **Substrate** | Viscoelastic scalar φ; one medium, no container | The zero-free-action (ZFA) closure base; information as ½-spin distinction | [C] |
| **State / Event** | A condition of the substrate | A ZFA-closed history (a realized event) | [C] |
| **Possibility** | An unlocked, not-yet-relaxed configuration | A non-closed history (exists but not realized) | [C] |
| **Closure / Realization** | Relaxation to a locked, self-sustaining state | ZFA balance: Σᵢ imbalanceᵢ = 0 | [C] |
| **Self-renewal rate** | How fast a state re-sets its own pattern (native clock) | Local clock f = 1/t carried by each closure | [C] — see §E (SDF) for whether the two are the same object |
| **Organization** | Degree of ordered structure in a state | Logical density of the closure | [C] |
| **Coherence** | Self-consistent, phase-locked structure | Balanced, closed structure | [C] |
| **Memory / Residual** | Residual Organization (RO): lasting bias left by a prior configuration | Hysteresis / persistent wake in the closure history | [C] |

---

## B. LIGHT & PARTICLES

| Unified term | SRC (mechanism) | QLF (formal) | Status |
|---|---|---|---|
| **Light** | Coherent Shear Configuration (CSC): self-renewing transverse configuration | Null closure; photon history e.g. `^^^<^<^<` (null interval) | [C] |
| **Particle** | Stable Configuration (SC): topologically protected, self-sustaining state | ½-spin (spinor) closure; knot; one bit of information | [C] |
| **Photon (shadow)** | — | null qubit (Bloch sphere = celestial sphere) | [G] — QLF-only; SRC projects CSC to this for data |
| **Electron / fermion (shadow)** | — | spinor closure with Pauli exclusion | [G] — QLF-only; SRC projects SC to this for data |
| **Local c** | c = √(G_shear/ρ); handoff rate, pattern-rigid | c = L_P/τ_P (Lean: QLF_SubstrateLightSpeed) | [C] — Lean-anchored theorem; the two expressions are the same Tier-1 result in two vocabularies |

---

## C. GRAVITY & COSMOLOGY

| Unified term | SRC (mechanism) | QLF (formal) | Status |
|---|---|---|---|
| **Gravity** | Local Organization Factor (LOF): stiffness set by local organization | Gravity from delay; α_G = exp(−28π) (Lean-anchored) | [C] |
| **Refraction (shadow)** | — | — | [O] — Tier-1 sentence not yet written for either framework; do not import as a Tier-2 concept |
| **Redshift** | State-Rate Relation (SRR): ratio of self-renewal rates of two states (endpoint, not path) | Redshift = time dilation, one phenomenon; cross-frequency Lorentz | **[L]** — see §F.4. **Blocker:** if QLF's "time dilation" is substrate-native (clock-ratio at two states) it agrees with SRR and this row closes. If it is standard proper-time dilation along a worldline, it is a Tier-2 import wearing Tier-1 clothes and the row is a live conflict. |
| **1+z (shadow)** | SRR − 1 | f_source / f_observer | [C] as shadow projection; inherits status of the Redshift row above |
| **Damping / energy loss (shadow)** | Relaxation of coherence (γ): amplitude/energy transport only | — | [G] — SRC-only; QLF has no explicit γ. The γ role is an SRC deliverable that QLF inherits by projection. |
| **Cosmological constant Λ** | GHOST in SRC (removed) | Ω_Λ = log 2 (Lean: QLF_CosmologicalConstant) | **[L]** — see §F.1 |
| **Dark matter** | GHOST in SRC (removed; flat curves via shear-lag/CSC) | Denser logic on same Hubble horizon; a₀ = cH₀/2π (SPARC fit) | **[L]** — see §F.2 |
| **Big Bang** | ABSENT in SRC (stochastic η seeding, no singularity) | "Logical bang": Planck-mass BH Hawking-cascade | **[L]** — see §F.3 |
| **Cosmic age** | Relaxation timescale τ ≈ 1/γ (~26 Gyr) | Derived count of Planck ticks t₀ = N·τ_Planck | [C] — both are Tier-1; numerical agreement is a check, not a derivation |

---

## D. QUANTUM LAYER

| Unified term | SRC (mechanism) | QLF (formal) | Status |
|---|---|---|---|
| **Superposition** | Unlocked self-renewal; multiple rates held until relaxation | Non-closed history (possibility, not yet event) | [C] |
| **Collapse / measurement** | Relaxation of coherence (irreversible move to locked state) | ZFA closure selection: only balanced histories realized | [C] |
| **Interference** | Residual Organization biasing current self-renewal | Closure history / path structure | [C] |
| **Entanglement** | Shared Residual Organization; co-determined self-renewal | Non-separable closure; ER=EPR (Quantum_Gravity.md) | [C] |
| **Quantization (discrete spectra)** | Mode-locking of self-renewal to f_res + hysteresis | Spinor = 1 bit; spin-statistics; Pauli exclusion (Lean-proven) | [C] |
| **Born rule / probability** | OPEN in SRC | Integer path-counts (Lean: QLF_BornProbability) | [G] — QLF fills SRC gap. SRC deliverable: write the Tier-1 sentence for probability as residual-organization weighting. |
| **Spin / statistics (shadow)** | — | 2-spinors, SL(2,ℂ)→SO⁺(1,3) double cover (Lean-proven) | [G] — QLF-only at Tier 1; SRC projects SC to this for data. |

---

## E. DYNAMICS & PARAMETERS

| Unified term | SRC (mechanism) | QLF (formal) | Status |
|---|---|---|---|
| **Relaxation coefficient γ** | Relaxation-of-coherence rate (~1.2×10⁻¹⁸ s⁻¹); ³He-anchored | — | [G] — SRC-only; QLF has no explicit γ. See §C γ-row. |
| **Stiffness β, G_shear** | Longitudinal / transverse stiffness (set self-renewal rate) | — (emerge via closure structure) | [G] — SRC has the explicit parameter; QLF expects it to emerge. **Open:** write the Tier-1 sentence that says "closure structure encodes stiffness." |
| **χ (piezoelectric coupling)** | Transverse-shear stress → EM field | Gauge-fold delay as EM | **[O]** — QLF column needs a Tier-1 sentence. Do not treat as closed. |
| **η (stochastic noise)** | Quantum Butterfly perturbation | Non-closed history tail (pruned by full_zeno_prune — implementation detail, not a Tier-1 statement) | [C] at Tier 1; the Lean pruning function is a Tier-2 / implementation note. |
| **f_res (global heartbeat)** | Global resonance frequency; the global self-renewal rate | — (no direct analog yet) | **[O]** — **This is the SDF question in disguise.** f_res is "which substrate variable sets the global self-renewal rate." See §F.5. |

---

## F. ADJUDICATION REGISTER (the decisive fork)

**Standard:** raw data decides. Whichever framework's cosmology survives on the data determines which quantum core we keep. No default anchor; no framework preferred a priori.

**Data sources to be used:**
- CMB origin & spectral shape (Planck, WMAP, ACT)
- Expansion history (SN Ia: Pantheon+; BAO: eBOSS, DESI)
- α-drift bounds (quasar absorption: Muether et al., King et al.)
- SPARC galaxy rotation curves (Lelli et al. 2016)
- GW speed v_GW vs c (GW170817 / GRB 170817A)
- ³He relaxation anchor (SRC experimental grounding)
- Cosmic age independent measurements (stellar ages, Hubble constant tension)

### F.1 Cosmological constant Λ
- **SRC:** GHOST (removed). No Λ term in the substrate dynamics.
- **QLF:** Ω_Λ = log 2 (Lean: QLF_CosmologicalConstant), claimed to close the 10^122 vacuum catastrophe.
- **Adjudication data:** expansion history (SN Ia + BAO), CMB acoustic peak structure, Hubble tension.
- **Status:** LIVE. Not yet adjudicated.

### F.2 Dark matter
- **SRC:** GHOST (removed). Flat rotation curves explained by shear-lag / CSC dynamics.
- **QLF:** Denser logic on same Hubble horizon; a₀ = cH₀/2π (SPARC fit).
- **Adjudication data:** SPARC rotation curves (fit quality, not just existence), cluster lensing (Bullet Cluster), CMB lensing, structure growth rate fσ₈.
- **Status:** LIVE. Not yet adjudicated.

### F.3 Big Bang / origin
- **SRC:** ABSENT. Stochastic η seeding, no singularity, no initial condition.
- **QLF:** "Logical bang": Planck-mass black-hole Hawking cascade.
- **Adjudication data:** CMB spectral shape (blackbody purity, non-Gaussianity), absence of a detectable singularity signature.
- **Status:** LIVE. Not yet adjudicated.

### F.4 Redshift mechanism
- **SRC:** State-Rate Relation (SRR): ratio of self-renewal rates at two endpoints. Not path-loss.
- **QLF:** Time dilation / cross-frequency Lorentz.
- **Blocker (must resolve before adjudication):** clarify QLF's "time dilation" — substrate-native clock ratio (agrees with SRR) vs. standard proper-time dilation (Tier-2 import).
- **Adjudication data (if genuinely in conflict):** α-drift bounds, spectral-line consistency across redshift, GW speed v_GW vs c, Tolman surface-brightness test.
- **Status:** BLOCKED on the QLF reading. If QLF = substrate-native, this row closes as [C]. If QLF = standard, this row becomes a live conflict to adjudicate.

### F.5 SDF — Single Open Object (gates both frameworks)
- **Question:** Which substrate variable sets the self-renewal rate?
- **SRC candidate:** LOF-set self-renewal rate (from the handoff/electron image).
- **QLF candidate:** Local clock per closure, f = 1/t (QLF_SubstrateLightSpeed.lean).
- **Check:** Are these the same object?
  - **If YES:** SDF closes for both frameworks at once. Redshift + gravity + quantization + ³He anchor all close together. **Highest-value result in the project.**
  - **If NO:** We have two competing clocks. One must be subordinate, or the ontology splits.
- **Status:** OPEN. This is the single highest-priority question. All other items in §F are downstream of this.

---

## G. CHANGELOG

**v1.1 (this version):**
- Added cell-status labels [C]/[G]/[L]/[O] to every row.
- §C Redshift row: flagged as [L] with explicit blocker on QLF's "time dilation" reading.
- §C Damping/γ row: relabeled [G] (SRC-only), not implied [C].
- §C Refraction row: relabeled [O] (no Tier-1 sentence in either framework).
- §D Born rule row: relabeled [G] with explicit SRC deliverable.
- §D Spin/statistics row: relabeled [G] (QLF-only at Tier 1).
- §E: table structure repaired (χ, η, f_res now separate rows).
- §E χ row: relabeled [O] (QLF needs a Tier-1 sentence).
- §E η row: Lean implementation detail (full_zeno_prune) demoted to a note, not a Tier-1 statement.
- §E f_res row: cross-referenced to §F.5 (SDF).
- §F: ADJUDICATION REGISTER added (was referenced but absent in v1). Contains the four decisive-fork items + SDF, each with the raw-data sources that will decide it.
- §G: changelog added.

**v1 (original):** as provided. §F was referenced from §C but not present. §E table was malformed.
```
