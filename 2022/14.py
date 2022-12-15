import time
start_time = time.time()

with open("14.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [[tuple(map(int, x.split(","))) for x in line.split(" -> ")] for line in lines]

borders = set()
for line in data:
    for start, stop in zip(line, line[1:]):
        if start[0] == stop[0]:
            if start[1] > stop[1]:
                it = range(stop[1], start[1]+1)
            else:
                it = range(start[1], stop[1]+1)
            l = lambda i, s: (s[0], i)
        else:
            if start[0] > stop[0]:
                it = range(stop[0], start[0]+1)
            else:
                it = range(start[0], stop[0]+1)
            l = lambda i, s: (i, s[1])

        for x in it:
            borders.add(l(x, start))

max_y = max(y[1] for y in borders)

settled = True
settled_sand = set()
while settled:
    sand = (500, 0)
    while True:
        if (sand[0], sand[1]+1) not in borders and (sand[0], sand[1]+1) not in settled_sand:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in borders and (sand[0]-1, sand[1]+1) not in settled_sand:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in borders and (sand[0]+1, sand[1]+1) not in settled_sand:
            sand = (sand[0]+1, sand[1]+1)
        else:
            settled_sand.add(sand)
            break
        if sand[1] > max_y:
            settled = False
            break

print(len(settled_sand))

new_y = max_y + 2
left, right = 500 - new_y - 1, 500 + new_y + 1
for x in range(left, right + 1):
    borders.add((x, new_y))

while (500, 0) not in settled_sand:
    sand = (500, 0)
    while True:
        if (sand[0], sand[1]+1) not in borders and (sand[0], sand[1]+1) not in settled_sand:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in borders and (sand[0]-1, sand[1]+1) not in settled_sand:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in borders and (sand[0]+1, sand[1]+1) not in settled_sand:
            sand = (sand[0]+1, sand[1]+1)
        else:
            settled_sand.add(sand)
            break

print(len(settled_sand))

print("--- %s seconds ---" % (time.time() - start_time))