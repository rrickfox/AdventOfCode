# ======== setup ===========
import time
start_time = time.time()
data = open("11.txt").read()

# ======== code =======

def run():
    global octopuses
    octopuses = [x + 1 for x in octopuses]
    flash = {i for i in range(100) if octopuses[i] == 10}
    while flash:
        i = flash.pop()
        for x in [-11, -10, -9, -1, 1, 9, 10, 11]:
            if not (i % 10 == 9 and x % 10 == 1 or i % 10 == 0 and x % 10 == 9 or i + x < 0):
                try: 
                    octopuses[i + x] += 1
                    if octopuses[i + x] == 10: flash.add(i + x)
                except IndexError: pass
    octopuses = [0 if x > 9 else x for x in octopuses]
    return octopuses.count(0)

octopuses = [int(x) for x in data if x != '\n']
print(sum([run() for _ in range(100)]))
octopuses = [int(x) for x in data if x != '\n']
for i in range(1, 10000):
    if run() == 100:
        print(i)
        break

print("--- %s seconds ---" % (time.time() - start_time))