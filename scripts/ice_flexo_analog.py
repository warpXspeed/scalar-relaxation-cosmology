# ice_flexo_analog.py
# =============================================================================
# SRC-compatible 2D simulation analog for flexoelectricity in water ice
# Models bending of an ice slab, computes strain gradient, and emergent polarization
# Calibrated to Wen et al. (Nature Physics, 2025): μ ≈ 1.14 nC/m
# Author: Adapted for SRC repository (Gerald Henton, January 2026)
# Dependencies: numpy, matplotlib
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# SRC-inspired default parameters (scaled for ice analog)
# -------------------------------
L = 1.0e-3          # Slab length (1 mm, typical experimental scale)
Nx = 256            # Grid points in x
Ny = 64             # Grid points in y (thin slab)
dx = L / (Nx - 1)
dy = 0.1 * L / (Ny - 1)  # FIXED: replaced "_L" with "* L"

# SRC substrate parameters (effective for ice viscoelastic response)
G_shear = 2.7e9     # Shear modulus ~ GPa range for ice (scaled from SRC vacuum equiv)
rho = 920.0         # Ice density kg/m³
c_T = np.sqrt(G_shear / rho)  # Transverse wave speed ~1700 m/s for ice

# Flexoelectric coefficient from Wen et al. (2025): 1.14 ± 0.13 nC/m = 1.14e-9 C/m
mu_flexo = 1.14e-9  # C/m  (bulk value; surface enhanced below 160 K)

# Temperature dependence: surface ferroelectric peak ~160 K
T = 200.0           # Temperature in K (set to 150–250 for tests)
T_crit = 160.0      # Critical temp for surface transition
surface_enhance = 5.0 * (1 - np.tanh((T - T_crit)/10.0))  # FIXED: replaced "_" with "*"

# Relaxation/viscous term (small for quasi-static bending)
gamma = 1e-3        # Effective damping (arbitrary units for static sim)

# -------------------------------
# Grid setup
# -------------------------------
x = np.linspace(0, L, Nx)
y = np.linspace(-0.05*L, 0.05*L, Ny)  # Symmetric thin slab
X, Y = np.meshgrid(x, y)

# -------------------------------
# Applied bending displacement (three-point bend approximation)
# Max displacement d_max at center
# -------------------------------
d_max = 1e-5        # 10 μm max deflection (realistic for experiments)
u_y = d_max * (1 - ((2*X/L - 1)**2)**2)  # FIXED: replaced "_" with "*" in two places

# Displacement vector u = (0, u_y)  → strain ε_xx = ∂u_x/∂x ≈ 0, ε_yy ≈ ∂u_y/∂y ≈ 0
# But strain gradient ∂ε_xx/∂x dominant in bending (simplified)

# Compute approximate strain ε_xx (curvature-induced)
kappa = np.gradient(np.gradient(u_y, dx, axis=1), dx, axis=1)  # 2nd derivative ≈ curvature
epsilon_xx = -Y * kappa  # FIXED: replaced "_" with "*"

# Strain gradient ∇ε (flexoelectric driving term)
grad_eps_x = np.gradient(epsilon_xx, dx, axis=1)  # ∂ε_xx / ∂x

# -------------------------------
# Emergent polarization P (flexoelectric response)
# P ≈ μ_ ∇ε + surface enhancement near boundaries
# -------------------------------
# FIXED: Removed premature multiplication by surface_enhance (should be surface-only)
P = mu_flexo * grad_eps_x  # FIXED: replaced "_" with "*"

# Surface mask: boost near top/bottom (y boundaries)
# FIXED: Original mask was backwards (max at center). Now correctly peaks at surfaces.
surface_thickness = 0.02 * L
distance_from_surface = 0.05 * L - np.abs(Y)
surface_mask = np.exp(-(distance_from_surface / surface_thickness)**2)  # FIXED: surface mask

# Apply surface enhancement only near boundaries
P *= (1 + (surface_enhance - 1) * surface_mask)  # FIXED: replaced "_" with "*=" and "*"

# Average flexoelectric coefficient (effective)
mu_eff = np.mean(np.abs(P) / np.abs(grad_eps_x + 1e-12))  # Avoid div by zero
print(f"Effective flexoelectric coefficient: {mu_eff:.3e} C/m")
print(f"(Target from Wen et al. 2025: ~1.14e-9 C/m)")

# -------------------------------
# Visualization
# -------------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 1. Displacement (bending)
axs[0,0].imshow(u_y, extent=[0, L*1e3, -0.05*L*1e3, 0.05*L*1e3],
                aspect='auto', cmap='viridis', origin='lower')
axs[0,0].set_title('Applied Displacement u_y (mm)')
axs[0,0].set_xlabel('x (mm)')
axs[0,0].set_ylabel('y (mm)')

# 2. Strain gradient
axs[0,1].imshow(grad_eps_x, extent=[0, L*1e3, -0.05*L*1e3, 0.05*L*1e3],
                aspect='auto', cmap='RdBu_r', origin='lower')
axs[0,1].set_title('Strain Gradient ∂ε_xx/∂x')
axs[1,1].set_xlabel('x (mm)')  # FIXED: corrected axis label

# 3. Polarization P
# FIXED: "P _1e9" → "P * 1e9" and "L_1e3" → "L * 1e3"
im = axs[1,0].imshow(P * 1e9, extent=[0, L * 1e3, -0.05*L*1e3, 0.05*L*1e3],
                     aspect='auto', cmap='seismic', origin='lower', vmin=-5, vmax=5)
axs[1,0].set_title('Polarization P (nC/m²)')
axs[1,0].set_xlabel('x (mm)')
fig.colorbar(im, ax=axs[1,0], label='nC/m²')

# 4. Line profile at mid-y
mid_y = Ny//2
axs[1,1].plot(x*1e3, P[mid_y, :]*1e9, label='P (nC/m²)')
axs[1,1].set_title('Polarization profile at mid-slab')
axs[1,1].set_xlabel('x (mm)')
axs[1,1].legend()

plt.tight_layout()
plt.show()

# Optional: Save figure for repo
# plt.savefig('ice_flexo_simulation.png', dpi=300)
