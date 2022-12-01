import time
start_time = time.time()

with open("16.txt") as file:
    data = [int(x) for x in file.read()]

pattern = (0, 1, 0, -1)

for _ in range(100):
    out = []
    for i in range(len(data)):
        s = 0
        j = -1
        while j < len(data):
            for p in pattern:
                for _ in range(i + 1):
                    if j >= 0 and j < len(data):
                        s += data[j] * p
                    j += 1
        out.append(abs(s) % 10)
    data = out

print("".join([str(x) for x in data[:8]]))

print("--- %s seconds ---" % (time.time() - start_time))