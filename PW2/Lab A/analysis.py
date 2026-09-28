"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

# Assuming the CSV has a header row like time,y
t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

print(f"Mean acceleration: {np.mean(a):.2f} m/s^2")
print(f"Standard deviation: {np.std(a):.2f} m/s^2")


v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]

y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_recovered - y))
print(f"Max difference: {max_diff:.2f} m")


# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Top panel: Position
ax1.plot(t, y, color="blue")
ax1.set_ylabel("Position (m)")
ax1.set_title("Object Motion over Time")

# Middle panel: Velocity
ax2.plot(t, v, color="orange")
ax2.set_ylabel("Velocity (m/s)")

# Bottom panel: Acceleration
ax3.plot(t, a, color="green", label="Measured")
ax3.axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s²") # Dashed line for expected gravity
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s²)")
ax3.legend()

plt.tight_layout()
plt.savefig("motion.png")


# --- Bonus: 2D Tracked Trajectory ---

t_traj, x, y = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1, unpack=True)
vx = np.gradient(x, t_traj)
vy = np.gradient(y, t_traj)
speed = np.sqrt(vx**2 + vy**2)

# Create a 1x2 figure for the bonus plots
fig2, (ax_path, ax_speed) = plt.subplots(1, 2, figsize=(10, 4))

# Left panel: Plot the 2D path
ax_path.plot(x, y, color="purple")
ax_path.set_title("2D Path")
ax_path.set_xlabel("x (m)")
ax_path.set_ylabel("y (m)")

ax_speed.plot(t_traj, speed, color="teal")
ax_speed.set_title("Speed over Time")
ax_speed.set_xlabel("Time (s)")
ax_speed.set_ylabel("Speed (m/s)")

plt.tight_layout()
plt.savefig("trajectory.png")