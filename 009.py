for i,j in [(a,b) for a in xrange(1,1000) for b in xrange(1,1000-a+1)]:
    if(i**2 + j**2 == (1000 - i - j)**2): break

print i*j*(1000-i-j)
