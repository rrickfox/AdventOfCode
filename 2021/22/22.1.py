import time
start_time = time.time()

with open("22.txt") as file:
	lines = file.readlines()

onoff = [set(), set()]

for line in lines:
	coords = [(int(xyz.split("=")[1].split("..")[0]), int(xyz.split("=")[1].split("..")[1])) for xyz in line.split(" ")[1].split(",")]
	if -50 <= coords[0][0] and coords[0][1] <= 50 and -50 <= coords[1][0] and coords[1][1] <= 50 and -50 <= coords[2][0] and coords[2][1] <= 50:
		cubes = set([(x, y, z) for x in range(coords[0][0], coords[0][1]+1) for y in range(coords[1][0], coords[1][1]+1) for z in range(coords[2][0], coords[2][1]+1)])
		if line[:2] == "on":
			onoff[0] |= cubes
			onoff[1] -= cubes
		else:
			onoff[1] |= cubes
			onoff[0] -= cubes

print(len([tup for tup in onoff[0]]))

print("--- %s seconds ---" % (time.time() - start_time))
