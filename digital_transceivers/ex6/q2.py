import numpy as np

num_tx_antennas = 2 
num_rx_antennas = 3

H = (np.random.randn(num_rx_antennas, num_tx_antennas) + 1j * np.random.randn(num_rx_antennas, num_tx_antennas)) / np.sqrt(2)

print("H:")
print(H)
