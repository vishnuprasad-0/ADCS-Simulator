import numpy as np
from controller import PID

# Runge-Kutta 4 integration method
def RK4(sat, dt):
    state = sat.get_state()

    # Calculate slopes at 4 points during each interval
    k1 = sat.state_dot(state) 
    k2 = sat.state_dot(state + dt*k1/2) 
    k3 = sat.state_dot(state + dt*k2/2) 
    k4 = sat.state_dot(state + dt*k3)

    # Update state vector based on RK4 formula
    next_state = state + (dt/6) * (k1 + 2*k2 + 2*k3 + k4) 
    next_state[3:] /= np.linalg.norm(next_state[3:]) # Normalize q to account for error

    return next_state

def run_integration(t0, tf, dt, sat):
    # Create arrays for time steps
    t_values = np.arange(t0, tf + dt, dt)
    omega_values = np.zeros((len(t_values), 3))
    q_values = np.zeros((len(t_values), 4))

    # Set initial conditions
    omega_values[0] = sat.omega
    q_values[0] = sat.q

    # Perform the RK4/PID iteration
    for i in range(1, len(t_values)):
        sat.torque = PID(sat)
        state = RK4(sat, dt)
        sat.set_state(state)

        omega_values[i] = sat.omega
        q_values[i] = sat.q

    return t_values, q_values, omega_values