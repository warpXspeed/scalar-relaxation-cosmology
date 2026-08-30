#!/usr/bin/env python3
"""
SREC Cosmic Clockwork — Ultra-Minimal Version (only needs numpy)
Runs on any openSUSE box with zero extra packages.
"""

import numpy as np

# USER SETTINGS — change anything
beta_g             = -4.8e-6
beta_gamma         =  5.5e-7
chaos_factor       =  0.02
main_period_yr     =  12_850
hallstatt_factor   =  5.35
nova_threshold     =  5.0
mass_loss_future   =  0.5
oort_feed_base     =  1e-5
disk_time_myr      =  6.0
future_gyr         =  5.0

sec_per_yr   = 365.25 * 24 *3600
age_universe_sec = 13.787e9 * sec_per_yr

def phi(t_sec):
    return 0.82 * (1.0 - t_sec/sec_per_yr / 13.8e9)

def alpha_eff(t_sec):
    return 7.2973525693e-3 * np.exp(beta_gamma * phi(t_sec))

def cme_kick(t_sec, period_yr):
    t_yr = t_sec / sec_per_yr
    phase = 2 * np.pi * (t_yr % period_yr) / period_yr
    return 1.0 + 1.8e-4 * np.sin(phase)**2

def total_kick(t_sec, mass_loss=1.0, feed=1e-5):
    k1 = cme_kick(t_sec, main_period_yr)
    k2 = cme_kick(t_sec, main_period_yr / hallstatt_factor)
    alpha_b = np.sqrt(alpha_eff(t_sec) / 7.2973525693e-3)
    cond_b  = 1.0 + 0.5 * np.log10(feed / 1e-5 + 1.0)
    return k1 * k2 * alpha_b * cond_b / mass_loss

# Simple eddy growth without scipy
def simulate_eddies(steps=150):
    t = np.linspace(0, disk_time_myr, steps)
    omega = np.zeros(steps)
    omega[0] = 1e-6
    dt = disk_time_myr / (steps-1)
    for i in range(1, steps):
        t_sec = t[i] * 1e6 * sec_per_yr
        em    = np.sqrt(alpha_eff(t_sec) / 7.2973525693e-3)
        chaos = chaos_factor * np.random.normal()
        omega[i] = omega[i-1] * (1 + dt * (em - 1.0 + chaos))
    return t, np.maximum(omega, 1e-30)

t, omega = simulate_eddies()

kick_early  = total_kick(age_universe_sec - 0.1e9 * sec_per_yr)
kick_future = total_kick(age_universe_sec + future_gyr*1e9*sec_per_yr,
                        mass_loss=mass_loss_future,
                        feed=oort_feed_base*25)

dv_jupiter = kick_early * 1e-3 / 5.0

hallstatt_period = main_period_yr / hallstatt_factor
years_to_next = hallstatt_period - (age_universe_sec/sec_per_yr % hallstatt_period)

nova = "NOVA — explosive reset!" if kick_future > nova_threshold else "Stable feeding"

# Text “plot”
print("\nEddy growth during planet formation (log scale):")
for i in range(0, len(t), 8):
    bars = int(40 * np.log10(omega[i]/1e-6 + 1))
    print(f"{t[i]:4.1f} Myr → {'█'*bars} {omega[i]:.2e}")

print("\nSREC COSMIC CLOCKWORK — CURRENT PREDICTIONS")
print("="*56)
print(f"Early kick (0.1 Gyr ago)           : {kick_early: .4f} × today")
print(f"Velocity kick at 5 AU (Jupiter)    : {dv_jupiter:.3f} km s⁻¹")
print(f"Future declining-Sun kick            : {kick_future:.3f} × today")
print(f"→ {nova}")
print(f"Next Hallstatt peak (~2400 yr)      : ~{years_to_next:.0f} years from now")
print(f"   → around year {2025 + years_to_next:.0f} CE")
print("="*56)
