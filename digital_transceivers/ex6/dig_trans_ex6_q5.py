import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the MIMO system
num_tx_antennas = 2  # Number of transmit antennas
num_rx_antennas = 3  # Number of receive antennas

# Define SNR values in dB
snr_dB_values = np.arange(-10, 21, 2)  # SNR values from -10 dB to 20 dB in steps of 2 dB

# Initialize an array to store SER results
ser_results = []

# Number of repetitions
num_repetitions = 1000

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)
Tx = np.random.choice(qam_symbols, size=(4, 1))


for snr_dB in snr_dB_values:
    snr_linear = 10 ** (snr_dB / 10)  # Convert SNR to linear scale
    ser_sum = 0

    for _ in range(num_repetitions):
        # Generate a complex Gaussian MIMO channel matrix H as previously explained

        # Generate the Tx vector (4x1 4-QAM symbols) as previously explained

        # Compute the power of the transmitted signal
        P_Tx = np.mean(np.abs(Tx) ** 2)

        # Calculate the noise power based on the current SNR
        P_N = P_Tx / (snr_linear * 2)  # Divide by 2 due to complex noise

        # Generate the AWGN vector N
        N = np.sqrt(P_N / 2) * (np.random.randn(num_rx_antennas, 1) + 1j * np.random.randn(num_rx_antennas, 1))

        # Generate the received vector R
        R = np.dot(H, Tx) + N

        # Perform Zero-Forcing (ZF) detection as previously explained
        H_inv = np.linalg.pinv(H)
        decoded_symbols = np.dot(H_inv, R)

        # Calculate the symbol errors
        symbol_errors = np.sum(np.round(decoded_symbols) != np.round(Tx))
        ser_sum += symbol_errors

    # Calculate the average SER for the current SNR
    average_ser = ser_sum / num_repetitions

    ser_results.append(average_ser)

# Plot the results in a log-scale y-axis
plt.figure()
plt.semilogy(snr_dB_values, ser_results, marker='o', linestyle='-', color='b')
plt.grid(True)
plt.title('Average Symbol-Error-Rate vs. SNR')
plt.xlabel('SNR (dB)')
plt.ylabel('Average SER (log scale)')
plt.show()
