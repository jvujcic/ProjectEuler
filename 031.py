mem = {}
def rek(n, skup):
    temp = frozenset(skup)
    if n == 0: return 1
    if n < 0 or len(skup) == 0: return 0
    if (n, temp) in mem: return mem[n,temp]
    for p in skup:
        mem[n, temp] = rek(n, skup - set([p])) + rek(n - p, set(skup))
        return mem[n, temp]
        

print rek(200, set([1, 2, 5, 10, 20, 50, 100, 200]))
