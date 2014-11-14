from math import sqrt

def numDiv(n):
    nD = 1
    for i in range(2, int(sqrt(n))+1):
        a = 0
        while True:
            if n % i == 0: a, n = a+1, n/i
            else: break
        nD = nD * (a + 1)
        
    if n != 1: return nD*2
    else: return nD
 
s, i = 0, 1
while True:
    s += i
    if numDiv(s) > 500: break
    i+=1

print s
