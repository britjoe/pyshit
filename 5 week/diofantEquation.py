a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
for x in range(0, e):
    if ((a * (x ** 3)) + (b * (x ** 2)) + (c * x) + d) / (x - e) == 0:
        count += 1
for x in range(e + 1, 1001):
    if ((a * (x ** 3)) + (b * (x ** 2)) + (c * x) + d) / (x - e) == 0:
        count += 1
print(count)
