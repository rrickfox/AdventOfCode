import time
start_time = time.time()

#   2
#  / \
# 1---3
# | X |
# 0---4

neighbours = [{1, 3, 4}, {0, 2, 3, 4}, {1, 3}, {0, 1, 2, 4}, {0, 1, 3}]

def run(before, current):
    if len(before) == 8:
        print("Done all: " + str(before))
        return [before]
    if len({tuple(sorted([i, current])) for i in neighbours[current]}.difference(set(before))) == 0:
        print("Done, not possible: " + str(before))
        return []

    ret = []
    for i in {tuple(sorted([i, current])) for i in neighbours[current]}.difference(set(before)):
        if current == i[0]:
            ret += run(before + [tuple(sorted([current, i[1]]))], i[1])
        else:
            ret += run(before + [tuple(sorted([current, i[0]]))], i[0])
    return ret

found = run([], 0)
paths = []

for path in found:
    p = [0]
    last = 0
    for node in path:
        last = node[1] if node[0] == last else node[0]
        p += [last]
    paths.append(p)

for p in paths: print(p)
print(len(paths))

print("--- %s seconds ---" % (time.time() - start_time))