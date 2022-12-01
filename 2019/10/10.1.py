import time, math
start_time = time.time()

with open("10.txt") as file:
    data = [list(x.strip()) for x in file.readlines()]

asteroids = set()
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            asteroids.add((x, y))

visible = {}

for source in asteroids:
    seen = set()
    for target in asteroids:
        if source != target:
            direction = (target[0] - source[0], target[1] - source[1])
            gcd = math.gcd(*direction)
            direction = (direction[0] / gcd, direction[1] / gcd)
            seen.add(direction)
    visible[source] = seen

print(max([len(x) for x in visible.values()]))

print("--- %s seconds ---" % (time.time() - start_time))