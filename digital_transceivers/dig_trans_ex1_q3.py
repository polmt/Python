import numpy as np

def generate_random_symbols(N):
    # Generate N random values from a uniform distribution in the range [0, 1]
    random_values = np.random.rand(N)

    # Assign -1 with probability 0.75 and 1 with probability 0.25
    symbols = np.where(random_values < 0.75, -1, 1)

    return symbols

# Example usage:
N = 10  # You can change N to your desired size
random_array = generate_random_symbols(N)
print(random_array)
