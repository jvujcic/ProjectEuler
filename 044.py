limit = 10000
pentag = set(n*(3*n-1)/2 for n in xrange(1, limit))

print min(x-y for x in pentag for y in pentag if x+y in pentag if x-y in pentag)
