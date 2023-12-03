import time
start_time = time.time()

with open("03.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

num = 0
for y, line in enumerate(lines):
    currentNum = ""
    isValid = False
    for x, char in enumerate(line):
        if char.isnumeric():
            currentNum += char
            isValid = isValid or any([lines[y+dy][x+dx] not in "0123456789." for dx, dy in [(0, -1), (-1, 0), (0, 1), (-1, -1), (-1, 1)] if 0 <= x+dx < len(line) and 0 <= y+dy < len(lines)])
        elif char == ".":
            if currentNum != "":
                isValid = isValid or any([lines[y+dy][x+dx] not in "0123456789." for dx, dy in [(0, -1), (-1, 0), (0, 1), (-1, -1), (-1, 1)] if 0 <= x+dx < len(line) and 0 <= y+dy < len(lines)])
                # print(currentNum, isValid)
                if isValid:
                    num += int(currentNum)
                currentNum = ""
                isValid = False
        else:
            if currentNum != "":
                # print(currentNum, True)
                num += int(currentNum)
                currentNum = ""
                isValid = False
    if currentNum != "":
        # print(currentNum, isValid)
        if isValid:
            num += int(currentNum)
        currentNum = ""
        isValid = False

print(num)

num = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "*":
            starting_points = set()
            neighbours = [(x+dx, y+dy) for (dx, dy) in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] if 0 <= x+dx < len(line) and 0 <= y+dy < len(lines)]
            for nx, ny in neighbours:
                if not lines[ny][nx].isnumeric():
                    continue
                while True:
                    if not lines[ny][nx].isnumeric():
                        starting_points.add((nx + 1, ny))
                        break;
                    if nx == 0:
                        starting_points.add((nx, ny))
                        break;
                    else:
                        nx -= 1
            if len(starting_points) == 2:
                n = 1
                for nx, ny in starting_points:
                    v = ""
                    print(nx, ny)
                    while nx < len(lines[0]) and lines[ny][nx].isnumeric():
                        v += lines[ny][nx]
                        nx += 1
                    n *= int(v)
                num += n

print(num)

print(f"--- {(time.time() - start_time)} seconds ---")