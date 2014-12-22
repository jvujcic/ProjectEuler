from sympy.ntheory import sieve
from collections import Counter
from itertools import combinations

solution = 0
min = float("inf")

is_perm = lambda x, y: Counter(str(x)) == Counter(str(y))

primes = sieve.primerange(10**3, 10**4)

for x, y in combinations(primes, 2):
        n = x * y
        if n < 10**7:
            fi = (x - 1) * (y - 1)
            q = n / fi
            if q < min and is_perm(n, fi):
                solution, min = n, q

print(solution)
