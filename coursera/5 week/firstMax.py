listNum = list(map(int, input().split()))
listLen = len(listNum)
a = listNum[0]
for i in range(1, listLen):
    if a < listNum[i]:
        a = listNum[i]
inId = list.index(listNum, a)
print(a, inId)
