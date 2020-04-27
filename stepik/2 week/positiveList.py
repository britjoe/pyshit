class NonPositiveError(Exception):
    pass


class PositiveList(list):
    pass

    def append(self, a):
        if a > 0:
            list.append(self, a)
        else:
            raise NonPositiveError


a = PositiveList()
a.append(1)
print(a)
a.append(-1)