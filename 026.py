max = 0
for d in range(2, 1000):
    r, n, i = 1, 10, 1
    dec = {}
    while True:
        r, i = n % d, i+1
        n = 10 * r
        if n in dec:
            if max < i - dec[n]: max, x = i - dec[n], d
            break
        else: dec[n] = i
print x
            
        
