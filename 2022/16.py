import time, parse
from copy import copy
start_time = time.time()

p = parse.compile("Valve {} has flow rate={}; {}")

with open("16.txt", "r") as file:
    lines = [(p.parse(line.strip())) for line in file.readlines()]
    data = {line[0]:(int(line[1]), [line[2].split(", ")[0].split(" ")[-1]] + line[2].split(", ")[1:]) for line in lines}

# dijkstra pathfinding between valves

def check_neighbours(nextPos, visited, todo):
    global data
    for n in data[nextPos][1]:
        if n not in visited and n not in todo:
            visited[n] = visited[nextPos] + 1
            todo.append(n)

def pathfinding(start_pos: str):
    visited = {start_pos: 0}
    todo = [start_pos]

    while len(todo):
        check_neighbours(todo.pop(0), visited, todo)

    visited[start_pos] = 1
    return visited

# valves that have a non-zero flow rate
valves_to_open = set([valve for valve in data if data[valve][0] > 0])
# distances between all valves
paths = {valve: pathfinding(valve) for valve in ["AA"]+list(valves_to_open)}

# part 1
def next_valve(current_pos:str, remaining_time:int, open_valves:set):
    global data, paths
    rets = []
    if remaining_time <= 0:
        return 0

    # open valve if possible
    if remaining_time >= 1 and data[current_pos][0] > 0 and current_pos not in open_valves:
        rets.append((remaining_time-1) * data[current_pos][0] + next_valve(
            current_pos,
            remaining_time-1,
            open_valves.union([current_pos])))
    else:
        # move to all valves that are not yet open
        for n in valves_to_open.difference(open_valves):
            rets.append(next_valve(
                n,
                remaining_time - paths[current_pos][n],
                open_valves))

    # if nothing is possible, nothing is gained
    rets.append(0)
    # return maximum that is possible to get going from here
    return max(rets)

print(next_valve("AA", 30, set()))

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# part 2
def next_elephant(current_pos_ele:str, current_pos_me:str, remaining_time_ele:int, remaining_time_me:int, open_valves:set):
    global data, paths
    rets = []
    # if both are done nothing is possible anymore
    if remaining_time_ele <= 0 and remaining_time_me <= 0:
        return 0

    # move elephant if it hat more time than me, this should make us move mostly evenly
    if remaining_time_ele >= remaining_time_me:
        # move elephant, but only if it has time left
        if remaining_time_ele >= 1:
            # turn on valve if possible
            if data[current_pos_ele][0] > 0 and current_pos_ele not in open_valves:
                rets.append((remaining_time_ele-1) * data[current_pos_ele][0] + next_elephant(
                    current_pos_ele,
                    current_pos_me,
                    remaining_time_ele - 1,
                    remaining_time_me,
                    open_valves.union([current_pos_ele])))
            else:
                # move to all valves that are not opened yet and that I am not standing at
                for n in (valves_to_open.difference(open_valves)).difference([current_pos_me]):
                    rets.append(next_elephant(
                        n,
                        current_pos_me,
                        remaining_time_ele - paths[current_pos_ele][n],
                        remaining_time_me,
                        open_valves))
    else:
        # move me
        if remaining_time_me >= 1:
            if data[current_pos_me][0] > 0 and current_pos_me not in open_valves:
                rets.append((remaining_time_me-1) * data[current_pos_me][0] + next_elephant(
                    current_pos_ele,
                    current_pos_me,
                    remaining_time_ele,
                    remaining_time_me - 1,
                    open_valves.union([current_pos_me])))
            else:
                for n in (valves_to_open.difference(open_valves)).difference([current_pos_ele]):
                    rets.append(next_elephant(
                        current_pos_ele,
                        n,
                        remaining_time_ele,
                        remaining_time_me - paths[current_pos_me][n], open_valves))

    rets.append(0)
    return max(rets)

print(next_elephant("AA", "AA", 26, 26, set()))

print("--- %s seconds ---" % (time.time() - start_time))