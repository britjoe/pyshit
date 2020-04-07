from sys import stdin

wordsAll = stdin.read().split()
wordsDict = dict()
for word in wordsAll:
    wordsDict[word] = wordsDict.get(word, 0) + 1
listWordAll = []
for wordList in wordsDict:
    listWordAll.append([wordsDict[wordList] * -1, wordList])
finalValue = []
for wordd in sorted(listWordAll):
    finalValue.append(wordd[1])
print('\n'.join(finalValue))
