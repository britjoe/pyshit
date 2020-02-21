inFile = open('input.txt')
lines = inFile.readlines()
nl = []
dicty = dict()
cntList = []
for i in lines:
    nl.append(i.split())
for i in nl:
    for j in i:
        if j not in dicty:
            dicty[j] = 0
            print(0, end=' ')
        else:
            dicty[j] += 1
            print(dicty[j], end=' ')

inFile.close()
