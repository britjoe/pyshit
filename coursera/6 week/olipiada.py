l = int(input())
a = []


def sf(a):
    return int(a[1])


for i in range(l):
    a.append(input())

nl = []
for i in a:
    nl.append(i.split())
nl.sort(key=sf, reverse=True)

for i in nl:
    print(i[0])
