from sympy import symbols, Eq, solve

x, y= symbols("x, y")
eq1 = Eq((x+y), 1)
print(eq1)
eq2 = Eq((x-y), 1)
print(eq2)
solving = solve((eq1, eq2), (x,y))
print(solving)