f = open('067.txt', 'r')

max_sum = [list() for i in range(100)]

for i, line in enumerate(f):
    for j, x in enumerate(line.split()):
        x = int(x)
        if i == 0:
            max_sum[0].append(x)
        elif j == 0:
            max_sum[i].append(x + max_sum[i-1][0])
        elif j == i:
            max_sum[i].append(x + max_sum[i-1][i-1])
        else:
            max_sum[i].append(x + max(max_sum[i-1][j], max_sum[i-1][j-1]))

print(max(max_sum[len(max_sum) - 1]))