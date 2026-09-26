"""
Riemann theta-function evaluator for low-genus (g <= 4) finite-gap solutions.
Pure NumPy + SciPy implementation; no external algebraic-geometry packages required.

The sum is truncated over a finite lattice box whose size is controlled by
the imaginary part of the period matrix. For production use with g=1..3
and moderate Im(Omega) this is both fast and accurate to double precision.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _lattice_points(g: int, radius: int) -> NDArray[np.int64]:
    """Generate integer lattice points n in Z^g with ||n||_inf <= radius."""
    ranges = [np.arange(-radius, radius + 1) for _ in range(g)]
    grids = np.meshgrid(*ranges, indexing="ij")
    pts = np.stack([g.ravel() for g in grids], axis=-1)
    return pts.astype(np.int64)


def riemann_theta(
    z: ArrayLike,
    Omega: ArrayLike,
    radius: int | None = None,
    deriv: tuple[int, ...] | None = None,
) -> complex | NDArray[np.complex128]:
    """
    Evaluate the Riemann theta function (or a partial derivative)

        θ(z|Ω) = Σ_{n∈Z^g} exp(π i n·Ω·n + 2π i n·z)

    Parameters
    ----------
    z : array-like, shape (g,) or (N, g)
        Argument (can be vectorised over leading batch dimension).
    Omega : array-like, shape (g, g)
        Period matrix (must have positive-definite imaginary part).
    radius : int, optional
        Truncation radius of the lattice sum.  If None a safe default
        based on Im(Omega) is chosen.
    deriv : tuple of int, optional
        Multi-index of the derivative.  e.g. (1,0) means ∂/∂z_0,
        (1,1) means ∂²/∂z_0∂z_1, etc.  None = plain theta.

    Returns
    -------
    complex or ndarray
        Value(s) of θ or its derivative.
    """
    z = np.asarray(z, dtype=np.complex128)
    Omega = np.asarray(Omega, dtype=np.complex128)
    g = Omega.shape[0]
    assert Omega.shape == (g, g)

    # Ensure positive-definite Im(Omega) for convergence
    ImO = Omega.imag
    # crude lower bound on the quadratic form
    eig_min = np.linalg.eigvalsh(ImO).min()
    if eig_min <= 0:
        raise ValueError("Im(Omega) must be positive definite")

    if radius is None:
        # heuristic: exp(-π * eig_min * R²) < 1e-16
        radius = max(3, int(np.ceil(np.sqrt(16.0 / (np.pi * eig_min)))))

    n = _lattice_points(g, radius)  # (M, g)

    # quadratic form: n·Ω·n  (broadcast)
    # n_i Ω_ij n_j
    quad = np.einsum("mi,ij,mj->m", n, Omega, n)

    # linear term: n·z
    if z.ndim == 1:
        lin = n @ z
        phase = np.pi * 1j * quad + 2 * np.pi * 1j * lin
        terms = np.exp(phase)
        if deriv is None:
            return terms.sum()
        # derivative multi-index
        factor = np.ones(n.shape[0], dtype=np.complex128)
        for k, d in enumerate(deriv):
            if d:
                factor *= (2 * np.pi * 1j * n[:, k]) ** d
        return (terms * factor).sum()
    else:
        # batch: z shape (N, g)
        lin = n @ z.T  # (M, N)
        phase = np.pi * 1j * quad[:, None] + 2 * np.pi * 1j * lin
        terms = np.exp(phase)
        if deriv is None:
            return terms.sum(axis=0)
        factor = np.ones(n.shape[0], dtype=np.complex128)
        for k, d in enumerate(deriv):
            if d:
                factor *= (2 * np.pi * 1j * n[:, k]) ** d
        return (terms * factor[:, None]).sum(axis=0)


def log_theta_derivatives(
    z: ArrayLike,
    Omega: ArrayLike,
    radius: int | None = None,
) -> tuple[complex, NDArray, NDArray]:
    """
    Compute log θ, its gradient and Hessian at a single point z.

    Returns
    -------
    log_theta : complex
    grad : ndarray (g,)
        ∂_i log θ
    hess : ndarray (g, g)
        ∂_i ∂_j log θ
    """
    z = np.asarray(z, dtype=np.complex128)
    g = len(z)

    theta = riemann_theta(z, Omega, radius=radius)
    if abs(theta) < 1e-30:
        raise FloatingPointError("theta vanished – singular point")

    # first derivatives
    grad_theta = np.array(
        [riemann_theta(z, Omega, radius=radius, deriv=tuple(1 if i == k else 0 for i in range(g)))
         for k in range(g)],
        dtype=np.complex128,
    )
    grad = grad_theta / theta

    # second derivatives
    hess_theta = np.zeros((g, g), dtype=np.complex128)
    for i in range(g):
        for j in range(i, g):
            multi = [0] * g
            multi[i] += 1
            multi[j] += 1
            hess_theta[i, j] = riemann_theta(z, Omega, radius=radius, deriv=tuple(multi))
            hess_theta[j, i] = hess_theta[i, j]
    hess = hess_theta / theta - np.outer(grad, grad)

    return np.log(theta), grad, hess
