import numpy as np
import matplotlib.pyplot as plt

# Simple 1D damped Klein-Gordon relaxation demo
L = 50.0
Nx = 500
dx = L / (Nx - 1)
dt = 0.005
gamma = 0.1  # damping rate
lambda_ = 0.05  # nonlinearity

x = np.linspace(0, L, Nx)
phi = np.exp(- (x - L/2)**2 / 2)  # initial Gaussian

phi_history = [phi.copy()]
for _ in range(2000):  # ~t=10
    d2phi = (np.roll(phi, -1) - 2*phi + np.roll(phi, 1)) / dx**2
    dphi_dt = -gamma * phi + d2phi - lambda_ * phi**3
    phi += dt * dphi_dt
    if len(phi_history) % 200 == 0:
        phi_history.append(phi.copy())

plt.plot(x, phi_history[0], label='t=0')
plt.plot(x, phi_history[-1], label='t≈10')
plt.xlabel('x')
plt.ylabel('φ(x)')
plt.title('Damped Klein-Gordon Relaxation')
plt.legend()
plt.savefig('kg_damping_plot.png')
plt.show()
