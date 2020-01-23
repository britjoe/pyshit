from math import sqrt


def distance(x1, y1, x2, y2):
    hip = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return hip


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

print(distance(a, b, c, d) + distance(c, d, e, f) + distance(e, f, a, b))
