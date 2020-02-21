fin = open('input.txt')
lines = fin.readlines()
nl = []

for i in lines:
    nl.append(i.split())

dicty = dict()

for i in lines:
    nl.append(i.split())

for i in nl:
    for j in i:
        if j not in dicty:
            dicty[j] = 0
        else:
            dicty[j] += 1

newDicty = dict()
for i in dicty:
    if dicty[i] not in newDicty:
        newDicty[dicty[i]] = []
    newDicty[dicty[i]].append(i)

maxV = max(newDicty)
a = sorted(newDicty[maxV])
print(a[0])

fin.close()
# newDicty = {max(dicty.values()): 0}
