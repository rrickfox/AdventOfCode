import os
import sys

with open(os.path.join(sys.path[0], "3.txt"), "r") as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]

out1 = [0] * len(lines[0]);

for line in lines:
    for index, i in enumerate(line):
        out1[index] += (int(i)-.5)*2

gamma = list(map(lambda v: 1 if v > 0 else 0, out1))
epsilon = list(map(lambda v: 0 if v > 0 else 1, out1))

out = [0] * 2;

gamma.reverse()
epsilon.reverse()

for index, i in enumerate(gamma):
    out[0] += i * 2**index
for index, i in enumerate(epsilon):
    out[1] += i * 2**index

print(out[0] * out[1])