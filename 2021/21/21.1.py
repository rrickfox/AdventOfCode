import time
start_time = time.time()

with open("21.txt") as file:
	lines = file.readlines()
	p0_pos = int(lines[0].strip()[-1])
	p1_pos = int(lines[1].strip()[-1])

p0_points = 0
p1_points = 0
die = 1
turns = 0

while True:
	if p0_points >= 1000:
		print(p1_points * turns * 3)
		break
	if p1_points >= 1000:
		print(p0_points * turns * 3)
		break
	t = 3 * ((die - 1) % 100 + 1) + 3
	if turns % 2 == 0:
		p0_pos = (p0_pos + t - 1) % 10 + 1
		p0_points += p0_pos
	else:
		p1_pos = (p1_pos + t - 1) % 10 + 1
		p1_points += p1_pos
	die += 3
	turns += 1

print("--- %s seconds ---" % (time.time() - start_time))
