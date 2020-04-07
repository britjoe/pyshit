numList = list(map(int, input().split()))
listLen = len(numList)
cnt = 0
for i in range(1, listLen - 1):
    if numList[i - 1] < numList[i] > numList[i + 1]:
        cnt += 1
print(cnt)
