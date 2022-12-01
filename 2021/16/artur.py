# import numpy as np
import time, math
start_time = time.time()
data = open("16.txt").readline()

# ======== code =======

def parse() -> tuple:
    global data
    version = int(data[:3], 2)
    packetID = int(data[3:6], 2)
    data = data[6:]
    if packetID == 4:
        value = data[1:5]
        while data[0] != '0':
            data = data[5:]
            value += data[1:5]
        data = data[5:]
        value = [int(value, 2)]
    else:
        if data[0] == '0':
            length = len(data) - int(data[1:16], 2) - 16
            data = data[16:]
            value = []
            while len(data) > length:
                value.append(parse())
        else:
            number = int(data[1:12], 2)
            data = data[12:]
            value = [parse() for _ in range(number)]

    return (version, packetID, value)

def sumversion(packet):
    return 0 if type(packet) == int else packet[0] + sum([sumversion(x) for x in packet[2]])

def calc(packet):
    if type(packet) == int: return packet
    if packet[1] == 0: return sum([calc(x) for x in packet[2]])
    if packet[1] == 1: return math.prod([calc(x) for x in packet[2]])
    if packet[1] == 2: return min([calc(x) for x in packet[2]])
    if packet[1] == 3: return max([calc(x) for x in packet[2]])
    if packet[1] == 5: return calc(packet[2][0]) > calc(packet[2][1])
    if packet[1] == 6: return calc(packet[2][0]) < calc(packet[2][1])
    if packet[1] == 7: return calc(packet[2][0]) == calc(packet[2][1])
    return packet[2][0]


data = (bin(int(data, 16))[2:]).zfill(len(data) * 4)
packet = parse()
print(sumversion(packet))
print(calc(packet))

print("--- %s seconds ---" % (time.time() - start_time))