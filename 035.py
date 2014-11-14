from sympy.ntheory import isprime
from sympy import sieve

limit = 1000000

def is_circ(n):
    s, i = str(n), 0
    if '0' in s or '2' in s or '4' in s or '6' in s or '8' in s: return False
    while i < len(s):
        if not isprime(int(s)):
                return False
        s = s[1:len(s)]+s[0]
        i+=1
    return True


print len(set(x for x in sieve.primerange(3, limit) if is_circ(x))) + 1
