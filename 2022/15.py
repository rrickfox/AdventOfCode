import time
import parse
start_time = time.time()

p = parse.compile("Sensor at x={}, y={}: closest beacon is at x={}, y={}")

with open("15.txt", "r") as file:
    lines = [list(map(int, p.parse(line.strip()))) for line in file.readlines()]
    data = [((line[0], line[1]), (line[2], line[3])) for line in lines]

min_x_beacon = min(x[1][0] for x in data)
max_x_beacon = max(x[1][0] for x in data)

beacons = set(x[1] for x in data)

distances = {}

def calc_distance(sensor, beacon):
    return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

for sensor, beacon in data:
    d = calc_distance(sensor, beacon)
    distances[sensor] = d

max_x_distance = max(distances.values())

def calc_intersection(a, b):
    if b[0] > a[1] or a[0] > b[1]:
        # no intersection
        return False
    return max(a[0], b[0]), min(a[1], b[1])

# find intersections between ranges
# if two ranges overlap, remove the intersection again
# example
# +++++++++++++
#            +++++++++++++++++
#            --
# when summed up the minus signs remove the intersection again before being added by the second range
r = {}
y = 2000000
for sensor, distance in distances.items():
    if abs(sensor[1] - y) <= distance:
        n = (sensor[0] - (distance - abs(sensor[1] - y)), sensor[0] + (distance - abs(sensor[1] - y)))
        new = {}
        for range_none in r:
            i = calc_intersection(range_none, n)
            if i:
                new[i] = (new.get(i, r.get(i, 0))) - r[range_none]
        r.update(new)
        r[n] = r.get(n, 0) + 1

print(sum((x[1]-x[0]+1)*sign for x, sign in r.items()) - sum(1 for beacon in beacons if beacon[1] == y))


print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print()

# part two
# only consider the edge of each sensor, check each point against all the other sensors

bubbleUp = False
for sensor, distance in distances.items():
    for y_off in range(distance + 2):
        s = set()
        s.add((sensor[0]+(distance+1-y_off), sensor[1]+y_off))
        s.add((sensor[0]+(distance+1-y_off), sensor[1]-y_off))
        s.add((sensor[0]-(distance+1-y_off), sensor[1]-y_off))
        s.add((sensor[0]-(distance+1-y_off), sensor[1]+y_off))
        for x, y in s:
            if x < 0 or x > 4000000 or y < 0 or y > 4000000:
                continue
            if (x, y) in beacons:
                continue
            possible = True
            for sensor2, _ in data:
                if sensor == sensor2:
                    continue
                if calc_distance(sensor2, (x, y)) <= distances[sensor2]:
                    possible = False
                    break
            if possible:
                print(x*4000000+y)
                bubbleUp = True
                break
        if bubbleUp:
            break
    if bubbleUp:
        break

print("--- %s seconds ---" % (time.time() - start_time))