import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

print("Starting simulation with")


start_loop = time.perf_counter()
simulate_loop(N0, lam)
end_loop = time.perf_counter()
loop_time = end_loop - start_loop

print(f"Loop version took:  {loop_time:.4f} seconds")

# Time the vectorized NumPy version
start_numpy = time.perf_counter()
simulate(N0, lam)
end_numpy = time.perf_counter()
numpy_time = end_numpy - start_numpy
print(f"NumPy version took: {numpy_time:.4f} seconds")

# Calculate the speed-up factor
speed_up = loop_time / numpy_time
print(f"\nNumPy is {speed_up:.1f}x faster!")