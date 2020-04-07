prevN = -1
cnt_prev = 0
cnt = 0
n = int(input())
while n != 0:
    if prevN == n:
        cnt_prev += 1
    else:
        prevN = n
        cnt = max(cnt, cnt_prev)
        cnt_prev = 1
    n = int(input())
cnt = max(cnt, cnt_prev)
print(cnt)
