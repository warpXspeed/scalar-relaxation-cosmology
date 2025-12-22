#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cupy as cp
import numpy as np
import scipy.fft as fft
import csv
from pathlib import Path

# Parameters
N = 256
num_slabs = 4
slab_sz = N // num_slabs
L = 1.0
dx = L / N
dt = 1e-3
steps = 12000  # Full production; set to 2000 for test
output_int = 1200

beta = 1.2e-4
gamma = 5e-4
lam = 4e-4

# Wavenumbers (global)
k = fft.fftfreq(N, d=dx) * 2 * np.pi
kx, ky, kz = cp.meshgrid(k, k, k, indexing='ij')
k2 = kx**2 + ky**2 + kz**2
k2[0,0,0] = 1.0

# Hopfion initial (full grid)
def hopf_initial():
    x = cp.linspace(0, L, N, endpoint=False)
    y = cp.linspace(0, L, N, endpoint=False)
    z = cp.linspace(0, L, N, endpoint=False)
    X, Y, Z = cp.meshgrid(x, y, z, indexing='ij')
    r2 = (X - 0.5)**2 + (Y - 0.5)**2 + (Z - 0.5)**2
    phi = cp.arctan2(Y - 0.5, X - 0.5) + cp.pi * cp.tanh(r2 * 10)
    return cp.tanh((1 - r2 * 20)) * cp.cos(phi)

phi_full = hopf_initial()
phi_t_full = cp.zeros_like(phi_full)

# Physics functions
def top_term(phi):
    phi_hat = fft.fftn(phi)
    gx = fft.ifftn(1j * kx * phi_hat).real
    gy = fft.ifftn(1j * ky * phi_hat).real
    gz = fft.ifftn(1j * kz * phi_hat).real
    grad_sq = gx**2 + gy**2 + gz**2
    return 0.5 * beta * grad_sq**2

def step(phi, phi_t):
    lap = fft.ifftn(-k2 * fft.fftn(phi)).real
    dV = 4 * lam * phi * (phi**2 - 1.0)
    rhs = lap - gamma * phi_t - dV - top_term(phi)
    phi_t = phi_t + dt * rhs
    phi = phi + dt * phi_t
    return phi, phi_t

def winding_number(phi):
    line = phi[N//2, N//2, :]
    phase = cp.angle(cp.exp(1j * line))
    dphase = cp.unwrap(phase)
    W = (dphase[-1] - dphase[0]) / (2 * cp.pi)
    return int(cp.rint(W).get())

def project_winding(phi):
    line = phi[N//2, N//2, :]
    phase = cp.angle(cp.exp(1j * line))
    dphase = cp.unwrap(phase)
    W_meas = (dphase[-1] - dphase[0]) / (2 * cp.pi)
    delta = cp.rint(W_meas) - W_meas
    corr = (delta * 2 * cp.pi) * (cp.arange(N) / N)
    phi[N//2, N//2, :] += corr
    return phi

def energy(phi, phi_t):
    kin = 0.5 * phi_t**2
    pot = lam * (phi**2 - 1.0)**2
    top = top_term(phi)
    return cp.sum(kin + pot + top) * dx**3

# Run with slabs
out_dir = Path("run_output_256")
out_dir.mkdir(exist_ok=True)
csv_file = out_dir / "diagnostics.csv"
with open(csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["step", "time", "winding", "energy"])

for s in range(steps + 1):
    for slab in range(num_slabs):
        z0 = slab * slab_sz
        z1 = z0 + slab_sz
        phi_s = phi_full[:, :, z0:z1]
        phi_t_s = phi_t_full[:, :, z0:z1]

        phi_s, phi_t_s = step(phi_s, phi_t_s)

        phi_full[:, :, z0:z1] = phi_s
        phi_t_full[:, :, z0:z1] = phi_t_s

        if slab > 0:
            phi_full[:, :, z0-1] = 0.5 * (phi_full[:, :, z0-1] + phi_s[:, :, 0])
        if slab < num_slabs - 1:
            phi_full[:, :, z1] = 0.5 * (phi_full[:, :, z1] + phi_s[:, :, -1])

    phi_full = project_winding(phi_full)

    if s % output_int == 0:
        W = winding_number(phi_full)
        E = energy(phi_full, phi_t_full).get()
        t = s * dt
        with open(csv_file, "a") as f:
            writer = csv.writer(f)
            writer.writerow([s, t, W, E])
        print(f"step {s:5d} | t={t:7.3f} | W={W:+d} | E={E:.3e}")

print("256³ run complete.")
