from math import sqrt

def sum_div(n):
    s = 1
    for i in xrange(2, int(sqrt(n)+1)):
        q, r = divmod(n, i)
        if r == 0:
            s += i
            if(q != i): s += q
    return s
 
print sum(x for x in xrange(2, 10000)
          if sum_div(x) != x and sum_div(sum_div(x)) == x)
