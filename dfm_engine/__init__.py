"""
DFM finite-gap engine
"""

from .theta import riemann_theta, log_theta_derivatives
from .reconstruction import (
    kp_potential,
    scalar_potential,
    current_density,
    shear_tensor_1d,
)
from .events import Event, EventLog, apply_pulse, apply_moduli_drift
from .engine import DFMState
from .diagnostics import decay_envelope, EnvelopeReport, StageResult
from .chart import ToroidalChart, shear_tensor_3d, shear_eigenvalues, trace_check

__all__ = [
    "riemann_theta",
    "log_theta_derivatives",
    "kp_potential",
    "scalar_potential",
    "current_density",
    "shear_tensor_1d",
    "Event",
    "EventLog",
    "apply_pulse",
    "apply_moduli_drift",
    "DFMState",
    "decay_envelope",
    "EnvelopeReport",
    "StageResult",
    "ToroidalChart",
    "shear_tensor_3d",
    "shear_eigenvalues",
    "trace_check",
]
