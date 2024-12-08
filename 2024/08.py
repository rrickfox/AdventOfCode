import time
from collections import defaultdict
from itertools import combinations
start_time = time.time()

with open("08.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

width = len(lines[0])
height = len(lines)

data = defaultdict(set)
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        if val != "." and val != "#": data[val].add((x, y))

antinodes = set()
for freq in data.values():
    for a, b in combinations(freq, 2):
        diff = (b[0]-a[0], b[1]-a[1])
        antinodes.add((b[0] + diff[0], b[1] + diff[1]))
        antinodes.add((a[0] - diff[0], a[1] - diff[1]))

print(sum(1 for tup in antinodes if 0<=tup[0]<width and 0<=tup[1]<height))

antinodes = set()
for freq in data.values():
    for a, b in combinations(freq, 2):
        diff = (b[0]-a[0], b[1]-a[1])
        i = 0
        while True:
            i += 1
            if 0<=(b[0] + i*diff[0])<width and 0<=(b[1] + i*diff[1])<height:
                antinodes.add((b[0] + i*diff[0], b[1] + i*diff[1]))
            else: break
        i = 0
        while True:
            i += 1
            if 0<=(a[0] - i*diff[0])<width and 0<=(a[1] - i*diff[1])<height:
                antinodes.add((a[0] - i*diff[0], a[1] - i*diff[1]))
            else: break
        antinodes.add(a)
        antinodes.add(b)

print(len(antinodes))

print(f"--- {(time.time() - start_time)} seconds ---")