import time
start_time = time.time()

with open("10.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

value = 1
result = 0
curr = None
timeSinceLast = 0
out = ""
for i in range(1, 241):
    if curr == None:
        curr = data.pop(0)
        timeSinceLast = 0
    if i in {20, 60, 100, 140, 180, 220}:
        # print(i)
        # print(value)
        result += i * value
    if (i-1) % 40 in {value, value - 1, value + 1}: # middle, left, right block of sprite
        out += "#"
    else:
        out += " "
    if timeSinceLast == 0:
        if curr == "noop":
            curr = None
    elif timeSinceLast == 1:
        add = int(curr.split(" ")[1])
        value += add
        curr = None
    timeSinceLast += 1

print(result)
print("\n".join(out[i:i+40] for i in range(0, len(out), 40)))

print("--- %s seconds ---" % (time.time() - start_time))