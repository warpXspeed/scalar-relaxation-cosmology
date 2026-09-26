"""
Translation layer: finite-gap data (Ω, Z, U) → DFM observables
(scalar potential u, current components v_i, shear tensor).

This is the algebraic core of the Dynamic Fluid Medium engine.
All quantities are obtained from logarithmic derivatives of the
Riemann theta function; no spatial discretisation is performed
until a laboratory chart is requested for visualisation.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .theta import log_theta_derivatives, riemann_theta


def kp_potential(
    x: float | NDArray,
    t: ArrayLike,
    Omega: ArrayLike,
    U: ArrayLike,
    Z0: ArrayLike,
    radius: int | None = None,
) -> complex | NDArray:
    r"""
    Leading KP potential

        u(x,t) = 2 ∂_x² log θ( U x + V·t + Z0 | Ω )

    Here the first frequency vector U[:,0] is identified with the
    spatial direction; the remaining columns of U are the higher
    hierarchy times.

    Parameters
    ----------
    x : float or array
        Laboratory spatial coordinate(s).
    t : array-like, shape (N_times,)
        Hierarchy times (t_2, t_3, \ldots).  For pure KdV set t=[0].
    Omega : (g,g) period matrix
    U : (g, 1+N_times) frequency matrix; columns are the b-period vectors
    Z0 : (g,) initial phase
    """
    Omega = np.asarray(Omega, dtype=np.complex128)
    U = np.asarray(U, dtype=np.complex128)
    Z0 = np.asarray(Z0, dtype=np.complex128)
    t = np.atleast_1d(np.asarray(t, dtype=np.complex128)).ravel()

    g = Omega.shape[0]
    assert U.shape[0] == g

    # phase argument: Z = U_x * x + sum U_k * t_k + Z0
    # U[:,0] is the x-frequency.  When t is empty the higher times
    # are assumed already absorbed into Z0 (the usual case inside
    # DFMState after evolve / inject).
    n_time = U.shape[1] - 1
    if t.size == 0 or n_time == 0:
        time_term = 0.0
    else:
        t_use = t[:n_time] if t.size >= n_time else np.pad(t, (0, n_time - t.size))
        time_term = U[:, 1:] @ t_use

    if np.isscalar(x) or (isinstance(x, np.ndarray) and x.ndim == 0):
        Z = U[:, 0] * x + time_term + Z0
        _, _, hess = log_theta_derivatives(Z, Omega, radius=radius)
        u = 2.0 * np.dot(U[:, 0], hess @ U[:, 0])
        return u
    else:
        x = np.asarray(x, dtype=np.complex128)
        us = []
        for xi in x:
            Z = U[:, 0] * xi + time_term + Z0
            _, _, hess = log_theta_derivatives(Z, Omega, radius=radius)
            us.append(2.0 * np.dot(U[:, 0], hess @ U[:, 0]))
        return np.asarray(us, dtype=np.complex128)


def current_density(
    x: float,
    t: ArrayLike,
    Omega: ArrayLike,
    U: ArrayLike,
    Z0: ArrayLike,
    order: int = 1,
    radius: int | None = None,
) -> complex:
    """
    Leading current component extracted from the first coefficient
    of the Baker-Akhiezer expansion.

    For the KP hierarchy the first current is essentially

        v = ∂_x log θ   (up to a constant factor that can be fixed
                         by the normalisation of the local parameter).

    Higher-order currents follow from higher derivatives or from
    the residue of z^k ∂_x log ψ.
    """
    Omega = np.asarray(Omega, dtype=np.complex128)
    U = np.asarray(U, dtype=np.complex128)
    Z0 = np.asarray(Z0, dtype=np.complex128)
    t = np.atleast_1d(np.asarray(t, dtype=np.complex128)).ravel()

    n_time = U.shape[1] - 1
    if t.size == 0 or n_time == 0:
        time_term = 0.0
    else:
        t_use = t[:n_time] if t.size >= n_time else np.pad(t, (0, n_time - t.size))
        time_term = U[:, 1:] @ t_use

    Z = U[:, 0] * x + time_term + Z0
    _, grad, _ = log_theta_derivatives(Z, Omega, radius=radius)
    v = np.dot(U[:, 0], grad)
    return v


def shear_tensor_1d(
    x: float | NDArray,
    t: ArrayLike,
    Omega: ArrayLike,
    U: ArrayLike,
    Z0: ArrayLike,
    radius: int | None = None,
) -> NDArray:
    """
    One-dimensional reduction of the shear: simply the gradient of
    the current (i.e. second derivative of log θ).

    In a full 3-D embedding one would form the symmetric traceless
    part of ∇v + (∇v)^T; here we return the scalar shear rate
    appropriate for a 1-D or planar flow.
    """
    # shear ~ ∂_x v = ∂_x² log θ = u/2
    u = kp_potential(x, t, Omega, U, Z0, radius=radius)
    return np.real(u) / 2.0   # take real part for physical shear


def scalar_potential(
    x: float | NDArray,
    t: ArrayLike,
    Omega: ArrayLike,
    U: ArrayLike,
    Z0: ArrayLike,
    radius: int | None = None,
) -> NDArray:
    """
    DFM scalar potential identified with the KP field u.
    """
    return np.real(kp_potential(x, t, Omega, U, Z0, radius=radius))
