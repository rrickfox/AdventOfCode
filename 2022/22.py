import time
from collections import deque
start_time = time.time()

with open("22.txt", "r") as file:
    field, moves_uncut = file.read().split("\n\n")
    moves_uncut = deque(moves_uncut.strip())

moves = []
s = ""
while moves_uncut:
    t = moves_uncut.popleft()
    if t.isdigit():
        s += t
    else:
        moves.append(int(s))
        s = ""
        moves.append(t)

if s != "":
    moves.append(int(s))

m = []
for y, line in enumerate(field.split("\n")):
    m.append({})
    line = line.rstrip()
    for x, char in enumerate(line):
        if char == " ": continue
        else:
            m[y][x] = True if char == "#" else False

def move(pos, direction):
    x, y = pos
    dx, dy = direction
    if dy != 0 and dx != 0:
        print("Shouldn't happen!")
    if dy != 0:
        if y+dy < 0 or (dy == -1 and x not in m[y+dy]):
            # search for next at bottom
            new_y = max(ny for ny in range(len(m)) if x in m[ny])
            if m[new_y][x]:
                return (x, y)
            else:
                return (x, new_y)
        elif y+dy >= len(m) or (dy == 1 and x not in m[y+dy]):
            # search for next at top
            new_y = min(ny for ny in range(len(m)) if x in m[ny])
            if m[new_y][x]:
                return (x, y)
            else:
                return (x, new_y)
        else:
            if m[y+dy][x]:
                return (x, y)
            else:
                return (x, y+dy)
    else:
        if x+dx < min(m[y].keys()):
            # search for next on the right
            new_x = max(m[y].keys())
            if m[y][new_x]:
                return (x, y)
            else:
                return (new_x, y)
        elif x+dx > max(m[y].keys()):
            # search for next at top
            new_x = min(m[y].keys())
            if m[y][new_x]:
                return (x, y)
            else:
                return (new_x, y)
        else:
            if m[y][x+dx]:
                return (x, y)
            else:
                return (x+dx, y)

move_direction = {
    "R": (0, (1, 0)),
    "D": (1, (0, 1)),
    "L": (2, (-1, 0)),
    "U": (3, (0, -1))
}
turn_direction = {
    "R": {
        "R": "D",
        "L": "U"
    },
    "D": {
        "R": "L",
        "L": "R"
    },
    "L": {
        "R": "U",
        "L": "D"
    },
    "U": {
        "R": "R",
        "L": "L"
    }
}

pos = (min(m[0].keys()), 0)
looking = "R"
# s = ""
for move_instr in moves:
    if isinstance(move_instr, int):
        for _ in range(move_instr):
            n = move(pos, move_direction[looking][1])
            if (n == pos):
                break
            else:
                pos = n
                # s += str(pos) + "\n"
    else:
        looking = turn_direction[looking][move_instr]

# with open("test.txt", "w") as file:
#     file.write(s)

print(1000 * (pos[1]+1) + 4 * (pos[0]+1) + move_direction[looking][0])

def move2(pos, direction):
    global move_direction
    # print(pos)
    x, y = pos
    dx, dy = move_direction[direction][1]

    if x >= 0 and x < 50: # 5 or 6
        if y >= 0 and y < 100:
            print(f"shouldn't happen, {pos}")
        elif y >= 100 and y < 150:
            block = 5
        elif y >= 150 and y < 200:
            block = 6
        else:
            print(f"shouldn't happen, {pos}")
    elif x >= 50 and x < 100: # 2, 3 or 4
        if y >= 0 and y < 50:
            block = 2
        elif y >= 50 and y < 100:
            block = 3
        elif y >= 100 and y < 150:
            block = 4
        else:
            print(f"shouldn't happen, {pos}")
    elif x >= 100 and x < 150:
        if y >= 0 and y < 50:
            block = 1
        else:
            print(f"shouldn't happen, {pos}")
    else:
        print(f"shouldn't happen, {pos}")

    if dy != 0:
        if y+dy < 0 or (dy == -1 and x not in m[y+dy]):
            # going above a block
            if block == 1:
                new_x = x - 100
                new_y = 199
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "U"
            elif block == 2:
                new_y = x + 100
                new_x = 0
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "R"
            elif block == 5:
                new_x = 50
                new_y = x + 50
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "R"
            else:
                print(f"shouldn't happen, {pos}")
        elif y+dy >= len(m) or (dy == 1 and x not in m[y+dy]):
            # below block
            if block == 1:
                new_x = 99
                new_y = x - 50
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "L"
            elif block == 4:
                new_x = 49
                new_y = x + 100
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "L"
            elif block == 6:
                new_y = 0
                new_x = x + 100
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "D"
            else:
                print(f"shouldn't happen, {pos}")
        else:
            if m[y+dy][x]:
                return (x, y), direction
            else:
                return (x, y+dy), direction
    else:
        if x+dx < min(m[y].keys()):
            # left of block
            if block == 2:
                new_y = 149 - y
                new_x = 0
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "R"
            elif block == 3:
                new_x = y - 50
                new_y = 100
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "D"
            elif block == 5:
                new_y = 149 - y
                new_x = 50
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "R"
            elif block == 6:
                new_x = y - 100
                new_y = 0
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "D"
            else:
                print(f"shouldn't happen, {pos}")
        elif x+dx > max(m[y].keys()):
            # right of block
            if block == 1:
                new_y = 149 - y
                new_x = 99
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "L"
            elif block == 3:
                new_y = 49
                new_x = y + 50
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "U"
            elif block == 4:
                new_y = 149 - y
                new_x = 149
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "L"
            elif block == 6:
                new_y = 149
                new_x = y - 100
                if m[new_y][new_x]:
                    return pos, direction
                else:
                    return (new_x, new_y), "U"
            else:
                print(f"shouldn't happen, {pos}")
        else:
            if m[y][x+dx]:
                return (x, y), direction
            else:
                return (x+dx, y), direction

pos = (min(m[0].keys()), 0)
looking = "R"
# s = ""
for move_instr in moves:
    if isinstance(move_instr, int):
        for _ in range(move_instr):
            n, looking = move2(pos, looking)
            if (n == pos):
                break
            else:
                pos = n
                # s += str(pos) + "\n"
    else:
        looking = turn_direction[looking][move_instr]

print(1000 * (pos[1]+1) + 4 * (pos[0]+1) + move_direction[looking][0])

print("--- %s seconds ---" % (time.time() - start_time))