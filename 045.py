from math import sqrt

limit = 10000000

t = [n*(n+1)/2 for n in xrange(1, limit)]
p = set(n*(3*n-1)/2 for n in xrange(1, limit))
h = set(n*(2*n-1) for n in xrange(1, limit))

isti = [x for x in t if x in p and x in h]

print (-1 + sqrt(1+8*isti[2]))/2
