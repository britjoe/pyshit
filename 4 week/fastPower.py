def isEven(n):
    return n != 0 and n % 2 == 0


def fastPower(a, n):
    if isEven(n):
        res2 = (a ** 2) ** (n // 2)
        return res2
    else:
        if n == 0:
            return 1
        if n != 0:
            res = a * fastPower(a, n - 1)
            return res


x = float(input())
y = int(input())
print(fastPower(x, y))
