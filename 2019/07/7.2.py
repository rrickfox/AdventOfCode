import time
from copy import copy
from itertools import permutations
start_time = time.time()

class Intcode:
    def __init__(self, data, inp = None):
        self.data = data
        self.inp = [] if inp is None else inp
        self.halted = False
        self.i = 0

    def input_single(self, inp):
        self.inp.append(inp)

    def parameters(self, param_mode, param_count):
        params = []
        for j in range(1, param_count + 1):
            mode = param_mode % 10
            param_mode //= 10
            if mode == 1: # immediate mode
                params.append(self.data[self.i + j])
            elif mode == 0: # position mode
                params.append(self.data[self.data[self.i + j]])
            else:
                print("Unexpected param mode!")
        return params

    def run_until_halt(self):
        output = []
        while True:
            ret = self.execute_step()
            if not ret:
                break
            output += ret
        return output

    def run_until_output(self):
        output = []
        while True:
            output = self.execute_step()
            if output is None or len(output) > 0:
                break
        return output

    def execute_step(self):
        output = []
        opcode = self.data[self.i] % 100
        param_mode = self.data[self.i] // 100
        if opcode == 99:
            self.halted = True
            return None
        elif opcode == 1:
            params = self.parameters(param_mode, 2)
            # print(self.data)
            self.data[self.data[self.i + 3]] = params[0] + params[1]
            self.i += 4
        elif opcode == 2:
            params = self.parameters(param_mode, 2)
            self.data[self.data[self.i + 3]] = params[0] * params[1]
            self.i += 4
        elif opcode == 3:
            if len(self.inp) > 0:
                self.data[self.data[self.i + 1]] = self.inp.pop(0)
            else:
                self.data[self.data[self.i + 1]] = int(input(">"))
            self.i += 2
        elif opcode == 4:
            param = self.parameters(param_mode, 1)[0]
            print(str(param))
            output.append(param)
            self.i += 2
        elif opcode == 5:
            params = self.parameters(param_mode, 2)
            if params[0] != 0:
                self.i = params[1]
            else:
                self.i += 3
        elif opcode == 6:
            params = self.parameters(param_mode, 2)
            if params[0] == 0:
                self.i = params[1]
            else:
                self.i += 3
        elif opcode == 7:
            params = self.parameters(param_mode, 2)
            self.data[self.data[self.i + 3]] = 1 if params[0] < params[1] else 0
            self.i += 4
        elif opcode == 8:
            params = self.parameters(param_mode, 2)
            self.data[self.data[self.i + 3]] = 1 if params[0] == params[1] else 0
            self.i += 4
        else:
            print("Unexpected Opcode")
            return None
        return output

with open("7.txt") as file:
    data = [int(x) for x in file.read().split(",")]

m = 0

for perm in permutations(range(5, 10)):
    instances = [Intcode(copy(data), [i]) for i in perm]
    val = 0
    while not any([x.halted for x in instances]):
        for x in instances:
            x.input_single(val)
            out = x.run_until_output()
            if not x.halted:
                val = out[0]
    m = max(m, val)

print()
print(m)

print("--- %s seconds ---" % (time.time() - start_time))