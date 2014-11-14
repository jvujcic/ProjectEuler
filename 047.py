from sympy.ntheory import primefactors

limit = 1000000

for n in xrange(limit):
    ok = True
    for i in xrange(4):
        if len(primefactors(n+i)) != 4:
            ok = False
            break
    if ok:
        print n
        break
    
