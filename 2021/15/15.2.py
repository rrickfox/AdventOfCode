import time
start_time = time.time()

with open("15.txt") as file:
	orig_lines = file.readlines()
	orig_lines = [[int(x) for x in line.strip()] for line in orig_lines]

lines = []
for i in range(5):
	for line in orig_lines:
		new_line = []
		for j in range(5):
			new_line += [x+i+j if x+i+j<=9 else (x+i+j)%10+1 for x in line]
		lines.append(new_line)

found = set()
nextInLine = {(0, 0): 0}
end = (len(lines)-1, len(lines[0])-1)

def neighbours(x, y):
	if y > 0 and (x, y-1) not in nextInLine and (x, y-1) not in found:
		nextInLine[(x, y-1)] = nextInLine[(x, y)] + lines[y-1][x]
	if x > 0 and (x-1, y) not in nextInLine and (x-1, y) not in found:
		nextInLine[(x-1, y)] = nextInLine[(x, y)] + lines[y][x-1]
	if y < len(lines)-1 and (x, y+1) not in nextInLine and (x, y+1) not in found:
		nextInLine[(x, y+1)] = nextInLine[(x, y)] + lines[y+1][x]
	if x < len(lines[0])-1 and (x+1, y) not in nextInLine and (x+1, y) not in found:
		nextInLine[(x+1, y)] = nextInLine[(x, y)] + lines[y][x+1]

while len(nextInLine):
	if end in nextInLine:
		print(nextInLine[end])
		break
	current = min(nextInLine, key=nextInLine.get)
	found.add(current)
	neighbours(*current)
	del nextInLine[current]

print("--- %s seconds ---" % (time.time() - start_time))