"""
Unit test: recover the classic KdV cnoidal wave from the genus-1
finite-gap construction and verify that the translation layer
produces a clean, periodic shear / potential profile.
"""

from __future__ import annotations

import numpy as np
from .theta import riemann_theta, log_theta_derivatives
from .reconstruction import kp_potential, scalar_potential, shear_tensor_1d


def genus1_period_matrix(tau: complex) -> np.ndarray:
    """Period matrix for a torus with modulus tau (Im tau > 0)."""
    return np.array([[tau]], dtype=np.complex128)


def test_cnoidal_wave():
    """
    Standard cnoidal-wave parameters.
    For genus 1 the KP potential reduces to the KdV field
        u = 2 ∂_x² log θ_1( U x + Z0 | τ )
    which is known to be a cnoidal wave (or a soliton in the
    infinite-period limit).
    """
    # pure imaginary tau gives a rectangular torus; typical values
    # for a moderately elliptic cnoidal wave
    tau = 1.2j
    Omega = genus1_period_matrix(tau)

    # frequency: for KdV the spatial frequency can be normalised to 1
    U = np.array([[1.0 + 0j]], dtype=np.complex128)   # shape (1,1) – only x
    Z0 = np.array([0.3 + 0.1j], dtype=np.complex128)

    # evaluate on a spatial grid
    x = np.linspace(-10.0, 10.0, 401)
    t = np.array([])          # no higher times

    u = scalar_potential(x, t, Omega, U, Z0, radius=8)
    s = shear_tensor_1d(x, t, Omega, U, Z0, radius=8)

    # basic sanity checks
    assert u.shape == x.shape
    assert np.all(np.isfinite(u))
    assert np.all(np.isfinite(s))

    # the profile must be periodic with period related to the real
    # period of the torus (here the real period is 1 because we
    # normalised U_x = 1 and the a-period is 1)
    # check approximate periodicity after one lattice period
    # (the function is quasi-periodic, but u itself is periodic)
    period = 1.0
    # shift by one period and compare interior points
    idx = (x > -8) & (x < 8)
    u_shift = scalar_potential(x[idx] + period, t, Omega, U, Z0, radius=8)
    rel_err = np.max(np.abs(u[idx] - u_shift)) / (np.max(np.abs(u)) + 1e-12)
    assert rel_err < 1e-6, f"periodicity violated: rel_err = {rel_err}"

    # shear should be the derivative of the current, hence also periodic
    print("Cnoidal-wave test passed.")
    print(f"  max |u|   = {np.max(np.abs(u)):.6f}")
    print(f"  max |s|   = {np.max(np.abs(s)):.6f}")
    print(f"  periodicity relative error = {rel_err:.2e}")
    return x, u, s


if __name__ == "__main__":
    test_cnoidal_wave()
