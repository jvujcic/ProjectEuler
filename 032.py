from itertools import permutations

skup = set()

for it in permutations('123456789', 9):
    for i in xrange(1, 4):
        for j in xrange(3,5):
            a, b, c = int(''.join(it[0:i])), int(''.join(it[i:i+j])), int(''.join(it[i+j:]))
            if a*b == c: skup.add(a*b)

print sum(skup)
