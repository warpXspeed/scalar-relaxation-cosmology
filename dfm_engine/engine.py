"""
DFM finite-gap simulation engine.

Holds the geometric state (Omega, U, Z), the event log, the moduli
trajectory, and provides methods for autonomous phase evolution,
pulse injection, and adiabatic moduli drift.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .events import EventLog, apply_pulse, apply_moduli_drift, Event
from .reconstruction import scalar_potential, shear_tensor_1d, current_density


class DFMState:
    """
    Complete finite-gap state of the Dynamic Fluid Medium.

    - Omega         : current period matrix
    - omega_history : list of (t, Omega) snapshots (piecewise-constant)
    - U             : frequency vectors
    - Z             : current phase vector
    - t             : current hierarchy time
    - log           : explicit ledger of pulses, drifts, projections
    """

    def __init__(
        self,
        Omega: ArrayLike,
        U: ArrayLike,
        Z0: ArrayLike,
        t0: float = 0.0,
    ):
        self.Omega = np.asarray(Omega, dtype=np.complex128).copy()
        self.U = np.asarray(U, dtype=np.complex128)
        self.Z = np.asarray(Z0, dtype=np.complex128).copy()
        self.t = float(t0)
        self.log = EventLog()
        # moduli trajectory — piecewise constant between drifts
        self.omega_history: list[tuple[float, NDArray]] = [
            (self.t, self.Omega.copy())
        ]

        g = self.Omega.shape[0]
        assert self.U.shape[0] == g
        assert self.Z.shape == (g,)
        assert self.Omega.shape == (g, g)

    # ------------------------------------------------------------------
    # Moduli accessor (piecewise-constant)
    # ------------------------------------------------------------------
    def omega_at(self, t: float) -> NDArray:
        """
        Return the period matrix that was active at time t.
        Piecewise-constant: last snapshot with snapshot_time <= t.
        Exactly matches the engine's discrete adiabatic steps.
        """
        if not self.omega_history:
            return self.Omega.copy()
        # history is kept in chronological order
        active = self.omega_history[0][1]
        for ts, Om in self.omega_history:
            if ts <= t + 1e-14:
                active = Om
            else:
                break
        return active.copy()

    # ------------------------------------------------------------------
    # Autonomous evolution (inner loop)
    # ------------------------------------------------------------------
    def evolve(self, dt: float) -> None:
        """Advance phase only; Omega stays fixed unless drift is called."""
        if self.U.shape[1] > 1:
            self.Z = self.Z + self.U[:, 1] * dt
        self.t += dt

    # ------------------------------------------------------------------
    # Pulse injection
    # ------------------------------------------------------------------
    def inject_pulse(
        self,
        delta_Z: ArrayLike,
        label: str = "",
        meta: dict | None = None,
    ) -> None:
        self.Z = apply_pulse(
            self.Z, delta_Z, log=self.log, time=self.t,
            label=label, meta=meta,
        )

    def inject_compound(
        self,
        impulses: list[tuple[float, ArrayLike, str]],
    ) -> None:
        for dt, delta, label in impulses:
            if dt > 0:
                self.evolve(dt)
            self.inject_pulse(delta, label=label)

    # ------------------------------------------------------------------
    # Adiabatic outer loop
    # ------------------------------------------------------------------
    def drift_moduli(
        self,
        delta_Omega: ArrayLike,
        label: str = "",
        meta: dict | None = None,
        enforce_posdef: bool = True,
    ) -> None:
        """
        Apply an adiabatic change to Omega and append to omega_history.
        If the positive-definite projection activates, a separate
        'projection' event is logged so the sweep can detect geometric
        clipping.
        """
        delta = np.asarray(delta_Omega, dtype=np.complex128)
        proposed = self.Omega + delta
        projected = False

        if enforce_posdef:
            Im = proposed.imag
            eigvals = np.linalg.eigvalsh(Im)
            if eigvals.min() <= 0:
                w, v = np.linalg.eigh(Im)
                w = np.maximum(w, 1e-8)
                Im_fixed = (v * w) @ v.T.conj()
                proposed = proposed.real + 1j * Im_fixed
                projected = True

        applied_delta = proposed - self.Omega
        self.Omega = apply_moduli_drift(
            self.Omega, applied_delta, log=self.log,
            time=self.t, label=label, meta=meta,
        )
        self.Omega = proposed
        self.omega_history.append((self.t, self.Omega.copy()))

        if projected:
            self.log.record(Event(
                time=self.t,
                kind="projection",
                label=f"posdef_clip:{label}",
                meta={"eig_min_before": float(eigvals.min())},
            ))

    def adiabatic_schedule(
        self,
        schedule: list[tuple[float, ArrayLike, str]],
    ) -> None:
        for dt, dOmega, label in schedule:
            if dt > 0:
                self.evolve(dt)
            self.drift_moduli(dOmega, label=label)

    # ------------------------------------------------------------------
    # Observables (use current Omega)
    # ------------------------------------------------------------------
    def potential(self, x: ArrayLike, radius: int | None = None) -> NDArray:
        return scalar_potential(
            x, t=[], Omega=self.Omega, U=self.U, Z0=self.Z, radius=radius
        )

    def shear(self, x: ArrayLike, radius: int | None = None) -> NDArray:
        return shear_tensor_1d(
            x, t=[], Omega=self.Omega, U=self.U, Z0=self.Z, radius=radius
        )

    def current(self, x: float, radius: int | None = None) -> complex:
        return current_density(
            x, t=[], Omega=self.Omega, U=self.U, Z0=self.Z, radius=radius
        )

    # ------------------------------------------------------------------
    # Counterfactual
    # ------------------------------------------------------------------
    def twin(self) -> "DFMState":
        """
        Counterfactual that shares the full omega_history (same
        background geometry trajectory) but recovers the pre-pulse
        initial phase and carries an empty pulse log.
        """
        Z0 = self.Z.copy()
        for e in reversed(self.log.pulses()):
            if e.delta_Z is not None:
                Z0 = Z0 - e.delta_Z
        if self.U.shape[1] > 1:
            Z0 = Z0 - self.U[:, 1] * self.t

        # start from the earliest Omega in the history
        Om0 = self.omega_history[0][1]
        twin = DFMState(Om0, self.U.copy(), Z0, t0=0.0)
        # replay the moduli trajectory without pulses
        for ts, Om in self.omega_history[1:]:
            twin.t = ts
            twin.Omega = Om.copy()
            twin.omega_history.append((ts, Om.copy()))
            # record a silent drift so the log structure matches
            twin.log.record(Event(
                time=ts, kind="moduli_drift",
                delta_Omega=Om - twin.omega_history[-2][1],
                label="twin_replay",
            ))
        twin.t = self.t
        twin.Omega = self.Omega.copy()
        # advance phase under autonomous hierarchy so twin.Z matches
        # the no-pulse counterfactual at final time
        if self.U.shape[1] > 1:
            twin.Z = twin.Z + self.U[:, 1] * self.t
        return twin

    def snapshot(self) -> dict:
        return {
            "t": self.t,
            "Z": self.Z.copy(),
            "Omega": self.Omega.copy(),
            "n_events": len(self.log.events),
            "n_omega_snapshots": len(self.omega_history),
        }

    def __repr__(self) -> str:
        return (
            f"DFMState(g={self.Omega.shape[0]}, t={self.t:.4f}, "
            f"events={len(self.log.events)}, "
            f"Ω-snaps={len(self.omega_history)})"
        )
