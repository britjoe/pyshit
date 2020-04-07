n = int(input())
i = 2
a = 0
while a == 0:
    if n % i == 0:
        a = i
        print(a)
    i = i + 1
