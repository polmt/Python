import numpy as np

# Define the dimensions of the MIMO system
num_tx_antennas = 2  # Number of transmit antennas
num_rx_antennas = 3  # Number of receive antennas

# Generate a complex Gaussian MIMO channel matrix H as previously explained
H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

# Generate the Tx vector (4x1 4-QAM symbols) as previously explained
Tx = np.random.choice(qam_symbols, size=(4, 1))


# Compute the power of the transmitted signal
P_Tx = np.mean(np.abs(Tx) ** 2)

# Calculate the noise power based on the desired SNR (3 dB)
SNR_dB = 3
SNR_linear = 10 ** (SNR_dB / 10)
P_N = P_Tx / (SNR_linear * 2)  # Divide by 2 due to complex noise

# Generate the AWGN vector N
N = np.sqrt(P_N / 2) * (np.random.randn(num_rx_antennas, 1) + 1j * np.random.randn(num_rx_antennas, 1))

# Compute the received vector R
R = np.dot(H, Tx) + N

# Print the resulting received vector R
print("R:")
print(R)
