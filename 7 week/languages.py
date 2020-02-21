pupils = [{input() for j in range(int(input()))} for i in range(int(input()))]
pups = set.intersection(*pupils)
lang = set.union(*pupils)
print(len(pups), *sorted(pups), sep='\n')
print(len(lang), *sorted(lang), sep='\n')
