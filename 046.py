from sympy import sieve

limit = 10000

prosti = list(sieve.primerange(2, limit))
trazeni = set(p +2*(n**2) for p in prosti for n in xrange(1, limit))
odd_composite = set(2*n+1 for n in xrange(1, limit)).difference(prosti)
print min(odd_composite.difference(trazeni))
