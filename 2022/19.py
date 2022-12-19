import time, parse
start_time = time.time()

p = parse.compile("Blueprint {}: Each ore robot costs {} ore. Each clay robot costs {} ore. Each obsidian robot costs {} ore and {} clay. Each geode robot costs {} ore and {} obsidian.")

with open("19.txt", "r") as file:
    lines = [list(map(int, p.parse(line.strip()))) for line in file.readlines()]
    data = [[[line[1], 0, 0], [line[2], 0, 0], [line[3], line[4], 0], [line[5], 0, line[6]]] for line in lines]

def sum_vector(a, b, neg = False):
    if neg: return [sum(x) for x in zip(a,(-x for x in b))]
    return [sum(x) for x in zip(a,b)]

def calc(rob, cost, res, time_start):
    maxes = [max(x) for x in zip(*cost)]
    done = set()
    todo = [(rob, res, time_start)]
    best_geode = 0
    while len(todo):
        robots, resources, remaining_time = todo.pop(0)

        # best_geode = max(best_geode, resources[-1])
        if resources[-1] > best_geode:
            best_geode = resources[-1]
            # print(f"new best: {best_geode}")
        if remaining_time == 0:
            continue

        # clamp robots (no need for 5 ore robots if we can only spend 4 ore per minute)
        # robots = list(robots)
        # for i in range(3):
        #     if robots[i] > maxes[i]:
        #         robots[i] = maxes[i]
        # robots = tuple(robots)

        # clamp resources (if we have 5 robots, 10 minutes left and can spend 10 per minute, the maximum number of resources we need now is 45 (10*10)-(9*5))
        resources = list(resources)
        if resources[0] >= remaining_time * maxes[0] - (remaining_time - 1) * robots[0]:
            resources[0] = remaining_time * maxes[0] - (remaining_time - 1) * robots[0]
        if resources[1] >= remaining_time * maxes[1] - (remaining_time - 1) * robots[1]:
            resources[1] = remaining_time * maxes[1] - (remaining_time - 1) * robots[1]
        if resources[2] >= remaining_time * maxes[2] - (remaining_time - 1) * robots[2]:
            resources[2] = remaining_time * maxes[2] - (remaining_time - 1) * robots[2]
        resources = tuple(resources)
        
        if (robots, resources, remaining_time) in done:
            continue
        done.add((robots, resources, remaining_time))
        
        if len(done) % 1000000 == 0:
            print(f"t: {remaining_time}, best: {best_geode}, done: {len(done)}")
            print("--- %s seconds ---" % (time.time() - start_time))
        
        building = []
        for robot_type, c in enumerate(cost):
            if all(available >= needed for available, needed in zip(resources, c)):
                building.append(robot_type)
        
        resources = tuple(sum_vector(resources, robots))
        todo.append((robots, resources, remaining_time - 1))
        for robot in building:
            if robot == 3 or robots[robot] < maxes[robot]:
                t = list(robots)
                t[robot] += 1
                todo.append((tuple(t), tuple(sum_vector(resources, cost[robot] + [0], True)), remaining_time - 1))

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