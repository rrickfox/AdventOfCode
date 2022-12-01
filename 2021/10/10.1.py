import time
start_time = time.time()
with open("10.txt") as file:
	lines = file.readlines()
	lines = [line.strip() for line in lines]

opening = {"(":")", "[":"]", "{":"}", "<":">"}
closing = {")":3, "]":57, "}":1197, ">":25137}

errors = []

for line in lines:
	opened = []
	for char in line:
		if char in opening:
			opened.append(char)
		elif opening[opened[-1]] == char:
			opened.pop() # current closes the last opened chunk
		else: # error
			errors.append(char)
			break

print(errors)
print(sum([closing[x] for x in errors]))

print("--- %s seconds ---" % (time.time() - start_time))