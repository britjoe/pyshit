import datetime

y, m, d = map(int, input().split())
delta = datetime.timedelta(int(input()))
q = datetime.date(y, m, d)
result = q + delta
print(result.year, result.month, result.day)
