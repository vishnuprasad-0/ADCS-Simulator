import numpy as np
from quaternion import q_mul, q_conj

def PID(sat):
    return sat.torque