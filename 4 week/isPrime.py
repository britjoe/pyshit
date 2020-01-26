def isPrime(n):
    sep = n ** 0.5
    i = 1
    if n == 2:
        return 'YES'
    else:
        while i <= sep:
            i += 1
            if n % i == 0:
                return 'NO'
    return 'YES'


n = int(input())
print(isPrime(n))
