import numpy as np

num_tx_antennas = 2  # Number of transmit antennas
num_rx_antennas = 3  # Number of receive antennas

H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

Tx = np.random.choice(qam_symbols, size=(4, 1))

P_Tx = np.mean(np.abs(Tx) ** 2)

SNR_dB = 3
SNR_linear = 10 ** (SNR_dB / 10)
P_N = P_Tx / (SNR_linear * 2)  # Divide by 2 due to complex noise

N = np.sqrt(P_N / 2) * (np.random.randn(num_rx_antennas, 1) + 1j * np.random.randn(num_rx_antennas, 1))

R = np.dot(H, Tx) + N

print("R:")
print(R)
