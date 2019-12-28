m = int(input())
h = m // (60)
hh = h % 24
mm = (m - hh*60) % 60
print(hh, mm)
