import numpy as np
import matplotlib.pyplot as plt

def omega_dot(torque, inertia, omega):
    Iomega = inertia @ omega
    rhs = torque - np.cross(omega, Iomega)
    omega_dot = np.linalg.solve(inertia, rhs)

    return omega_dot