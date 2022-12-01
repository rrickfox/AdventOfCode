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
        global last_direction
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
                d = {"u": 1, "d": 2, "l": 3, "r": 4}
                s = input("(u, d, l, r) >")
                last_direction = d[s]
                self.set(self.write_parameter(param_mode // 100, 1), d[s])
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

with open("15.txt") as file:
    data = [int(x) for x in file.read().split(",")]

instance = Intcode(copy(data))

def pos(x, y, d):
    if d == 1:
        return x, y - 1
    elif d == 2:
        return x, y + 1
    elif d == 3:
        return x - 1, y
    elif d == 4:
        return x + 1, y

def direction(dx, dy):
    if dx == 0 and dy == -1:
        return 1
    elif dx == 0 and dy == 1:
        return 2
    elif dx == -1 and dy == 0:
        return 3
    elif dx == 1 and dy == 0:
        return 4
    return None

todo = {(0, 0): [1, 2, 3, 4]}
path = []
tiles = {}
x = y = 0
last_direction = None
backtracking = False
oxygen = None

while todo:
    if (x, y) in todo:
        d = todo[(x, y)].pop(0)
        if len(todo[(x, y)]) == 0:
            del todo[(x, y)]
    else:
        last = path.pop()
        d = direction(last[0] - x, last[1] - y)
        backtracking = True
    last_direction = d
    instance.input_single(d)
    ret = instance.run_until_output()
    if not instance.halted:
        if ret == 0:
            tiles[pos(x, y, last_direction)] = 1
        elif ret == 1:
            tiles[(x, y)] = 0
            if backtracking:
                backtracking = False
            else:
                path.append((x, y))
            x, y = pos(x, y, last_direction)
            explore = [i for i in range(1, 5) if pos(x, y, i) not in tiles]
            if explore:
                todo[(x, y)] = explore
        elif ret == 2:
            tiles[(x, y)] = 0
            if backtracking:
                backtracking = False
            else:
                path.append((x, y))
            x, y = pos(x, y, last_direction)
            oxygen = (x, y)
            explore = [i for i in range(1, 5) if pos(x, y, i) not in tiles]
            if explore:
                todo[(x, y)] = explore

filled = set()
tobefilled = {oxygen}
steps = -1

while tobefilled:
    n = set()
    for tile in tobefilled:
        for i in range(1, 5):
            p = pos(tile[0], tile[1], i)
            if p not in filled and tiles[p] == 0:
                n.add(p)
    filled = filled.union(tobefilled)
    tobefilled = n
    steps += 1

print(steps)

print("--- %s seconds ---" % (time.time() - start_time))