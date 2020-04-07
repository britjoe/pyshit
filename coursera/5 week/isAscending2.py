def isAscending(numList):
    i = 0
    while numList[i + 1] > numList[i]:
        i += 1
        return 'YES'
    return 'NO'


numList = list(map(int, input().split()))
print(isAscending(numList))
