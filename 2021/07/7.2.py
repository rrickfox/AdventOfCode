import os, sys

with open(os.path.join(sys.path[0], "7.txt"), "r") as file:
    lines = file.readlines()
    inp = [int(x) for x in lines[0].strip().split(",")]

out = min(list([sum(list([(abs(x - i)*(abs(x - i) + 1) / 2) for x in inp])) for i in range(min(inp), max(inp) + 1)]))

print(out)