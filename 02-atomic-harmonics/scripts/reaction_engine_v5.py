"""
SRC Recursive Reaction Engine v0.5
Scalar Relaxation Cosmology - Atomic Harmonics Module

v0.5 principle: an interlocked partner engages its ENTIRE open boundary
configuration. The host loses boundary positions equal to the partner's
open-slot count. Assembly auto-orients around the node with the most
open boundary positions (the structural center).

Emergent stoichiometry: CH4, OH2 (water), NH3, CO2, SiO2, CCl4, MgCl2,
AlCl3, NaCl all fall out of boundary capacities. No lookup tables.

Honest notes:
 - Saturation is GEOMETRIC (boundary fully engaged), not an energy
   threshold; residual tau is the molecule's stored tension.
 - Multiple bonds (C=O) are approximated by full-boundary engagement;
   true phase geometry (the V vector) is not yet modeled.
"""

import numpy as np

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

# E = (tau, f, dP, slots)   slots = open boundary positions
ELEMENTS = {
    "H":  {"tau": 2.0, "freq": 1.0, "dP": -1.5, "slots": 1},
    "He": {"tau": 0.0, "freq": 2.0, "dP":  0.0, "slots": 0},
    "Li": {"tau": 3.5, "freq": 2.1, "dP":  2.0, "slots": 1},
    "Be": {"tau": 3.0, "freq": 2.4, "dP":  1.5, "slots": 2},
    "B":  {"tau": 1.2, "freq": 3.8, "dP": -0.5, "slots": 3},
    "C":  {"tau": 1.0, "freq": 4.0, "dP":  0.0, "slots": 4},
    "N":  {"tau": 2.5, "freq": 4.2, "dP": -2.0, "slots": 3},
    "O":  {"tau": 3.0, "freq": 4.5, "dP": -3.0, "slots": 2},
    "F":  {"tau": 3.8, "freq": 4.8, "dP": -4.0, "slots": 1},
    "Ne": {"tau": 0.0, "freq": 5.0, "dP":  0.0, "slots": 0},
    "Na": {"tau": 3.6, "freq": 5.1, "dP":  2.2, "slots": 1},
    "Mg": {"tau": 3.2, "freq": 5.4, "dP":  1.8, "slots": 2},
    "Al": {"tau": 1.5, "freq": 5.6, "dP":  0.3, "slots": 3},
    "Si": {"tau": 1.0, "freq": 6.0, "dP":  0.0, "slots": 4},
    "P":  {"tau": 2.5, "freq": 6.2, "dP": -1.8, "slots": 3},
    "S":  {"tau": 3.0, "freq": 6.5, "dP": -2.5, "slots": 2},
    "Cl": {"tau": 3.8, "freq": 6.8, "dP": -3.8, "slots": 1},
    "Ar": {"tau": 0.0, "freq": 7.0, "dP":  0.0, "slots": 0},
    "K":  {"tau": 3.6, "freq": 7.1, "dP":  2.3, "slots": 1},
    "Ca": {"tau": 3.2, "freq": 7.4, "dP":  1.9, "slots": 2},
    "Fe": {"tau": 1.5, "freq": 8.2, "dP":  0.5, "slots": 3},
    "Cu": {"tau": 1.6, "freq": 8.5, "dP": -0.4, "slots": 2},
    "Zn": {"tau": 1.8, "freq": 8.8, "dP":  0.8, "slots": 2},
    "Br": {"tau": 3.6, "freq": 9.0, "dP": -3.4, "slots": 1},
}

KJ_PER_TAU = 120.0   # calibration constant

# ---------------------------------------------------------------
# FIELD FUNCTIONS
# ---------------------------------------------------------------
def resonance_coupling(f1, f2):
    """Octave-reduced harmonic coupling, 0..1."""
    ratio = max(f1, f2) / min(f1, f2)
    while ratio >= 2.0:
        ratio /= 2.0
    simple = [1.0, 1.25, 1.333, 1.5, 1.666, 1.75, 2.0]
    d = min(abs(ratio - r) for r in simple)
    return float(np.exp(-(d ** 2) / 0.05))

def is_harmonic_zero(n):
    return n["tau"] == 0.0 and n["dP"] == 0.0

def make_node(sym):
    e = ELEMENTS[sym]
    return {"comp": {sym: 1}, "tau": e["tau"], "freq": e["freq"],
            "dP": e["dP"], "slots": e["slots"]}

def render(comp):
    """Composition-counted formula with subscripts (assembly order)."""
    s = ""
    for el, n in comp.items():
        s += el + (str(n) if n > 1 else "")
    return s.translate(SUB)

def pair_dtau(n1, n2):
    """Field interaction between two nodes. (d_tau, archetype) or (None, reason)."""
    if is_harmonic_zero(n1) or is_harmonic_zero(n2):
        return None, "BOUNCE (harmonic zero)"
    if n1["slots"] <= 0 or n2["slots"] <= 0:
        return None, "SATURATED (no open boundary)"
    coup = resonance_coupling(n1["freq"], n2["freq"])
    drive = abs(n1["dP"] - n2["dP"])
    cancel = min(0.3 * coup + 0.1 * drive, 0.85)
    tau_sum = n1["tau"] + n2["tau"]
    d = tau_sum * (1.0 - cancel) - tau_sum
    if drive > 3.0:
        arch = "IONIC SNAP"
    elif coup > 0.7:
        arch = "COVALENT LOCK"
    else:
        arch = "TENSOR LOCK"
    return d, arch

def merge(host, partner):
    """The bond product is a NEW NODE with a derived tuple.
    The partner's ENTIRE open boundary engages the host."""
    cancel = min(0.3 * resonance_coupling(host["freq"], partner["freq"])
                 + 0.1 * abs(host["dP"] - partner["dP"]), 0.85)
    tau_sum = host["tau"] + partner["tau"]
    comp = dict(host["comp"])
    for el, cnt in partner["comp"].items():
        comp[el] = comp.get(el, 0) + cnt
    consumed = min(partner["slots"], host["slots"])
    return {
        "comp": comp,
        "tau": tau_sum * (1.0 - cancel),
        "freq": 2.0 / (1.0 / host["freq"] + 1.0 / partner["freq"]),
        "dP": (host["dP"] + partner["dP"]) / 2.0,
        "slots": host["slots"] - consumed,
    }

# ---------------------------------------------------------------
# RECURSIVE ASSEMBLY
# ---------------------------------------------------------------
def react(sym_a, sym_b, max_steps=6, verbose=True):
    # Auto-orient: assembly centers on the node with the most
    # open boundary positions (the structural hub).
    a, b = make_node(sym_a), make_node(sym_b)
    if b["slots"] > a["slots"]:
        host_sym, partner_sym = sym_b, sym_a
    else:
        host_sym, partner_sym = sym_a, sym_b
    host = make_node(host_sym)

    if verbose:
        print(f"\n--- {sym_a} + {sym_b} ---")
        print(f"    assembly centers on {host_sym} "
              f"({host['slots']} open boundary positions)")

    total = 0.0
    for step in range(max_steps):
        partner = make_node(partner_sym)      # fresh partner from the bath
        d, arch = pair_dtau(host, partner)
        if d is None:
            if verbose:
                print(f"  STOP: {arch}")
            break
        if d >= 0:
            if verbose:
                print(f"  STOP: dTau = {d:+.3f} (no further drive)")
            break

        new = merge(host, partner)
        e = -d * KJ_PER_TAU
        total += e
        if verbose:
            print(f"  {render(host['comp'])} + {partner_sym} -> "
                  f"{render(new['comp'])}   [{arch}]  dTau={d:+.3f}"
                  f"  E~{e:.0f}  open slots={new['slots']}")
        host = new

        if host["slots"] <= 0:
            if verbose:
                print(f"  SATURATION: {render(host['comp'])} — boundary"
                      " fully engaged, geometric rest.")
            break

    if verbose:
        print(f"  Product: {render(host['comp'])}"
              f"   Total released: ~{total:.0f} scale units")
    return host, total

# ---------------------------------------------------------------
# DEMONSTRATIONS
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 75)
    print(" SRC RECURSIVE REACTION ENGINE v0.5")
    print("=" * 75)

    print("\n### The CO vs CO2 question")
    react("C", "O")

    print("\n### Recursive saturation: methane")
    react("C", "H")

    print("\n### Water")
    react("O", "H")

    print("\n### Ammonia")
    react("N", "H")

    print("\n### Salts and oxides")
    react("Na", "Cl")
    react("Mg", "O")
    react("Mg", "Cl")
    react("Al", "Cl")

    print("\n### Lattice formers")
    react("Si", "O")
    react("C", "Cl")

    print("\n### Noble rejection")
    react("H", "He")
    react("Na", "Ar")

