import numpy as np

num_tx_antennas = 2
num_rx_antennas = 3

H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

Tx = np.random.choice(qam_symbols, size=(4, 1))

SNR_dB = 3
SNR_linear = 10 ** (SNR_dB / 10)

P_Tx = np.mean(np.abs(Tx) ** 2)

P_N = P_Tx / (SNR_linear * 2)

N = np.sqrt(P_N / 2) * (np.random.randn(num_rx_antennas, 1) + 1j * np.random.randn(num_rx_antennas, 1))

R = np.dot(H, Tx) + N

H_inv = np.linalg.pinv(H)
decoded_symbols = np.dot(H_inv, R)

symbol_errors = np.sum(np.round(decoded_symbols) != np.round(Tx))

print("Symbol Errors:", symbol_errors)
