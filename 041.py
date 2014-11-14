from sympy import isprime
from itertools import permutations

print max(int(''.join(p)) for p in permutations('1234567') if isprime(int(''.join(p))))
