import time
from collections import deque
start_time = time.time()

with open("20.txt", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]
    data = [list(line) for line in lines]

class Portal:
    def __init__(self, name, direction, pos):
        self.name = name
        self.direction = direction
        self.dimension = -1 if insideOutside(pos) else 1
        self.neighbours = {}

    def __str__(self):
        return f"{self.name}: {self.direction}, dimension change: {self.dimension}"

def insideOutside(pos):
    global data
    distx = min(pos[0], len(data[0])-pos[0] - 1)
    disty = min(pos[1], len(data)-pos[1] - 1)
    return distx == 2 or disty == 2

portals_pos = {}
portals_name = {}

for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        if data[y][x].isalpha():
            if data[y-1][x].isalpha() and data[y+1][x] == ".":
                p = Portal(data[y-1][x] + data[y][x], "D", (x, y+1))
                portals_pos[(x, y+1)] = p
                portals_name[p.name] = portals_name.get(p.name, set()).union({(x, y+1)})
            elif data[y-1][x] == "." and data[y+1][x].isalpha():
                p = Portal(data[y][x] + data[y+1][x], "U", (x, y-1))
                portals_pos[(x, y-1)] = p
                portals_name[p.name] = portals_name.get(p.name, set()).union({(x, y-1)})
            elif data[y][x-1].isalpha() and data[y][x+1] == ".":
                p = Portal(data[y][x-1] + data[y][x], "R", (x+1, y))
                portals_pos[(x+1, y)] = p
                portals_name[p.name] = portals_name.get(p.name, set()).union({(x+1, y)})
            elif data[y][x-1] == "." and data[y][x+1].isalpha():
                p = Portal(data[y][x] + data[y][x+1], "L", (x-1, y))
                portals_pos[(x-1, y)] = p
                portals_name[p.name] = portals_name.get(p.name, set()).union({(x-1, y)})

aa = next(iter(portals_name["AA"]))
zz = next(iter(portals_name["ZZ"]))
todo = deque([(aa, 0, 0, [(aa, "AA", 0)])])

seen = set()
while todo:
    pos, dist, dimension, history = todo.popleft()
    
    if (pos, dimension) in seen:
        continue
    seen.add((pos, dimension))

    if pos == zz and dimension == 0:
        print(dist)
        break

    x, y = pos
    if data[y-1][x] == "." and (x, y-1) not in seen: # move up
        todo.append(((x, y-1), dist + 1, dimension, history))
    if data[y+1][x] == "." and (x, y+1) not in seen: # move down
        todo.append(((x, y+1), dist + 1, dimension, history))
    if data[y][x-1] == "." and (x-1, y) not in seen: # move left
        todo.append(((x-1, y), dist + 1, dimension, history))
    if data[y][x+1] == "." and (x+1, y) not in seen: # move right
        todo.append(((x+1, y), dist + 1, dimension, history))

    if pos in portals_pos and pos != aa and pos != zz:
        portal = portals_pos[pos]
        if (dimension + portal.dimension) >= 0 and pos != history[-1][0]:
            name = portal.name
            new_pos = next(iter(portals_name[name].difference({pos})))
            todo.append((new_pos, dist+1, dimension + portal.dimension, history + [(pos, name, dimension + portal.dimension)]))


print("--- %s seconds ---" % (time.time() - start_time))