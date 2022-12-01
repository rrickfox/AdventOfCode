import time
start_time = time.time()

with open("24.txt") as file:
	lines = [line.split() for line in file.readlines()]
	inp = [(int(lines[i+4][-1]), int(lines[i+5][-1]), int(lines[i+15][-1])) for i in range(0, len(lines), 18)]
	print(inp)

def operation(a, b, c, z, w):
	if (z % 26 + b) != w:
		z = z // a * 26 + w + c
	else:
		z = z // a
	return z

z_dict = {0: 0}
for working_digit, p in enumerate(inp):
	new_z_dict = {}
	for old_z, num in z_dict.items():
		for digit in range(9, 0, -1):
			new_z = operation(*p, old_z, digit)

			# only add if in beginning or at end and z is actually getting smaller
			if p[0] == 1 or (p[0] == 26 and new_z < old_z):
				new_z_dict[new_z] = max(new_z_dict.get(new_z, num*10+digit), num*10+digit)

	z_dict = new_z_dict
	print("Digit " + str(working_digit + 1) + ", count of z values: " + str(len(z_dict)))

print(z_dict[0])

print("--- %s seconds ---" % (time.time() - start_time))