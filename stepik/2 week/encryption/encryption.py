import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open('passwords.txt') as p:
    l = []
    for line in p:
        l.append(line.rstrip())
    for i in l:
        try:
            d = simplecrypt.decrypt(i, encrypted)
        except:
            pass
        else:
            print(i, d)
    print(type(d))
