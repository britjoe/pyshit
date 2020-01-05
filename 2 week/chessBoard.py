x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 % 2 == 0 and y1 % 2 == 0 and x2 % 2 == 0 and y2 % 2 == 0:
    print('YES')
elif x1 % 2 == 0 and y1 % 2 == 0 and x2 % 2 != 0 and y2 % 2 != 0:
    print('YES')
elif x1 % 2 != 0 and y1 % 2 != 0 and x2 % 2 != 0 and y2 % 2 != 0:
    print('YES')
elif x1 % 2 != 0 and y1 % 2 != 0 and x2 % 2 == 0 and y2 % 2 == 0:
    print('YES')
else:
    print('NO')

