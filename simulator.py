import numpy as np
import matplotlib.pyplot as plt
from dynamics import omega_dot
from kinematics import q_dot

# Parameters
omega_0 = np.array([1.,0.,0.])
q_0 = np.array([1.,0.,0.,0.])
inertia = np.diag([2.0, 3.0, 4.0])
torque = np.array([0., 0., 0.])
t0 = 0
tf = 5
dt = 0.01

def state_dot(state):
    omega = state[:3]
    q = state[3:]

    return np.concatenate((
        omega_dot(torque, inertia, omega),
        q_dot(q, omega)
    ))

def RK4(state, dt):
    k1 = state_dot(state)
    k2 = state_dot(state + k1/2)
    k3 = state_dot(state + k2/2)
    k4 = state_dot(state + k3)

    state += dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    state[3:] /= np.linalg.norm(state[3:])

    return state

def run_integration(t0, tf, dt, omega_0, q_0):
    t_values = np.arange(t0, tf + dt, dt)
    omega_values = np.zeros((len(t_values), 3))
    q_values = np.zeros((len(t_values), 4))

    omega_values[0] = omega_0
    q_values[0] = q_0
    state = np.concatenate((omega_0, q_0))

    for i in range(1, len(t_values)):
        state = RK4(state, dt)

        omega_values[i] = state[:3]
        q_values[i] = state[3:]

    return t_values, q_values, omega_values