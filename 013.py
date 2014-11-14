f = open('013.txt', 'r')
print str(sum(int(x) for x in f))[:10]
