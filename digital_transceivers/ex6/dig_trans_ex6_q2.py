import numpy as np

# Define the dimensions of the MIMO system
num_tx_antennas = 2  # Number of transmit antennas
num_rx_antennas = 3  # Number of receive antennas

# Generate a complex Gaussian MIMO channel matrix H
H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)

# Print the resulting MIMO channel matrix
print("H:")
print(H)
