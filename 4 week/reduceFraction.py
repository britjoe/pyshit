def minDivisor(n):
    sep = n ** 0.5
    i = 1
    while i <= sep:
        i += 1
        if n % i == 0:
            return i
    return n


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def reduceFraction(n, m):
    p = n // gcd(n, m)
    q = m // gcd(n, m)
    return p, q


x = int(input())
y = int(input())

print(*reduceFraction(x, y))
