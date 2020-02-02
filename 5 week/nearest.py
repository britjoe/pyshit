y = int(input())
a = list(map(int, input().split()))
x = int(input())
b = []

for i in range(len(a)):
    b.append(abs(a[i] - x))
    map(abs, b)

c = b[0]
inId = 0

for i in range(1, len(b)):
    if c > b[i]:
        c = b[i]
inId = list.index(b, c)

print(a[inId])
