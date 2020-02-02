numList = list(map(int, input().split()))
listLen = len(numList)
i = 0
while i < listLen - 1:
    if numList[i] * numList[i + 1] > 0:
        a = numList[i]
        b = numList[i + 1]
        print(a, b)
        break
    i += 1
