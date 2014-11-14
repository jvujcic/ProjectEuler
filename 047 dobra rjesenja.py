from math import sqrt

lim = 1000000
l = 4
sieve = [0] * lim
ls = [l] * l

for i in range(2,int(sqrt(lim)) + 1):
    if sieve[i] == 0:
        sieve[i+i::i] = [x + 1 for x in sieve[i+i::i]]

for i in range(2,len(sieve) - l):
    if sieve[i:i+l] == ls:
        print i
        break

######################################

def problem47(n = 200000):

    a, l = [0] * n, 1000
    for i in xrange(l):
        if a[i]: continue
        s = i + 2; t = i + i + 2
        for j in xrange(t, n, s):
            a[j] += 1
            if a[j] == a[j-1] == a[j-2] == a[j-3] == 4:
                return j - 1
    
