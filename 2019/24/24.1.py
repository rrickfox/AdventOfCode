import time
start_time = time.time()

with open("24.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

data = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            data.add((x, y))

def step():
    global data
    new_data = set()
    for x, y in ((x, y) for y in range(5) for x in range(5)):
        neighbours = sum((x+dx, y+dy) in data for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)))
        if (x, y) in data and neighbours == 1:
            new_data.add((x, y))
        elif (x, y) not in data and (neighbours == 1 or neighbours == 2):
            new_data.add((x, y))
    data = new_data

def print_data():
    global data
    for y in range(5):
        for x in range(5):
            print("#" if (x, y) in data else ".", end="")
        print()

def hash():
    global data
    exp = 0
    ret = 0
    for y in range(5):
        for x in range(5):
            if (x, y) in data:
                ret += 2**exp
            exp += 1
    return ret

seen = set()
while True:
    h = hash()
    if h in seen:
        print(h)
        break
    seen.add(h)
    step()

print(f"--- {(time.time() - start_time)} seconds ---")