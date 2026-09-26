"""
Interference run + path-dependent falsifiability sweep.

omega_history / omega_at make residual shear path-dependent.
The sweep now varies the *duration* over which a fixed total ΔΩ
is applied, thereby scanning the dimensionless adiabatic
parameter ε = |Ω̇| / (|U|·|Im Ω|).
"""

from __future__ import annotations

import numpy as np
from .engine import DFMState
from .diagnostics import decay_envelope
from .reconstruction import shear_tensor_1d


def _baseline_capture(scale: float = 1.0):
    Omega = np.array([[1.5j]], dtype=np.complex128)
    U = np.array([[1.0 + 0j, 0.35 + 0j]], dtype=np.complex128)
    Z0 = np.array([0.25 + 0.05j], dtype=np.complex128)
    state = DFMState(Omega, U, Z0)
    state.inject_compound([
        (0.0, scale * (0.35 + 0.12j), "EM_induction"),
        (1.0, scale * (0.12 + 0.04j), "Joule_heating"),
        (2.0, scale * (0.05 + 0.02j), "tidal_lock"),
    ])
    state.evolve(2.0)
    twin = state.twin()
    report = decay_envelope(state, twin, x_ref=0.0, n_samples=128)
    return state, report


def _interference_run(scale: float = 1.0):
    Omega = np.array([[1.5j]], dtype=np.complex128)
    U = np.array([[1.0 + 0j, 0.35 + 0j]], dtype=np.complex128)
    Z0 = np.array([0.25 + 0.05j], dtype=np.complex128)
    state = DFMState(Omega, U, Z0)

    state.inject_pulse(scale * (0.35 + 0.12j), label="EM_induction")
    state.evolve(0.8)
    state.drift_moduli(np.array([[0.04j]]), label="solar_1")

    state.evolve(0.8)
    state.inject_pulse(scale * (0.12 + 0.04j), label="Joule_heating")
    state.evolve(0.8)
    state.drift_moduli(np.array([[0.05j]]), label="solar_2")

    state.evolve(0.8)
    state.inject_pulse(scale * (0.05 + 0.02j), label="tidal_lock")
    state.evolve(2.0)

    twin = state.twin()
    report = decay_envelope(state, twin, x_ref=0.0, n_samples=128)
    return state, report


def _integrated_residual(state: DFMState, twin: DFMState, x_ref: float = 0.0, n: int = 96) -> float:
    ts = np.linspace(0.0, state.t, n)
    pulses = state.log.pulses()
    Z_init = state.Z.copy()
    for e in reversed(pulses):
        if e.delta_Z is not None:
            Z_init = Z_init - e.delta_Z
    if state.U.shape[1] > 1:
        Z_init = Z_init - state.U[:, 1] * state.t

    total = 0.0
    dt = state.t / max(n - 1, 1)
    for ti in ts:
        Z_inj = Z_init.copy()
        for e in pulses:
            if e.time <= ti + 1e-12 and e.delta_Z is not None:
                Z_inj = Z_inj + e.delta_Z
        if state.U.shape[1] > 1:
            Z_inj = Z_inj + state.U[:, 1] * ti
        Z_base = Z_init.copy()
        if twin.U.shape[1] > 1:
            Z_base = Z_base + twin.U[:, 1] * ti

        Om_inj = state.omega_at(ti)
        Om_base = twin.omega_at(ti)
        s = float(np.real(shear_tensor_1d(x_ref, t=[], Omega=Om_inj, U=state.U, Z0=Z_inj)))
        s0 = float(np.real(shear_tensor_1d(x_ref, t=[], Omega=Om_base, U=twin.U, Z0=Z_base)))
        total += abs(s - s0) * dt
    return total


def _drift_rate_sweep(
    total_dOmega: complex = 0.20j,
    durations=(0.5, 1.0, 2.0, 4.0, 8.0, 16.0),
    n_steps: int = 8,
):
    """
    Fixed total ΔΩ, fixed number of steps, varying duration.
    This scans the mean drift rate |Ω̇| = |ΔΩ| / T and therefore
    the dimensionless adiabatic parameter
        ε = |Ω̇| / (|U| · |Im Ω|).
    """
    results = []
    U_time = 0.35
    for T in durations:
        Omega = np.array([[1.5j]], dtype=np.complex128)
        U = np.array([[1.0 + 0j, U_time + 0j]], dtype=np.complex128)
        Z0 = np.array([0.25 + 0.05j], dtype=np.complex128)
        state = DFMState(Omega, U, Z0)
        state.inject_pulse(0.30 + 0.10j, label="probe_pulse")

        step = total_dOmega / n_steps
        dt = T / n_steps
        for i in range(n_steps):
            state.evolve(dt * 0.5)
            state.drift_moduli(np.array([[step]]), label=f"sweep_T{T}_{i}")
            state.evolve(dt * 0.5)

        twin = state.twin()
        integ = _integrated_residual(state, twin)

        omega_dot = abs(total_dOmega) / T
        im_omega = float(np.mean([Om.imag.ravel()[0] for _, Om in state.omega_history]))
        eps = omega_dot / (abs(U_time) * abs(im_omega) + 1e-30)

        n_proj = len([e for e in state.log.events if e.kind == "projection"])
        results.append({
            "duration": T,
            "omega_dot": omega_dot,
            "eps_adiabatic": eps,
            "integrated_residual": integ,
            "n_projections": n_proj,
            "final_ImOmega": float(state.Omega.imag.ravel()[0]),
        })
    return results


def run_interference_demo(scale: float = 1.0):
    print("=" * 64)
    print("INTERFERENCE + PATH-DEPENDENT ADIABATIC SWEEP")
    print("=" * 64)

    base_state, base_report = _baseline_capture(scale)
    print("\n[Baseline — pure capture, no drift]")
    print(base_report.summary())

    int_state, int_report = _interference_run(scale)
    print("\n[Interference — capture during drift]")
    print(int_state.log.summary())
    print()
    print(int_report.summary())

    print("\nMemory survival")
    print(f"  raw |ΔZ| baseline / interference = "
          f"{base_report.total_phase_offset:.6f} / {int_report.total_phase_offset:.6f}")
    print(f"  memory ratio baseline            = {base_report.memory_ratio:.6f}")
    print(f"  memory ratio interference        = {int_report.memory_ratio:.6f}")
    print(f"  relative change in ratio         = "
          f"{(int_report.memory_ratio - base_report.memory_ratio) / (base_report.memory_ratio + 1e-30):+.2%}")

    print("\nγ shift")
    for b, i in zip(base_report.stages, int_report.stages):
        print(f"  {i.label:18s}  γ_base={b.gamma:.4f}  γ_int={i.gamma:.4f}  "
              f"Δγ={i.gamma - b.gamma:+.4f}")

    print("\n[Falsifiability sweep — fixed ΔΩ, varying duration T]")
    print("  ε = |Ω̇| / (|U|·|Im Ω|)   (dimensionless adiabatic parameter)")
    sweep = _drift_rate_sweep()
    for r in sweep:
        proj = f"  proj={r['n_projections']}" if r['n_projections'] else ""
        print(f"  T={r['duration']:5.1f}  |Ω̇|={r['omega_dot']:.4f}  "
              f"ε={r['eps_adiabatic']:.4f}  "
              f"mean|ΔS|={r['integrated_residual']/r['duration']:.6f}  "
              f"ImΩ={r['final_ImOmega']:.4f}{proj}")

    print("\nResidual vs ε (looking for flattening at small ε)")
    for a, b in zip(sweep[:-1], sweep[1:]):
        rel = (b["integrated_residual"] - a["integrated_residual"]) / (
            a["integrated_residual"] + 1e-30
        )
        print(f"  ε={a['eps_adiabatic']:.4f}→{b['eps_adiabatic']:.4f}:  "
              f"Δ(∫|ΔS|)/∫|ΔS| = {rel:+.4%}")

    # crude knee: first point where successive relative change < 1%
    knee = None
    for a, b in zip(sweep[:-1], sweep[1:]):
        ma = a["integrated_residual"] / a["duration"]
        mb = b["integrated_residual"] / b["duration"]
        rel = abs(mb - ma) / (ma + 1e-30)
        if rel < 0.01:
            knee = b
            break
    if knee:
        print(f"\nApproximate ε_crit (rel change < 1%):  ε ≲ {knee['eps_adiabatic']:.4f}")
    else:
        print("\nNo clear knee at the 1% level within this scan; extend durations.")

    print()
    print("Validity condition:")
    print("  |Ω̇| / (|U| · |Im Ω|)  ≪  ε_crit")
    print("with ε_crit read from the flattening of ∫|ΔS| vs ε.")
    print("=" * 64)

    return {
        "baseline": (base_state, base_report),
        "interference": (int_state, int_report),
        "sweep": sweep,
    }


if __name__ == "__main__":
    run_interference_demo()
