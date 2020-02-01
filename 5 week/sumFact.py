def factorial(num):
    fact = 1
    i = 2
    while i <= num:
        fact *= i
        i += 1
    return fact


n = int(input())
d = 0
for i in range(1, n + 1):
    d = d + factorial(i)

print(d)
