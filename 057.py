#!/usr/bin/env python3

from fractions import Fraction
import math

x = Fraction(1, 2)
num_digits = lambda n: math.floor(math.log10(n)) + 1
solution = 0

for i in range(1001):
    x = Fraction(1, 2 + x)
    y = 1 + x
    if num_digits(y.numerator) > num_digits(y.denominator):
        solution += 1

print(solution)
