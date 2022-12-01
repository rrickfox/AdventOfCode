import time, math
start_time = time.time()

with open("14.txt") as file:
    lines = [line.strip().split(" => ") for line in file.readlines()]
    lines = [({x.split(" ")[1]: int(x.split(" ")[0]) for x in line[0].split(", ")}, line[1].split(" ")) for line in lines]
    data = {line[1][1]: (int(line[1][0]), line[0]) for line in lines}

still_needed = {"FUEL": 1}
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

print(ore)

print("--- %s seconds ---" % (time.time() - start_time))