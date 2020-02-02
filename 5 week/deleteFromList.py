numList = list(map(int, input().split()))
k = int(input())

listLen = len(numList)
for i in range(listLen-1):
    if i >= k:
        numList[i] = numList[i+1]
numList.pop()
print(*numList)
