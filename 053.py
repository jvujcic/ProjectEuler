#!/usr/bin/env python3

from sympy import binomial

print(len([1 for n in range(1, 101) for k in range(1, n) if binomial(n, k) > 1000000]))
