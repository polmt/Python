import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift


def DSBsc_demod(S_mod, f_car, f_s):
    t = np.arange(0, len(S_mod) / f_s, 1 / f_s)
    car = np.cos(2 * np.pi * f_car * t)

    S_demod = S_mod * car

    f_cut = 2 * np.pi * 500
    S_demod = np.convolve(S_demod, sinc_filter(f_cut, t), mode='same')

    return S_demod


def sinc_filter(f_cut, t):
    return np.sinc(2 * f_cut * t)


def plot_signals(t, S_x, S_mod, S_demod, f_s):
    plt.figure(figsize=(12, 8))

    plt.subplot(4, 1, 1)
    plt.plot(t, S_x)
    plt.title('Original Message Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 2)
    plt.plot(t, S_mod)
    plt.title('DSB-SC Modulated Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 3)
    plt.plot(t, S_demod)
    plt.title('Demodulated Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    spec_mod = fftshift(fft(S_mod))
    spec_demod = fftshift(fft(S_demod))
    f_mod = np.fft.fftshift(np.fft.fftfreq(len(S_mod), 1 / f_s))
    f_demod = np.fft.fftshift(np.fft.fftfreq(len(S_demod), 1 / f_s))

    plt.subplot(4, 1, 4)
    plt.plot(f_mod, np.abs(spec_mod), label='Modulated Signal')
    plt.plot(f_demod, np.abs(spec_demod), label='Demodulated Signal')
    plt.title('Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    f_x = 10
    f_car = 100
    f_s = 500
    time = np.arange(0, 1, 1 / f_s)
    S_x = 0.5 * np.sin(2 * np.pi * f_x * time)
    S_mod = 0.5 * S_x * np.cos(2 * np.pi * f_car * time)

    S_demod = DSBsc_demod(S_mod, f_car, f_s)

    plot_signals(time, S_x, S_mod, S_demod, f_s)
