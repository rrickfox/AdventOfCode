import os, sys, time
start_time = time.time()
with open(os.path.join(sys.path[0], "6.txt"), "r") as file:
    lines = file.readlines()
    inp = [int(x) for x in lines[0].strip().split(",")]

for i in range(80):
    print(str(i) + ": " + str(len(inp)))
    new = []
    for x in inp:
        if x == 0:
            new.append(8)
    inp = list([6 if x == 0 else x-1 for x in inp])
    inp += new

print(len(inp))
print("--- %s seconds ---" % (time.time() - start_time))