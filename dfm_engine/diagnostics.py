"""
Decay-envelope diagnostic for pulse trains.

Compares an injected DFMState against a counterfactual twin.
Both states carry omega_history; residual shear is evaluated with
the period matrix that was actually active at each sample time
(piecewise-constant).  This makes γ and integrated residuals
path-dependent and turns the drift-rate sweep into a real
adiabatic-threshold extractor.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass

from .engine import DFMState
from .reconstruction import shear_tensor_1d


@dataclass
class StageResult:
    label: str
    t_pulse: float
    peak: float
    gamma: float
    window: float


@dataclass
class EnvelopeReport:
    stages: list[StageResult]
    total_phase_offset: float
    sum_peaks: float
    memory_ratio: float

    def summary(self) -> str:
        lines = ["Decay-envelope report"]
        lines.append("-" * 50)
        for s in self.stages:
            lines.append(
                f"  {s.label:18s}  t={s.t_pulse:7.3f}  "
                f"peak={s.peak:8.4f}  γ={s.gamma:8.4f}"
            )
        lines.append("-" * 50)
        lines.append(f"  |ΔZ_total|          = {self.total_phase_offset:.6f}")
        lines.append(f"  sum of peaks        = {self.sum_peaks:.6f}")
        lines.append(f"  memory ratio        = {self.memory_ratio:.6f}")
        lines.append("")
        lines.append(
            "Note: γ measures phase mixing against the multi-frequency "
            "theta background, not dissipative energy loss. "
            "Ω(t) is taken from each state's omega_history "
            "(piecewise-constant)."
        )
        return "\n".join(lines)


def _fit_exponential(dt: NDArray, resid: NDArray) -> float:
    mask = resid > 1e-12 * (resid.max() + 1e-30)
    if mask.sum() < 4:
        return 0.0
    t = dt[mask]
    y = np.log(resid[mask])
    A = np.vstack([np.ones_like(t), -t]).T
    try:
        coeff, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        return max(float(coeff[1]), 0.0)
    except Exception:
        return 0.0


def _phase_at(Z_init: NDArray, U: NDArray, pulses: list, t: float) -> NDArray:
    Z = Z_init.copy()
    for e in pulses:
        if e.time <= t + 1e-12 and e.delta_Z is not None:
            Z = Z + e.delta_Z
    if U.shape[1] > 1:
        Z = Z + U[:, 1] * t
    return Z


def decay_envelope(
    state: DFMState,
    twin: DFMState,
    x_ref: float = 0.0,
    window_factor: float = 0.85,
    n_samples: int = 256,
    radius: int | None = None,
) -> EnvelopeReport:
    pulses = state.log.pulses()
    if not pulses:
        raise ValueError("state has no recorded pulses")

    # recover common initial phase
    Z_init = state.Z.copy()
    for e in reversed(pulses):
        if e.delta_Z is not None:
            Z_init = Z_init - e.delta_Z
    if state.U.shape[1] > 1:
        Z_init = Z_init - state.U[:, 1] * state.t

    t_pulses = [e.time for e in pulses]
    t_final = state.t
    t_edges = t_pulses + [t_final]

    stages: list[StageResult] = []
    sum_peaks = 0.0

    for k, ev in enumerate(pulses):
        t_k = ev.time
        t_next = t_edges[k + 1]
        window = max((t_next - t_k) * window_factor, 1e-6)
        ts = np.linspace(t_k, t_k + window, n_samples)
        resid = np.empty(n_samples, dtype=float)

        for i, ti in enumerate(ts):
            Z_inj = _phase_at(Z_init, state.U, pulses, ti)
            Z_base = _phase_at(Z_init, twin.U, [], ti)

            # path-dependent Omega
            Om_inj = state.omega_at(ti)
            Om_base = twin.omega_at(ti)

            s_inj = float(np.real(shear_tensor_1d(
                x_ref, t=[], Omega=Om_inj, U=state.U, Z0=Z_inj, radius=radius
            )))
            s_base = float(np.real(shear_tensor_1d(
                x_ref, t=[], Omega=Om_base, U=twin.U, Z0=Z_base, radius=radius
            )))
            resid[i] = abs(s_inj - s_base)

        peak = float(resid.max())
        gamma = _fit_exponential(ts - t_k, resid)
        sum_peaks += peak

        stages.append(StageResult(
            label=ev.label or f"pulse_{k}",
            t_pulse=t_k,
            peak=peak,
            gamma=gamma,
            window=window,
        ))

    # Permanent phase memory is the net pulse content, not the
    # difference of final Z vectors (the latter also contains
    # autonomous hierarchy evolution that both trajectories share).
    net_pulse = np.zeros_like(state.Z)
    for e in pulses:
        if e.delta_Z is not None:
            net_pulse = net_pulse + e.delta_Z
    total_offset = float(np.linalg.norm(net_pulse))
    memory_ratio = total_offset / sum_peaks if sum_peaks > 1e-30 else 0.0

    return EnvelopeReport(
        stages=stages,
        total_phase_offset=total_offset,
        sum_peaks=sum_peaks,
        memory_ratio=memory_ratio,
    )
