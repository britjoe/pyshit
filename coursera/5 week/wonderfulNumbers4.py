x = int(input())
y = int(input())

for a in range(x, y + 1):
    t = a // 1000
    s = (a - t * 1000) // 100
    d = (a - t * 1000 - s * 100) // 10
    e = a - t * 1000 - s * 100 - d * 10
    te = (t - e) ** 2
    sd = (s - d) ** 2
    if (0 ** (te + sd)) == 1:
        print(a)
