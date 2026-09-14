"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
# pytest.raises checks that the code inside the 'with' block throws a ValueError
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
         simulate(1000, -0.4)


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?
def test_matches_law():
    N0 = 1000
    lam = 0.4
    dt = 0.05
    step_index = 40  # Check the array at step 40
    
    # Run the simulation 100 times, changing the seed every time!
    results = []
    for s in range(100):
        # We pass the loop variable 's' as the seed to get random results
        sim_data = simulate(N0, lam, dt=dt, seed=s)
        results.append(sim_data[step_index])
        
    avg_remaining = np.mean(results)
    
    # Actual physical time is (number of steps * time per step)
    physical_time = step_index * dt 
    
    # Calculate exact physical law: N0 * e^(-lam * time)
    expected = N0 * np.exp(-lam * physical_time)
    
    # Compare with a 5% tolerance
    assert avg_remaining == pytest.approx(expected, rel=0.05)