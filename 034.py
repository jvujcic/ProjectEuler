from math import factorial
from collections import deque
fac = [factorial(n) for n in xrange(0,10)]
limit = 3000000

def digitize(n):
    dq = deque()
    while n > 0:
        q, r = divmod(n ,10)
        dq.appendleft(r)
        n = q
    return dq

print sum(n for n in xrange(3, limit) if n == sum(fac[z] for z in digitize(n)))
