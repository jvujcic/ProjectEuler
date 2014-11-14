from sympy import primerange

limit = 1000000
sieve = list(primerange(2, limit))
set_sieve = set(sieve)
maks = maks_dif = 0

for i in xrange(len(sieve)):
    suma = 0
    for j in xrange(len(sieve)-i):
        suma += sieve[i+j]
        if suma > limit: break
        if suma in set_sieve and maks_dif < j - i:
            maks, maks_dif = suma, j - i

print maks, maks_dif
    
