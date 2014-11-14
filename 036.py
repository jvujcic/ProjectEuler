def is_palindrom(n):
    if str(n) != str(n)[::-1]: return False
    b = bin(n)[2:]
    if b != b[::-1]: return False
    return True

limit = 1000000

print sum(x for x in xrange(1, limit) if is_palindrom(x))
