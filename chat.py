import chatMembers as Cm

names = Cm.ChatMembers()
b = ['John', 'David', 'Kate', 'Alex']
for i in b:
    names.append(i)

names.pop(-1)

names.remove("David")


l = ['John', 'David', 'Kate', 'Alex']
l.pop['John']
print(l)