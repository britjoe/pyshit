a = input()
if a.find('f') != -1:
    print(a.find('f'))
    if a.rfind('f') != -1 and a.find('f') != a.rfind('f'):
        print(a.rfind('f'))
