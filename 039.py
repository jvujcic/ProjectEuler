from math import sqrt

limit = 1000

perimeter = dict()

for a in xrange(1, limit):
    for b in xrange(a, limit):
        c = int(sqrt(a**2 + b**2))
        if a**2 + b**2 == c**2:
            p = a + b + c
            if p <= limit:
                if p in perimeter: perimeter[p]+=1
                else: perimeter[p] = 1

print max(perimeter.iterkeys(), key=lambda k: perimeter[k])
