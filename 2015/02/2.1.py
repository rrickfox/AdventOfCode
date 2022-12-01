import time
start_time = time.time()

with open("2.txt") as file:
	lines = [tuple(map(int, line.strip().split("x"))) for line in file.readlines()]

s = 0
for line in lines:
	sort = sorted(line)
	s += 2 * (sort[0]*sort[1] + sort[1]*sort[2] + sort[0]*sort[2])
	s += sort[0]*sort[1]

print(s)

print("--- %s seconds ---" % (time.time() - start_time))