import time
from copy import copy
from collections import deque
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
        if index >= len(self.data):
            return self.mem.get(index, 0)
        else:
            return self.data[index]

    def set(self, index, value):
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
                self.set(self.write_parameter(param_mode, 1), self.inp.pop(0))
            else:
                self.set(self.write_parameter(param_mode, 1), int(input(">")))
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

with open("21.txt") as file:
    data = [int(x) for x in file.read().split(",")]

# instructions = "NOT B J\nAND C J\nWALK\n"
# instructions = "NOT A J\nNOT B T\nAND T J\nNOT C T\nAND T J\nAND D J\nWALK\n"
# instructions = "NOT D J\nWALK\n"

# instructions = "NOT C J\nAND D J\nNOT A T\nOR T J\nWALK\n" # Found on reddit afterwards
instructions = "OR A T\nAND C T\nNOT T J\nAND D J\nWALK\n"

inp = [ord(s) for s in instructions]
instance = Intcode(copy(data), inp)
out = instance.run_until_halt()
for c in out:
    if c <= 127:
        print(chr(c), end="")
    else:
        print(c)

# this code calculates the working instruction in ~15 minutes

# instructions = ["AND", "OR", "NOT"]
# first = ["A", "B", "C", "D", "T", "J"]
# second = ["T", "J"]

# todo = deque()
# seen = set()
# for instruction in instructions:
#     for a in first:
#         for b in second:
#             todo.append(([f"{instruction} {a} {b}\n"], 0))
# topdepth = 0
# while todo:
#     current, depth = todo.popleft()
    
#     if depth > topdepth:
#         print(depth, current, len(todo))
#         topdepth = depth

#     t = "".join(current)
#     if t in seen:
#         continue
#     seen.add(t)

#     inp = [ord(s) for s in t+"WALK\n"]
#     instance = Intcode(copy(data), inp)
#     out = instance.run_until_halt()

#     if len(out) >= 35 and out[34] <= 127 and chr(out[34]) == "D":
#         # print(depth)
#         pass
#     else:
#         print(current)
#         for s in out:
#             if s <= 127:
#                 print(chr(s), end="")
#             else:
#                 print(s)
#         break

#     if len(current) <= 15:
#         for instruction in instructions:
#             for a in first:
#                 for b in second:
#                     if f"{instruction} {a} {b}\n" != current[-1]:
#                         todo.append((current + [f"{instruction} {a} {b}\n"], depth + 1))

print("--- %s seconds ---" % (time.time() - start_time))