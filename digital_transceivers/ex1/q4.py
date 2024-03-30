import numpy as np

def generate_random_symbols(N):
    # Generate N random values from a uniform distribution in the range [0, 1]
    random_values = np.random.rand(N)

    # Assign -1 with probability 0.75 and 1 with probability 0.25
    symbols = np.where(random_values < 0.75, -1, 1)

    return symbols
def calculate_relative_frequency(random_array):
    unique, counts = np.unique(random_array, return_counts=True)
    total_count = len(random_array)
    relative_frequencies = counts / total_count
    return dict(zip(unique, relative_frequencies))

# Generate arrays for N=10, N=100, and N=1000
N_values = [10, 100, 1000]
for N in N_values:
    random_array = generate_random_symbols(N)
    relative_frequency = calculate_relative_frequency(random_array)
    print(f"Relative frequency for N={N}: {relative_frequency}")
