import numpy as np
from quaternion import q_mul

# Euler's rotation equation (vector form)
def omega_dot(inertia, torque, omega):
    Iomega = inertia @ omega
    rhs = torque - np.cross(omega, Iomega)
    omega_dot = np.linalg.solve(inertia, rhs)

    return omega_dot

# q_dot = 1/2 * q x w
def q_dot(q, omega):
    omega_q = np.insert(omega, 0, 0) # converts omega to quaternion form
    return 0.5 * q_mul(q, omega_q)