import time
start_time = time.time()

with open("8.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [[int(i) for i in line] for line in lines]

def getDataOrMinus1(x, y):
    if y < 0 or y >= len(data): return -1
    if x < 0 or x >= len(data[0]): return -1
    return data[y][x]

visible = [[None for _ in range(len(data[0]))] for _ in range(len(data))]

def getVisibleOrTrue(x, y):
    # print((x, y))
    if y < 0 or y >= len(visible):
        # print("19")
        return True
    if x < 0 or x >= len(visible[0]):
        # print(22)
        return True
    # print(visible[y][x])
    return visible[y][x]

for y in range(len(data)):
    for x in range(len(data[0])):
        # up
        if all(getDataOrMinus1(x, dy) < getDataOrMinus1(x, y) for dy in range(y-1, -1, -1)):
            visible[y][x] = True
            continue
        # left
        if all(getDataOrMinus1(dx, y) < getDataOrMinus1(x, y) for dx in range(x-1, -1, -1)):
            visible[y][x] = True
            continue
        # down
        if all(getDataOrMinus1(x, dy) < getDataOrMinus1(x, y) for dy in range(y+1, len(data)+1)):
            visible[y][x] = True
            continue
        # right
        if all(getDataOrMinus1(dx, y) < getDataOrMinus1(x, y) for dx in range(x+1, len(data[0])+1)):
            visible[y][x] = True

print("\n".join("".join("1" if i else "0" for i in line) for line in visible))

print(sum([sum(x for x in line if x) for line in visible]))

print("--- %s seconds ---" % (time.time() - start_time))

def search(a, b):
    try:
        k = a.index(b)
        return k 
    except ValueError:
        return -1

def runUntilValueOrMinus1(gen, val):
    index = 0
    for i in gen:
        if i == val:
            return index, None
        index += 1
    return (-1, index)

scenic = []
for y in range(len(data)):
    for x in range(len(data[0])):
        # up
        up, lUp = runUntilValueOrMinus1((getDataOrMinus1(x, dy) < getDataOrMinus1(x, y) for dy in range(y-1, -1, -1)), False)
        up = (lUp-1 if up == -1 else up) + 1
        # down
        down, lDown = runUntilValueOrMinus1((getDataOrMinus1(x, dy) < getDataOrMinus1(x, y) for dy in range(y+1, len(data))), False)
        down = (lDown-1 if down == -1 else down) + 1
        # left
        left, lLeft = runUntilValueOrMinus1((getDataOrMinus1(dx, y) < getDataOrMinus1(x, y) for dx in range(x-1, -1, -1)), False)
        left = (lLeft-1 if left == -1 else left) + 1
        # right
        right, lRight = runUntilValueOrMinus1((getDataOrMinus1(dx, y) < getDataOrMinus1(x, y) for dx in range(x+1, len(data[0]))), False)
        right = (lRight-1 if right == -1 else right) + 1
        scenic.append(up*down*left*right)

print(max(scenic))

print("--- %s seconds ---" % (time.time() - start_time))