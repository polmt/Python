import numpy as np

# Define the size of the matrix
rows, cols = 3, 3

# Generate complex Gaussian random elements with zero mean and unit variance
real_part = np.random.randn(rows, cols) / np.sqrt(2)
imag_part = np.random.randn(rows, cols) / np.sqrt(2)

# Create the complex Rayleigh MIMO matrix
rayleigh_matrix = real_part + 1j * imag_part

# Display the resulting matrix
print("Complex Rayleigh MIMO Matrix:")
print(rayleigh_matrix)
