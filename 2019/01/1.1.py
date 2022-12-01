import time, math
start_time = time.time()

with open("1.txt") as file:
    data = [int(line) for line in file.readlines()]

print(sum([math.floor(x / 3) - 2 for x in data]))

print("--- %s seconds ---" % (time.time() - start_time))