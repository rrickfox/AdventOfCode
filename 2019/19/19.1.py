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

    def reset(self, data, inp = None):
        self.__init__(data, inp)

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
                # print("inputting: " + str(self.inp[0]))
                # print("instruction (i = " + str(self.i) + "): " + str(self.data[self.i]) + " " + str(self.data[self.i + 1]))
                # print("relative base" + str(self.relative_base) + ", param_mode")
                self.set(self.write_parameter(param_mode, 1), self.inp.pop(0))
            else:
                s = int(input(">"))
                # print("inputting: " + str(s))
                self.set(self.write_parameter(param_mode, 1), s)
            self.i += 2
        elif opcode == 4:
            param = self.parameters(param_mode, 1)[0]
            # if param < 128:
            #     print(chr(param), end="")
            # else:
            #     print(param)
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

with open("19.txt") as file:
    data = [int(x) for x in file.read().split(",")]

instance = Intcode(copy(data))

count = 0
for y in range(50):
    for x in range(50):
        instance.reset(copy(data), [x, y])
        if instance.run_until_output() == 1:
            print("#", end="")
            count += 1
        else:
            print(" ", end="")
    print()

print(count)

print("--- %s seconds ---" % (time.time() - start_time))