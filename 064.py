from math import sqrt, floor
from decimal import *

def periodic(n):
    n = Decimal(n)
    a = Decimal.sqrt(n)
    a, b = a // 1, a - a // 1
    if a**2 == n: return 0
    x = set()
    x.add(round(b, 5))
    period = 1
    while True:
        a = 1/b
        a, b = a // 1, a - a // 1
        if round(b,5) in x: break
        x.add(round(b,5))
        period += 1
    return period

getcontext().prec = 1000
solution = sum(periodic(n) % 2 for n in range(2, 10001))
print(solution)