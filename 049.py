from sympy import primerange
from itertools import permutations

p = list(primerange(1000, 10000))

for i in xrange(len(p)-1):
    for j in xrange(i+1, len(p)):
        x = 2*p[j] - p[i]
        if x in p:
            perm = list(permutations(str(p[j])))
            if tuple(str(p[i])) in perm and tuple(str(x)) in perm:
                print p[i], p[j], x
    
