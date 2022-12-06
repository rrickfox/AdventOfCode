import time
start_time = time.time()

with open("6.txt", "r") as file:
    data = file.read().strip()

for i in range(len(data) - 4):
    s = set(data[i:i+4])
    if len(s) == 4:
        print(i+4)
        break

for i in range(len(data) - 14):
    s = set(data[i:i+14])
    if len(s) == 14:
        print(i+14)
        break

print("--- %s seconds ---" % (time.time() - start_time))