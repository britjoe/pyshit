numList = list(map(int, input().split()))
ln = len(numList)
a = numList[0]
inId = 0
for i in range(1, ln):
    if numList[i] >= a:
        a = numList[i]
        inId = i

print(a, inId)
