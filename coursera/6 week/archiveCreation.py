disk, users = map(int, input().split())
usList = []
for i in range(users):
    usList.append(int(input()))
usList.sort()
i = 0
space = usList[i]
while space <= disk:
    i += 1
    if i < len(usList):
        space = space + usList[i]
    else:
        break

print(i)
