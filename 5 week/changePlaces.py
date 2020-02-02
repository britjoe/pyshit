numList = list(map(int, input().split()))
listLen = len(numList)
b = []

for i in range(0, listLen - 1, 2):
    b.append(numList[i + 1])
    b.append(numList[i])
if listLen % 2 != 0:
    b.append(numList[listLen - 1])
print(*b)
