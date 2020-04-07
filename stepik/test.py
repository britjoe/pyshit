class Counter:
    def __init__(self, start=0):
        self.count = start

    def inc(self):
        self.count += 1

    def res(self):
        self.count = 0


x = Counter()
for i in range(5):
    x.inc()
print(x.count)
x.res()
print(x.count)

