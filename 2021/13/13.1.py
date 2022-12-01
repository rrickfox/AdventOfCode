import time
start_time = time.time()

with open("13.txt") as file:
	dots, folds = file.read().split("\n\n")
	dots = [[int(x) for x in line.split(",")] for line in dots.split("\n")]
	# print(dots)
	folds = [(line.split("=")[0][-1], int(line.split("=")[1])) for line in folds.split("\n")]
	# print(folds)

maxX = max([v[0] for v in dots])
maxY = max([v[1] for v in dots])

sheet = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]

for dot in dots:
	sheet[dot[1]][dot[0]] += 1

fold = folds[0]
for y, line in enumerate(sheet):
	if sum(line):
		sheet[y] = [1 if line[x] or (fold[1]*2-x < len(line) and line[fold[1]*2-x]) else 0 for x in range(fold[1])]
	else:
		sheet[y] = [0]*fold[1]

print(sum([sum(line) for line in sheet]))

print("--- %s seconds ---" % (time.time() - start_time))