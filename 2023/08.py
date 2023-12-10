import time, parse, math
from itertools import cycle
start_time = time.time()

p = parse.compile("{} = ({}, {})")

with open("08.txt", "r") as file:
    lines = [line.strip() for line in file.read().split("\n\n")]
    instructions = [1 if c == "R" else 0 for c in lines[0].strip()]
    data : dict[str, tuple[str, str]] = {x[0]:(x[1], x[2]) for line in lines[1].split("\n") if (x := p.parse(line))}

pos = "AAA"
steps = 0

for i in cycle(instructions):
    if pos == "ZZZ": break
    pos = data[pos][i]
    steps += 1

print(steps)

positions = [k for k in data.keys() if k.endswith("A")]
num_steps = []
for k in positions:
    steps = 0
    for i in cycle(instructions):
        if k.endswith("Z"): break
        k = data[k][i]
        steps += 1
    num_steps.append(steps)

print(math.lcm(*num_steps))

print(f"--- {(time.time() - start_time)} seconds ---")