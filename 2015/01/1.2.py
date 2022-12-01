import time
start_time = time.time()

with open("1.txt") as file:
	line = file.readline().strip()

for i in range(len(line)+1):
	if line[:i].count("(") - line[:i].count(")") < 0:
		print(i)
		break

print("--- %s seconds ---" % (time.time() - start_time))