from sympy import symbols, Eq, solve

x, y, z= symbols("x, y, z")
eq1 = Eq((x+y+z), 1)
print(eq1)
eq2 = Eq((3*x+2*y+z), 2)
print(eq2)
eq3 = Eq((4*x-2*y-3*z), 3)
print(eq3)
solving = solve((eq1, eq2, eq3), (x,y,z))
print(solving)

