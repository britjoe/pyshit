a = input()
first = a.find('h')
last = a.rfind('h')
fin = a[:first] + a[last+1:]
print(fin)
