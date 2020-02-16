inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
nl = []
mySet = set([])

for i in lines:
    nl.append(i.split())
for i in nl:
    for j in i:
        mySet.add(j)

print(len(mySet))

inFile.close()
outFile.close()
