import time, math
start_time = time.time()

with open("20.txt") as file:
	text = file.read().split("\n\n")
	algo = text[0]
	lines = text[1].split("\n")

outside = "."

def neighbours(ox, oy):
	return "".join(["0" if get_lines(ox + x, oy + y) == "." else "1" for y in [-1, 0, 1] for x in [-1, 0, 1]])

def get_lines(x, y):
	t = lines[y] if y >= 0 and y < len(lines) else []
	return t[x] if x >= 0 and x < len(t) else outside

for i in range(2):
	new = []
	for y in range(-1, len(lines)+1):
		temp = ""
		for x in range(-1, len(lines[0])+1):
			temp += algo[int(neighbours(x, y), 2)]
		new.append(temp)
	outside = algo[int(9*("0" if outside == "." else "1"), 2)]
	lines = new

for line in lines:
	print(line)

print(sum([sum([0 if c == "." else 1 for c in line]) for line in lines]))

print("--- %s seconds ---" % (time.time() - start_time))