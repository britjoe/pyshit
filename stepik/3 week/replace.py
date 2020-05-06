s = input()
a = input()
b = input()

i = 0
while True:
    if a in s:
        s = s.replace(a, b)
        i += 1
    if i > 1000 or a not in s:
        break

if i <= 1000:
    print(i)
else:
    print('Impossible')
