import sympy as sp

n, z = sp.symbols('n z')

x_n = 3**n * sp.Heaviside(n)

X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = 3^n u[n]:")
print(sp.simplify(X_z))

import sympy as sp

n, z, w = sp.symbols('n z w', real=True)

x_n = sp.cos(w*n) * sp.Heaviside(n)

X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = cos(w n) u[n]:")
print(sp.simplify(X_z))
