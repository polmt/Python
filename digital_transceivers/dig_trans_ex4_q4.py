import numpy as np

# Define the 4-QAM symbol set
qam_symbols = np.array([1 + 1j, 1 - 1j, -1 - 1j, -1 + 1j])

# Generate a random 2x1 vector using the symbols
vector = np.random.choice(qam_symbols, size=(2, 1))

# Display the resulting vector
print("2x1 Vector with 4-QAM Symbols:")
print(vector)
