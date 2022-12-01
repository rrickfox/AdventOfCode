import time
from copy import copy
start_time = time.time()

class Intcode:
    def __init__(self, data, inp = None):
        self.data = data
        self.inp = [] if inp is None else inp
        self.halted = False
        self.i = 0
        self.relative_base = 0
        self.mem = {}

    def input_single(self, inp):
        self.inp.append(inp)

    def get(self, index):
        # print("Get value at " + str(index), end="")
        if index >= len(self.data):
            # print(": " + str(self.mem.get(index, 0)))
            return self.mem.get(index, 0)
        else:
            # print(": " + str(self.data[index]))
            return self.data[index]

    def set(self, index, value):
        # print("Set value " + str(value) + " at index " + str(index))
        if index >= len(self.data):
            self.mem[index] = value
        else:
            self.data[index] = value

    def parameters(self, param_mode, param_count):
        params = []
        for j in range(1, param_count + 1):
            mode = param_mode % 10
            param_mode //= 10
            if mode == 2: # relative mode
                params.append(self.get(self.relative_base + self.get(self.i + j)))
            elif mode == 1: # immediate mode
                params.append(self.get(self.i + j))
            elif mode == 0: # position mode
                params.append(self.get(self.get(self.i + j)))
            else:
                print("Unexpected param mode!")
        return params
    
    def write_parameter(self, param_mode, nth_param):
        if param_mode == 2:
            return self.relative_base + self.get(self.i + nth_param)
        elif param_mode == 0:
            return self.get(self.i + nth_param)
        else:
            print("Can't write in immediate Mode!")

    def run_until_halt(self):
        output = []
        while True:
            ret = self.execute_step()
            if ret is None:
                break
            output += ret
        return output

    def run_until_output(self):
        output = []
        while True:
            output = self.execute_step()
            if output is None or len(output) > 0:
                break
        return output[0] if not self.halted else None

    def execute_step(self):
        output = []
        opcode = self.get(self.i) % 100
        param_mode = self.get(self.i) // 100
        if opcode == 99:
            self.halted = True
            return None
        elif opcode == 1:
            params = self.parameters(param_mode, 2)
            self.set(self.write_parameter(param_mode // 100, 3), params[0] + params[1])
            self.i += 4
        elif opcode == 2:
            params = self.parameters(param_mode, 2)
            self.set(self.write_parameter(param_mode // 100, 3), params[0] * params[1])
            self.i += 4
        elif opcode == 3:
            if len(self.inp) > 0:
                self.set(self.write_parameter(param_mode // 100, 1), self.inp.pop(0))
            else:
                self.set(self.write_parameter(param_mode // 100, 1), int(input(">")))
            self.i += 2
        elif opcode == 4:
            param = self.parameters(param_mode, 1)[0]
            # print(str(param))
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
            self.set(self.write_parameter(param_mode // 100, 3), 1 if params[0] < params[1] else 0)
            self.i += 4
        elif opcode == 8:
            params = self.parameters(param_mode, 2)
            self.set(self.write_parameter(param_mode // 100, 3), 1 if params[0] == params[1] else 0)
            self.i += 4
        elif opcode == 9:
            params = self.parameters(param_mode, 1)
            self.relative_base += params[0]
            self.i += 2
        else:
            print("Unexpected Opcode")
            return None
        return output

with open("11.txt") as file:
    data = [int(x) for x in file.read().split(",")]

panels = {(0, 0): 1}
x = 0
y = 0
direction = 0 # 0:up, 1:right, 2:down, 3:left
steps = 0

instance = Intcode(copy(data))

while not instance.halted:
    steps += 1
    instance.input_single(panels[(x, y)] if (x, y) in panels else 0)
    color = instance.run_until_output()
    turn = instance.run_until_output()
    if not instance.halted:
        panels[(x, y)] = color
        if turn == 0:
            direction -= 1
        else:
            direction += 1
        direction %= 4
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1

min_x = min([p[0] for p in panels.keys()])
max_x = max([p[0] for p in panels.keys()])
min_y = min([p[1] for p in panels.keys()])
max_y = max([p[1] for p in panels.keys()])

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        print("O" if (x, y) in panels and panels[(x, y)] == 1 else " ", end="")
    print()

print("--- %s seconds ---" % (time.time() - start_time))