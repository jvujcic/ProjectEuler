from sympy.ntheory import isprime
from sympy import sieve

limit = 1000
maxi, max_a, max_b = 0, 0, 0

for a, b in ((a,b) for a in xrange(-limit + 1, limit, 2) for b in sieve.primerange(2, limit)):
        n = 0
        while isprime(n**2 + a*n + b): n+=1
        if maxi < n: maxi, max_a, max_b = n, a, b
        
print max_a*max_b
