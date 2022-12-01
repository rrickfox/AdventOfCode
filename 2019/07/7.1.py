import time
from copy import copy
from itertools import permutations
start_time = time.time()

with open("7.txt") as file:
    data = [int(x) for x in file.read().split(",")]

def parameters(data, i, param_mode, param_count):
    params = []
    for j in range(1, param_count + 1):
        mode = param_mode % 10
        param_mode //= 10
        if mode == 1: # immediate mode
            params.append(data[i + j])
        elif mode == 0: # position mode
            params.append(data[data[i + j]])
        else:
            print("Unexpected param mode!")
    return params

def intcode(data, inp = []):
    i = 0
    output = []
    while True:
        opcode = data[i] % 100
        param_mode = data[i] // 100
        if opcode == 99: break
        elif opcode == 1:
            params = parameters(data, i, param_mode, 2)
            data[data[i + 3]] = params[0] + params[1]
            i += 4
        elif opcode == 2:
            params = parameters(data, i, param_mode, 2)
            data[data[i + 3]] = params[0] * params[1]
            i += 4
        elif opcode == 3:
            if len(inp) > 0:
                data[data[i + 1]] = inp.pop(0)
            else:
                data[data[i + 1]] = int(input(">"))
            i += 2
        elif opcode == 4:
            param = parameters(data, i, param_mode, 1)[0]
            print(str(param))
            output.append(param)
            i += 2
        elif opcode == 5:
            params = parameters(data, i, param_mode, 2)
            if params[0] != 0:
                i = params[1]
            else:
                i += 3
        elif opcode == 6:
            params = parameters(data, i, param_mode, 2)
            if params[0] == 0:
                i = params[1]
            else:
                i += 3
        elif opcode == 7:
            params = parameters(data, i, param_mode, 2)
            data[data[i + 3]] = 1 if params[0] < params[1] else 0
            i += 4
        elif opcode == 8:
            params = parameters(data, i, param_mode, 2)
            data[data[i + 3]] = 1 if params[0] == params[1] else 0
            i += 4
        else:
            print("Unexpected Opcode")
            break
    return data, output

m = 0

for perm in permutations(range(5)):
    val = 0
    for i in perm:
        _, ret = intcode(copy(data), [i, val])
        val = ret[0]
    m = max(m, val)

print()
print(m)

print("--- %s seconds ---" % (time.time() - start_time))