#!/usr/bin/env python3

from sympy import isprime

n = 1
total_primes = 0

while True:
    donji_lijevi = (2*n + 1)**2 - 2*n
    gornji_lijevi = donji_lijevi - 2*n
    gornji_desni = gornji_lijevi - 2*n
    if isprime(donji_lijevi):
        total_primes += 1
    if isprime(gornji_lijevi):
        total_primes += 1
    if isprime(gornji_desni):
        total_primes += 1
    if total_primes / (4*n + 1) < 0.1:
        print(2*n + 1)
        break
    n += 1
