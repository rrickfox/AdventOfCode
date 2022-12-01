import time
start_time = time.time()
from copy import copy

with open("25.txt") as file:
	lines = [list(line.strip()) for line in file.readlines()]

height = len(lines)
width = len(lines[0])

def move_to(c, pos):
	if c == ">": return (pos + 1) % width
	if c == "v": return (pos + 1) % height
	return None

moved = True
count = 0

while moved:
	count += 1
	# print("Beginning")
	moved = False
	new = []
	for y, line in enumerate(lines):
		# print()
		new_line = copy(line)
		for x, c in enumerate(line):
			if c in {".", "v"}: continue
			# print(c)
			# print(line)
			nx = move_to(c, x)
			# print(nx)
			# print(line[nx])
			if line[nx] == ".":
				# print("moving")
				new_line[nx] = ">"
				new_line[x] = "."
				moved = True
		# print(new_line)
		new.append(new_line)
		del new_line
	lines = new
	del new

	new_columns = []
	for x, column in enumerate(zip(*lines)):
		column = list(column)
		# print(column)
		new_column = copy(column)
		for y, c in enumerate(column):
			# print("char: "+ str(c))
			if c in {".", ">"}: continue
			ny = move_to(c, y)
			if column[ny] == ".":
				new_column[ny] = "v"
				new_column[y] = "."
				moved = True
		new_columns.append(new_column)
		del new_column
	lines = [list(a) for a in zip(*new_columns)]
	del new_columns

	# for line in lines:
	# 	print("".join(line))

print(count)

print("--- %s seconds ---" % (time.time() - start_time))