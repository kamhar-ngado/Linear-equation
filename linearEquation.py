from sympy import symbols, Eq, solve

x, y, z = symbols('x,y,z')

eq1 = Eq((-6*x-4*y+3*z), 7)
eq2 = Eq((-2*x+5*y+z), 15)
eq3 = Eq((x-5*y+6*z), -19)
  
print(solve((eq1, eq2, eq3), (x, y, z)))