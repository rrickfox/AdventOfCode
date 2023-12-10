import time
start_time = time.time()

with open("10.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

x, y = [(x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "S"][0]

directions = "NESW"
deltas = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
symbols = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE", ".": ""}

next_dir = ""
for dir in directions:
    d = data[y+deltas[dir][1]][x+deltas[dir][0]]
    if directions[directions.index(dir)+2%4] in symbols[d]:
        next_dir = dir
        break

steps = 0
visited = set()
while True:
    dx, dy = deltas[next_dir]
    x += dx
    y += dy
    visited.add((x, y))
    if data[y][x] == "S": break
    next_dir = symbols[data[y][x]].replace(directions[(directions.index(next_dir)+2)%4], "")
    steps += 1

print((steps+1)//2)

inside = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) in visited:
            continue
        north = "".join(data[py][px] for (px, py) in sorted(list({(x, ny) for ny in range(y-1, -1, -1)}.intersection(visited)), key= lambda z: z[1])).replace("|", "").replace("7L", "-").replace("FJ", "-")
        south = "".join(data[py][px] for (px, py) in sorted(list({(x, ny) for ny in range(y+1, len(data))}.intersection(visited)), key= lambda z: z[1])).replace("|", "").replace("7L", "-").replace("FJ", "-")
        west =  "".join(data[py][px] for (px, py) in sorted(list({(nx, y) for nx in range(x-1, -1, -1)}.intersection(visited)), key= lambda z: z[0])).replace("-", "").replace("FJ", "|").replace("L7", "|")
        east =  "".join(data[py][px] for (px, py) in sorted(list({(nx, y) for nx in range(x+1, len(data[0]))}.intersection(visited)), key= lambda z: z[0])).replace("-", "").replace("FJ", "|").replace("L7", "|")
        if all(len(n)%2 == 1 for n in [north, west, south, east]): inside += 1

print(inside)

print(f"--- {(time.time() - start_time)} seconds ---")