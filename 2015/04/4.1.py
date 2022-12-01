import time
start_time = time.time()
import hashlib

with open("4.txt") as file:
	line = file.readline().strip()

i = 1
while True:
	s = hashlib.md5((line + str(i)).encode()).hexdigest()
	if s.startswith("00000"):
		break
	i += 1

print(i)

print("--- %s seconds ---" % (time.time() - start_time))