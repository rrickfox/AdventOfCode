import time
from collections import deque
start_time = time.time()

with open("24.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

blizzards = {}
width = len(lines[0]) - 2
height = len(lines) - 2
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in {">", "<", "v", "^"}:
            blizzards[(x-1, y-1)] = blizzards.get((x-1, y-1), []) + [char]

def moveBlizzards(blizzards):
    global width, height
    newPositions = {}
    for blizzard, directions in blizzards.items():
        x, y = blizzard
        for direction in directions:
            new_x = x
            new_y = y
            if direction == ">":
                new_x = x + 1
                if new_x == width: new_x = 0
            elif direction == "<":
                new_x = x - 1
                if new_x == -1: new_x = width - 1
            elif direction == "v":
                new_y = y + 1
                if new_y == height: new_y = 0
            elif direction == "^":
                new_y = y - 1
                if new_y == -1: new_y = height - 1
            else:
                print(f"shouldn't happen {direction}")
            newPositions[(new_x, new_y)] = newPositions.get((new_x, new_y), []) + [direction]
    return newPositions

def printBlizzards(blizzards):
    global width, height
    for y in range(height):
        for x in range(width):
            if (x, y) in blizzards:
                if len(blizzards[(x, y)]) == 1:
                    print(blizzards[(x, y)][0], end="")
                else:
                    print(len(blizzards[(x, y)]), end="")
            else:
                print(".", end="")
        print()

blizzard_cache = {0: blizzards}
def calc(start, end, starttime=0):
    global width, height, blizzard_cache
    best = 100000000
    todo = deque([(start, starttime)])
    seen = set()
    i = 0
    while todo:
        pos, time = todo.pop()
        i += 1
        if pos == end:
            best = min(time, best)
            # print(f"new best: {best}, remaining: {len(todo)}")
        if (pos, time) in seen:
            continue
        seen.add((pos, time))
        if time >= best:
            continue
        # check manhattan distance if better than best is even possible
        if time + (end[0] - pos[0]) + (end[1] - pos[1]) >= best:
            continue

        time += 1
        if time not in blizzard_cache:
            blizz = moveBlizzards(blizzard_cache[time - 1])
            blizzard_cache[time] = blizz
        else:
            blizz = blizzard_cache[time]

        if pos != start:
            if pos not in blizz: # wait in place
                todo.append((pos, time))
            x, y = pos
            if start == (0, -1):
                if x > 0 and (x - 1, y) not in blizz: # move left
                    todo.append(((x - 1, y), time))
                if y > 0 and (x, y - 1) not in blizz: # move up
                    todo.append(((x, y - 1), time))
                if (y < height - 1 and (x, y + 1) not in blizz) or (x, y + 1) == end: # move down
                    todo.append(((x, y + 1), time))
                if x < width - 1 and (x + 1, y) not in blizz: # move right
                    todo.append(((x + 1, y), time))
            else:
                if x < width - 1 and (x + 1, y) not in blizz: # move right
                    todo.append(((x + 1, y), time))
                if (y < height - 1 and (x, y + 1) not in blizz): # move down
                    todo.append(((x, y + 1), time))
                if y > 0 and (x, y - 1) not in blizz or (x, y - 1) == end: # move up
                    todo.append(((x, y - 1), time))
                if x > 0 and (x - 1, y) not in blizz: # move left
                    todo.append(((x - 1, y), time))
        else:
            if pos not in blizz: # wait in place
                todo.append((pos, time))
            x, y = pos
            if start == (0, -1) and y < height - 1 and (x, y + 1) not in blizz: # move down
                todo.append(((x, y + 1), time))
            if start == (width-1, height) and y > 0 and (x, y - 1) not in blizz: # move up
                todo.append(((x, y - 1), time))

    return best

forward = calc((0, -1), (width - 1, height))
print(forward)
backward = calc((width - 1, height), (0, -1), forward)
forward2 = calc((0, -1), (width - 1, height), backward)
print(forward2)


print("--- %s seconds ---" % (time.time() - start_time))