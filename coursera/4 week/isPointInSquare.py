def isPointInSquare(x1, y1):
    return -1 <= x1 <= 1 and -1 <= y1 <= 1


a = float(input())
b = float(input())
if isPointInSquare(a, b):
    print('YES')
else:
    print('NO')
