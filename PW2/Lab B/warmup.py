"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""

import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
gd=0.0
lr = 0.1
for _ in range(100):
    step=lr*df(gd)
    gd=gd-step
    if(abs(step)<1e-6): break
print(f"Gradient Descent: x = {gd:.4f}")

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
x_newton = newton(df, 0.0, fprime=d2f)
print(f"Newton's Method: x = {x_newton:.4f}")

#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
res = minimize(f, 0.0, method="SLSQP")
print(f"SLSQP: x = {res.x[0]:.4f}\n")



print("---------- 2B: harder landscape ----------")
# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.

for x0 in [0.0, 2.0]:
    
    
    # 1. Gradient descent
    x_gd = x0
    lr = 0.05
    for _ in range(1000):
        step = lr * dg(x_gd)
        x_gd = x_gd - step
        if abs(step) < 1e-6: break
    print(f"Gradient Descent: x = {x_gd:.4f}")
    
    
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
    x_newton = newton(dg, x0, fprime=d2g)
    curvature = d2g(x_newton)
    if curvature > 0:
        nature = "minimum"
    elif curvature < 0: 
        nature = "maximum"
    else:
        nature = "inflection point"
    print(f"Newton's Method: x = {x_newton:.4f} ({nature})")
    
    # 3. SLSQP Minimize
    res_slsqp = minimize(g, x0, method="SLSQP")
    print(f"SLSQP: x = {res_slsqp.x[0]:.4f}\n")

#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?