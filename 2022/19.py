import time, parse
from collections import deque
start_time = time.time()

p = parse.compile("Blueprint {}: Each ore robot costs {} ore. Each clay robot costs {} ore. Each obsidian robot costs {} ore and {} clay. Each geode robot costs {} ore and {} obsidian.")

with open("19.txt", "r") as file:
    lines = [list(map(int, p.parse(line.strip()))) for line in file.readlines()]
    data = [[line[1], line[2], (line[3], line[4]), (line[5], line[6])] for line in lines]

def calc(rob, cost, res, time_start):
    done = set()
    todo = deque([(*rob, *res, time_start)])
    best_geode = 0
    r1cost, r2cost, (r3costOre, r3costClay), (r4costOre, r4costObs) = cost
    maxOre = max([r1cost, r2cost, r3costOre, r4costOre])
    while todo:
        r1, r2, r3, r4, res1, res2, res3, res4, remaining_time = todo.popleft()

        best_geode = max(best_geode, res4)

        if remaining_time == 0 or best_geode > res4 + remaining_time*r4 + (remaining_time*(remaining_time-1))/2:
            continue


        # clamp resources (if we have 5 robots, 10 minutes left and can spend 10 per minute, the maximum number of resources we need now is 45 (10*10)-(9*5))
        if res1 >= remaining_time * maxOre - (remaining_time - 1) * r1:
            res1 = remaining_time * maxOre - (remaining_time - 1) * r1
        if res2 >= remaining_time * r3costClay - (remaining_time - 1) * r2:
            res2 = remaining_time * r3costClay - (remaining_time - 1) * r2
        if res3 >= remaining_time * r4costObs - (remaining_time - 1) * r3:
            res3 = remaining_time * r4costObs - (remaining_time - 1) * r3
        
        if (r1, r2, r3, r4, res1, res2, res3, res4, remaining_time) in done:
            continue
        done.add((r1, r2, r3, r4, res1, res2, res3, res4, remaining_time))
        
        # if len(done) % 1000000 == 0:
        #     print(f"t: {remaining_time}, best: {best_geode}, done: {len(done)}")
        #     print("--- %s seconds ---" % (time.time() - start_time))

        todo.append((r1, r2, r3, r4, res1 + r1, res2 + r2, res3 + r3, res4 + r4, remaining_time - 1))

        # buy and also clamp robots (no need for 5 ore robots if we can only spend 4 ore per minute)
        if res1 >= r1cost and r1 < maxOre:
            todo.append((r1 + 1, r2, r3, r4, res1 + r1 - r1cost, res2 + r2, res3 + r3, res4 + r4, remaining_time - 1))
        if res1 >= r2cost and r2 < r3costClay:
            todo.append((r1, r2 + 1, r3, r4, res1 + r1 - r2cost, res2 + r2, res3 + r3, res4 + r4, remaining_time - 1))
        if res1 >= r3costOre and res2 >= r3costClay and r3 < r4costObs:
            todo.append((r1, r2, r3 + 1, r4, res1 + r1 - r3costOre, res2 + r2 - r3costClay, res3 + r3, res4 + r4, remaining_time - 1))
        if res1 >= r4costOre and res3 >= r4costObs:
            todo.append((r1, r2, r3, r4 + 1, res1 + r1 - r4costOre, res2 + r2, res3 + r3 - r4costObs, res4 + r4, remaining_time - 1))

    return best_geode

res = 0
for i, cost in enumerate(data):
    c = calc((1, 0, 0, 0), cost, (0, 0, 0, 0), 24)
    res += (i+1) * c

print(res)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

res = 1
for cost in data[:3]:
    c = calc((1, 0, 0, 0), cost, (0, 0, 0, 0), 32)
    res *= c

print(res)

print("--- %s seconds ---" % (time.time() - start_time))