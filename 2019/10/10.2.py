import time, math
start_time = time.time()

with open("10.txt") as file:
    data = [list(x.strip()) for x in file.readlines()]

asteroids = set()
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] != ".":
            asteroids.add((x, y))

visible = {}

for source in asteroids:
    seen = {}
    for target in asteroids:
        if source != target:
            direction = (target[0] - source[0], target[1] - source[1])
            gcd = math.gcd(*direction)
            direction_shortened = (direction[0] / gcd, direction[1] / gcd)
            if direction_shortened in seen:
                seen[direction_shortened] += [direction]
            else:
                seen[direction_shortened] = [direction]
    visible[source] = seen

m = max([len(x.keys()) for x in visible.values()])
best = None
for x in visible:
    if len(visible[x].keys()) == m:
        best = x
        break

def deg(x, y):  
    if x == 0:
        return 0 if y < 0 else 180
    return (90 - math.degrees(math.atan(-1*y / x))) % 360 + (180 if x < 0 else 0)

# make a list with the values of visible[best], sorted by the respective keys in the deg function
d = {}
l = []
for k, v in visible[best].items():
    if deg(k[0], k[1]) not in d:
        d[deg(k[0], k[1])] = v
        l.append(deg(k[0], k[1]))
    else:
        d[deg(k[0], k[1])] += v

l.sort()
for i in l:
    d[i].sort(key = lambda v: v[0]*v[0] + v[1]*v[1])

i = 0
while len(l) > 0:
    new = []
    for index, x in enumerate(l):
        r = d[x].pop(0)
        i += 1
        if i == 200:
            ret = r
        if len(d[x]) == 0:
            del d[x]
        else:
            new.append(x)
    l = new

print(100 * (best[0] + ret[0]) + (best[1] + ret[1]))

print("--- %s seconds ---" % (time.time() - start_time))