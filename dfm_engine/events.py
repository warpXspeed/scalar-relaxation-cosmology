"""
Event log and pulse-injection / moduli-drift primitives for the DFM engine.

Every discontinuous jump in the phase vector Z or slow change in the
period matrix Omega is recorded as a first-class Event.  The log is
the explicit geological / intervention history of the substrate; the
tau-function already encodes the same information implicitly.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass
class Event:
    """A single discontinuity or slow geometric change written into the aether."""
    time: float
    kind: str                            # "pulse", "moduli_drift", ...
    delta_Z: NDArray[np.complex128] | None = None
    delta_Omega: NDArray[np.complex128] | None = None
    label: str = ""
    meta: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.delta_Z is not None:
            self.delta_Z = np.asarray(self.delta_Z, dtype=np.complex128)
        if self.delta_Omega is not None:
            self.delta_Omega = np.asarray(self.delta_Omega, dtype=np.complex128)


class EventLog:
    """Ordered ledger of all discontinuities and moduli changes."""

    def __init__(self):
        self.events: list[Event] = []

    def record(self, event: Event) -> None:
        self.events.append(event)
        self.events.sort(key=lambda e: e.time)

    def pulses(self) -> list[Event]:
        return [e for e in self.events if e.kind == "pulse"]

    def drifts(self) -> list[Event]:
        return [e for e in self.events if e.kind == "moduli_drift"]

    def summary(self) -> str:
        lines = [f"EventLog ({len(self.events)} entries)"]
        for e in self.events:
            extra = e.label or ""
            if e.delta_Z is not None:
                extra += f"  |ΔZ|={np.linalg.norm(e.delta_Z):.4g}"
            if e.delta_Omega is not None:
                extra += f"  |ΔΩ|={np.linalg.norm(e.delta_Omega):.4g}"
            lines.append(f"  t={e.time:8.3f}  {e.kind:12s}  {extra}")
        return "\n".join(lines)


def apply_pulse(
    Z: NDArray[np.complex128],
    delta_Z: ArrayLike,
    log: EventLog | None = None,
    time: float = 0.0,
    label: str = "",
    meta: dict | None = None,
) -> NDArray[np.complex128]:
    """
    Instantaneous divisor / phase jump.

    Omega is left untouched; the phase configuration is permanently
    shifted.  Subsequent autonomous evolution never returns to the
    pre-pulse state.
    """
    delta = np.asarray(delta_Z, dtype=np.complex128)
    Z_new = Z + delta
    if log is not None:
        log.record(Event(
            time=time,
            kind="pulse",
            delta_Z=delta,
            label=label,
            meta=meta or {},
        ))
    return Z_new


def apply_moduli_drift(
    Omega: NDArray[np.complex128],
    delta_Omega: ArrayLike,
    log: EventLog | None = None,
    time: float = 0.0,
    label: str = "",
    meta: dict | None = None,
) -> NDArray[np.complex128]:
    """
    Adiabatic change of the period matrix.

    The drift is assumed slow relative to the phase dynamics so that
    the hierarchy invariants are preserved (no memory leak).  The
    change is recorded in the event log as first-class geometric
    history.
    """
    delta = np.asarray(delta_Omega, dtype=np.complex128)
    Omega_new = Omega + delta
    # enforce positive-definiteness of Im(Omega) at the call site if needed
    if log is not None:
        log.record(Event(
            time=time,
            kind="moduli_drift",
            delta_Omega=delta,
            label=label,
            meta=meta or {},
        ))
    return Omega_new
