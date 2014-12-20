solution = dict()

for n in range(10900):
    m = n**3
    sorted_digits = ''.join(sorted(str(m)))
    if sorted_digits not in solution:
        solution[sorted_digits] = (m, 1)
    else:
        key, val = solution[sorted_digits]
        solution[sorted_digits] = (key, val +1)


minimal_cube = min(cube for _, (cube, times) in solution.items() if times == 5)

print(minimal_cube)