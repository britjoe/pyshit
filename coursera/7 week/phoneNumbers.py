a = input()
a = a.replace('(', '')
a = a.replace(')', '')
a = a.replace('-', '')
a = a.replace('+7', '8')

phoneDict = dict()

for t in range(3):
    num = input()
    newnum = num.replace('(', '')
    newnum = newnum.replace(')', '')
    newnum = newnum.replace('-', '')
    newnum = newnum.replace('+7', '8')
    if len(newnum) < 11:
        newnum = '8495' + newnum
    phoneDict[num] = newnum
print(phoneDict)



# newPD = set()
#
# for num in phoneDict:
#
#     if len(newnum) < 11:
#         newnum = '8495' + newnum
#     newPD.add(newnum)

# print(a, phoneDict, newPD, sep='\n')
