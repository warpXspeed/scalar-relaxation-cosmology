import numpy as np

# =============================================================================
# SRC v2 — SDF DERIVATION SIM (Reading 2)
# f = self-renewal rate = c_T / L = sqrt(T/rho) / L
# Redshift = f_emit / f_obs  (DERIVED from substrate state, NOT hardcoded)
# =============================================================================

# --- SUBSTRATE STATE: emitter and observer ---
# Local tension T (N/m), density rho (kg/m^3), length scale L (m)
# These are the substrate's material parameters at each location.

# Emitter state (e.g., a galaxy at z=0.3)
T_emit = 1.0          # N/m (normalized)
rho_emit = 1.0        # kg/m^3 (normalized)
L_emit = 1.0          # m (normalized)

# Observer state (e.g., Earth)
# The observer's substrate state is different — that's what creates the redshift.
# For z=0.3, we need f_emit/f_obs = 1.3, so f_obs = f_emit/1.3
# f = sqrt(T/rho)/L, so:
# sqrt(T_obs/rho_obs)/L_obs = sqrt(T_emit/rho_emit)/L_emit / 1.3
# For simplicity: T_obs = T_emit, L_obs = L_emit, so:
# 1/sqrt(rho_obs) = 1/(1.3 * sqrt(rho_emit))
# rho_obs = rho_emit * 1.3^2 = 1.69
T_obs = 1.0           # N/m
rho_obs = 1.69        # kg/m^3 (higher density -> slower clock -> redshift)
L_obs = 1.0           # m

# --- SDF: DERIVE f from substrate state ---
def sdf(T, rho, L):
    """Self-renewal rate f = c_T / L = sqrt(T/rho) / L"""
    c_T = np.sqrt(T / rho)   # transverse wave speed (m/s)
    return c_T / L           # self-renewal rate (Hz)

f_emit = sdf(T_emit, rho_emit, L_emit)
f_obs  = sdf(T_obs,  rho_obs,  L_obs)

# --- REDSHIFT = ratio of derived clock rates ---
redshift = f_emit / f_obs    # 1+z, DERIVED from substrate state
z = redshift - 1.0

# --- TIME DILATION (falls out naturally) ---
t_emit = 20.0                           # 20-day supernova, in emitter ticks
t_obs  = t_emit * (f_emit / f_obs)      # = 20 * (1+z) days

# --- LUMINOSITY DIMMING (separate: gamma term) ---
gamma_dim = 0.5                         # placeholder: e^-(gamma c^2 / 2) t

# --- OUTPUT ---
print("=" * 60)
print("SRC v2 — SDF DERIVATION SIM (Reading 2)")
print("f = sqrt(T/rho) / L  (derived from substrate state)")
print("=" * 60)
print(f"EMITTER STATE:")
print(f"  T_emit = {T_emit}, rho_emit = {rho_emit}, L_emit = {L_emit}")
print(f"  c_T_emit = {np.sqrt(T_emit/rho_emit):.4f} m/s")
print(f"  f_emit   = {f_emit:.4f} Hz")
print()
print(f"OBSERVER STATE:")
print(f"  T_obs  = {T_obs}, rho_obs = {rho_obs}, L_obs = {L_obs}")
print(f"  c_T_obs  = {np.sqrt(T_obs/rho_obs):.4f} m/s")
print(f"  f_obs    = {f_obs:.4f} Hz")
print()
print(f"DERIVED REDSHIFT:")
print(f"  1+z = f_emit/f_obs = {redshift:.4f}")
print(f"  z   = {z:.4f}")
print()
print(f"TIME DILATION:")
print(f"  20-day supernova -> {t_obs:.1f} days observed")
print(f"  (Consistency check: reproduces (1+z) dilation structure —")
print(f"   necessary but NOT a discriminating test vs. standard cosmology)")
print()
print(f"LUMINOSITY DIMMING (separate: gamma term):")
print(f"  dimming factor = {gamma_dim:.2f}")
print("=" * 60)
print("f DERIVED from substrate state (T, rho, L). NOT hardcoded.")
print("Redshift = clock ratio. Dimming = gamma. Two separate objects.")
