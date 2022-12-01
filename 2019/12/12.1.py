import time
from itertools import combinations
start_time = time.time()

with open("12.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def add_tuple(a, b):
    return [sum(x) for x in zip(a, b)]

pos = []
for line in lines:
    l = line.split(",")
    x = int(l[0][3:])
    y = int(l[1][3:])
    z = int(l[2][3:-1])
    pos.append([x, y, z])

vel = [[0, 0, 0] for _ in range(4)]

for j in range(1000):
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

print(sum([sum([abs(x) for x in pos[i]]) * sum([abs(x) for x in vel[i]]) for i in range(4)]))

print("--- %s seconds ---" % (time.time() - start_time))