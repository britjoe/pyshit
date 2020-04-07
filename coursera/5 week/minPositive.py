def onlyPlusValue(a):
    b = []
    for i in range(len(a)):
        if a[i] > 0:
            b.append(a[i])
    return b


numList = list(map(int, input().split()))
opv = onlyPlusValue(numList)
c = 0
for i in range(1, len(opv)):
    if opv[i] < opv[c]:
        c = i
print(opv[c])
