"""
Adiabatic moduli-drift demonstration.

A slow change in the period matrix Omega models solar-driven (or
cosmologically driven) evolution of the DFM substrate.  Because the
drift is applied between ordinary phase steps, the hierarchy
invariants are preserved and the event log records the geometric
history as first-class data.
"""

from __future__ import annotations

import numpy as np
from .engine import DFMState


def run_adiabatic_demo():
    # genus-1 background with a mild time frequency
    tau0 = 1.5j
    Omega = np.array([[tau0]], dtype=np.complex128)
    U = np.array([[1.0 + 0j, 0.25 + 0j]], dtype=np.complex128)
    Z0 = np.array([0.2 + 0.0j], dtype=np.complex128)

    state = DFMState(Omega, U, Z0)

    # sample shear before any drift
    x = np.linspace(-6.0, 6.0, 201)
    s_before = state.shear(x)
    Omega_before = state.Omega.copy()

    # slow drift schedule: three small increments of Im(tau)
    # (increasing the imaginary part stretches the torus and
    # softens the cnoidal profile)
    schedule = [
        (1.0, np.array([[0.05j]]), "solar_step_1"),
        (1.5, np.array([[0.05j]]), "solar_step_2"),
        (2.0, np.array([[0.08j]]), "solar_step_3"),
    ]
    state.adiabatic_schedule(schedule)

    # continue autonomous evolution a little further
    state.evolve(1.0)

    s_after = state.shear(x)
    Omega_after = state.Omega.copy()

    print("=" * 60)
    print("ADIABATIC MODULI DRIFT — solar-driven Omega(t)")
    print("=" * 60)
    print(state.log.summary())
    print()
    print(f"Omega before : {Omega_before.ravel()}")
    print(f"Omega after  : {Omega_after.ravel()}")
    print(f"|ΔOmega|     : {np.linalg.norm(Omega_after - Omega_before):.6f}")
    print(f"max |Δshear| : {np.max(np.abs(s_after - s_before)):.6f}")
    print(f"final t      : {state.t:.3f}")
    print()
    print("The phase vector continued to evolve under the hierarchy")
    print("while the background geometry was slowly deformed.")
    print("All changes are recorded in the event log.")
    print("=" * 60)

    return {
        "state": state,
        "x": x,
        "s_before": s_before,
        "s_after": s_after,
    }


if __name__ == "__main__":
    run_adiabatic_demo()
