with open("8.txt") as file:
	lines = file.readlines()
	lines = [x.strip().split(" | ") for x in lines]

lines = [(line[0].split(" "), line[1].split(" ")) for line in lines]

print(sum([1 if len(x) in [2, 4, 3, 7] else 0 for line in lines for x in line[1]]))