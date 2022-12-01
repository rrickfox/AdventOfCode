import time
from copy import copy
start_time = time.time()

with open("2.txt") as file:
    data = [int(x) for x in file.read().split(",")]

def intcode(data):
    i = 0
    while True:
        if data[i] == 99: break
        elif data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            i += 4
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i += 4
        else:
            print("Unexpected Opcode")
            break
    return data

def solve(data):
    for x in range(100):
        for y in range(100):
            data[1] = x
            data[2] = y
            if intcode(copy(data))[0] == 19690720:
                return x, y

noun, verb = solve(data)
print(100 * noun + verb)

print("--- %s seconds ---" % (time.time() - start_time))