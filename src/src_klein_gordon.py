#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SRC-twist Klein-Gordon solver (3-D pseudo-spectral, CPU)
"""

import numpy as np
import scipy.fft as fft
import csv
from pathlib import Path

# Parameters
N = 64  # grid points per side
L = 1.0
dx = L / N
dt = 1e-3
steps = 12000
output_int = 1200

beta = 1.2e-4
gamma = 5e-4
lam = 4e-4

# Domain & wavenumbers
x = np.linspace(0, L, N, endpoint=False)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')  # Use x for all
k = fft.fftfreq(N, d=dx) * 2*np.pi
kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
k2 = kx**2 + ky**2 + kz**2
k2[0,0,0] = 1.0

# Initial Hopfion
def hopf_initial():
    r2 = (X-0.5)**2 + (Y-0.5)**2 + (Z-0.5)**2
    phi = np.arctan2(Y-0.5, X-0.5) + np.pi * np.tanh(r2*10)
    return np.tanh((1 - r2*20)) * np.cos(phi)

phi = hopf_initial()
phi_t = np.zeros_like(phi)

# Energy
def energy(phi, phi_t):
    kin = 0.5 * phi_t**2
    phi_hat = fft.fftn(phi)
    grad_sq = (fft.ifftn(k2 * phi_hat).real**2 +
               fft.ifftn(1j*kx*phi_hat).real**2 +
               fft.ifftn(1j*ky*phi_hat).real**2 +
               fft.ifftn(1j*kz*phi_hat).real**2)
    pot = lam * (phi**2 - 1.0)**2
    top = 0.5 * beta * grad_sq**2
    return np.sum(kin + pot + top) * dx**3

# Winding
def winding_number(phi):
    line = phi[N//2, N//2, :]
    phase = np.angle(np.exp(1j*line))
    dphase = np.unwrap(phase)
    W = (dphase[-1] - dphase[0]) / (2*np.pi)
    return int(np.round(W))

# Top term
def top_term(phi):
    phi_hat = fft.fftn(phi)
    gx = fft.ifftn(1j*kx*phi_hat).real
    gy = fft.ifftn(1j*ky*phi_hat).real
    gz = fft.ifftn(1j*kz*phi_hat).real
    grad_sq = gx**2 + gy**2 + gz**2
    return 0.5 * beta * grad_sq**2

# Projection
def project_winding(phi):
    line = phi[N//2, N//2, :]
    phase = np.angle(np.exp(1j*line))
    dphase = np.unwrap(phase)
    W_meas = (dphase[-1] - dphase[0]) / (2*np.pi)
    delta = np.round(W_meas) - W_meas
    correction = (delta * 2*np.pi) * (np.arange(N) / N)
    phi[N//2, N//2, :] += correction
    return phi

# Step
def step(phi, phi_t):
    lap = fft.ifftn(-k2 * fft.fftn(phi)).real
    dV = 4*lam*phi*(phi**2 - 1.0)
    rhs = lap - gamma*phi_t - dV - top_term(phi)
    phi_t_new = phi_t + dt * rhs
    phi_new = phi + dt * phi_t_new
    phi_new = project_winding(phi_new)
    return phi_new, phi_t_new

# Run
out_dir = Path("run_output")
out_dir.mkdir(exist_ok=True)
csv_file = out_dir / "diagnostics.csv"
with open(csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["step", "time", "winding", "energy"])

for s in range(steps + 1):
    if s % output_int == 0:
        W = winding_number(phi)
        E = energy(phi, phi_t)
        t = s * dt
        with open(csv_file, "a") as f:
            writer = csv.writer(f)
            writer.writerow([s, t, W, E])
        print(f"step {s:5d} | t={t:7.3f} | W={W:+d} | E={E:.3e}")
    phi, phi_t = step(phi, phi_t)

print("Run complete.")
