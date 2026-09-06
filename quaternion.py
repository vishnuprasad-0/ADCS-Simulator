import numpy as np

# Quaternion multiplication
def q_mul(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])

# Quaternion conjugation
def q_conj(q):
    w, x, y, z = q
    return np.array([w, -x, -y, -z])

# Quaternion to rotational matrix conversion
def q_to_matrix(q):
    w, x, y, z = q
    return np.array([
        [1-2*(y**2 + z**2), 2*(x*y - w*z), 2*(x*z + w*y)],
        [2*(x*y + w*z), 1-2*(x**2 + z**2), 2*(y*z - w*x)],
        [2*(x*z - w*y), 2*(y*z + w*x), 1-2*(x**2 + y**2)]
    ])