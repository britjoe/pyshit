razmer = int(input()) - 3
sizes = sorted(map(int, input().split()))
count = 0
for shoes in sizes:
    if shoes >= razmer + 3:
        count += 1
        razmer = shoes
print(count)
