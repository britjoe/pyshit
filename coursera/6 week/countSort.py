def countSort(a):
    cntA = [0] * (101)
    for i in a:
        cntA[i] += 1
    for nowA in range(101):
        print((str(nowA) + ' ') * cntA[nowA], end='')


a = list(map(int, input().split()))
countSort(a)
