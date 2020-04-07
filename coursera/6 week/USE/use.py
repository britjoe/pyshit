inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')


def popPlusSum(a):
    i = 0

    while i < len(a):
        j = -3
        while j < 0:
            if int(a[i][j]) < 40:
                a.pop(i)
                break
            else:
                j += 1
        i += 1

    for e in a:
        y = e[-3:]
        e.append(sum(map(int, y)))

    for p in a:
        n = -4
        while n < -1:
            p.pop(n)
            n += 1
    return a


def points(a):
    return int(a[-1])


k = inFile.readline()
k = int(k)
lines = inFile.readlines()
nl = []
for i in lines:
    nl.append(i.split())

a = popPlusSum(nl)
a.sort(key=points, reverse=True)

cntStud = len(a)

entrPoint = a[k - 1][-1]

cnt = 0
for i in a:
    if i[-1] >= entrPoint:
        cnt += 1

cntmax = 0
maxPoint = a[0][-1]
for i in a:
    if i[-1] == maxPoint:
        cntmax += 1

if cntStud == k:
    print(0, file=outFile)
elif cntmax > k:
    print(1, file=outFile)
else:
    if cnt > k:
        itog = []
        for i in a:
            if i[-1] > entrPoint:
                itog.append(i)
        newEntrPoint = itog[-1][-1]
        print(newEntrPoint, file=outFile)
    else:
        print(entrPoint, file=outFile)

inFile.close()
outFile.close()
