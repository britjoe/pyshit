def isPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

if isPointInCircle(a, b, c, d, e):
    print('YES')
else:
    print('NO')
