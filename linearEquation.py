from sympy import symbols, Eq, solve
import numpy as np

x,y = symbols("x,y")
eq1= Eq((2*x+3*y), 16)
print(eq1)
eq2= Eq((x-2*y), 1)
print(eq2)
solving = solve((eq1,eq2),(x,y))
print(solving)

A = np.array([[2, 3], [1, -2]])
B = np.array([16, 1])
X = np.linalg.solve(A,B)
print(X)