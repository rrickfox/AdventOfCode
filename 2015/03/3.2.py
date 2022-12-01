import time
start_time = time.time()

with open("3.txt") as file:
	line = file.readline().strip()

x = y = 0
x2 = y2 = 0
visited = {(0, 0)}
turn = True
for c in line:
	if turn:
		if c == "^": y -= 1
		elif c == ">": x += 1
		elif c == "<": x -= 1
		elif c == "v": y += 1
		visited.add((x, y))
	else:
		if c == "^": y2 -= 1
		elif c == ">": x2 += 1
		elif c == "<": x2 -= 1
		elif c == "v": y2 += 1
		visited.add((x2, y2))
	turn = not turn

print(len(visited))

print("--- %s seconds ---" % (time.time() - start_time))