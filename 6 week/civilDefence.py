def nearest(list1, x):
    b = []

    for i in range(len(list1)):
        b.append(abs(list1[i] - x))
        map(abs, b)

    c = b[0]
    # inId = 0

    for i in range(1, len(b)):
        if c > b[i]:
            c = b[i]
    inId = list.index(b, c)

    return inId


def sortTuple(a):
    return a[1], a[0]


# numOfSet = 10
# a = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
# numOfShel = 10
# b = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]
numOfSet = int(input())
a = list(map(int, input().split()))
numOfShel = int(input())
b = list(map(int, input().split()))

# settle = []
# for i in range(numOfSet):
#     settle.append((i, a[i]))
#
# bomb = []
# for i in range(numOfShel):
#     bomb.append((i, b[i]))
#
# settle.sort(key=sortTuple)
# bomb.sort(key=sortTuple)

result = []
for i in range(len(a)):
    result.append((nearest(b, a[i])+1))
i
print(*result)
