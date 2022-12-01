import time
start_time = time.time()
with open("11.txt") as file:
	lines = file.readlines()
	lines = [[int(x) for x in line.strip()] for line in lines]

flashcount = 0

for i in range(100):
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
			if point[0] > 0:
				if point[1] > 0:
					lines[point[1]-1][point[0]-1] += 1
					if lines[point[1]-1][point[0]-1] == 10:
						new.add((point[0]-1, point[1]-1))
				lines[point[1]][point[0]-1] += 1
				if lines[point[1]][point[0]-1] == 10:
					new.add((point[0]-1, point[1]))
				if point[1] < len(lines)-1:
					lines[point[1]+1][point[0]-1] += 1
					if lines[point[1]+1][point[0]-1] == 10:
						new.add((point[0]-1, point[1]+1))
			if point[1] > 0:
				lines[point[1]-1][point[0]] += 1
				if lines[point[1]-1][point[0]] == 10:
					new.add((point[0], point[1]-1))
			if point[1] < len(lines)-1:
				lines[point[1]+1][point[0]] += 1
				if lines[point[1]+1][point[0]] == 10:
					new.add((point[0], point[1]+1))
			if point[0] < len(line)-1:
				if point[1] > 0:
					lines[point[1]-1][point[0]+1] += 1
					if lines[point[1]-1][point[0]+1] == 10:
						new.add((point[0]+1, point[1]-1))
				lines[point[1]][point[0]+1] += 1
				if lines[point[1]][point[0]+1] == 10:
					new.add((point[0]+1, point[1]))
				if point[1] < len(lines)-1:
					lines[point[1]+1][point[0]+1] += 1
					if lines[point[1]+1][point[0]+1] == 10:
						new.add((point[0]+1, point[1]+1))
		flashes = new
	lines = [[0 if x > 9 else x for x in line] for line in lines]

print(flashcount)

print("--- %s seconds ---" % (time.time() - start_time))