import math

p = int(input())
x = int(input())
y = int(input())

dep = x * 100 + y
kap = dep * (p / 100) + dep
rub = int(kap) // 100
kop = int(kap) % 100
print(rub, kop)
