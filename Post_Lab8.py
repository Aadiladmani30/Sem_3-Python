import math

degree = float(input("Enter angle in degrees: "))

radian = degree * (math.pi / 180)

print("Angle in radians:", radian)

import math

x = float(input("Enter value of x: "))

y = 6 * (x ** 2) + 4 * math.sin(x)

print("y =", y)

import math

def evaluate_functions(x):
    f = math.cos(2 * x)
    f1 = -2 * math.sin(2 * x)
    f2 = -4 * math.cos(2 * x)
    return f, f1, f2

# Evaluate at x = π
x = math.pi
result = evaluate_functions(x)

print("f(x)  =", result[0])
print("f'(x) =", result[1])
print("f''(x) =", result[2])
