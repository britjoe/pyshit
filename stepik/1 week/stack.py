import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, a):
        self.log(a)
        list.append(self, a)


a = LoggableList()
a.append(3)
a.append(3)
print(a)
