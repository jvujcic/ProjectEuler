from math import sqrt

def isPrime(n):
    for i in xrange(2, int(sqrt(n))+1):
        if(n % i == 0): return False
    return True

br = 0
x = 1
while br < 10001:
    x+=1
    if isPrime(x): br+=1

print x
