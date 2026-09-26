"""
Terminal Capture demonstration + decay-envelope diagnostic.

Models the Moon-arrival EM / Joule / tidal sequence as a compound
pulse train on a genus-1 finite-gap background that carries a
genuine time frequency.  A counterfactual twin (never pulsed) is
evolved in lockstep; the residual shear supplies the transient
peaks, phase-mixing rates γ, and the memory ratio.
"""

from __future__ import annotations

import numpy as np
from .engine import DFMState
from .diagnostics import decay_envelope


def run_capture_demo(scale: float = 1.0):
    # ---------------------------------------------------------------
    # Background geometry (rectangular torus) + time frequency
    # U[:,0] = spatial, U[:,1] = primary hierarchy time
    # ---------------------------------------------------------------
    tau = 1.5j
    Omega = np.array([[tau]], dtype=np.complex128)
    U = np.array([[1.0 + 0j, 0.35 + 0j]], dtype=np.complex128)  # (g, 2)
    Z0 = np.array([0.25 + 0.05j], dtype=np.complex128)

    state = DFMState(Omega, U, Z0, t0=0.0)

    # ---------------------------------------------------------------
    # Compound pulse sequence (amplitudes left numerically convenient;
    # scale= lets a later units convention rescale them without
    # touching the geometric structure)
    # ---------------------------------------------------------------
    impulses = [
        # (dt from previous, delta_Z, label)
        (0.0, scale * (0.35 + 0.12j), "EM_induction"),
        (0.8, scale * (0.12 + 0.04j), "Joule_heating"),
        (2.5, scale * (0.05 + 0.02j), "tidal_lock"),
    ]
    state.inject_compound(impulses)

    # let the system run a little past the last pulse so the final
    # window has room for an envelope fit
    state.evolve(1.5)

    # ---------------------------------------------------------------
    # Counterfactual twin (identical geometry, never pulsed)
    # ---------------------------------------------------------------
    twin = state.twin()
    # advance the twin to the same final time under pure autonomous flow
    twin.evolve(state.t)

    # ---------------------------------------------------------------
    # Decay-envelope diagnostic
    # ---------------------------------------------------------------
    report = decay_envelope(
        state, twin,
        x_ref=0.0,
        window_factor=0.85,
        n_samples=256,
    )

    print("=" * 60)
    print("TERMINAL CAPTURE — compound pulse + decay envelope")
    print("=" * 60)
    print(state.log.summary())
    print()
    print(report.summary())
    print("=" * 60)

    return {
        "state": state,
        "twin": twin,
        "report": report,
    }


if __name__ == "__main__":
    run_capture_demo()
