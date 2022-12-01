import time
start_time = time.time()

with open("3.txt") as file:
	line = file.readline().strip()

x = y = 0
visited = {(0, 0)}
for c in line:
	if c == "^": y -= 1
	elif c == ">": x += 1
	elif c == "<": x -= 1
	elif c == "v": y += 1
	visited.add((x, y))

print(len(visited))

print("--- %s seconds ---" % (time.time() - start_time))