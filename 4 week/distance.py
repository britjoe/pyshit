from math import sqrt


def distance(x1, y1, x2, y2):
    hip = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return hip


a = float(input())
b = float(input())
c = float(input())
d = float(input())
print('{0:.5f}'.format(distance(a, b, c, d)))
