def power(a, n):
    if n == 0:
        return 1
    if n != 0:
        res = a * power(a, n-1)
    return res


x = float(input())
y = int(input())
print(power(x, y))
