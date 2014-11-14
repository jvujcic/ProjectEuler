from math import sqrt
import itertools

def sum_div(n):
    s, i, temp = 1, 2, n
    while i <= sqrt(n):
        a = 0
        while n % i == 0: a, n = a+1, n/i
        s *= (i**(a+1)-1)/(i-1)
        i+=1
    if(n!=1): s*=(n**2-1)/(n-1)
    return s - temp

limit = 28124
abundant = [x for x in xrange(1, limit) if sum_div(x) > x]
sum_of_abundant = set([x + y for x in abundant for y in abundant])
print sum(set(xrange(1,limit)) - sum_of_abundant)

