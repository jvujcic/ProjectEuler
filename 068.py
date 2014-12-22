from itertools import permutations

nums = [i for i in range(1, 11)]
max_solution = 0


for perm in permutations(nums, 6):
    ring = [[0]*3 for i in range(5)]

    for i in range(len(perm) - 1):
        if i == 4:
            k = 0
        else:
            k = i + 1
        ring[i][1] = perm[i]
        ring[i][2] = perm[k]

    used = set(perm)
    ring[0][0] = perm[5]
    suma = sum(ring[0])
    ok = True

    for i in range(1, 5):
        temp = suma - sum(ring[i])
        if temp > 10 or temp < 1 or temp in used:
            ok = False
            break
        else:
            ring[i][0] = temp
            used.add(temp)
    if ok:
        min, min_index = 11, 0
        for i in range(5):
            if ring[i][0] < min:
                min, min_index = ring[i][0], i
                   
        solution = []
        for i in range(5):
            solution += ring[min_index]
            if min_index == 4:
                min_index = 0
            else:
                min_index += 1

        solution = [str(x) for x in solution]
        solution = ''.join(solution)
        if len(solution) == 16:
            solution = int(solution)
            if solution > max_solution:
                max_solution = solution

print(max_solution)
            