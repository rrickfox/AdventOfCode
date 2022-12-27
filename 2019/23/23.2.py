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

    # day 23
    def run_until_io(self):
        output = []
        while True:
            output = self.execute_step(True, -1)
            if output is None or output is True or len(output) > 0:
                break
        return output if not self.halted else None

    def execute_step(self, stop_after_input = False, default_input = None):
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
            elif default_input == None:
                self.set(self.write_parameter(param_mode, 1), int(input(">")))
            else:
                self.set(self.write_parameter(param_mode, 1), default_input)
            self.i += 2
            if stop_after_input:
                return True
        elif opcode == 4:
            param = self.parameters(param_mode, 1)[0]
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

class NetworkNode:
    def __init__(self, data, address, target_address, network):
        self.instance = Intcode(data, [address])
        self.instance.run_until_io()
        self.address = address
        self.target_address = target_address
        self.network = network
        self.packets = []
        self.idle = False

    def run_until_io_or_done(self):
        if self.packets:
            self.instance.inp = [self.packets[0][0]]
        else:
            if len(self.instance.inp) == 0:
                self.instance.input_single(-1)

        out = self.instance.run_until_io()
        if out is True:
            if self.packets:
                _, y = self.packets.pop(0)
                self.instance.input_single(y)
                self.instance.run_until_io()
            else:
                self.idle = True
        else:
            self.idle = False
            dest = out[0]
            x = self.instance.run_until_output()
            y = self.instance.run_until_output()
            if dest == self.target_address:
                return dest, x, y
            self.network[dest].packets.append((x, y))

class NAT:
    def __init__(self, network):
        self.network = network
        self.packet = None
        self.last_y = None

    def network_idle(self):
        return all(n.idle for n in self.network)

    def has_packet(self):
        return self.packet is not None

    def same_y(self):
        return self.packet[1] == self.last_y

    def send_packet(self):
        self.last_y = self.packet[1]
        self.network[0].packets.append(self.packet)
        self.packet = None

with open("23.txt") as file:
    data = [int(x) for x in file.read().split(",")]

instances = []

for i in range(50):
    instances.append(NetworkNode(copy(data), i, 255, instances))

nat = NAT(instances)

while True:
    for instance in instances:
        packet = instance.run_until_io_or_done()
        if packet is not None and packet[0] == 255:
            nat.packet = (packet[1], packet[2])
    if nat.network_idle() and nat.has_packet():
        if nat.same_y():
            print(nat.last_y)
            break
        else:
            nat.last_y = None
        nat.send_packet()

print(f"--- {(time.time() - start_time)} seconds ---")