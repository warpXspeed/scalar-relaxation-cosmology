
# DFM Finite-Gap Engine

**Algebraic core for the Dynamic Fluid Medium (DFM) / dark-aether model.**

Maps Riemann-surface data (Sato Grassmannian finite-gap solutions) onto physical observables: scalar potential, current, and shear. History is treated as data — pulses write permanent phase memory, slow moduli drift reshapes the background geometry, and both are queryable from a single event log.

```
Ω, Z, U  →  θ(Z|Ω)  →  u, v, S
```

No spatial grid. No dissipative damping. Exact integrable hierarchy.

---

## Install / run

```bash
# pure NumPy / SciPy — no external algebraic-geometry packages required
cd dfm_engine
python -m dfm_engine.test_cnoidal      # unit test (periodicity 6.5e-15)
python -m dfm_engine.demo_capture      # Terminal Capture + decay envelope
python -m dfm_engine.demo_adiabatic    # solar-driven Ω(t) drift
python -m dfm_engine.demo_interference # capture interleaved with drift + ε sweep
python -m dfm_engine.demo_chart        # toroidal 3-D shear eigenvalues
```

---

## Layout

```
dfm_engine/
├── theta.py              # Riemann theta evaluator (g ≤ 4)
├── reconstruction.py     # Ω, Z, U → potential, current, 1-D shear
├── events.py             # EventLog, apply_pulse, apply_moduli_drift
├── engine.py             # DFMState (evolve, inject, drift, twin, omega_at)
├── diagnostics.py        # path-dependent decay_envelope
├── chart.py              # ToroidalChart + shear_tensor_3d
├── test_cnoidal.py
├── demo_capture.py
├── demo_adiabatic.py
├── demo_interference.py
├── demo_chart.py
└── __init__.py
```

---

## Core geometry

| Object | Role |
|--------|------|
| **Ω** (period matrix) | Slow geometric background. Adiabatically deformable. |
| **Z** (phase vector) | Fast dynamical variable. Carries permanent memory. |
| **U** (frequency vectors) | Hierarchy directions (spatial + time). |
| **τ / θ** | Tau-function / Riemann theta. Encodes the entire history. |
| **EventLog** | Explicit, queryable geological record of every pulse and drift. |

A point on the finite-gap locus is a compact Riemann surface Σ of genus *g*. The engine stays inside that locus: evolution is algebraic, not grid-based.

---

## Geometric results (path-dependent)

### 1. Phase memory is protected

Raw |ΔZ| (net pulse content) is **invariant** under arbitrary slow moduli drift. Memory lives in the fiber (Z), not the base (Ω). A later secular evolution can modulate the *expression* of an earlier event but cannot erase its existence in the record.

### 2. Observable transients feel the background

Interference run — capture pulses interleaved with solar-driven drift (path-dependent Ω(t)):

| quantity            | baseline | interference | Δ       |
|---------------------|----------|--------------|---------|
| raw \|ΔZ\|          | 0.550273 | 0.550273     | 0       |
| memory ratio        | 0.090146 | 0.103128     | +14.4 % |
| γ (Joule_heating)   | 0.0000   | 1.1930       | +1.193  |
| γ (tidal_lock)      | 0.6385   | 0.3817       | −0.257  |

γ is a **phase-mixing rate**, not dissipative damping. The same impulse train writes memory at different rates depending on the solar state of the substrate at arrival time. Timing-of-arrival is a first-class dynamical variable.

> Pre-Ω-history figures (memory ratio +29 %, different γ values) were artifacts of replaying the final Ω over the whole trajectory and are superseded by the numbers above. Qualitative conclusions survived; the quantities did not.

### 3. Measured adiabatic threshold (genus-1)

Dimensionless adiabatic parameter:

```
ε = |Ω̇| / (|U| · |Im Ω|)
```

Mean residual shear vs ε (fixed total ΔΩ, varying duration):

```
ε        mean|ΔS|
0.714    0.378
0.357    0.556
0.179    0.600
0.089    0.675
0.045    0.675   ← flattens (Δ ≈ 0 %)
0.022    0.689   ← +2 % creep
```

**Interpretation of the rising curve.**  
Fast drift scrambles phase coherence → the pulse response dephases quickly → residual against the twin is small.  
Slow drift preserves coherent response longer → residual grows toward its adiabatic limit.  
The plateau is where the observable becomes **drift-rate-independent** — the operational definition of adiabaticity for this engine. It is *not* the point where residual vanishes.

**Honesty caveats**

- The plateau still creeps (+2 % from ε = 0.045 → 0.022). Quote the threshold as  
  **ε ≲ 0.05 with residual converging at ∼2 % per further halvings**, not as a hard knee.  
  One more decade (ε ≈ 0.01) would tighten the bound.
- **Zero projection activations** across the entire sweep: the physically motivated solar-driven schedules never push Im Ω against the positive-definite boundary. The cone constraint is satisfied by the dynamics, not enforced by clipping.

**Validity condition (genus-1, this hierarchy frequency):**

```
|Ω̇| / (|U| · |Im Ω|)  ≪  0.05
```

### Residual definition (reproducibility)

```
mean|ΔS| = (1/T) ∫₀ᵀ |S_injected(t) − S_twin(t)| dt
```

- *S* = 1-D shear rate from `shear_tensor_1d`
- both trajectories use path-dependent Ω(t) via `omega_at(t)`
- twin = uninjected counterfactual sharing the same `omega_history`
- window = full run duration *T* of the sweep trajectory

---

## Toroidal chart lift (3-D shear)

```python
from dfm_engine import DFMState, ToroidalChart, shear_tensor_3d, shear_eigenvalues, trace_check

chart = ToroidalChart(R=1.0, r=0.3)
S = shear_tensor_3d(x, state, chart)   # traceless 3×3
w, V = shear_eigenvalues(S)            # poloidal / toroidal split
assert trace_check(S) < 1e-12
```

**Terminal Capture eigenvalue tracks** (x = 0, θ = φ = 0):

```
stage                   λ1        λ2        λ3     |tr S|
post EM_induction    0.487    -0.244    -0.244    5.6e-17
post Joule_heating  -0.631     0.316     0.316    1.1e-16
post tidal_lock     -0.381     0.191     0.191    5.6e-17
final                0.433    -0.216    -0.216    5.6e-17
```

- Trace vanishes to machine precision (max |tr S| = 1.1×10⁻¹⁶) — consistency check **PASS**.
- Sequenced sign flip and magnitude change across the three stages is the poloidal/toroidal shear signature of the capture train on the chart.

The engine remains chart-agnostic; `ToroidalChart` owns only the laboratory mapping. A Cartesian chart can be added later without touching the core.

---

## Quick API

```python
from dfm_engine import DFMState, decay_envelope, ToroidalChart, shear_tensor_3d
import numpy as np

Omega = np.array([[1.5j]])
U     = np.array([[1.0+0j, 0.35+0j]])   # spatial + time frequency
Z0    = np.array([0.25+0.05j])

state = DFMState(Omega, U, Z0)

# Terminal Capture compound sequence
state.inject_compound([
    (0.0, 0.35+0.12j, "EM_induction"),
    (0.8, 0.12+0.04j, "Joule_heating"),
    (2.5, 0.05+0.02j, "tidal_lock"),
])
state.evolve(1.5)

# Counterfactual twin + decay envelope
twin = state.twin()
report = decay_envelope(state, twin)
print(report.summary())

# Adiabatic solar-driven drift
state.drift_moduli(np.array([[0.04j]]), label="solar_step")
print(state.log.summary())

# 3-D shear on the toroidal chart
chart = ToroidalChart(R=1.0, r=0.3)
S = shear_tensor_3d(0.0, state, chart)
```

---

## Roadmap status

| # | Item | Status |
|---|------|--------|
| 1 | Pulse injection / Terminal Capture | **done** |
| 2 | Decay-envelope diagnostic (counterfactual twin) | **done** |
| 3 | Adiabatic outer loop on Ω(t) | **done** |
| 4 | Ω-history + measured ε_crit | **done** |
| 5 | 3-D traceless shear (toroidal chart) | **done** |
| 6 | Genus-2 extension (2×2 Ω, threshold surface) | next |

The engine is complete for the genus-1 demonstration regime. The natural next step is the genus-2 extension — period matrix becomes genuinely 2×2, the adiabatic threshold becomes a surface over two drift directions — toward the multi-phase substrate required by the full SRC / double-toroid models.

---

## Design invariants

- Inner loop moves only **Z**; **Ω** changes only via explicit drift.
- Pulses write permanent phase offsets (memory without dissipation).
- γ measures phase mixing against the multi-frequency theta background, **not** energy loss.
- All geometric history is queryable from the `EventLog`.
- Pulse amplitudes accept a `scale=` factor for later physical calibration — no geometric fudge factors.
- Chart lift is optional presentation; the algebraic core never depends on it.
