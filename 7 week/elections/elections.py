inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.read().splitlines()

candidates = dict()
for i in range(len(lines)):
    if lines[i] not in candidates:
        candidates[lines[i]] = 0
    candidates[lines[i]] += 1

canList = list(candidates.items())
canList = sorted(canList, key=lambda x: x[1], reverse=True)

if int(canList[0][1]) * 2 > len(lines):
    print(canList[0][0],
          file=outFile)
else:
    print(canList[0][0],
          canList[1][0],
          sep='\n',
          file=outFile)

# print(lines, candidates, canList, sep='\n')

inFile.close()
outFile.close()
