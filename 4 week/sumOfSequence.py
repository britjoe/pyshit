def sumOfSequence():
    n = int(input())
    if n != 0:
        return n + sumOfSequence()
    return 0


print(sumOfSequence())
