import numpy as np

# Parameters
N = 10000  # Number of transmissions to simulate
Ch_var = 1.0  # Variance of the complex Gaussian channel
n_var = 0.1  # Variance of the noise

# Simulation
u1_Tx = np.random.choice([-1, 1], N)
u2_Tx = np.random.choice([-1, 1], N)
Ch = np.sqrt(Ch_var) * (np.random.randn(N) + 1j * np.random.randn(N))
n = np.sqrt(n_var) * (np.random.randn(N) + 1j * np.random.randn(N))

Rx_sigs = []  # Received signals

for i in range(N):
    u_Tx = np.random.choice([1, 2])  # Randomly select a user to transmit
    if u_Tx == 1:
        Rx_sig = u1_Tx[i] * Ch[i] + n[i]
    else:
        Rx_sig = u2_Tx[i] * Ch[i] + n[i]

    Rx_sigs.append(Rx_sig)

# ML Detection
u_det = []  # detected_users
sym_det = []  # detected_symbols

for i in range(N):
    u1_like = np.abs(np.sum(np.conj(u1_Tx[i]) * Rx_sigs[i]))
    u2_like = np.abs(np.sum(np.conj(u2_Tx[i]) * Rx_sigs[i]))

    if u1_like > u2_like:
        u_det.append(1)
        sym_det.append(u1_Tx[i])
    else:
        u_det.append(2)
        sym_det.append(u2_Tx[i])

# Calculate bit error rate
bits_err = np.sum(np.abs(u1_Tx - sym_det))
BER = bits_err / (N * 1.0)

print("Bit Error Rate =", BER)
