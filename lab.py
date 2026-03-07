import numpy as np
import time

# Generate random temperature data (in Fahrenheit)
raw_data = np.random.uniform(low=-600, high=120, size=1_000_000)

# ----------------------------------------
# APPROACH 1: TRADITIONAL LOOP METHOD
# ----------------------------------------
def process_with_loops(data):
    result = []

    for temp in data:
        # Filter: keep temperatures above absolute zero (-459.67°F)
        if temp > -459.67:
            # Convert Fahrenheit to Celsius
            celsius = (temp - 32) * (5/9)
            result.append(celsius)

    return result


print("Starting loop-based processing...")
start_time = time.time()

loop_output = process_with_loops(raw_data)

loop_duration = time.time() - start_time
print(f"Loop Duration: {loop_duration:.4f} seconds")


# ----------------------------------------
# APPROACH 2: NUMPY VECTORIZATION METHOD
# ----------------------------------------
def process_with_numpy(data):

    # Create mask for valid temperatures
    mask = data > -459.67

    # Filter valid data
    valid_data = data[mask]

    # Convert to Celsius using vectorized operation
    celsius_array = (valid_data - 32) * (5/9)

    return celsius_array


print("\nStarting NumPy vectorized processing...")
start_time = time.time()

numpy_output = process_with_numpy(raw_data)

numpy_duration = time.time() - start_time
print(f"NumPy Duration: {numpy_duration:.4f} seconds")


# ----------------------------------------
# Compare performance
# ----------------------------------------
print("\nPerformance Comparison:")
print(f"Loop Time  : {loop_duration:.4f} seconds")
print(f"NumPy Time : {numpy_duration:.4f} seconds")

speedup = loop_duration / numpy_duration
print(f"Speedup    : {speedup:.2f}x faster using NumPy")