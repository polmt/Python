import numpy as np

def sym_rand(N):
    if N % 2 != 0:
        raise ValueError("N should be an even number for equal probability of -1 and 1.")

    # Generate N/2 random values from a uniform distribution in the range [0, 1]
    random_values = np.random.rand(N // 2)

    # Map values less than 0.5 to -1 and values greater than or equal to 0.5 to 1
    symbols = np.where(random_values < 0.5, -1, 1)

    # Create the final array by repeating the symbols
    random_array = np.tile(symbols, 2)

    return random_array

# Example usage:
N = 10  # You can change N to your desired size
random_array = sym_rand(N)
print(random_array)
