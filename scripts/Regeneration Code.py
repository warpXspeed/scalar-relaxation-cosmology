import numpy as np

# Parameters from your validation run
gamma_eff = 5.09e-4  # s^{-1} (from fit)
h0 = 1.52e-22        # peak strain at 30 Hz
f0 = 30.0            # Hz
t_max = 12.0         # seconds
dt = 0.001           # timestep for strain series

# Time array
t = np.arange(0, t_max + dt, dt)  # 12001 points

# Strain h(t): damped sinusoid
h = h0 * np.exp(-gamma_eff * t) * np.sin(2 * np.pi * f0 * t)

# Save gw_strain.txt
np.savetxt('gw_strain.txt', np.column_stack([t, h]), fmt='%.6e %.6e', header='t (s) h(t)', comments='')

# PSD (one-sided, strain² Hz⁻¹)
H = np.fft.rfft(h)
psd = 2.0 * np.abs(H)**2 / len(h)**2  # One-sided PSD
f = np.fft.rfftfreq(len(h), d=dt)

# Save gw_psd.txt
np.savetxt('gw_psd.txt', np.column_stack([f, psd]), fmt='%.6e %.6e', header='f (Hz) PSD (strain² Hz⁻¹)', comments='')

print("Files generated: gw_strain.txt and gw_psd.txt")
