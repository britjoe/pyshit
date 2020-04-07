a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    print(a)
else:
    if a < b >= c:
        print(b)
    else:
        if a > c:
            print(a)
        else:
            print(c)
