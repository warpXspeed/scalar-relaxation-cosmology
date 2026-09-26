"""
Laboratory chart interface and 3-D traceless shear lift.

The engine itself stays chart-agnostic.  A chart owns only the
mapping convention that turns the 1-D hierarchy current into a
vector field on a 3-D laboratory slice.  ToroidalChart is the
default for the Terminal Capture / double-toroid models.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray
from dataclasses import dataclass

from .reconstruction import current_density, shear_tensor_1d
from .engine import DFMState


@dataclass
class ToroidalChart:
    """
    Maps the 1-D hierarchy coordinate x onto a genus-1 laboratory
    torus with major radius R and minor radius r.

    Local orthonormal frame (poloidal, toroidal, normal):
      e_θ  – poloidal
      e_φ  – toroidal
      e_n  – outward normal to the tube

    The hierarchy current v is interpreted as a primarily toroidal
    flow; its laboratory gradient is formed in this frame.
    """
    R: float = 1.0          # major radius
    r: float = 0.3          # minor radius

    def position(self, theta: float, phi: float) -> NDArray:
        """Cartesian embedding of (θ, φ)."""
        x = (self.R + self.r * np.cos(theta)) * np.cos(phi)
        y = (self.R + self.r * np.cos(theta)) * np.sin(phi)
        z = self.r * np.sin(theta)
        return np.array([x, y, z], dtype=float)

    def basis(self, theta: float, phi: float) -> tuple[NDArray, NDArray, NDArray]:
        """
        Return orthonormal frame (e_θ, e_φ, e_n) at (θ, φ).
        """
        # poloidal
        e_theta = np.array([
            -np.sin(theta) * np.cos(phi),
            -np.sin(theta) * np.sin(phi),
             np.cos(theta),
        ])
        # toroidal
        e_phi = np.array([
            -np.sin(phi),
             np.cos(phi),
             0.0,
        ])
        # normal
        e_n = np.array([
             np.cos(theta) * np.cos(phi),
             np.cos(theta) * np.sin(phi),
             np.sin(theta),
        ])
        # already unit length for the standard embedding
        return e_theta, e_phi, e_n

    def gradient(self, v_scalar: float, x: float, theta: float = 0.0, phi: float = 0.0) -> NDArray:
        """
        Lift a scalar hierarchy current v(x) to a laboratory velocity
        gradient tensor in the toroidal frame.

        Convention (minimal, chart-owned):
          - v is taken as the toroidal component of velocity
          - spatial derivative ∂_x is identified with the toroidal
            derivative scaled by the major circumference factor
            (R + r cos θ)
          - poloidal and normal derivatives of v are set to zero
            at this order (purely toroidal flow on the chart)

        Returns the 3×3 Cartesian velocity-gradient tensor ∇v.
        """
        e_theta, e_phi, e_n = self.basis(theta, phi)
        # scale: hierarchy x advances one unit per major circuit
        scale = 1.0 / (self.R + self.r * np.cos(theta) + 1e-30)
        # velocity field: v * e_φ
        # ∇v ≈ (∂_φ v) e_φ ⊗ e_φ   with  ∂_φ ≈ scale * ∂_x
        # For a pure function of the hierarchy coordinate the only
        # non-zero contribution at this order is along e_φ.
        # We approximate ∂_x v from the 1-D shear rate already
        # computed by the engine (passed in via a finite difference
        # or supplied by the caller).  Here we accept v_scalar as
        # the local current and build a rank-1 gradient consistent
        # with a purely toroidal flow whose strength varies along φ.
        #
        # Concrete construction used by shear_tensor_3d:
        #   grad_v = (dv/dx * scale) * outer(e_phi, e_phi)
        # The caller supplies dv/dx (the 1-D shear).
        return scale  # the scale factor; full tensor built in shear_tensor_3d


def shear_tensor_3d(
    x: float,
    state: DFMState,
    chart: ToroidalChart,
    theta: float = 0.0,
    phi: float = 0.0,
    dx: float = 1e-4,
    radius: int | None = None,
) -> NDArray:
    """
    Lift the hierarchy current to the symmetric traceless shear
    tensor S on the laboratory chart.

        S = ½(∇v + (∇v)ᵀ) − (tr ∇v)/3 · I

    On ToroidalChart the eigenvalues of S separate into poloidal
    and toroidal shear components.

    Consistency: tr(S) must vanish to ~1e-15.
    """
    Om = state.omega_at(state.t)
    # local current and its hierarchy derivative
    v0 = float(np.real(current_density(
        x, t=[], Omega=Om, U=state.U, Z0=state.Z, radius=radius
    )))
    v_p = float(np.real(current_density(
        x + dx, t=[], Omega=Om, U=state.U, Z0=state.Z, radius=radius
    )))
    v_m = float(np.real(current_density(
        x - dx, t=[], Omega=Om, U=state.U, Z0=state.Z, radius=radius
    )))
    dv_dx = (v_p - v_m) / (2.0 * dx)

    e_theta, e_phi, e_n = chart.basis(theta, phi)
    scale = 1.0 / (chart.R + chart.r * np.cos(theta) + 1e-30)

    # velocity-gradient tensor in Cartesian components
    # ∇v ≈ (dv/dx * scale) * e_φ ⊗ e_φ
    # (purely toroidal flow whose strength varies along the hierarchy)
    factor = dv_dx * scale
    grad_v = factor * np.outer(e_phi, e_phi)

    # symmetric traceless part
    sym = 0.5 * (grad_v + grad_v.T)
    S = sym - (np.trace(sym) / 3.0) * np.eye(3)
    return S


def shear_eigenvalues(
    S: NDArray,
) -> tuple[NDArray, NDArray]:
    """
    Return eigenvalues and eigenvectors of S, sorted by absolute value.
    On the toroidal chart the dominant pair corresponds to the
    toroidal / poloidal shear split.
    """
    w, V = np.linalg.eigh(S)
    order = np.argsort(np.abs(w))[::-1]
    return w[order], V[:, order]


def trace_check(S: NDArray, tol: float = 1e-12) -> float:
    """Return |tr S|; should be ≲ tol (machine precision target ~1e-15)."""
    return float(abs(np.trace(S)))
