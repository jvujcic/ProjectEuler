from sympy.ntheory import totient
from sympy.ntheory import sieve

limit = 1000001

#solution, max = 0, 0
#
# for n in range(1, limit):
#     x = n / totient(n)
#     if x > max:
#         solution, max = n, x

prime = sieve.primerange(1, 100)
solution = 1

for p in prime:
    temp = solution * p
    if temp < limit:
        solution = temp
    else:
        break

print(solution)
