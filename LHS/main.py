import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_AadilAdmani_92510133026 import unitary_signals as us
from signal_ICT_AadilAdmani_92510133026 import trigonometric_signals as ts
from signal_ICT_AadilAdmani_92510133026 import operations as op

# Generate discrete index n
n = np.arange(-10, 10, 1)

# --- Test unitary signals ---
step = us.unit_step(n)
impulse = us.unit_impulse(n)
ramp = us.ramp_signal(n)

# --- Test trigonometric signals ---
t = np.linspace(0, 1, 500)
sine = ts.sine_wave(2, 5, 0, t)
cosine = ts.cosine_wave(2, 5, 0, t)
expo = ts.exponential_signal(1, 2, t)

# --- Test operations ---
# Time shift
shifted_sine = op.time_shift(sine, 5)
plt.plot(t, sine, label='Original Sine')
plt.plot(t, shifted_sine, label='Shifted Sine (+5)')
plt.title("Time Shifting")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# Time scale (demo)
scaled_sine = op.time_scale(sine, 2)
plt.plot(t[::2], scaled_sine)
plt.title("Time Scaling (factor=2)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Addition (example: step + ramp)
added = op.signal_addition(step, ramp)
plt.stem(n, added)
plt.title("Signal Addition (step + ramp)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Multiplication (example: sine * cosine)
product = op.signal_multiplication(sine, cosine)
plt.plot(t, product)
plt.title("Signal Multiplication (sine × cosine)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
