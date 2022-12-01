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

image = []
for y in range(6):
    row = []
    for x in range(25):
        pixel = 2
        for layer in data:
            if layer[y][x] != 2:
                pixel = layer[y][x]
                break
        row.append(pixel)
    image.append(row)

for y in image:
    print("".join([" " if x == 0 else "O" for x in y]))

print("--- %s seconds ---" % (time.time() - start_time))