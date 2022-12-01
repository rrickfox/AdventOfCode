import time
start_time = time.time()

with open("16.txt") as file:
    data = [int(x) for x in file.read()]

data = (data * 10000)[int("".join([str(x) for x in data[:7]])):]

for _ in range(100):
    s = 0
    for i in range(len(data)-1, -1, -1):
        s = (s + data[i]) % 10
        data[i] = s

print("".join([str(x) for x in data[:8]]))

print("--- %s seconds ---" % (time.time() - start_time))