import math

num_digits = lambda n: math.floor(math.log10(n))+1

a, b, i = 1, 1, 1
while num_digits(a) < 1000:
    a, b, i = b, a+b, i+1
print i
    
