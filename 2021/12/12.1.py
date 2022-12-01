import time
start_time = time.time()

with open("12.txt") as file:
	lines = file.readlines()
	connected = {}
	for line in lines:
		a, b = line.strip().split("-")
		connected[a] = connected.get(a, []) + [b]
		connected[b] = connected.get(b, []) + [a]

print(connected)

def check_neighbours(nextCave: str, done: list):
	if nextCave=="end":
		return [done.append("end")]
	if nextCave.islower() and nextCave in done:
		return []
	result = []
	for cave in connected[nextCave]:
		result += check_neighbours(cave, done+[nextCave])
	return result

print(len(check_neighbours("start", [])))

print("--- %s seconds ---" % (time.time() - start_time))