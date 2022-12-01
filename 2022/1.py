import time
start_time = time.time()

with open("1.txt", "r") as file:
    lines = file.read().split("\n\n")

data = [sum([int(x) for x in line.split("\n")]) for line in lines]
data.sort(reverse=True)
print(data[0])
print(sum(data[:3]))

print("--- %s seconds ---" % (time.time() - start_time))