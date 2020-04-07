a = int(input())
i = 1
b1 = 0
while i <= a:
    b = 1 / (i ** 2)
    b1 = b1 + b
    i += 1
print('{0:.6f}'.format(b1))
