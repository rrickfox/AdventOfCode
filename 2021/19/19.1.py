import time, math
import itertools
from typing import Tuple
start_time = time.time()

with open("19.txt") as file:
	text = file.read().split("\n\n")
	scanners = [[tuple(map(int, line.split(","))) for line in block.split("\n")[1:]] for block in text]

def rotate(beacon: Tuple[int, int, int], deg_inc):
	if deg_inc == 0:
		return (beacon[0], beacon[1], beacon[2])
	elif deg_inc == 1:
		return (-beacon[1], beacon[0], beacon[2])
	elif deg_inc == 2:
		return (-beacon[0], -beacon[1], beacon[2])
	elif deg_inc == 3:
		return (beacon[1], -beacon[0], beacon[2])

def transform(beacons: set):
	ret = [{rotate(beacon, i) for beacon in beacons} for i in range(4)] # z is up
	ret += [{rotate((beacon[0], beacon[2], -beacon[1]), i) for beacon in beacons} for i in range(4)] # z is back
	ret += [{rotate((beacon[0], -beacon[2], beacon[1]), i) for beacon in beacons} for i in range(4)] # z is front
	ret += [{rotate((-beacon[2], beacon[1], beacon[0]), i) for beacon in beacons} for i in range(4)] # z is left
	ret += [{rotate((beacon[2], beacon[1], -beacon[0]), i) for beacon in beacons} for i in range(4)] # z is right
	ret += [{rotate((-beacon[0], beacon[1], -beacon[2]), i) for beacon in beacons} for i in range(4)] # z is down
	return ret

def relative(beacons: set):
	return {x: set(tuple(y[i] - x[i] for i in range(3)) for y in beacons if x != y) for x in beacons}

def check(beacons_fixed, beacons_test):
	for beacons_test_rotated in beacons_test:
		for beacons, beacons_transformed in itertools.product(beacons_fixed, beacons_test_rotated):
			if len(beacons_fixed[beacons] & beacons_transformed) >= 11:
				print("found!")
				print(len(beacons_fixed[beacons] & beacons_transformed))
				return (beacons, beacons_transformed)
	return False

beacons_abs = set(scanners[0])
beacons = relative(beacons_abs)
# print(beacons)
# print(len(beacons))
scanners.pop(0)

while len(scanners):
	print("new while")
	for scanner in scanners:
		print("new scanner")
		result = check(beacons, [relative(x).values() for x in transform(scanner)])
		if result:
			print(result)
			beacons_abs |= {tuple(result[0][i] + y[i] for i in range(3)) for y in result[1]}
			beacons = relative(beacons_abs)
			scanners.remove(scanner)
			break

print(len(beacons))
print(len(set.union(*beacons.values())))

print("\n--- %s seconds ---" % (time.time() - start_time))