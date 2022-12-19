import time, itertools
start_time = time.time()

with open("18.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = {tuple(map(int, line.split(","))) for line in lines}

neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

print(sum(sum(0 if (cube[0]+x, cube[1]+y, cube[2]+z) in data else 1 for x, y, z in neighbours) for cube in data))

extent = ([min(cube[i] for cube in data) for i in range(3)], [max(cube[i] for cube in data) for i in range(3)])

air = {(x, y, z) for x in range(extent[0][0], extent[1][0]+1) for y in range(extent[0][1], extent[1][1]+1) for z in range(extent[0][2], extent[1][2]+1) if (x, y, z) not in data}
outside = {block for block in air if block[0] in list(zip(*extent))[0] or block[1] in list(zip(*extent))[1] or block[2] in list(zip(*extent))[2]}

todo = list(outside)
while len(todo):
    x, y, z = todo.pop(0)
    outside.add((x, y, z))
    for xd, yd, zd in neighbours:
        t = (x+xd, y+yd, z+zd)
        if t not in todo and t in air and t not in outside:
            todo.append(t)

for t in air.difference(outside):
    data.add(t)

print(sum(sum(0 if (cube[0]+x, cube[1]+y, cube[2]+z) in data else 1 for x, y, z in neighbours) for cube in data))

print("--- %s seconds ---" % (time.time() - start_time))