import time
from collections import deque
start_time = time.time()

with open("22.txt", "r") as file:
    lines = [line.strip().split(" ") for line in file.readlines()]

data = [i for i in range(10007)]

for instructions in lines:
    if instructions[0] == "cut":
        cut = int(instructions[1])
        data = data[cut:] + data[:cut]
    elif instructions[1] == "into":
        data.reverse()
    elif instructions[1] == "with":
        increment = int(instructions[3])
        new_data = [None for i in range(len(data))]
        todo = deque(data)
        for i in range(len(new_data)):
            new_data[(i*increment) % len(new_data)] = todo.popleft()
        data = new_data

print(data.index(2019))

print("--- %s seconds ---" % (time.time() - start_time))