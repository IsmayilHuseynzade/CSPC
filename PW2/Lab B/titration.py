import numpy as np
import matplotlib.pyplot as plt

v,pH = np.loadtxt("titration.csv", delimiter=",", skiprows=1, unpack=True)


slope=np.gradient(pH,v)

max_slope_index = np.argmax(slope)
eq_v= v[max_slope_index]
print(f"Equivalence point volume: {eq_v:.2f} mL")




fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First plot: pH curve
ax1.plot(v, pH, marker='.', color='blue')
ax1.axvline(eq_v, color='red', linestyle='--', label=f'Eq Pt ~{eq_v:.0f}mL')
ax1.set_xlabel("Volume of Base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.legend()

# Second plot: Slope curve
ax2.plot(v, slope, marker='.', color='orange')
ax2.axvline(eq_v, color='red', linestyle='--', label=f'Max Slope')
ax2.set_xlabel("Volume of Base (mL)")
ax2.set_ylabel("Slope (dpH/dV)")
ax2.set_title("Derivative Curve")
ax2.legend()

plt.tight_layout()
plt.savefig("titration.png")