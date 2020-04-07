class MoneyBox:
    def __init__(self, capacity):
        self.volume = capacity
        self.money = 0

    def can_add(self, v):
        return self.money + v <= self.volume

    def add(self, v):
        if self.can_add(v) is True:
            self.money += v


myBox = MoneyBox(10)
print(myBox.money)
x = 5
y = 5
print(myBox.can_add(x))
myBox.add(x)
print(myBox.money)
print(myBox.can_add(y))
myBox.add(y)
print(myBox.money)
