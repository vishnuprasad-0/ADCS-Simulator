import numpy as np
from dynamics import omega_dot, q_dot

class Spacecraft:
    def __init__(self, inertia, torque, omega, q):
        self.inertia = inertia
        self.torque = torque
        self.omega = omega
        self.q = q

    def get_state(self):
        return np.concatenate((self.omega, self.q))

    def set_state(self, state):
        self.omega = state[:3]
        self.q = state[3:]

    def state_dot(self, state):
        omega = state[:3]
        q = state[3:]
        
        return np.concatenate((
            omega_dot(self.inertia, self.torque, omega),
            q_dot(q, omega)
        ))