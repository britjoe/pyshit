s = input()
t = input()

i = 0
cnt = 0
while True:
    i = s.find(t, i)
    if i == -1:
        break
    else:
        i += 1
    cnt += 1

print(cnt)
