numList = list(map(int, input().split()))
k, C = list(map(int, input().split()))
listLen = len(numList)
a = [0, ]
numList += a

for i in range(listLen, k, -1):
    numList[i] = numList[i - 1]
numList[k] = C

print(*numList)
