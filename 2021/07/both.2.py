import time
start_time = time.time()
inp = [int(x) for x in open("7.txt").readline().strip().split(",")]
print(min([sum([abs(x - i) for x in inp]) for i in range(min(inp), max(inp) + 1)]))
print(min([sum([int(abs(x - i)*(abs(x - i) + 1) / 2) for x in inp]) for i in range(min(inp), max(inp) + 1)]))
print("--- %s seconds ---" % (time.time() - start_time))