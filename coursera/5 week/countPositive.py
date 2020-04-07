numList = list(map(int, input().split()))
ln = len(numList)
a = 0
for i in range(ln):
    if numList[i] > 0:
        a += 1
print(a)
