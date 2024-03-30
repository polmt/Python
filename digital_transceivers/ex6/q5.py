import numpy as np
import matplotlib.pyplot as plt

num_tx_antennas = 2
num_rx_antennas = 3

snr_dB_values = np.arange(-10, 21, 2)

ser_results = []

num_repetitions = 1000

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)
Tx = np.random.choice(qam_symbols, size=(4, 1))


for snr_dB in snr_dB_values:
    snr_linear = 10 ** (snr_dB / 10)
    ser_sum = 0

    for _ in range(num_repetitions):

        P_Tx = np.mean(np.abs(Tx) ** 2)

        P_N = P_Tx / (snr_linear * 2)

        N = np.sqrt(P_N / 2) * (np.random.randn(num_rx_antennas, 1) + 1j * np.random.randn(num_rx_antennas, 1))

        R = np.dot(H, Tx) + N

        H_inv = np.linalg.pinv(H)
        decoded_symbols = np.dot(H_inv, R)

        symbol_errors = np.sum(np.round(decoded_symbols) != np.round(Tx))
        ser_sum += symbol_errors

    average_ser = ser_sum / num_repetitions

    ser_results.append(average_ser)

plt.figure()
plt.semilogy(snr_dB_values, ser_results, marker='o', linestyle='-', color='b')
plt.grid(True)
plt.title('Average Symbol-Error-Rate vs. SNR')
plt.xlabel('SNR (dB)')
plt.ylabel('Average SER (log scale)')
plt.show()
