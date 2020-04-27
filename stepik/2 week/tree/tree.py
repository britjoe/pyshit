import shutil
import os
import os.path

with open('res.txt', 'w') as r:
    y = []
    for cd, dire, f in os.walk('./main'):
        for file in f:
            if file[-3:] == '.py':
                y.append(cd[2:])
                break
    r.write('\n'.join(sorted(y))+'\n')
    print(y)
