import time
start_time = time.time()

with open("12.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

s = [(x.find("S"), i) for i, x in enumerate(grid) if x.find("S") > -1][0]
e = [(x.find("E"), i) for i, x in enumerate(grid) if x.find("E") > -1][0]

grid = [[ord(x) - ord("a") for x in line] for line in grid]
grid[s[1]][s[0]] = 0
grid[e[1]][e[0]] = 25

def get_neighbours(pos):
    x, y = pos
    if y-1 >= 0 and grid[y-1][x]-1 <= grid[y][x]:
        yield (x, y-1)
    if x+1 < len(grid[0]) and grid[y][x+1]-1 <= grid[y][x]:
        yield (x+1, y)
    if y+1 < len(grid) and grid[y+1][x]-1 <= grid[y][x]:
        yield (x, y+1)
    if x-1 >= 0 and grid[y][x-1]-1 <= grid[y][x]:
        yield (x-1, y)

visited = {s: 0}
todo = [s]
def check_neighbours(nextPos):
    if nextPos == e:
        return
    for n in get_neighbours(nextPos):
        if n not in visited and n not in todo:
            visited[n] = visited[nextPos] + 1
            todo.append(n)

while len(todo):
    check_neighbours(todo.pop(0))

print(visited[e])

print("--- %s seconds ---" % (time.time() - start_time))

a = []
for y, line in enumerate(grid):
    for x, val in enumerate(line):
        if val == 0 and (x, y) != s:
            a.append((x, y))

m = visited[e]
for start in a:
    visited = {start: 0}
    todo = [start]
    while len(todo):
        check_neighbours(todo.pop(0))
    m = min(m, visited.get(e, m))

print(m)

print("--- %s seconds ---" % (time.time() - start_time))