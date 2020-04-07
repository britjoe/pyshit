maxNum = int(input())
mySet = set(map(str, range(1, maxNum + 1)))

while True:
    beatrice = input()
    if beatrice == 'HELP':
        break
    beatrice = set(beatrice.split())
    au = input()
    if au == 'YES':
        mySet &= beatrice
    else:
        mySet -= beatrice

print(' '.join(sorted(mySet)))
