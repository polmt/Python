import numpy as np
import matplotlib.pyplot as plt

constellation = {(0, 0): complex(-1, -1),
                 (0, 1): complex(-1, 1),
                 (1, 0): complex(1, -1),
                 (1, 1): complex(1, 1)}

n = 1000
SNR_dB = 14

bits = np.random.randint(0, 2, n)

def encode_4qam(bits):
    symbols = [constellation[tuple(bits[i:i + 2])] for i in range(0, len(bits), 2)]
    return symbols

symbols = encode_4qam(bits)

noise_std = 10 ** (-SNR_dB / 20)
noisy_symbols = symbols + noise_std * (np.random.randn(n // 2) + 1j * np.random.randn(n // 2))

def decode_4qam(symbols):
    bits = []
    for symbol in symbols:
        dist_min = float('inf')
        nearest_bitpair = None
        for bitpair, constellation_point in constellation.items():
            dist = abs(symbol - constellation_point)
            if dist < dist_min:
                dist_min = dist
                nearest_bitpair = bitpair
        bits.extend(nearest_bitpair)
    return bits


decoded_bits = decode_4qam(noisy_symbols)

bit_error_rate = np.sum(np.abs(decoded_bits - bits)) / n

print(f"Bit Error Rate: {bit_error_rate:.4f}")

received_symbols = np.array(noisy_symbols)
plt.scatter(received_symbols.real, received_symbols.imag, marker='x', color='r', label='Received Symbols')
plt.scatter(np.array(list(constellation.values())).real, np.array(list(constellation.values())).imag, marker='o',
            color='b', label='Constellation Points')
plt.legend()
plt.title('4QAM Constellation Diagram')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid(True)
plt.show()
