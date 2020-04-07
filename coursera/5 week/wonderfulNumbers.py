a = 10
b = 100
for i in range(a, b):
    d = i // 10
    e = i % 10
    if i == 2 * d * e:
        print(i)
