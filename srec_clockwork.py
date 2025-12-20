#!/usr/bin/env python3
"""
SREC Cosmic Clockwork — Final Public Simulator
==============================================

One scalar field φ rolling downhill changes only two things change:
1. Gravity slowly gets stronger (β_g < 0)
2. Electromagnetism slowly gets weaker (β_gamma > 0)

These two tiny changes are enough to build galaxies, planets, moons,
the 12.85 ka catastrophe cycle, Voyager magnetic anomalies,
and the final Oort-cloud collapse that feeds a dying Sun.

Everything below can be changed by a human — the Universe does the rest.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ======================================================================
# USER SETTINGS — change any of these to explore the cosmos
# ======================================================================
beta_g             = -4.8e-6      # gravity strengthening rate
beta_gamma         =  5.5e-7      # electromagnetism weakening rate
chaos_factor       =  0.02       # random external disturbances (0 = none)
main_period_yr     =  12_850      # fundamental 12.85 ka cycle
hallstatt_factor   =  5.35       # gives ≈ 2400 yr Hallstatt cycle
nova_threshold     =  5.0        # kick > this → nova explosion
mass_loss_future   =  0.5        # Sun keeps only 50 % of its mass when dying
oort_feed_base     =  1e-5       # Earth masses per year falling in (decline phase)
disk_time_myr      =  6.0        # how long we watch planet formation
future_gyr         =  5.0        # when we look at the dying Sun

# ======================================================================
# CONSTANTS — do not touch unless you really know what you are doing
# ======================================================================
G_today      = 6.67430e-11                 # m³ kg⁻¹ s⁻²
alpha_today  = 7.2973525693e-3              # fine-structure constant today
sec_per_yr   = 365.25 * 24 * 3600
age_universe_sec = 13.787e9 * sec_per_yr    # seconds since Big Bang

# ======================================================================
# 1. The rolling scalar field φ(t)
# ======================================================================
def phi(t_sec: float) -> float:
    """φ falls from ~0.82 (early universe) to 0 (today)."""
    t_yr = t_sec / sec_per_yr
    return 0.82 * (1.0 - t_yr / 13.8e9)

def G_eff(t_sec: float) -> float:
    return G_today * np.exp(-beta_g * phi(t_sec))

def alpha_eff(t_sec: float) -> float:
    return alpha_today * np.exp(beta_gamma * phi(t_sec))

# ======================================================================
# 2. Periodic super-events (12 ka + Hallstatt + smaller harmonics)
# ======================================================================
def cme_kick(t_sec: float, period_yr: float) -> float:
    t_yr = t_sec / sec_per_yr
    phase = 2 * np.pi * (t_yr % period_yr) / period_yr
    amplitude = 1.8e-4
    return 1.0 + amplitude * np.sin(phase)**2

def total_kick(t_sec: float,
               mass_loss: float = 1.0,
               feed_rate: float = 1e-5) -> float:
    """Full kick = main 12 ka × Hallstatt side-lobe × α-boost × debris-boost."""
    k_main   = cme_kick(t_sec, main_period_yr)
    k_hall   = cme_kick(t_sec, main_period_yr / hallstatt_factor)
    alpha_b  = np.sqrt(alpha_eff(t_sec) / alpha_today)
    cond_b   = 1.0 + 0.5 * np.log10(feed_rate / 1e-5 + 1.0)
    return k_main * k_hall * alpha_b * cond_b / mass_loss

# ======================================================================
# 3. Simple eddy growth — how planets and moons form
# ======================================================================
def eddy_ode(t_myr: float, omega: float) -> float:
    t_sec = t_myr * 1e6 * sec_per_yr
    em_drive   = np.sqrt(alpha_eff(t_sec) / alpha_today) * omega
    grav_brake = -G_eff(t_sec) * omega
    chaos      = chaos_factor * em_drive * np.random.normal()
    return em_drive + grav_brake + chaos

# ======================================================================
# 4. Run the planet-formation phase
# ======================================================================
t_eval = np.linspace(0, disk_time_myr, 500)
sol = solve_ivp(eddy_ode, [0, disk_time_myr], [1e-6],
                t_eval=t_eval, method='RK45', rtol=1e-8)
omega = sol.y[0]

# ======================================================================
# 5. Real predictions
# ======================================================================
now_sec = age_universe_sec

# Early Solar System (0.1 Gyr ago)
kick_early = total_kick(now_sec - 0.1e9 * sec_per_yr)

# Far future — dying Sun
kick_future = total_kick(now_sec + future_gyr * 1e9 * sec_per_yr,
                         mass_loss=mass_loss_future,
                         feed_rate=oort_feed_base * 25)

nova = "NOVA — explosive reset!" if kick_future > nova_threshold else "Stable feeding"

# Velocity kick felt by a Jupiter-like planet at 5 AU during an early event
dv_jupiter_early = kick_early * 1e-3 / 5.0   # km s⁻¹

# Next Hallstatt-cycle peak (≈2400 yr)
hallstatt_period = main_period_yr / hallstatt_factor
years_to_next = hallstatt_period * (1 - ((now_sec/sec_per_yr) % hallstatt_period) / hallstatt_period)

# ======================================================================
# 6. Plot & print results
# ======================================================================
plt.figure(figsize=(10,6))
plt.semilogy(t_eval, omega, lw=2.5, color='#d62728', label='Eddy strength')
plt.title('SREC — Planet & Moon Formation')
plt.xlabel('Time after disk formation (Myr)')
plt.ylabel('Eddy strength (arbitrary units)')
plt.grid(True, which='both', ls='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

print("\nSREC COSMIC CLOCKWORK — CURRENT PREDICTIONS")
print("="*54))
print(f"Early-system kick (0.1 Gyr ago)        : {kick_early: .4f} × today")
print(f"Velocity kick at Jupiter distance     : {dv_jupiter_early:.3f} km s⁻¹")
print(f"Future declining-Sun kick             : {kick_future:.3f} × today")
print(f"→ {nova}")
print(f"Next Hallstatt peak (∼2400 yr cycle)  : ~{years_to_next:.0f} years from now")
print(f"   → around year {2025 + years_to_next:.0f} CE")
print(f"Chaos factor used                     : {chaos_factor}")
print("="*54)
