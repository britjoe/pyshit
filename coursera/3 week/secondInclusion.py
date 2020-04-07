a = input()
b = a.find('f')
c = a.rfind('f')
if b == -1:
    print(-2)
elif b == c:
    print(-1)
else:
    b = a.find('f', b + 1)
    print(b)
