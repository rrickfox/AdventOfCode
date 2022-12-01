import time, math
start_time = time.time()

with open("14.txt") as file:
    lines = [line.strip().split(" => ") for line in file.readlines()]
    lines = [({x.split(" ")[1]: int(x.split(" ")[0]) for x in line[0].split(", ")}, line[1].split(" ")) for line in lines]
    data = {line[1][1]: (int(line[1][0]), line[0]) for line in lines}

def get_ore(c):
    still_needed = {"FUEL": c}
    in_stock = {}
    ore = 0

    while len(still_needed) > 0:
        key, val = still_needed.popitem()
        produced, needed = data[key]
        val -= in_stock.get(key, 0)
        multiplier = math.ceil(val / produced)
        in_stock[key] = produced * multiplier - val
        for item, quantity in needed.items():
            quantity *= multiplier
            if item == "ORE":
                ore += quantity
                continue
            still_needed[item] = still_needed.get(item, 0) + quantity

    return ore

first = math.floor(10**12 / get_ore(1))
low = first
high = first * 2
for i in range(2, 11):
    if get_ore(i * first) < 10**12:
        low = i * first
        high = (i + 1) * first

while high - low > 100:
    mid = (high + low) // 2
    if get_ore(mid) < 10**12:
        low = mid
    else:
        high = mid

m = low
for i in range(low, high):
    if get_ore(i) < 10**12:
        m = i

print(m)

print("--- %s seconds ---" % (time.time() - start_time))