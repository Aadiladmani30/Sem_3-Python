# unitary_signals.py
import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    step = np.where(n >= 0, 1, 0)
    plt.stem(n, step)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return step

def unit_impulse(n):
    impulse = np.where(n == 0, 1, 0)
    plt.stem(n, impulse)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return impulse

def ramp_signal(n):
    ramp = np.where(n >= 0, n, 0)
    plt.stem(n, ramp)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return ramp
