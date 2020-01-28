n = int(input())
b = 10 ** n - 1
a = 10 ** (n - 1) - 1

for i in range(b, a, -2):
    print(i, end=' ')
