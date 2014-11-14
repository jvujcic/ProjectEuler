ukupno = 0
for i in xrange(2, 600000):
    s = sum(int(z)**5 for z in str(i))
    if i == s: ukupno += i
print ukupno
        
