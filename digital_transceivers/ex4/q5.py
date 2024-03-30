import numpy as np

# Define the 4-QAM symbol set
qam_symbols = np.array([1 + 1j, 1 - 1j, -1 - 1j, -1 + 1j])

# Generate a random 2x1 vector using the symbols
vector = np.random.choice(qam_symbols, size=(2, 1))

# Calculate the covariance matrix
covariance_matrix = np.outer(vector, np.conj(vector))

# Calculate the total power
total_power = np.sum(np.abs(vector) ** 2)

# Display the covariance matrix and total power
print("Covariance Matrix:")
print(covariance_matrix)

print("\nTotal Power of the Vector:", total_power)
