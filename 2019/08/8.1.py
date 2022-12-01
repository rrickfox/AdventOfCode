import time
start_time = time.time()

with open("8.txt") as file:
    data = []
    f = list(file.read())
    while len(f) > 0:
        layer = []
        for _ in range(6):
            layer.append([int(x) for x in f[:25]])
            del f[:25]
        data.append(layer)

count_zeros = [sum([sum([1 if x == 0 else 0 for x in y]) for y in layer]) for layer in data]
index = count_zeros.index(min(count_zeros))

print(sum([sum([1 if x == 1 else 0 for x in y]) for y in data[index]]) * sum([sum([1 if x == 2 else 0 for x in y]) for y in data[index]]))

print("--- %s seconds ---" % (time.time() - start_time))