import time
from itertools import combinations
import math
start_time = time.time()

with open("12.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def add_tuple(a, b):
    return [sum(x) for x in zip(a, b)]

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

pos = []
for line in lines:
    l = line.split(",")
    x = int(l[0][3:])
    y = int(l[1][3:])
    z = int(l[2][3:-1])
    pos.append([x, y, z])

vel = [[0, 0, 0] for _ in range(4)]

orig_pos = pos[:]
orig_vel = vel[:]

again = [0, 0, 0]

steps = 0
while any([True if x == 0 else False for x in again]):
    steps += 1
    for a, b in combinations(range(4), 2):
        for i in range(3):
            if pos[a][i] > pos[b][i]:
                vel[a][i] -= 1
                vel[b][i] += 1
            elif pos[a][i] < pos[b][i]:
                vel[a][i] += 1
                vel[b][i] -= 1
    for i in range(4):
        pos[i] = add_tuple(pos[i], vel[i])
    for i in range(3):
        if again[i] == 0 and [p[i] for p in orig_pos] == [p[i] for p in pos] and [v[i] for v in orig_vel] == [v[i] for v in vel]:
            again[i] = steps + 1

print(lcm(again[0], lcm(again[1], again[2])))

print("--- %s seconds ---" % (time.time() - start_time))