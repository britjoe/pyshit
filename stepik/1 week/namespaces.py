nsParent = {'global': None}
nsVar = {'global': []}


def create(par, ns):
    global nsParent
    nsParent[par] = ns
    nsVar[par] = []


def add(ns, var):
    global nsVar
    c = nsVar[ns]
    c.append(var)
    nsVar[ns] = c


def get(ns, var):
    if var in nsVar[ns]:
        return ns
    else:
        if nsParent[ns] is not None:
            return get(nsParent[ns], var)
        else:
            return None


n = int(input())

for i in range(n):
    cmd, ns, param = input().split()
    if cmd == 'create':
        create(ns, param)
    elif cmd == 'add':
        add(ns, param)
    elif cmd == 'get':
        print(get(ns, param))
