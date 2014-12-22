from sympy.abc import x, y, t
from sympy.solvers.diophantine import diop_quadratic

limit = 1001

max_x = 0

for d in range(2, limit):
    s = list(diop_quadratic(x**2 - d * (y**2) - 1, 0))
    if s[0][0] > max_x:
        max_x, solution_d = s[0][0], d

print(solution_d)