from time import time
start = time()
data = open("22.txt").read().split('\n')

# ======== code =======

def part1(data):
    grid = [[[0 for _ in range(100)]for _ in range(100)] for _ in range(100)]
    for (value, steps) in data:
        for x in range(steps[0][0], steps[0][1] + 1):
            for y in range(steps[1][0], steps[1][1] + 1):
                for z in range(steps[2][0], steps[2][1] + 1):
                        grid[x][y][z] = value
    return sum(sum(sum(z for z in y) for y in x) for x in grid)

def intersect(cube1, cube2):
    (ax0, ax1), (ay0, ay1), (az0, az1) = cube1
    (bx0, bx1), (by0, by1), (bz0, bz1) = cube2
    x0 = max(ax0, bx0)
    y0 = max(ay0, by0)
    z0 = max(az0, bz0)
    x1 = min(ax1, bx1)
    y1 = min(ay1, by1)
    z1 = min(az1, bz1)
    if x0 <= x1 and y0 <= y1 and z0 <= z1:
        return ((x0, x1), (y0, y1), (z0, z1))
    return False


def part2(data):
    cubes = {}
    for line in data:
        new = {}
        for cube in cubes:
            intersec = intersect(line[1], cube)
            if intersec: new[intersec] = new.get(intersec, cubes.get(intersec, 0)) - cubes[cube]
        cubes |= new
        cubes[line[1]] = cubes.get(line[1], 0) + line[0]
    return sum((cube[0][1] - cube[0][0] + 1) * (cube[1][1] - cube[1][0] + 1) * (cube[2][1] - cube[2][0] + 1) * value for cube, value in cubes.items())


data = [(line[:2] == "on", tuple((int(x.split("..")[0][x.index('=') + 1:]), int(x.split("..")[1])) for x in line.split(','))) for line in data]
print(part1([line for line in data if max([max(x) for x in line[1]]) - min([min(x) for x in line[1]]) <= 100]))
print(part2(data))
print(f"\n===== {time() - start} sec =====")