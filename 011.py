grid = [[0]*26 for _ in xrange(23)]
f = open('012.txt', 'r')

i = 0
for line in f:
    temp = line.split()
    grid[i][3:23] = [int(x) for x in temp]
    i+=1

maks = 0
for i, j in [(i,j) for i in xrange(20) for j in xrange(3,23)]:
    p1 = p2 = p3 = p4 = p5 = 1
    for k in xrange(4):
        p1 = p1 * grid[i][j-k]
        p2 = p2 * grid[i][j+k]
        p3 = p3 * grid[i+k][j]
        p4 = p4 * grid[i+k][j+k]
        p5 = p5 * grid[i+k][j-k]
    if p1 > maks: maks = p1
    if p2 > maks: maks = p2
    if p3 > maks: maks = p3
    if p4 > maks: maks = p4
    if p5 > maks: maks = p5

print maks
        


