limit = 1000000
s = '.'
for i in xrange(1, limit): s = s + str(i)
rez = 1
for i in xrange(7): rez *= int(s[10**i])
print rez
