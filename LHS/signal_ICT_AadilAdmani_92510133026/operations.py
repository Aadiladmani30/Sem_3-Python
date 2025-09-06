# operations.py
import numpy as np

def time_shift(signal, k):
    """Shifts the signal by k units (circular shift)."""
    shifted = np.roll(signal, k)
    return shifted

def time_scale(signal, k):
    """Scales the time axis by factor k (simple resampling)."""
    indices = np.arange(0, len(signal), k, dtype=int)
    scaled = signal[indices]
    return scaled

def signal_addition(signal1, signal2):
    """Performs addition of two signals (same length)."""
    return np.add(signal1, signal2)

def signal_multiplication(signal1, signal2):
    """Performs point-wise multiplication of two signals (same length)."""
    return np.multiply(signal1, signal2)
