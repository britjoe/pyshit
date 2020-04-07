maxN = int(input())
prevMaxN = int(input())
n = maxN
if maxN < prevMaxN:
    f = maxN
    maxN = prevMaxN
    prevMaxN = f
while n != 0:
    n = int(input())
    if maxN < n:
        prevMaxN = maxN
        maxN = n
    elif prevMaxN < n <= maxN:
        prevMaxN = n
print(prevMaxN)
