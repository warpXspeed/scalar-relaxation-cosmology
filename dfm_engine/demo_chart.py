"""
Toroidal chart lift of the Terminal Capture sequence.

Runs the compound pulse train, evaluates the 3-D traceless shear
tensor on the toroidal chart at a fixed laboratory point, and
reports the eigenvalue tracks (poloidal / toroidal shear) together
with the trace-consistency check.
"""

from __future__ import annotations

import numpy as np
from .engine import DFMState
from .chart import ToroidalChart, shear_tensor_3d, shear_eigenvalues, trace_check


def run_chart_demo():
    Omega = np.array([[1.5j]], dtype=np.complex128)
    U = np.array([[1.0 + 0j, 0.35 + 0j]], dtype=np.complex128)
    Z0 = np.array([0.25 + 0.05j], dtype=np.complex128)
    state = DFMState(Omega, U, Z0)

    chart = ToroidalChart(R=1.0, r=0.3)

    # capture sequence
    impulses = [
        (0.0, 0.35 + 0.12j, "EM_induction"),
        (1.0, 0.12 + 0.04j, "Joule_heating"),
        (2.0, 0.05 + 0.02j, "tidal_lock"),
    ]
    # sample times: just before each pulse and after the last
    sample_times = []
    labels = []

    state.inject_pulse(impulses[0][1], label=impulses[0][2])
    sample_times.append(state.t)
    labels.append("post EM_induction")

    state.evolve(impulses[1][0])
    state.inject_pulse(impulses[1][1], label=impulses[1][2])
    sample_times.append(state.t)
    labels.append("post Joule_heating")

    state.evolve(impulses[2][0])
    state.inject_pulse(impulses[2][1], label=impulses[2][2])
    sample_times.append(state.t)
    labels.append("post tidal_lock")

    state.evolve(1.5)
    sample_times.append(state.t)
    labels.append("final")

    x_ref = 0.0
    print("=" * 64)
    print("TOROIDAL CHART LIFT — Terminal Capture eigenvalue tracks")
    print("=" * 64)
    print(f"Chart: R={chart.R}, r={chart.r}")
    print()

    max_trace = 0.0
    for t_label, lab in zip(sample_times, labels):
        # advance a temporary view is unnecessary; we already stopped
        # at each sample.  Re-create a snapshot state at the recorded
        # times by using the current final state only for the last
        # point; for intermediate points we recompute S from the
        # phase that existed then via a lightweight replay.
        pass

    # simpler: evaluate at the final state for the consistency check,
    # and also walk the pulse log to show the sequenced pattern
    print(f"{'stage':22s}  {'λ1':>10s}  {'λ2':>10s}  {'λ3':>10s}  {'|tr S|':>10s}")
    print("-" * 64)

    # replay from initial condition to each stage
    Z = Z0.copy()
    Om = Omega.copy()
    t = 0.0
    stages = [
        (0.0, 0.35 + 0.12j, "post EM_induction"),
        (1.0, 0.12 + 0.04j, "post Joule_heating"),
        (2.0, 0.05 + 0.02j, "post tidal_lock"),
        (1.5, None, "final"),
    ]
    for dt, delta, lab in stages:
        if dt > 0:
            Z = Z + U[:, 1] * dt
            t += dt
        if delta is not None:
            Z = Z + np.asarray(delta, dtype=np.complex128)

        snap = DFMState(Om, U, Z, t0=t)
        S = shear_tensor_3d(x_ref, snap, chart)
        w, _ = shear_eigenvalues(S)
        tr = trace_check(S)
        max_trace = max(max_trace, tr)
        print(f"{lab:22s}  {w[0]:10.6f}  {w[1]:10.6f}  {w[2]:10.6f}  {tr:10.2e}")

    print("-" * 64)
    print(f"max |tr S| across stages = {max_trace:.2e}")
    if max_trace < 1e-12:
        print("Trace consistency: PASS (machine-precision traceless)")
    else:
        print("Trace consistency: FAIL — chart gradient lift has an error")
    print("=" * 64)

    return {"max_trace": max_trace}


if __name__ == "__main__":
    run_chart_demo()
