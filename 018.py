f = open('018.txt', 'r')
n = 15
trokut = []

def rek(poz):
    if poz in maks:
        return maks[poz]
    else:
        return trokut[poz][0] + max(rek(poz+trokut[poz][1]),
                                    rek(poz+trokut[poz][1]+1))

i = 1
for line in f:
    trokut += [(int(x),i) for x in line.split()]
    i+=1

maks = { poz : trokut[poz][0] for poz in range(len(trokut)-15, len(trokut)) }
print rek(0)
