num = 600851475143
x = 2

while x <= num:
    if num % x == 0:
        num, mx = num / x, x
    else:
        x+=1
        
print mx
