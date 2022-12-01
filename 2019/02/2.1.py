import time
start_time = time.time()

with open("2.txt") as file:
    data = [int(x) for x in file.read().split(",")]

data[1] = 12
data[2] = 2

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

print(data[0])

print("--- %s seconds ---" % (time.time() - start_time))