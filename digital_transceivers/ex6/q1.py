import numpy as np

# Define the 4-QAM symbols
qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

# Generate a random 4x1 vector of 4-QAM symbols
Tx = np.random.choice(qam_symbols, size=(4, 1))

# Print the resulting vector
print("Tx:")
print(Tx)
