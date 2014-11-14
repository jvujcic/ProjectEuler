L = lambda n: n/2 if n%2 == 0 else 3*n+1

n = 1000000
duljine = {1:1}

def rek(n):
    if n in duljine: return duljine[n]
    else:
        duljine[n] = 1 + rek(L(n))
        return duljine[n]

for i in range(1,n): rek(i)

print max(duljine.iterkeys(), key=lambda k: duljine[k] if k < n else -1)

