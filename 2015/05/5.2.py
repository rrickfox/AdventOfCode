import time
start_time = time.time()

with open("5.txt") as file:
	lines = [line.strip() for line in file.readlines()]

count = 0
for line in lines:
	doubles = list(zip(enumerate(line[:-1]), line[1:]))
	dic = {}
	for d in doubles:
		dic[d[0][1]+d[1]] = dic.get(d[0][1]+d[1], []) + [d[0][0]]
	a = False
	for d in dic:
		if any(dic[d][i]+2 <= dic[d][i+1] for i in range(len(dic[d])-1)):
			a = True
	if a and any(line[i] == line[i+2] for i in range(len(line)-2)):
		count += 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))