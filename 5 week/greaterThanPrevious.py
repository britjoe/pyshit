numList = list(map(int, input().split()))
ln = len(numList)
a = numList[0]
for i in range(1, ln):
    if numList[i] > a:
        print(numList[i], end=' ')
    a = numList[i]
