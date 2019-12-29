rub = int(input())
kop = int(input())
n = int(input())
tot = (rub*100+kop) * n
rub2 = tot % 100
kop2 = tot // 100
print(kop2, rub2)
