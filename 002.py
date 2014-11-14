a, b, s = 1, 2, 0
while(a < 4000000):
    if(a%2 == 0): s += a
    a, b = b, a+b
print s
