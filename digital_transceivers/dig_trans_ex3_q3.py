import numpy as np

# Function to generate TR
def generate_random_symbols(N):
    TR = np.random.choice([-1, 1], size=N)
    return TR

# Function to generate AWGN with a specified SNR
def generate_awgn(N, SNR_dB):
    signal_power = np.var(TR)
    noise_power = signal_power / (10 ** (SNR_dB / 10))
    noise = np.random.normal(0, np.sqrt(noise_power), N)
    return noise

# Function to decode RC using the given rule
def decode_RC(RC, threshold):
    decoded_symbols = np.where(RC >= threshold, 1, -1)
    return decoded_symbols

N = 100
SNR_dB = 5
num_simulations = 1000
threshold = 0.5  # For the last part of the question

errors = 0

for _ in range(num_simulations):
    TR = generate_random_symbols(N)
    AWGN = generate_awgn(N, SNR_dB)
    RC = TR + AWGN
    decoded_symbols = decode_RC(RC, threshold)
    errors += np.sum(decoded_symbols != TR)

SER = errors / (N * num_simulations)

print("Symbol Error Rate (SER) for SNR =", SNR_dB, "and N =", N, "is:", SER)

# Repeat the steps for N=1000
N = 1000
errors = 0

for _ in range(num_simulations):
    TR = generate_random_symbols(N)
    AWGN = generate_awgn(N, SNR_dB)
    RC = TR + AWGN
    decoded_symbols = decode_RC(RC, threshold)
    errors += np.sum(decoded_symbols != TR)

SER = errors / (N * num_simulations)

print("Symbol Error Rate (SER) for SNR =", SNR_dB, "and N =", N, "is:", SER)
