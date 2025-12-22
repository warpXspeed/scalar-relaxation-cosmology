#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SRC-twist Klein-Gordon solver – GPU version (CuPy)
"""

import cupy as cp
import scipy.fft as fft
import csv
from pathlib import Path

# Parameters
N = 64  # Change to 128/256 for production
L = 1.0
dx = L / N
dt = 1e-3
steps = 12000
output_int = 1200

beta = 1.2e-4
gamma = 5e-4
lam = 4e-4

# Grid & wavenumbers (GPU arrays)
x = cp.linspace(0, L, N, endpoint=False)
y = cp.linspace(0, L, N, endpoint=False)
z = cp.linspace(0, L, N, endpoint=False)
X, Y, Z = cp.meshgrid(x, y, z, indexing='ij')

k = fft.fftfreq(N, d=dx) * 2 * cp.pi
kx, ky, kz = cp.meshgrid(k, k, k, indexing='ij')
k2 = kx**2 + ky**2 + kz**2
k2[0,0,0] = 1.0

# Initial Hopfion (GPU)
def hopf_initial():
    r2 = (X - 0.5)**2 + (Y - 0.5)**2 + (Z - 0.5)**2
    phi = cp.arctan2(Y - 0.5, X - 0.5) + cp.pi * cp.tanh(r2 * 10)
    return cp.tanh((1 - r2 * 20)) * cp.cos(phi)

phi = hopf_initial()
phi_t = cp.zeros_like(phi)

# Energy
def energy(phi, phi_t):
    kin = 0.5 * phi_t**2
    phi_hat = fft.fftn(phi)
    grad_sq = (fft.ifftn(k2 * phi_hat).real**2 +
               fft.ifftn(1j * kx * phi_hat).real**2 +
               fft.ifftn(1j * ky * phi_hat).real**2 +
               fft.ifftn(1j * kz * phi_hat).real**2)
    pot = lam * (phi**2 - 1.0)**2
    top = 0.5 * beta * grad_sq**2
    return cp.sum(kin + pot + top) * dx**3

# Winding
def winding_number(phi):
    line = phi[N//2, N//2, :]
    phase = cp.angle(cp.exp(1j * line))
    dphase = cp.unwrap(phase)
    W = (dphase[-1] - dphase[0]) / (2 * cp.pi)
    return int(cp.rint(W).get())

# Top term
def top_term(phi):
    phi_hat = fft.fftn(phi)
    gx = fft.ifftn(1j * kx * phi_hat).real
    gy = fft.ifftn(1j * ky * phi_hat).real
    gz = fft.ifftn(1j * kz * phi_hat).real
    grad_sq = gx**2 + gy**2 + gz**2
    return 0.5 * beta * grad_sq**2

# Projection
def project_winding(phi):
    line = phi[N//2, N//2, :]
    phase = cp.angle(cp.exp(1j * line))
    dphase = cp.unwrap(phase)
    W_meas = (dphase[-1] - dphase[0]) / (2 * cp.pi)
    delta = cp.rint(W_meas) - W_meas
    correction = (delta * 2 * cp.pi) * (cp.arange(N) / N)
    phi[N//2, N//2, :] += correction
    return phi

# Step
def step(phi, phi_t):
    lap = fft.ifftn(-k2 * fft.fftn(phi)).real
    dV = 4 * lam * phi * (phi**2 - 1.0)
    rhs = lap - gamma * phi_t - dV - top_term(phi)
    phi_t_new = phi_t + dt * rhs
    phi_new = phi + dt * phi_t_new
    phi_new = project_winding(phi_new)
    return phi_new, phi_t_new

# Run
out_dir = Path("run_output_gpu")
out_dir.mkdir(exist_ok=True)
csv_file = out_dir / "diagnostics.csv"
with open(csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["step", "time", "winding", "energy"])

for s in range(steps + 1):
    if s % output_int == 0:
        W = winding_number(phi)
        E = energy(phi, phi_t).get()
        t = s * dt
        with open(csv_file, "a") as f:
            writer = csv.writer(f)
            writer.writerow([s, t, W, E])
        print(f"step {s:5d} | t={t:7.3f} | W={W:+d} | E={E:.3e}")
    phi, phi_t = step(phi, phi_t)

print("GPU run complete.")
