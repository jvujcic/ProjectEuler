from sympy.ntheory import totient

limit = 1000001
solution = 0

print(sum(totient(n) for n in range(2, limit)))