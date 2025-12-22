#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_figures.py – Generate publication-ready plots for SRC-twist project
Requires: numpy, matplotlib, pyvista (for isosurface)
"""
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
import os
# Configuration
DIAGNOSTICS_FILE = 'diagnostics_64.csv'   # or 'diagnostics_256_extrap.csv'
PSD_FILE = 'gw_psd.txt'
PHI_FINAL_FILE = 'phi_final.npy'   # Generate from simulation: np.save('phi_final.npy', cp.asnumpy(phi_full))
# Ensure figs/ exists
os.makedirs('figs', exist_ok=True)
# 1. Load diagnostics (robust: skip header if present, handle comments)
try:
    data = np.loadtxt(DIAGNOSTICS_FILE, delimiter=',', skiprows=1, comments='#')
    t = data[:, 1]
    E = data[:, 3]
    W = data[:, 2]
except Exception as e:
    print(f"Error loading {DIAGNOSTICS_FILE}: {e}")
    print("Make sure file exists and has format: step,time,winding,energy")
    exit(1)
# Fig 1: Energy decay (semi-log with fit)
plt.figure(figsize=(6, 4))
plt.semilogy(t, E, 'o-', label='Simulation')
p = np.polyfit(t, np.log(E), 1)
gamma_fit = -p[0]
plt.semilogy(t, np.exp(p[1]) * np.exp(-gamma_fit * t), '--', label=f'Fit γ={gamma_fit:.3e} s⁻¹')
plt.xlabel('Time (s)')
plt.ylabel('Total Energy')
plt.title('Exponential Decay')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('figs/energy_decay.png', dpi=300)
plt.close()
# Fig 2: Winding stability
plt.figure(figsize=(6, 3))
plt.plot(t, W, 'k.-')
plt.ylim(0.9, 1.1)
plt.xlabel('Time (s)')
plt.ylabel('Winding Number')
plt.title('Topological Winding Stability')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('figs/winding_stability.png', dpi=300)
plt.close()
# Fig 3: PSD overlay
try:
    data_psd = np.loadtxt(PSD_FILE, skiprows=1, usecols=(0, 1), dtype=float)
    f = data_psd[:, 0]
    psd = data_psd[:, 1]
except Exception as e:
    print(f"Error loading {PSD_FILE}: {e}")
    print("File should have format: f PSD (skip header)")
    exit(1)
lvk_f = np.array([20, 30, 40, 50])
lvk_h = np.array([1.8e-22, 1.5e-22, 1.2e-22, 9.5e-23])
lvk_psd = lvk_h**2 / (2 * lvk_f)
plt.figure(figsize=(6, 4))
plt.loglog(f, psd, label='SRC-twist')
plt.loglog(lvk_f, lvk_psd, 's', label='LVK O4 bursts')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD $S_h(f)$ (strain² Hz⁻¹)')
plt.title('Power-Law Strain Spectrum')
plt.legend()
plt.grid(which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('figs/psd_overlay.png', dpi=300)
plt.close()
# Supp Fig A: Isosurface (requires phi_final.npy)
if os.path.exists(PHI_FINAL_FILE):
    phi_np = np.load(PHI_FINAL_FILE)
    mag = np.abs(phi_np)
    dx = 1.0 / phi_np.shape[0]   # Approximate dx
    grid = pv.UniformGrid(dimensions=mag.shape, spacing=(dx, dx, dx), origin=(0,0,0))
    grid['scalars'] = mag.ravel(order='F')
    contour = grid.contour([0.5])
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(contour, cmap='viridis')
    plotter.show_grid()
    plotter.screenshot('figs/isosurface.png')
    print("Isosurface saved: figs/isosurface.png")
else:
    print("phi_final.npy not found - skipping isosurface")

# Supp Fig B: β-term spectrum (placeholder - add if needed)
print("Figures generated in figs/: energy_decay.png, winding_stability.png, psd_overlay.png")
