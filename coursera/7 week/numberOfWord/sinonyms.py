sin = dict()
sin2 = dict()
for i in range(int(input())):
    line = input().split()
    sin[line[1]] = line[0]
    sin2[line[0]] = line[1]

a = input()
if sin.get(a, 0) == 0:
    print(sin2[a])
else:
    print(sin[a])
