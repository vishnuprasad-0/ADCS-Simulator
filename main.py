import numpy as np
from integrator import run_integration
from plotting import plotGraphs
from spacecraft import Spacecraft

# q = quaternion orientation
# omega = rotational velocity

def main():
    # Defines initial simulation parameters
    t0 = 0
    tf = 5
    dt = 0.01
    sat = Spacecraft(
        inertia = np.diag([2.0, 3.0, 4.0]),
        torque = np.array([1., 2., 3.]),
        omega = np.array([1.,2.,3.]),
        q = np.array([1.,0.,0.,0.])
    )

    # Calculates and plots q, omega through timeframe
    t_values, q_values, omega_values = run_integration(t0, tf, dt, sat)
    plotGraphs(t_values, q_values, omega_values)

if __name__ == '__main__':
    main()