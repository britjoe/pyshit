import math

a = float(input())
r = int((a - math.floor(a)) * 10)
if r == 5:
    a = math.ceil(a)
elif r < 5:
    a = math.floor(a)
else:
    a = math.ceil(a)
print(a)
