import math

price = float(input())
rub = int(price)
a = math.floor(price)
kop = round((price - math.floor(price)) * 100)
print(rub, kop)
