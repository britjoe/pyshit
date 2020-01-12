a, b, c = int(input()), int(input()), int(input())
if a == b and b == c and c == a:
    print(3)
elif a != b and b != c and c != a:
    print(0)
else:
    print(2)
