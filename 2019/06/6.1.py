# this is massively overcomplicated
# i build the whole tree instead of doing it via a dictionary

import time
start_time = time.time()

with open("6.txt") as file:
    data = [(x.split(")")[0], x.strip().split(")")[1]) for x in file.readlines()]

orbiting = [(data[0][0], [data[0][1]])]

def search_insert(node, insert):
    if isinstance(node, str):
        if node == insert[0]:
            return True, (node, insert[1])
        else:
            return False, node
    elif node[0] == insert[0]:
        return True, (node[0], node[1] + insert[1])
    else:
        children = []
        flag = False
        for n in node[1]:
            if not flag:
                f, ret = search_insert(n, insert)
                flag = flag or f
                children.append(ret)
            else:
                children.append(n)
        return flag, (node[0], children)

def tryfitin(orbits):
    flag = False
    new = [orbits.pop(0)]
    while len(orbits) > 0:
        current = orbits.pop()
        inserted = False
        for i in range(len(new)):
            f, ret = search_insert(new[i], current)
            flag = flag or f
            inserted = inserted or f
            new[i] = ret
            if inserted:
                break
        if not inserted:
            new.append(current)
    return new, flag

for x in data[1:]:
    x = (x[0], [x[1]])
    flag = False
    for i in range(len(orbiting)):
        f, ret = search_insert(orbiting[i], x)
        flag = flag or f
        orbiting[i] = ret
        if flag:
            break
    if not flag:
        orbiting.append(x)

flag = True
while flag:
    orbiting, flag = tryfitin(orbiting)

orbiting.reverse()
orbiting, _ = tryfitin(orbiting)
orbiting.reverse()
orbiting, _ = tryfitin(orbiting)

def search_depth(node, depth = 0):
    if isinstance(node, str):
        return depth
    else:
        return sum([search_depth(x, depth + 1) for x in node[1]]) + depth

print(search_depth(orbiting[0]))

print("--- %s seconds ---" % (time.time() - start_time))