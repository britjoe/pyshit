fSet = set(map(int, input().split()))
sSet = set(map(int, input().split()))
print(*sorted(fSet & sSet))
