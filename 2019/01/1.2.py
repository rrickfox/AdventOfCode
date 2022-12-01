import time, math
start_time = time.time()

with open("1.txt") as file:
    data = [int(line) for line in file.readlines()]

s = 0
for x in data:
    a = math.floor(x / 3) - 2
    s += a
    a = math.floor(a / 3) - 2
    while a > 0:
        s += a
        a = math.floor(a / 3) - 2

print(s)

print("--- %s seconds ---" % (time.time() - start_time))