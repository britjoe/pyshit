n = int(input())
a = 0
z = 0
for i in range(1, n):
    z = int(input())
    a = a + z
# print(a)
c = 0
for i in range(0, n + 1):
    c += i
print(c - a)
