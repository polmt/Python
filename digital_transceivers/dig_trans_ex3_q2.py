import numpy as np

def generate_awgn(N, SNR_dB):
    # Generate an AWGN vector with N samples and a specified SNR in dB
    signal_power = np.var(TR)  # Calculate the power of the TR signal
    noise_power = signal_power / (10 ** (SNR_dB / 10))  # Calculate the power of noise
    noise = np.random.normal(0, np.sqrt(noise_power), N)  # Generate noise samples
    return noise

N = int(input("Enter the number of samples (N): "))
SNR_dB = float(input("Enter the SNR in dB: "))

def generate_random_symbols(N):
    # Generate N random symbols (-1 or 1) with equal probability
    TR = np.random.choice([-1, 1], size=N)
    return TR

# Generate the TR array as in the previous question
TR = generate_random_symbols(N)

# Generate the AWGN vector
N = generate_awgn(N, SNR_dB)

print("Generated AWGN vector N:", N)
