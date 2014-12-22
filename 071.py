from fractions import Fraction

limit = 1000000
x = solution = Fraction(0, 1)
y = Fraction(3, 7)

while True:
    x = (x + y)/2
    x = Fraction(x).limit_denominator(limit)
    if x == y:
        break
    solution = x
    
print(solution)