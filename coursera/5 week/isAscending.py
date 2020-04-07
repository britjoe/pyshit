def isAscending(numList):
    i = 0
    y = 0
    while i <= len(numList) - 2:
        if numList[i + 1] > numList[i]:
            y += 1
        i += 1
    if y == len(numList) - 1:
        return 'YES'
    else:
        return 'NO'


numList = list(map(int, input().split()))
print(isAscending(numList))
