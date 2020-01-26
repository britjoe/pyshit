def sum(a, b):
    if b == 0:
        return a
    if b != 0:
        a = a + 1
        b = b - 1
        return sum(a, b)


x = int(input())
y = int(input())
print(sum(x, y))
