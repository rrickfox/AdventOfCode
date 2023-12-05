import time, parse
start_time = time.time()

p = parse.compile("{} {} {}")

with open("05.txt", "r") as file:
    lines = [line.strip() for line in file.read().split("\n\n")]
    seeds = [int(x) for x in parse.parse("seeds: {}", lines[0])[0].split(" ")]
    maps = [{int(x[1]):(int(x[0]), int(x[2])) for line in lines[i].split("\n")[1:] if (x:=p.parse(line))} for i in range(1, 8)]



# for m in maps:
#     new_values = set()
#     for value in seeds:
#         found = False
#         for source, (dest, rang) in m.items():
#             if source <= value < source + rang:
#                 # value is in this range
#                 diff = value - source
#                 new_values.add(dest + diff)
#                 found = True
#         if not found:
#             new_values.add(value)
#     # print(new_values)
#     seeds = new_values

# print(list(sorted(seeds))[0])

new_values = set()
for value in seeds:
    # print("--", value, "--")
    for m in maps:
        for source, (dest, rang) in m.items():
            # print(source, dest, rang)
            if source <= value < source + rang:
                # value is in this range
                diff = value - source
                value = dest + diff
                break
        # print(value)
    new_values.add(value)

print(list(sorted(new_values))[0])

res = 10000000000000000000000000

for n in zip(seeds[::2], seeds[1::2]):
    ranges = [n]
    for m in maps:
        # print(ranges, m)
        new_ranges = []
        while len(ranges) > 0:
            start, length = ranges.pop(0)
            # print("current range:", (start, length))
            anything_done = False
            for source in sorted(m.keys()): # from smallest to largest map range
                dest, rang = m[source]
                # print(source, dest, rang)
                if source <= start < source + rang:
                    # start lies in this range
                    # print("start lies in this range")
                    diff = start - source
                    # print("diff", diff)
                    if rang - diff >= length: # full current tuple fits into range
                        # print("full current tuple")
                        new_ranges.append((dest + diff, length))
                        anything_done = True
                        break
                    else: # current tuple needs to be cut in half
                        # print("current tuple needs")
                        new_ranges.append((dest + diff, rang - diff))
                        # print("new_ranges", (dest + diff, rang - diff))
                        ranges.append((source + rang, length - (rang - diff)))
                        # print("ranges", (source + rang, length - (rang - diff)))
                        anything_done = True
                        break
                elif start <= source < start + length: # some of current range is not in any map
                    # print("source of map lies in current range")
                    diff = source - start
                    new_ranges.append((start, diff))
                    if source + rang <= start + length: # map range is fully in start + length
                        new_ranges.append((dest, rang))
                        if start + length > source + rang:
                            ranges.append((source + rang, (start + length) - (source + rang)))
                            anything_done = True
                            break
                    else: # map range is only partially in start + length, nothing left over
                        new_ranges.append((dest, length - diff))
                        anything_done = True
                        break
            if not anything_done:
                new_ranges.append((start, length))
        ranges = new_ranges
    # print(ranges)
    res = min([x[0] for x in ranges] + [res])

print(res)

print(f"--- {(time.time() - start_time)} seconds ---")