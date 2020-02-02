numList = list(map(int, input().split()))
ln = len(numList)
for i in range(ln):
    if numList[i] % 2 == 0:
        print(numList[i], end=' ')
