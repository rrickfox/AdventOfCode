import time
from parse import compile
from copy import deepcopy
start_time = time.time()

p = compile("move {} from {} to {}")

with open("5.txt", "r") as file:
    config, lines = file.read().split("\n\n")
    lines = lines.split("\n")

moves = [list(map(int, p.parse(line))) for line in lines]
config = config.split("\n")
count_stacks = int(config[-1][-2])
del config[-1]

stacks = [[] for i in range(count_stacks)]

for line in config:
    for i in range(count_stacks):
        d = line[i*4 + 1]
        if d != " ":
            stacks[i].append(d)

stacks2 = deepcopy(stacks)

for (count, source, target) in moves:
    for i in range(count):
        # part 1
        d = stacks[source-1].pop(0)
        stacks[target-1].insert(0, d)
    # part 2
    d2 = stacks2[source-1][:count]
    del stacks2[source-1][:count]
    stacks2[target-1] = d2 + stacks2[target-1]

print("".join(stacks[i][0] for i in range(count_stacks)))
print("".join(stacks2[i][0] for i in range(count_stacks)))

print("--- %s seconds ---" % (time.time() - start_time))