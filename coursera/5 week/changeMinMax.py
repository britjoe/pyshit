numList = list(map(int, input().split()))
ln = len(numList)
minVal = numList[0]
inMin = 0

for i in range(1, len(numList)):
    if minVal > numList[i]:
        minVal = numList[i]
inMin = list.index(numList, minVal)

maxVal = numList[0]
inMax = 0

for i in range(1, len(numList)):
    if maxVal < numList[i]:
        maxVal = numList[i]
inMax = list.index(numList, maxVal)

numList[inMin] = maxVal
numList[inMax] = minVal

print(*numList)
