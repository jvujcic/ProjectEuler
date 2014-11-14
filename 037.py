from sympy.ntheory import isprime
from sympy import sieve

def is_truncprime(n):
    s = str(n)
    for i in xrange(1, len(s)):
        if not isprime(int(s[0:len(s)-i])): return False
        if not isprime(int(s[i:len(s)])): return False
    return True

limit = 1000000

print sum(n for n in sieve.primerange(10, limit) if is_truncprime(n))
