"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
     return (2*x)**2/((a-x)*(b-x)) -K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton=newton(k_imbalance,x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def objective(x):
    return k_imbalance(x[0])**2

res = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print(f"Extent x (Newton): {x_newton:.4f}")
print(f"Extent x (SLSQP):  {x_slsqp:.4f}")

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

H2 = a - x_newton
I2 = b - x_newton
HI = 2 * x_newton

print(f"\nEquilibrium Amounts:")
print(f"H2: {H2:.4f} mol")
print(f"I2: {I2:.4f} mol")
print(f"HI: {HI:.4f} mol")


x_vals = np.linspace(0, 0.99, 100)  # 100 extent values from 0 to 0.99
H2_vals = a - x_vals
I2_vals = b - x_vals # same as H2
HI_vals = 2 * x_vals

plt.plot(x_vals, H2_vals, label="H2 / I2 amount")
plt.plot(x_vals, HI_vals, label="HI amount")
plt.axvline(x_newton, color="red", linestyle="--", label="Equilibrium x")
plt.xlabel("Extent of reaction (x)")
plt.ylabel("Moles")
plt.legend()
plt.savefig("equilibrium.png")