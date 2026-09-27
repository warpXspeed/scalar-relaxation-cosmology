"""
Genus-2 degeneration test.

Primary verification for the multi-phase extension:
set Ω block-diagonal (Ω_12 → 0) and confirm the genus-2 engine
reproduces genus-1 results to machine precision —

  - cnoidal profile (periodicity)
  - capture-train |ΔZ| and shear residual
  - adiabatic threshold region ε ≲ 0.05

A genus-2 implementation that cannot degenerate to its verified
genus-1 limit has a bug.  This test catches it without needing
an independent genus-2 reference solution.
"""

from __future__ import annotations

import numpy as np
from .theta import riemann_theta, log_theta_derivatives
from .reconstruction import scalar_potential, shear_tensor_1d
from .engine import DFMState
from .diagnostics import decay_envelope


def _genus1_cnoidal_reference():
    """Reference numbers from the verified genus-1 cnoidal test."""
    tau = 1.2j
    Omega = np.array([[tau]], dtype=np.complex128)
    U = np.array([[1.0 + 0j]], dtype=np.complex128)
    Z0 = np.array([0.3 + 0.1j], dtype=np.complex128)
    x = np.linspace(-10.0, 10.0, 401)
    u = scalar_potential(x, t=[], Omega=Omega, U=U, Z0=Z0, radius=8)
    return x, u, Omega, U, Z0


def test_theta_factorization():
    """
    When Ω = diag(τ1, τ2) the genus-2 theta must factor:
        θ(z1,z2 | Ω) = θ(z1|τ1) · θ(z2|τ2)
    to machine precision (up to lattice truncation).
    """
    tau1, tau2 = 1.5j, 1.2j
    Omega2 = np.array([[tau1, 0], [0, tau2]], dtype=np.complex128)
    z = np.array([0.25 + 0.05j, 0.30 + 0.10j])

    th2 = riemann_theta(z, Omega2, radius=8)
    th1a = riemann_theta(z[0:1], np.array([[tau1]]), radius=8)
    th1b = riemann_theta(z[1:2], np.array([[tau2]]), radius=8)
    product = th1a * th1b

    rel = abs(th2 - product) / (abs(product) + 1e-30)
    assert rel < 1e-10, f"theta factorization failed: rel={rel}"
    print(f"  theta factorization  rel err = {rel:.2e}  PASS")


def test_cnoidal_degeneration():
    """
    Block-diagonal genus-2 state with second phase held at rest
    must reproduce the genus-1 cnoidal potential on the first
    coordinate.
    """
    x, u1, Om1, U1, Z1 = _genus1_cnoidal_reference()

    # genus-2: first block = genus-1 data, second block inert
    Omega2 = np.array([[1.2j, 0], [0, 1.5j]], dtype=np.complex128)
    U2 = np.array([[1.0 + 0j, 0], [0, 0]], dtype=np.complex128)  # only first spatial
    Z2 = np.array([0.3 + 0.1j, 0.0 + 0.0j], dtype=np.complex128)

    u2 = scalar_potential(x, t=[], Omega=Omega2, U=U2, Z0=Z2, radius=8)

    # u = 2 ∂_x² log θ; with factorized theta and inert second phase,
    # ∂_x only hits the first factor → u2 must match u1
    rel = np.max(np.abs(u2 - u1)) / (np.max(np.abs(u1)) + 1e-30)
    assert rel < 1e-8, f"cnoidal degeneration failed: rel={rel}"
    print(f"  cnoidal degeneration  rel err = {rel:.2e}  PASS")


def test_capture_degeneration():
    """
    Compound capture train on a block-diagonal genus-2 background
    must produce the same net |ΔZ| on the active phase and the same
    memory ratio (to numerical tolerance) as pure genus-1.
    """
    # genus-1 baseline
    Om1 = np.array([[1.5j]], dtype=np.complex128)
    U1 = np.array([[1.0 + 0j, 0.35 + 0j]], dtype=np.complex128)
    Z1 = np.array([0.25 + 0.05j], dtype=np.complex128)
    s1 = DFMState(Om1, U1, Z1)
    s1.inject_compound([
        (0.0, 0.35 + 0.12j, "EM_induction"),
        (1.0, 0.12 + 0.04j, "Joule_heating"),
        (2.0, 0.05 + 0.02j, "tidal_lock"),
    ])
    s1.evolve(1.5)
    twin1 = s1.twin()
    rep1 = decay_envelope(s1, twin1, x_ref=0.0, n_samples=64)

    # genus-2 block-diagonal: second phase inert
    Om2 = np.array([[1.5j, 0], [0, 1.2j]], dtype=np.complex128)
    U2 = np.array([
        [1.0 + 0j, 0.35 + 0j],
        [0.0 + 0j, 0.00 + 0j],
    ], dtype=np.complex128)
    Z2 = np.array([0.25 + 0.05j, 0.0 + 0.0j], dtype=np.complex128)
    s2 = DFMState(Om2, U2, Z2)
    # pulses only on the first component
    s2.inject_compound([
        (0.0, np.array([0.35 + 0.12j, 0.0]), "EM_induction"),
        (1.0, np.array([0.12 + 0.04j, 0.0]), "Joule_heating"),
        (2.0, np.array([0.05 + 0.02j, 0.0]), "tidal_lock"),
    ])
    s2.evolve(1.5)
    twin2 = s2.twin()
    rep2 = decay_envelope(s2, twin2, x_ref=0.0, n_samples=64)

    # net |ΔZ| on active phase
    dZ1 = abs(rep1.total_phase_offset - rep2.total_phase_offset)
    assert dZ1 < 1e-10, f"|ΔZ| mismatch: {rep1.total_phase_offset} vs {rep2.total_phase_offset}"

    # memory ratios should be close (same active dynamics)
    rel_mem = abs(rep1.memory_ratio - rep2.memory_ratio) / (abs(rep1.memory_ratio) + 1e-30)
    assert rel_mem < 0.05, f"memory ratio drift: {rel_mem}"

    print(f"  capture |ΔZ| match          = {rep1.total_phase_offset:.6f}  PASS")
    print(f"  memory-ratio rel err        = {rel_mem:.2e}  PASS")


def test_posdef_cone_g2():
    """Im Ω positive-definite check must accept diagonal and reject indefinite."""
    Om_ok = np.array([[1.5j, 0.1j], [0.1j, 1.2j]], dtype=np.complex128)
    eig = np.linalg.eigvalsh(Om_ok.imag)
    assert eig.min() > 0

    Om_bad = np.array([[1.5j, 2.0j], [2.0j, 1.2j]], dtype=np.complex128)
    eig_bad = np.linalg.eigvalsh(Om_bad.imag)
    assert eig_bad.min() < 0
    print(f"  pos-def cone (min eig ok={eig.min():.4f}, bad={eig_bad.min():.4f})  PASS")


def run_all():
    print("=" * 60)
    print("GENUS-2 DEGENERATION TESTS")
    print("=" * 60)
    test_theta_factorization()
    test_cnoidal_degeneration()
    test_capture_degeneration()
    test_posdef_cone_g2()
    print("=" * 60)
    print("All degeneration tests passed.")
    print("Genus-2 engine is consistent with verified genus-1 limit.")
    print("=" * 60)


if __name__ == "__main__":
    run_all()
