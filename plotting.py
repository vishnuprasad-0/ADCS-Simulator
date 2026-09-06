import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from quaternion import q_to_matrix

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

def plotRotation(t_values, q_values, omega_values, step=16):
    """Plots and animates the rotation of a satellite in 3D space based on quaternion orientation and angular velocity."""

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(-1,1); ax.set_ylim(-1,1); ax.set_zlim(-1,1) # Stops matplotlib from auto-scaling the axes
    ax.set_box_aspect([1,1,1]) # Equal axis scale on screen
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z') # Label the axes
    
    colors = ['tab:red', 'tab:green', 'tab:blue']  # Colors for the axes
    arrows = []
    title = ax.set_title('')

    HALF = 0.35
    CUBE_VERTICES = HALF * np.array([
        [-1, -1, -1],[-1, -1,  1],[-1,  1, -1],[-1,  1,  1],
        [ 1, -1, -1],[ 1, -1,  1],[ 1,  1, -1],[ 1,  1,  1]
    ], dtype=float)
    CUBE_FACES = [
        [0, 2, 3, 1], [4, 6, 7, 5], [0, 1, 5, 4], 
        [3, 2, 6, 7], [1, 5, 7, 3], [0, 4, 6, 2]
    ]  # Each face is defined by the indices of its vertices
    FACE_COLORS = ["#E26464"] + 1*["#b7cbe6"] +["#479859"] + 2*["#b7cbe6"] + ["#4b81c9"] # Color for each face of the cube

    body = Poly3DCollection([], facecolors=FACE_COLORS, edgecolors='k', linewidths=0.6, alpha=1.0)  # Create a Poly3DCollection for the satellite body
    ax.add_collection(body)
    ax.set_proj_type('ortho')

    def update(i):
        R = q_to_matrix(q_values[i])
        verts = CUBE_VERTICES @ R.T
        body.set_verts([[verts[k] for k in face] for face in CUBE_FACES])
        R = q_to_matrix(q_values[i]) # Get the rotation matrix for the current quaternion
        for a in arrows:
            a.remove()  # Remove the previous arrows
        arrows[:] = [ax.quiver(0,0,0,*R[:,j], color = colors[j], lw=2) for j in range(3)] # Draw new arrows for the current orientation            title.set_text(f't = {t[i]:.2f} s') # Update the title with the current time
        title.set_text(f't = {t_values[i]:.2f} s') # Update the title with the current time
        return()
    
    anim = FuncAnimation(fig, update, frames = range(0, len(t_values), step), interval=30, blit=False)
    plt.show()
    