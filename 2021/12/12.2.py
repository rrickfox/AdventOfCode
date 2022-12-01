import time
start_time = time.time()

with open("12.txt") as file:
	lines = file.readlines()
	connected = {}
	for line in lines:
		a,b = line.strip().split("-")
		connected[a] = connected.get(a, []) + [b]
		connected[b] = connected.get(b, []) + [a]

print(connected)

def check_neighbours(nextCave: str, done: list, canBeTwice = False):
	if nextCave=="end":
		return 1
	if nextCave.islower() and nextCave in done:
		if nextCave == "start" or not canBeTwice:
			return 0
		canBeTwice = False
	result = 0
	for cave in connected[nextCave]:
		result += check_neighbours(cave, done+[nextCave], canBeTwice)
	return result

print(check_neighbours("start", []))
print(check_neighbours("start", [], True))

print("--- %s seconds ---" % (time.time() - start_time))