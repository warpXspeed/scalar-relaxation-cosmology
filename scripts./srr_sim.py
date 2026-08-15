import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import engine

def run_redshift():
    nx, dx, dt, c, gamma = 1024, 0.1, 0.01, 1.0, 0.02
    x = np.linspace(0, nx*dx, nx)
    # Initial Wave Packet
    phi = np.exp(-(x - 20)**2 / 10) * np.sin(2 * np.pi * 5 * x)
    phi_old = phi.copy()
    beta = engine.get_step_params(gamma, dt)
    
    results = []
    for t in range(2000):
        phi_new = engine.update_phi(phi, phi_old, beta, dt**2 * c**2, dx**2)
        phi_old, phi = phi, phi_new
        
        if t % 500 == 0:
            spec = np.abs(fft(phi))
            freqs = fftfreq(nx, dx)
            idx = np.where(freqs > 0)
            peak_f = freqs[idx][np.argmax(spec[idx])]
            results.append((t*dt, peak_f))
    
    times, peaks = zip(*results)
    plt.plot(times, peaks, 'r-o')
    plt.xlabel("Propagation Time")
    plt.ylabel("Peak Frequency")
    plt.title("Viscous Redshift (Dissipative Loss)")
    plt.savefig("outputs/redshift_curve.png")
    plt.close()
    print("Redshift simulation complete.")

if __name__ == "__main__":
    run_redshift()
