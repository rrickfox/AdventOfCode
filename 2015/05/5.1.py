import time
start_time = time.time()

with open("5.txt") as file:
	lines = [line.strip() for line in file.readlines()]

count = 0
for line in lines:
	if any(x in line for x in {"ab", "cd", "pq", "xy"}): continue
	if sum(line.count(x) for x in "aeiou") >= 3 and any(line[i] == line[i+1] for i in range(len(line)-1)):
		count += 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))