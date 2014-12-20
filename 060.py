#!/usr/bin/env python3

from sympy import isprime, primerange
from itertools import permutations

def is_good_prime_pair(a, b):
    return  isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a)))

primes_1 = set(primerange(1, 10000))

primes_2 = set((a, b) for a, b in permutations(primes_1, 2) 
                       if is_good_prime_pair(a, b))

prime_dict_1 = dict()
prime_dict_2 = dict()
prime_dict_3 = dict()
prime_dict_4 = dict()

for a, b in primes_2:
    if a not in prime_dict_1:
        prime_dict_1[a] = set()
    prime_dict_1[a].add(b)

for a, prime_set in prime_dict_1.items():
    for b in prime_set:
        prime_dict_2[a, b] = prime_set.intersection(prime_dict_1[b])

for (a, b), prime_set in prime_dict_2.items():
    for c in prime_set:
        prime_dict_3[a, b, c] = prime_set.intersection(prime_dict_1[c])

for (a, b, c), prime_set in prime_dict_3.items():
    for d in prime_set:
        prime_dict_4[a, b, c, d] = prime_set.intersection(prime_dict_1[d])


solution = list()

for (a, b, c, d), prime_set in prime_dict_4.items():
    for p in prime_set:
        solution.append(a + b + c + d + p)

print(min(solution))
