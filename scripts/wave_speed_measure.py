#!/usr/bin/env python3
"""
High‑precision wave‑speed measurement using an exact spectral propagator.
Long simulation (4000 steps) + dense sampling gives a razor‑sharp FFT peak.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal   # detrend + windowing
import warnings

# ----------------------------------------------------------------------
# 1️⃣  PARAMETERS
# ----------------------------------------------------------------------
N      = 64                # grid points per dimension
L      = 1.0               # physical domain size
beta   = 1.2e-4            # wave‑equation coefficient (c = √β)
steps  = 65384            # total time‑steps (long run)
record_every = 5           # record every 5 steps → high temporal resolution
mode_k = 4                 # integer mode number of the plane wave
dt     = 0.25              # time step (small enough for Nyquist)

dx = L / N
kvec = 2*np.pi*np.fft.fftfreq(N, d=dx)       # spectral wavenumbers
kx, ky, kz = np.meshgrid(kvec, kvec, kvec, indexing='ij')
k2 = kx**2 + ky**2 + kz**2

# ----------------------------------------------------------------------
# 2️⃣  DISPERSION RELATION (add epsilon to avoid division‑by‑zero)
# ----------------------------------------------------------------------
omega_k = np.sqrt(beta * k2 + 1e-30)          # 1e‑30 safe for double precision
omega_k[0,0,0] = 1e-30                         # zero‑mode never contributes

# ----------------------------------------------------------------------
# 3️⃣  INITIAL CONDITIONS
# ----------------------------------------------------------------------
phi = np.zeros((N, N, N))
x = np.arange(N) * dx
pert = 1e-3 * np.sin(2*np.pi*mode_k * x / L)  # amplitude A = 1e‑3
phi += pert[:, None, None]                    # broadcast over y, z

phi_t = np.zeros_like(phi)                     # zero initial velocity

phi_hat   = np.fft.fftn(phi)
phi_t_hat = np.fft.fftn(phi_t)

# ----------------------------------------------------------------------
# 4️⃣  PROBE POSITION (automatic, at the sine maximum)
# ----------------------------------------------------------------------
probe_x = int(np.argmax(np.abs(pert)))          # should be N/(4*mode_k) ≈ 8
probe = (probe_x, N//2, N//2)
print(f"Probe location → x={probe_x}")

# ----------------------------------------------------------------------
# 5️⃣  PRE‑COMPUTE TIME‑EVOLUTION FACTORS (constant because dt is constant)
# ----------------------------------------------------------------------
cos_term = np.cos(omega_k * dt)
# Suppress the harmless “divide by zero” warning that can appear when omega_k is tiny
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    sin_term = np.sin(omega_k * dt) / omega_k

# ----------------------------------------------------------------------
# 6️⃣  TIME INTEGRATION + RECORDING
# ----------------------------------------------------------------------
record = []
for i in range(steps):
    # Exact spectral step
    new_phi_hat   = phi_hat * cos_term + phi_t_hat * sin_term
    new_phi_t_hat = -omega_k**2 * phi_hat * sin_term + phi_t_hat * cos_term

    phi_hat   = new_phi_hat
    phi_t_hat = new_phi_t_hat

    # Transform back to real space (only needed for the probe)
    phi = np.real(np.fft.ifftn(phi_hat))

    if i % record_every == 0:
        # Sparse progress output (once every 100 iterations)
        if i % (record_every * 500) == 0:
            print(f"Progress: {100*i/steps:.0f}%")
        record.append(phi[probe])

record = np.asarray(record)
t_record = np.arange(len(record)) * dt * record_every

# ----------------------------------------------------------------------
# 7️⃣  FREQUENCY ANALYSIS (detrend + Hann window → ultra‑sharp peak)
# ----------------------------------------------------------------------
record_clean = signal.detrend(record)               # remove any tiny linear drift
window       = np.hanning(len(record_clean))
spec = np.abs(np.fft.rfft(record_clean * window))

freqs = np.fft.rfftfreq(len(record_clean), d=dt*record_every)

# Find the dominant non‑zero frequency bin
peak_idx = np.argmax(spec[1:]) + 1
omega_meas = 2*np.pi * freqs[peak_idx]

# ----------------------------------------------------------------------
# 8️⃣  SPEED COMPARISON
# ----------------------------------------------------------------------
k_mag = mode_k * 2*np.pi / L          # |k| of the initial plane wave
c_meas = omega_meas / k_mag
c_theory = np.sqrt(beta)

print("\n=== HIGH‑PRECISION RESULTS ===")
print(f"Measured transverse speed cₜ = {c_meas:.12f}")
print(f"Theoretical √β               = {c_theory:.12f}")
print(f"Relative error               = {abs(c_meas - c_theory)/c_theory:.2e}")

# ----------------------------------------------------------------------
# 9️⃣  PLOTTING
# ----------------------------------------------------------------------
fig, ax = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)

ax[0].plot(t_record, record, 'k-', lw=1)
ax[0].set_title('Long‑time exact oscillation at probe')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('φ')
ax[0].grid(True)

ax[1].plot(freqs, spec, 'k-')
ax[1].axvline(freqs[peak_idx], color='red', ls='--',
              label=f'Peak → c_meas = {c_meas:.10f}')
ax[1].set_xlabel('Frequency (1 / time‑unit)')
ax[1].set_ylabel('Spectral amplitude')
ax[1].grid(True)
ax[1].legend()

plt.savefig('wave_speed_high_precision.pdf')
print("\nPlot saved as 'wave_speed_high_precision.pdf'")
