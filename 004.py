isPalindrom = lambda num: str(num) == str(num)[::-1]
m = 0
trozn = range(999, 99, -1)

for (x,y) in [(x,y) for x in trozn for y in trozn]:
        a = x*y
        if isPalindrom(a) and a > m: m = a

print m

    

