from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, a):
        self.a = copy.deepcopy(a)

    def __str__(self):
        result = ''
        for i in range(len(self.a)):
            result += '\t'.join(map(str, self.a[i]))
            if i < (len(self.a) - 1):
                result += '\n'
        return result

    def size(self):
        rows = len(self.a)
        column = len(self.a[0])
        result = (rows, column)
        return result

    def __add__(self, other):
        if len(self.a) == len(other.a) and len(self.a[0]) == len(other.a[0]):
            result = []
            for i in range(len(self.a)):
                row = []
                for j in range(len(self.a[i])):
                    x = (self.a[i][j] + other.a[i][j])
                    row.append(x)
                result.append(row)
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = []
        for i in range(len(self.a)):
            row = []
            for j in range(len(self.a[i])):
                x = self.a[i][j] * other
                row.append(x)
            result.append(row)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = []
        for i in range(len(self.a[0])):
            row = []
            for j in range(len(self.a)):
                row.append(self.a[j][i])
            result.append(row)
        self.a = result
        return Matrix(self.a)

    @staticmethod
    def transposed(x):
        result = []
        for i in range(len(x.a[0])):
            row = []
            for j in range(len(x.a)):
                row.append(x.a[j][i])
            result.append(row)
        return Matrix(result)


exec(stdin.read())
