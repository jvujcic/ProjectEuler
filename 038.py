from itertools import permutations

max = 0
trazeni = set('123456789')

for k in xrange(1, 5):
    for it in permutations('123456789', k):
        s = ''.join(it)
        n, i = int(s), 2
        while len(s) < 9: s, i = s + str(n * i), i + 1
        if len(s) == 9 and set(s) == trazeni and int(s) > max: max = int(s)

print max
        
