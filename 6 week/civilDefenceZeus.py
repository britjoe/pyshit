def sb(BombNeeded):
    return BombNeeded[1]


countSettle = int(input())
settle = list(map(int, input().split()))
countBomb = int(input())
bomb = list(map(int, input().split()))
i = 1
for i in range(countSettle):
    settle[i] = [settle[i], i + 1, 0]
for i in range(countBomb):
    bomb[i] = [bomb[i], i + 1]
settle.sort()
bomb.sort()

st = 0
for i in range(countSettle):
    BombNeeded = 0
    min = 10e10
    for k in range(st, countBomb):
        temp = abs(settle[i][0] - bomb[k][0])
        if temp < min:
            BombNeeded = k
            min = temp
            settle[i][2] = bomb[k][1]
        else:
            break
    st = BombNeeded
settle.sort(key=sb)

for l in range(len(settle)):
    print(settle[l][2], end=' ')
