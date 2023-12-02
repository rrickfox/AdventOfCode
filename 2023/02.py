import time, parse, math
start_time = time.time()

p = parse.compile("Game {:d}: {}")
p2 = parse.compile("{:d} {}")

with open("02.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = []
    for line in lines:
        r = p.parse(line)
        data.append((r[0], [{i[1]: i[0] for elem in bag.split(", ") if (i := p2.parse(elem))} for bag in r[1].split("; ")]))

res1 = 0
res2 = 0
for id, bag in data:
    needed = {}
    for showing in bag:
        for ball in showing:
            needed[ball] = max(needed.get(ball, 0), showing[ball])
    if needed.get("red", 0) <= 12 and needed.get("green", 0) <= 13 and needed.get("blue", 0) <= 14:
        res1 += id
    res2 += math.prod(needed.values())

print(res1)
print(res2)

print(f"--- {(time.time() - start_time)} seconds ---")