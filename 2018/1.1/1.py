import time
start_time = time.time()

with open("input.txt", "r") as file:
    lines = file.readlines()

data = [int(x) for x in lines]
print(sum(data))
# print(sum(data[:3]))

print("--- %s seconds ---" % (time.time() - start_time))