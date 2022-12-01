import os, sys

with open(os.path.join(sys.path[0], "6.txt"), "r") as file:
    lines = file.readlines()
    input = [int(x) for x in lines[0].strip().split(",")]

x = [len(list(filter(lambda v: v == x, input))) for x in set(input)]
x = [0] + x
fill = [0] * (10 - len(x))
x = x + fill

for i in range(256):
    print(str(i) + ": " + str(x))
    x[9] = x[0]
    resets = x[0]
    for j in range(1, len(x)):
        x[j-1] = x[j]
    x[9] = 0
    x[6] += resets

print(x)
print(sum(x))