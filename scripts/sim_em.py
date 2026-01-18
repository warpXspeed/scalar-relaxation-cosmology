import numpy as np
import matplotlib.pyplot as plt
import os

def run_em_emergence():
    nx, dx, dt, c, gamma, chi = 512, 0.1, 0.01, 1.0, 0.01, 0.1
    x = np.linspace(0, nx*dx, nx)
    phi = np.exp(-(x - 25)**2 / 2) # Local substrate displacement
    phi_old = phi.copy()
    
    os.makedirs('outputs', exist_ok=True)
    
    for t in range(600):
        # Update substrate
        lap = (np.roll(phi, -1) + np.roll(phi, 1) - 2*phi) / dx**2
        phi_new = (2*phi - phi_old*(1 - (gamma*dt)/2) + dt**2 * c**2 * lap) / (1 + (gamma*dt)/2)
        
        # Derive E field: E ~ grad( d_phi / dt )
        stress = (phi_new - phi) / dt
        E = -chi * np.gradient(stress, dx)
        
        phi_old, phi = phi, phi_new
        
        if t == 500:
            plt.plot(x, E, label="Emergent E-Field")
            plt.plot(x, phi/phi.max()*E.max(), '--', alpha=0.3, label="Scalar Phi (Scaled)")
            plt.legend()
            plt.savefig("outputs/em_field.png")
    
    print("EM emergence complete.")

if __name__ == "__main__":
    run_em_emergence()
