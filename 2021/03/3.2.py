import sys
import os

filename = "3.txt"

with open(os.path.join(sys.path[0], filename), "r") as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]

gamma = lines

for i in range(len(gamma[0])):
    mostBit = 0
    for line in gamma:
        mostBit += (int(line[i])-.5)*2
    sigBit = 1 if mostBit >= 0 else 0;
    gamma = list(filter(lambda v: int(v[i]) == sigBit, gamma))
    if len(gamma) == 1:
        break

gamma = list(map(int, gamma[0]))
gamma.reverse()

epsilon = lines

for i in range(len(epsilon[0])):
    mostBit = 0
    for line in epsilon:
        mostBit += (int(line[i])-.5)*2
    sigBit = 0 if mostBit >= 0 else 1;
    epsilon = list(filter(lambda v: int(v[i]) == sigBit, epsilon))
    if len(epsilon) == 1:
        break

epsilon = list(map(int, epsilon[0]))
epsilon.reverse()

out = [0]*2;

for index, i in enumerate(gamma):
    out[0] += i * 2**index
for index, i in enumerate(epsilon):
    out[1] += i * 2**index

print(out[0] * out[1])