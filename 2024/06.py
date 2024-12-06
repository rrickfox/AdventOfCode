import time
from itertools import cycle
start_time = time.time()

with open("06.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    size_x = len(lines[0])
    size_y = len(lines)

data = set()
pos_x = 0
pos_y = 0
start_pos_x = 0
start_pos_y = 0
dir = (0, -1)
dirs = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])

for y, line in enumerate(lines):
    for x, val in enumerate(line):
        if val == "#": data.add((x, y))
        elif val == "^":
            pos_x = start_pos_x = x
            pos_y = start_pos_y = y

visited = set([(pos_x, pos_y)])
while True:
    # check if have to turn
    while True:
        if (pos_x + dir[0], pos_y + dir[1]) not in data:
            break
        else:
            dir = next(dirs)

    pos_x += dir[0]
    pos_y += dir[1]
    
    if pos_x >= size_x or pos_x < 0 or pos_y >= size_y or pos_y < 0:
        break

    visited.add((pos_x, pos_y))

print(len(visited))

visited.discard((start_pos_x, start_pos_y))
num_loops = 0
for i, obstacle_pos in enumerate(visited):
    if i % 100 == 0: print("checking position", i, "of", len(visited))
    pos_x = start_pos_x
    pos_y = start_pos_y
    dir = (0, -1)
    dirs = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    visited_part2 = set([(pos_x, pos_y, dir)])
    loop = False

    while True:
        # check if have to turn
        while True:
            if (pos_x + dir[0], pos_y + dir[1]) not in data and (pos_x + dir[0], pos_y + dir[1]) != obstacle_pos:
                break
            else:
                dir = next(dirs)

        pos_x += dir[0]
        pos_y += dir[1]
        
        if pos_x >= size_x or pos_x < 0 or pos_y >= size_y or pos_y < 0:
            break
        
        if (pos_x, pos_y, dir) in visited_part2:
            loop = True
            break

        visited_part2.add((pos_x, pos_y, dir))
    
    if loop:
        num_loops += 1

print(num_loops)

print(f"--- {(time.time() - start_time)} seconds ---")