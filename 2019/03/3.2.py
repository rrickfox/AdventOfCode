from cmath import inf
import time
start_time = time.time()

with open("3.txt") as file:
    first = [(x[0], int(x[1:])) for x in file.readline().split(",")]
    second = [(x[0], int(x[1:])) for x in file.readline().split(",")]

x = 0
y = 0
dist = 0
points = {}

for inst in first:
    if inst[0] == "R":
        for i in range(1, inst[1] + 1):
            x += 1
            if (x, y) not in points:
                points[(x, y)] = dist + i
    elif inst[0] == "L":
        for i in range(1, inst[1] + 1):
            x -= 1
            if (x, y) not in points:
                points[(x, y)] = dist + i
    elif inst[0] == "U":
        for i in range(1, inst[1] + 1):
            y += 1
            if (x, y) not in points:
                points[(x, y)] = dist + i
    elif inst[0] == "D":
        for i in range(1, inst[1] + 1):
            y -= 1
            if (x, y) not in points:
                points[(x, y)] = dist + i
    dist += inst[1]

x = 0
y = 0
dist = 0
m = inf

for inst in second:
    if inst[0] == "R":
        for i in range(1, inst[1] + 1):
            x += 1
            if (x, y) in points:
                m = min(m, points[(x, y)] + dist + i)
    elif inst[0] == "L":
        for i in range(1, inst[1] + 1):
            x -= 1
            if (x, y) in points:
                m = min(m, points[(x, y)] + dist + i)
    elif inst[0] == "U":
        for i in range(1, inst[1] + 1):
            y += 1
            if (x, y) in points:
                m = min(m, points[(x, y)] + dist + i)
    elif inst[0] == "D":
        for i in range(1, inst[1] + 1):
            y -= 1
            if (x, y) in points:
                m = min(m, points[(x, y)] + dist + i)
    dist += inst[1]

print(m)

print("--- %s seconds ---" % (time.time() - start_time))