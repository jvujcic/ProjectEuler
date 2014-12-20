from math import log10, floor, pow

digits = lambda n: ((n==0) and 1) or floor(log10(abs(n)))+1

solution = 0
limit = 100

for n in range(1, 10):
    for k in range(1, limit):
        d = digits(n**k)
        if d < k: break
        if d == k: solution += 1

print(solution)