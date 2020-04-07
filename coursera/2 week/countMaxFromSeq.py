a = int(input())
i = 1
max = a
while a != 0:
    a = int(input())
    if a == max:
        i += 1
    if a > max and a != 0:
        max = a
        i = 1
print(i)
