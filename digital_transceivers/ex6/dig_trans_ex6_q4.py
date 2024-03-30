import numpy as np

# Define the dimensions of the MIMO system
num_tx_antennas = 2  # Number of transmit antennas
num_rx_antennas = 3  # Number of receive antennas

# Generate a complex Gaussian MIMO channel matrix H as previously explained
H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

# Generate the Tx vector (4x1 4-QAM symbols) as previously explained
Tx = np.random.choice(qam_symbols, size=(4, 1))

SNR_dB = 3
SNR_linear = 10 ** (SNR_dB / 10)

P_Tx = np.mean(np.abs(Tx) ** 2)

P_N = P_Tx / (SNR_linear * 2)  # Divide by 2 due to complex noise

N = np.sqrt(P_N / 2) * (np.random.randn(num_rx_antennas, 1) + 1j * np.random.randn(num_rx_antennas, 1))

# Generate the received vector R as previously explained
R = np.dot(H, Tx) + N

# Perform Zero-Forcing (ZF) detection
H_inv = np.linalg.pinv(H)  # Calculate the pseudo-inverse of H
decoded_symbols = np.dot(H_inv, R)

# Calculate the symbol errors
symbol_errors = np.sum(np.round(decoded_symbols) != np.round(Tx))  # Compare rounded symbols

# Print the results
print("Symbol Errors:", symbol_errors)
