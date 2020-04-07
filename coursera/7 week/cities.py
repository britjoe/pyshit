n = int(input())
cityDict = dict()

for p in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    for city in cities:
        if city not in cityDict:
            cityDict[city] = ''
        cityDict[city] = country

c = int(input())
for k in range(c):
    print(cityDict[input()])
