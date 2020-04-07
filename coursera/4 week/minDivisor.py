def minDivisor(n):
    sep = n ** 0.5
    i = 1
    while i <= sep:
        i += 1
        if n % i == 0:
            return i
    return n


n = int(input())
print(minDivisor(n))
