import time
start_time = time.time()

with open("11.txt") as file:
	lines = file.readlines()
	lines = [[int(x) for x in line.strip()] for line in lines]

flashcount = 0
count = 0
together = False

while not together:
	lines = [[x+1 for x in line] for line in lines]
	flashes = set()
	for y, line in enumerate(lines):
		for x, val in enumerate(line):
			if val == 10:
				flashes.add((x, y))
	while len(flashes):
		flashcount += len(flashes)
		new = set()
		for point in flashes:
			neighbours = set([(x2, y2) for x2 in range(point[0]-1, point[0]+2) 
									   for y2 in range(point[1]-1, point[1]+2) 
				if (-1<point[0]<=len(line)-1
					and -1<point[1]<=len(lines)-1
					and (point[0]!=x2 or point[1]!=y2)
					and (0<=x2<=len(line)-1)
					and (0<=y2<=len(lines)-1))
			])
			for p in neighbours:
				lines[p[1]][p[0]] += 1
			new.update(set([(p[0], p[1]) for p in neighbours if lines[p[1]][p[0]] == 10]))
		flashes = new
	lines = [[0 if x > 9 else x for x in line] for line in lines]
	together = len(set().union(set([x for line in lines for x in line]))) == 1
	count += 1
	if count == 100:
		print("Flashes after 100 iterations:")
		print(flashcount)

print("First time all are synchronized:")
print(count)

print("--- %s seconds ---" % (time.time() - start_time))