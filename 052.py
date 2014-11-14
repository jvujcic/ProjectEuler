#!/usr/bin/env python3

limit = 1000000

for n in range(1, limit):
    if all(sorted(str(n)) == sorted(str(n*i)) for i in range(1,7)):
           print(n)
           break
