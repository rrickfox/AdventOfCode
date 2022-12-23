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

print("--- %s seconds ---" % (time.time() - start_time))