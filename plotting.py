import numpy as np
import matplotlib.pyplot as plt

# TASK 1: Create a method that visualizes quaternion rotation from a given array of quaternions
# TASK 2 (optional): Test the RK4 integrator. Plot it against a known analytical solution and measure error in different test cases. Is angular momentum/energy conserved?

def plotGraphs(t_values, q_values, omega_values):
    q_w = q_values[:, 0]
    q_x = q_values[:, 1]
    q_y = q_values[:, 2]
    q_z = q_values[:, 3]

    plt.plot(t_values, q_w, label = 'w')
    plt.plot(t_values, q_x, label = 'x')
    plt.plot(t_values, q_y, label = 'y')
    plt.plot(t_values, q_z, label = 'z')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Orientation')
    plt.show()
    
    omega_x = omega_values[:, 0]
    omega_y = omega_values[:, 1]
    omega_z = omega_values[:, 2]

    plt.plot(t_values, omega_x, label = 'x')
    plt.plot(t_values, omega_y, label = 'y')
    plt.plot(t_values, omega_z, label = 'z')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.show()

def plotRotation(t_values, q_values, omega_values):
    return