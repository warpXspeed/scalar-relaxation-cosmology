import numpy as np
from scipy.ndimage import laplace

def get_step_params(gamma, dt):
    """Calculates stability coefficient beta."""
    return (gamma * dt) / 2

def update_phi(phi, phi_old, beta, dt_sq_c_sq, dx_sq):
    """
    Core SRC Damped Wave Update.
    phi_new = [2*phi - phi_old(1-beta) + dt^2 * c^2 * lap(phi)/dx^2] / (1+beta)
    """
    lap = laplace(phi) / dx_sq
    phi_new = (2*phi - phi_old*(1 - beta) + dt_sq_c_sq * lap) / (1 + beta)
    return phi_new

def get_energy(phi, phi_old, dt, c, dx):
    """Returns average Hamiltonian density (Kinetic + Potential)."""
    vel = (phi - phi_old) / dt
    # Gradient energy (approx via laplace for speed in 3D)
    # Correct grad energy is 0.5 * c^2 * |grad phi|^2
    gy, gx = np.gradient(phi, dx)
    return 0.5 * np.mean(vel**2) + 0.5 * (c**2) * np.mean(gx**2 + gy**2)
