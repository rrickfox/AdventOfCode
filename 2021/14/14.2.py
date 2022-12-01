import time
from collections import Counter
start_time = time.time()

with open("14.txt") as file:
	text, pairs = file.read().split("\n\n")
	pairs = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in pairs.split("\n")}

def run(text, iterations):
	neighbours = {kv[0]:kv[1] for kv in Counter(["".join(x) for x in zip(text, text[1:])]).most_common()}

	for _ in range(iterations):
		new = {}
		for k in neighbours:
			if k[0]+pairs[k] not in new:
				new[k[0]+pairs[k]] = 0
			new[k[0]+pairs[k]] += neighbours[k]
			if pairs[k]+k[1] not in new:
				new[pairs[k]+k[1]] = 0
			new[pairs[k]+k[1]] += neighbours[k]
		neighbours = new

	keycount = {}
	for k in neighbours:
		if k[0] not in keycount:
			keycount[k[0]] = 0
		keycount[k[0]] += neighbours[k]
	keycount[text[-1]] += 1

	return max(keycount.values()) - min(keycount.values())

print(run(text, 10))
print(run(text, 40))

print("--- %s seconds ---" % (time.time() - start_time))