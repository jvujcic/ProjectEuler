from math import ceil

n = 2000000

bitArray = [True] * n

for i in xrange(2, n):
    if bitArray[i]:
        for j in xrange(2, int(ceil(float(n)/i))):
            bitArray[i*j] = False

print sum([i for i in xrange(2,n) if bitArray[i]])

