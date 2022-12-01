import time
from collections import Counter
start_time = time.time()

with open("14.txt") as file:
	text, pairs = file.read().split("\n\n")
	pairs = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in pairs.split("\n")}

for _ in range(10):
	neighbours = [pairs[k] for k in ["".join(x) for x in zip(text, text[1:])]]
	res = [None] * (len(neighbours) + len(text))
	res[::2] = text
	res[1::2] = neighbours
	text = res
	print({kv[0]:kv[1] for kv in Counter(["".join(x) for x in zip(text, text[1:])]).most_common()})
	print(len(text))

# print(text)
keycount = {}
neighbours = {kv[0]:kv[1] for kv in Counter(["".join(x) for x in zip(text, text[1:])]).most_common()}
for k in neighbours:
	if k[0] not in keycount:
		keycount[k[0]] = 0
	keycount[k[0]] += neighbours[k]
keycount[text[-1]] += 1
print(max(keycount.values()) - min(keycount.values()))

counter = Counter(text)
print(counter.most_common(1)[0][1] - counter.most_common()[-1][1])

print("--- %s seconds ---" % (time.time() - start_time))