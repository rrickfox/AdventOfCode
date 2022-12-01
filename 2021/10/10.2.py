import time

def get_score(s: str):
	closing = {")":1, "]":2, "}":3, ">":4}
	score = 0
	for c in s:
		score *= 5
		score += closing[opening[c]]
	return score

start_time = time.time()
with open("10.txt") as file:
	lines = file.readlines()
	lines = [line.strip() for line in lines]

opening = {"(":")", "[":"]", "{":"}", "<":">"}

incomplete = []

for line in lines:
	opened = []
	error = False
	for char in line:
		if char in opening:
			opened.append(char)
		elif opening[opened[-1]] == char:
			opened.pop() # current closes the last opened chunk
		else: # error
			error = True
			break
	if error or len(opened) == 0:
		continue
	incomplete.append("".join(reversed(opened)))

print(incomplete)
print((sorted([get_score(x) for x in incomplete])[int((len(incomplete) - 1)/2)]))

print("--- %s seconds ---" % (time.time() - start_time))