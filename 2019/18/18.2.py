# no idea why this doesn't work, I checked up to 2 mil states, somewhere it seems to stop working :(

import math
import time
start_time = time.time()

with open("18.txt") as file:
    data = [line.strip() for line in file.readlines()]

points = set()
keys = {}
doors = {}
y = 0
p = None

for line in data:
    # print(line)
    x = 0
    for c in line:
        if c == ".":
            points.add((x, y))
        elif c == "@":
            points.add((x, y))
            p = (x, y)
        elif c != "#":
            if c.isalpha() and c.islower():
                keys[(x, y)] = c
            elif c.isalpha and c.isupper():
                doors[c] = (x, y)
            points.add((x, y))
        x += 1
    y += 1

def pos(x, y, d):
    if d == 0:
        return x, y - 1
    elif d == 1:
        return x + 1, y
    elif d == 2:
        return x, y + 1
    elif d == 3:
        return x - 1, y

points.remove(p)
for i in range(4):
    points.remove(pos(*p, i))
p = tuple([(p[0] + x, p[1] + y) for x in (-1, 1) for y in (-1, 1)])

def set2tuple(s):
    t = list(s)
    t.sort()
    return tuple(t)

def find_reachable(position):
    reachable = {}
    visited = set()
    todo = [(position, 0, set())]
    while len(todo) > 0:
        curr, s, blocked = todo.pop(0)
        visited.add(curr)
        for i in range(4):
            v = pos(*curr, i)
            if v in points and v not in visited and v not in set([x[0] for x in todo]):
                if v in keys:
                    reachable[v] = (s + 1, blocked)
                    todo.append((v, s + 1, blocked.union({keys[v]})))
                elif v in doors.values():
                    todo.append((v, s + 1, blocked.union(set([d for d in doors if doors[d] == v]))))
                else:
                    todo.append((v, s + 1, blocked))
    return reachable

reachable = {t: find_reachable(t) for t in p}
for v in keys.keys():
    reachable[v] = find_reachable(v)

for r in reachable:
    print(str(r) + " (" + keys.get(r, "starting") + ")")
    for t in reachable[r]:
        print(str(keys[t]) + ": " + str(reachable[r][t][1]) + ", ", end="")
    print()

m = math.inf
states_checked = 0
# state: current_position, steps, done, still_open, doors
states = [(p, 0, set(), set([k for k in keys]), {d: doors[d] for d in doors})]
while len(states) > 0:
    #TODO:
    # if states_checked > 250000:
    #     print("nothing found :(")
    #     break
    states_checked += 1
    if states_checked % 10000 == 0 or states_checked < 20:
        print(str(states_checked) + " states checked, " + str(len(states)) + " remaining, current best: " + str(m))
        # print(positions)
        # print(steps)
        # print(done)
        # print(open_keys)
        # print(open_doors)
        # print("other states:")
        # for t in states:
        #     print(t)

    positions, steps, done, open_keys, open_doors = states.pop()

    if steps > m:
        continue
    if len(open_keys) == 0:
        m = min(steps, m)

    for i in range(4):
        count = 0
        position = positions[i]
        r = reachable[position]
        # if states_checked < 20:
        #     print("position: " + str(position))
        # move to all reachables, add to states
        for key, (s, blocked) in r.items():
            if done.issuperset(blocked) and key in open_keys not in done:
                d = done.union({keys[key], keys[key].upper()})
                count += 1
                states.append(((*positions[:i], key, *positions[i+1:]), steps + s, d, open_keys.difference({key}), {d: doors[d] for d in open_doors if keys[key].upper() != d}))
                # if states_checked < 20:
                #     print(((*positions[:i], key, *positions[i+1:]), steps + s, d, open_keys.difference({key}), {d: doors[d] for d in open_doors if keys[key].upper() != d}))
        # if states_checked < 20:
        #     print("states added: " + str(count))

# min_x = min([v[0] for v in points])
# max_x = max([v[0] for v in points])
# min_y = min([v[1] for v in points])
# max_y = max([v[1] for v in points])

# for y_print in range(min_y, max_y + 1):
#     for x_print in range(min_x, max_x + 1):
#         if (x_print, y_print) in p:
#             print("@", end="")
#         # elif (x_print, y_print) in visited:
#         #     print("X", end="")
#         elif (x_print, y_print) in keys:
#             print(keys[(x_print, y_print)], end="")
#         elif (x_print, y_print) in doors:
#             print(doors[(x_print, y_print)], end="")
#         elif (x_print, y_print) in points:
#             print(" ", end="")
#         else:
#             print("#", end="")
#     print()

print(str(states_checked) + " states checked")
print(m)

print("--- %s seconds ---" % (time.time() - start_time))