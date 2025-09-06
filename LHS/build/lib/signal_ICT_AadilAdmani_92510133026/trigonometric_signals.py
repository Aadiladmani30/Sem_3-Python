# trigonometric_signals.py
import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    """Generates a sine wave."""
    y = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, y)
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

def cosine_wave(A, f, phi, t):
    """Generates a cosine wave."""
    y = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, y)
    plt.title("Cosine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

def exponential_signal(A, a, t):
    """Generates an exponential signal."""
    y = A * np.exp(a * t)
    plt.plot(t, y)
    plt.title("Exponential Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y
