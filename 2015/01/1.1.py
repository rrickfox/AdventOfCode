import time
start_time = time.time()

with open("1.txt") as file:
	line = file.readline().strip()

print(line.count("(") - line.count(")"))

print("--- %s seconds ---" % (time.time() - start_time))