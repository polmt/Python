import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

def generate_signal(duration, f_s, f):
    t = np.linspace(0, duration, int(f_s * duration), endpoint=False)
    S = np.sin(2 * np.pi * f * t)
    return t, S

def SSB_mod(S, f_s, f, SBup=True):
    # Perform FFT
    spectrum = fft(S)

    # Shift the spectrum
    if SBup:
        spectrum[int(f * S.size / f_s):] = 0
    else:
        spectrum[:int(f * S.size / f_s)] = 0

    # Perform IFFT
    S_mod = ifft(spectrum)

    return np.real(S_mod), spectrum

def S_spectrum_plt(t, S, S_mod, spectrum, title):
    plt.figure(figsize=(16, 8))

    # Plot Original Signal
    plt.subplot(3, 1, 1)
    plt.plot(t, S, label='Original Signal')
    plt.title(title + ' - Original Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    # Plot Modulated Signal
    plt.subplot(3, 1, 2)
    plt.plot(t, S_mod, label='Modulated Signal')
    plt.title(title + ' - SSB Modulated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    # Plot Spectrum
    plt.subplot(3, 1, 3)
    freq = np.fft.fftfreq(len(spectrum), d=1 / f_s)
    plt.plot(freq, np.abs(spectrum), label='Spectrum')
    plt.title(title + ' - Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Parameters
duration = 1  # seconds
f_s = 1000  # Hz
f = 10  # Hz

# Generate a simple sine wave signal
t, s = generate_signal(duration, f_s, f)

# Perform SSB modulation (upper sideband)
S_mod_up, spectrum_up = SSB_mod(s, f_s, f, SBup=True)

# Perform SSB modulation (lower sideband)
S_mod_low, spectrum_lower = SSB_mod(s, f_s, f, SBup=False)

# Plot the results and spectrum
S_spectrum_plt(t, s, S_mod_up, spectrum_up, 'Upper Sideband')
S_spectrum_plt(t, s, S_mod_low, spectrum_lower, 'Lower Sideband')
