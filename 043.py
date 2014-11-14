from itertools import permutations

prosti = [2, 3, 5, 7, 11, 13, 17]

def dobar(s):
    if s[0] == '0': return False
    for i in xrange(1,8):
        if int(s[i:i+3]) % prosti[i-1] != 0: return False
    return True

print sum(int(''.join(p)) for p in permutations('0123456789') if dobar(''.join(p)))
        

