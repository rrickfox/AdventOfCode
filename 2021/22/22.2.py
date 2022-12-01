import time
start_time = time.time()

with open("22.txt") as file:
	lines = file.readlines()

def calc_intersection(coords1, coords2):
	maxX = max(coords1[0][0], coords2[0][0])
	maxY = max(coords1[1][0], coords2[1][0])
	maxZ = max(coords1[2][0], coords2[2][0])
	minX = min(coords1[0][1], coords2[0][1])
	minY = min(coords1[1][1], coords2[1][1])
	minZ = min(coords1[2][1], coords2[2][1])
	if maxX <= minX and maxY <= minY and maxZ <= minZ:
		return (maxX, minX), (maxY, minY), (maxZ, minZ)
	return False

cubes = {}

for line in lines:
	coords = tuple([(int(xyz.split("=")[1].split("..")[0]), int(xyz.split("=")[1].split("..")[1])) for xyz in line.split(" ")[1].split(",")])
	
	new = {}
	for cube in cubes:
		i = calc_intersection(cube, coords)
		if i:
			new[i] = (new[i] if i in new else cubes.get(i, 0)) - cubes[cube]
	
	cubes = cubes | new

	if line[:2] == "on":
		cubes[coords] = 1

print(sum((coords[0][1]-coords[0][0]+1)*(coords[1][1]-coords[1][0]+1)*(coords[2][1]-coords[2][0]+1)*sign for coords, sign in cubes.items()))

print("--- %s seconds ---" % (time.time() - start_time))
