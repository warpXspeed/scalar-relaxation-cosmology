import numpy as np
import matplotlib.pyplot as plt
import engine
import os

def run_defect_sim(size=128, t_max=1000):
    os.makedirs('outputs', exist_ok=True)
    dx, dt, c, gamma = 1.0, 0.1, 1.0, 0.05
    beta = engine.get_step_params(gamma, dt)
    
    # Stochastic seed
    phi = np.random.normal(0, 1.0, (size, size))
    phi_old = phi.copy()
    
    for t in range(t_max):
        phi_new = engine.update_phi(phi, phi_old, beta, dt**2 * c**2, dx**2)
        phi_old, phi = phi, phi_new
        
        if t % 200 == 0:
            # Winding number logic
            gy, gx = np.gradient(phi)
            phase = np.arctan2(gy, gx)
            dp_x = (np.roll(phase, -1, axis=1) - phase + np.pi) % (2*np.pi) - np.pi
            dp_y = (np.roll(phase, -1, axis=0) - phase + np.pi) % (2*np.pi) - np.pi
            winding = (dp_x + np.roll(dp_y, -1, axis=1) - np.roll(dp_x, -1, axis=0) - dp_y) / (2*np.pi)
            
            plt.imshow(np.round(winding), cmap='RdBu')
            plt.title(f"Defect Map t={t}")
            plt.savefig(f"outputs/defect_t{t}.png")
            plt.close()
    print("Defect simulation complete.")

if __name__ == "__main__":
    run_defect_sim()
