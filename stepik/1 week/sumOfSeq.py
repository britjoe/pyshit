from sys import stdin

n = int(input())
i = 0
res = 0
start = map(int, stdin.read().split())
for i in start:
    res += i

print(res)
