"""
SRC First-Principles Reaction Engine (v0.3)
Scalar Relaxation Cosmology - Atomic Harmonics Module

Calculates delta-tau (dTau) purely from continuous field mechanics
of the element tuple: f (frequency), tau (torsional shear),
and P (aetheric pressure gradient). No hardcoded chemical patches.
"""

import itertools
import numpy as np

# ---------------------------------------------------------------
# ELEMENT TUPLES: E = (Gr, f, tau, V, dP)
# Pure physical parameters, no legacy exceptions.
# ---------------------------------------------------------------
ELEMENTS = {
    "H":  {"tau": 2.0, "freq": 1.0, "dP": -1.5},
    "He": {"tau": 0.0, "freq": 2.0, "dP":  0.0},
    "Li": {"tau": 3.5, "freq": 2.1, "dP":  2.0},
    "C":  {"tau": 1.0, "freq": 4.0, "dP":  0.0},
    "N":  {"tau": 2.5, "freq": 4.2, "dP": -2.0},
    "O":  {"tau": 3.0, "freq": 4.5, "dP": -3.0},
    "F":  {"name": "Fluorine", "tau": 3.8, "freq": 4.8, "dP": -4.0},
    "Ne": {"tau": 0.0, "freq": 5.0, "dP":  0.0},
    "Na": {"tau": 3.6, "freq": 5.1, "dP":  2.2},
    "Mg": {"tau": 3.2, "freq": 5.4, "dP":  1.8},
    "Si": {"tau": 1.0, "freq": 6.0, "dP":  0.0},
    "P":  {"tau": 2.5, "freq": 6.2, "dP": -1.8},
    "S":  {"tau": 3.0, "freq": 6.5, "dP": -2.5},
    "Cl": {"tau": 3.8, "freq": 6.8, "dP": -3.8},
    "Ar": {"tau": 0.0, "freq": 7.0, "dP":  0.0},
    "K":  {"name": "Potassium", "tau": 3.6, "freq": 7.1, "dP":  2.3},
    "Ca": {"tau": 3.2, "freq": 7.4, "dP":  1.9},
    "Fe": {"tau": 1.5, "freq": 8.2, "dP":  0.5},
}

# ---------------------------------------------------------------
# FIRST-PRINCIPLES FIELD CALCULATIONS
# ---------------------------------------------------------------
def resonance_coupling(f1, f2):
    """
    Continuous wave-interference coupling based on octave distance
    and harmonic integer proximity. Returns a factor between 0.0 and 1.0.
    """
    ratio = max(f1, f2) / min(f1, f2)
    while ratio >= 2.0:
        ratio /= 2.0  # Octave reduction
    
    # Distance to closest simple harmonic ratio (1:1, 5:4, 4:3, 3:2, 5:3, 2:1)
    simple_ratios = [1.0, 1.25, 1.333, 1.5, 1.666, 1.75, 2.0]
    min_dist = min(abs(ratio - r) for r in simple_ratios)
    
    # Gaussian coupling curve centered on harmonic perfection
    return np.exp(-(min_dist**2) / 0.05)

def compute_reaction(e1, e2):
    """
    Calculates dTau purely from field physics:
      - Initial shear: sum of unbonded torsional states (tau1 + tau2)
      - Coupling: product of frequency resonance and pressure differential
      - Combined shear: reduced by field cancellation efficiency.
    """
    tau1, tau2 = e1["tau"], e2["tau"]
    f1, f2 = e1["freq"], e2["freq"]
    dp1, dp2 = e1["dP"], e2["dP"]
    
    # 1. Harmonic resonance efficiency (0 to 1)
    coupling = resonance_coupling(f1, f2)
    
    # 2. Pressure gradient drive (absolute difference in aether suction)
    dp_drive = abs(dp1 - dp2)
    
    # 3. Noble zero check: if either element has zero shear and zero dP (inert), 
    #    field coupling is blocked.
    if (tau1 == 0.0 and dp1 == 0.0) or (tau2 == 0.0 and dp2 == 0.0):
        return 0.0, "BOUNCE (Harmonic Zero)"

    # 4. Shear cancellation: higher coupling and pressure drive reduce net tension
    cancellation_factor = 0.3 * coupling + 0.1 * dp_drive
    cancellation_factor = min(cancellation_factor, 0.85) # Never 100% cancel
    
    tau_combined = (tau1 + tau2) * (1.0 - cancellation_factor)
    d_tau = tau_combined - (tau1 + tau2)
    
    # Classification based on pressure driver magnitude
    if dp_drive > 3.0:
        archetype = "IONIC SNAP"
    elif coupling > 0.7:
        archetype = "COVALENT LOCK"
    else:
        archetype = "TENSOR / ALLOY"
        
    return d_tau, archetype

# ---------------------------------------------------------------
# EXECUTE
# ---------------------------------------------------------------
def run():
    print("=" * 75)
    print(" SRC FIRST-PRINCIPLES REACTION ENGINE (v0.3)")
    print("=" * 75)
    
    test_pairs = [
        ("H", "Cl"), ("H", "O"), ("Na", "Cl"), ("Mg", "O"),
        ("C", "O"), ("Si", "O"), ("H", "He"), ("Na", "Ar"),
        ("Li", "F"), ("Fe", "O"), ("C", "Ca")
    ]
    
    for s1, s2 in test_pairs:
        e1, e2 = ELEMENTS[s1], ELEMENTS[s2]
        d_tau, arch = compute_reaction(e1, e2)
        energy_out = abs(d_tau) * 120.0 if d_tau < 0 else 0.0
        
        status = "FORMS (Exothermic)" if d_tau < 0 else "REJECTED (No Drive)"
        print(f"\n{s1} + {s2}  ->  Type: {arch}")
        print(f"  dTau   : {d_tau:+.3f}")
        print(f"  Energy : ~{energy_out:.0f} arbitrary scale units")
        print(f"  Result : {status}")

if __name__ == "__main__":
    run()

