import time
start_time = time.time()

with open("23.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    # data = [list(line) for line in lines]

def count_data(p = False):
    global data
    min_x = min(x[0] for x in data)
    min_y = min(x[1] for x in data)
    max_x = max(x[0] for x in data)
    max_y = max(x[1] for x in data)
    ret = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in data:
                if p: print("#", end="")
            else:
                if p: print(".", end="")
                ret += 1
        if p: print()
    return ret

data = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            data.add((x, y))

# print(data)
# print_data()

def checkEmpty(pos, direction):
    global data
    x, y = pos
    if direction == 0: # North
        return all((x+dx, y-1) not in data for dx in (-1, 0, 1))
    if direction == 1: # south
        return all((x+dx, y+1) not in data for dx in (-1, 0, 1))
    if direction == 2: # west
        return all((x-1, y+dy) not in data for dy in (-1, 0, 1))
    if direction == 3: # east
        return all((x+1, y+dy) not in data for dy in (-1, 0, 1))

directions = [0, 1, 2, 3]
moving = [(0, -1), (0, 1), (-1, 0), (1, 0)]
rounds = 0

def calc():
    global directions, moving, data, rounds
    moved = False
    moves = {}
    occurring = {}
    for elf in data:
        if all(checkEmpty(elf, d) for d in directions):
            moves[elf] = elf
            occurring[elf] = occurring.get(elf, 0) + 1
            # print(f"elf {elf} not moving")
        else:
            for direction in directions:
                # print(f"elf {elf}, direction {direction}, empty {checkEmpty(elf, direction)}")
                if checkEmpty(elf, direction):
                    d = moving[direction]
                    moves[elf] = (elf[0]+d[0], elf[1]+d[1])
                    occurring[(elf[0]+d[0], elf[1]+d[1])] = occurring.get((elf[0]+d[0], elf[1]+d[1]), 0) + 1
                    moved = True
                    break
            if elf not in moves:
                moves[elf] = elf
                occurring[elf] = occurring.get(elf, 0) + 1
    # print(occurring)
    new_data = set()
    for elf, n in moves.items():
        if occurring[n] == 1:
            # print(f"elf {elf} moving to {n}")
            new_data.add(n)
        else:
            # print(f"elf {elf} not moving")
            new_data.add(elf)
    data = new_data
    directions.append(directions.pop(0))
    # print(data)
    # print_data()
    rounds += 1
    return moved

for _ in range(10):
    calc()

res = count_data()
print(res)

while calc():
    pass

count_data()
print(rounds)

print("--- %s seconds ---" % (time.time() - start_time))