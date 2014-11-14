f = open('names.txt', 'r')
imena = []
for line in f:
     imena = [ime.strip('"') for ime in line.split(',')]

imena.sort()

score = lambda ime: sum(ord(i)-ord('A')+1 for i in ime)
print sum((i+1)*score(ime) for i,ime in enumerate(imena))

