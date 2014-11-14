#!/usr/bin/env python3

from sympy import primerange
from itertools import combinations

limit = 1000000
sieve = list(primerange(2, limit))
set_sieve = set(sieve)

for p in sieve:
    p_str = str(p)
    for i in range(1, len(p_str)+1):
        for x in combinations(range(len(p_str)), i):
            ok, ukupno, z = False, 1, p_str[x[0]]
            for k in x:
                if p_str[k] != z: ok = True
            if ok: continue
            for j in range(10):
                p_str = str(p)
                for k in x: p_str = p_str[:k] + str(j) + p_str[k+1:]
                novi = int(p_str)
                if novi > p and novi in set_sieve: ukupno +=1
            if ukupno == 8: print(p)
