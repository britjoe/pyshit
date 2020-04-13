c = [1, 2, 1, 5, True, False, True, 'false', [], [1, 2], [1, 2]]
objects = set(c)
ans = 0
for obj in objects:
    ans += 1

print(ans)
