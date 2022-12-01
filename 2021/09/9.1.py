import time
start_time = time.time()
with open("9.txt") as file:
	lines = file.readlines()
	lines = [[int(x) for x in line.strip()] for line in lines]


minimaSum = 0
minima = set()

for indexY, line in enumerate(lines):
	for indexX, x in enumerate(line):
		minimum = True;
		if indexY > 0:
			if indexX > 0 and x > lines[indexY-1][indexX-1]:
				minimum = False
			if x > lines[indexY-1][indexX]:
				minimum = False
			if indexX < len(line)-1 and x > lines[indexY-1][indexX+1]:
				minimum = False
		if indexX > 0 and x > line[indexX-1]:
			minimum = False
		if indexX < len(line)-1 and x > line[indexX+1]:
			minimum = False
		if indexY < len(lines)-1:
			if indexX > 0 and x > lines[indexY+1][indexX-1]:
				minimum = False
			if x > lines[indexY+1][indexX]:
				minimum = False
			if indexX < len(line)-1 and x > lines[indexY+1][indexX+1]:
				minimum = False
		if minimum:
			minimaSum += x+1
			minima.add((indexX, indexY))

minimaSum2 = 0
minima2 = set()
for indexY, line in enumerate(lines):
	for indexX, x in enumerate(line):
		minimum = True;
		if indexY > 0 and x >= lines[indexY-1][indexX]:
			minimum = False
		if indexX > 0 and x >= line[indexX-1]:
			minimum = False
		if indexX < len(line)-1 and x >= line[indexX+1]:
			minimum = False
		if indexY < len(lines)-1 and x >= lines[indexY+1][indexX]:
			minimum = False
		if minimum:
			minimaSum2 += x+1
			minima2.add((indexX, indexY))


print(minimaSum)
print(minimaSum2)
print(minima^minima2)

print("--- %s seconds ---" % (time.time() - start_time))