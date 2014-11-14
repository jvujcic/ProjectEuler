triangle = set((n*(n+1))/2 for n in xrange(1, 50))
f = open('words.txt', 'r')

for line in f: rijeci = [ime.strip('"') for ime in line.split(',')]

print len(filter(lambda w: (sum(ord(c)-ord('A')+1 for c in w) in triangle), rijeci))
    
    
