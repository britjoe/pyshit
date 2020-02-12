inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()
nl = []
for i in lines:
    nl.append(i.split())
nl.sort()
for i in nl:
    i.pop(2)

for i in nl:
    print(*i, file=outFile)

inFile.close()
outFile.close()
