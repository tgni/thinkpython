def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)

print '50 15:' + str(gcd(50, 15))
print '1989 1590:' + str(gcd(1989, 1590))
