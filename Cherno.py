from sympy import *
init_printing()

x = Symbol('x')

z = -18 * x**3 + 5 * x**2 + 10 * x - 30
z1 = solve(z, x)

m = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
m1 = solve(m, x)
l = (x ** 2 + 3) / (3 * (x + 1))
l1 = solve(l, x)
