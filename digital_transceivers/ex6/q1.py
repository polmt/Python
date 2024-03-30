import numpy as np

qam_symbols = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])

Tx = np.random.choice(qam_symbols, size=(4, 1))

print("Tx:")
print(Tx)
