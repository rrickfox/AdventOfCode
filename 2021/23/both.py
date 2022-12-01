import time
start_time = time.time()
from copy import deepcopy
from cache import selective_cache

# read input by hand, too lazy to do with python
# rooms_start = ("BA", "CD", "BC", "DA") # Demo
c_to_room = {"A": 0, "B": 1, "C": 2, "D": 3}
room_to_c = ["A", "B", "C", "D"]
c_to_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
hallway_spots = (0, 1, 3, 5, 7, 9, 10)

def path_free(end_spot, room_num, hall):
	ind_hall = (room_num + 1) * 2

	if end_spot < ind_hall:
		segment = hall[end_spot+1:ind_hall+1]
	elif end_spot > ind_hall:
		segment = hall[ind_hall: end_spot]
	else:
		segment = ""

	return (segment == "."*len(segment))

def cost_hallway(c, spot, num, count_room):
	global max_room

	steps = abs(spot - ((num + 1)*2))
	steps += max_room + 1 - count_room
	return c_to_cost[c] * steps

def move_to_hallway(c, spot, num, rooms, hall):
	cost = cost_hallway(c, spot, num, len(rooms[num]))

	new_hall = hall[:spot] + c + hall[spot+1:]
	new_rooms = deepcopy(rooms)
	new_rooms = new_rooms[:num] + (rooms[num][1:], ) + new_rooms[num+1:]

	return cost, new_hall, new_rooms

def able_to_go_to_room(c, num, rooms):
	if c != room_to_c[num]:
		return False # if c does not belong into that room
	
	return rooms[num] == c * len(rooms[num]) # True if only same type in room

def cost_room(c, spot, num, count_room):
	global max_room

	steps = abs(spot - ((num + 1) * 2))
	steps += max_room - count_room
	return c_to_cost[c] * steps

def move_to_room(c, spot, num, rooms, hall):
	cost = cost_room(c, spot, num, len(rooms[num]))

	new_hall = hall[:spot] + "." + hall[spot+1:]
	new_rooms = deepcopy(rooms)
	new_rooms = new_rooms[:num] + (c + rooms[num], ) + new_rooms[num+1:]

	return cost, new_hall, new_rooms

@selective_cache("hall", "rooms", "cost")
def solve(rooms, hall, cost, path):
	global curr_best
	if cost > curr_best:
		print("bigger")
	if rooms == final:
		if cost < curr_best:
			curr_best = cost
			print("New best path: " + str(cost))
		return cost, path

	best = float("inf")
	bestpath = None

	# move from room to hallway:
	for num, room in enumerate(rooms):
		if not room:
			continue # if room is empty

		if room == room_to_c[num]*len(room):
			continue # if room is already finished

		for spot in hallway_spots:
			if hall[spot] == "." and path_free(spot, num, hall):
				move_cost, new_hall, new_rooms = move_to_hallway(room[0], spot, num, rooms, hall)

				if cost + move_cost > curr_best:
					continue # if path about to be gone done is worse than current best

				new_path = path + [f'{room[0]} r{num} --{move_cost}-> h{spot}']
				subcost, subpath = solve(new_rooms, new_hall, cost + move_cost, new_path)

				if subcost < best:
					best = subcost
					bestpath = subpath
		
	for spot in hallway_spots:
		c = hall[spot]

		if c == ".":
			continue # if nobody is here

		num = c_to_room[c]

		if not able_to_go_to_room(c, num, rooms):
			continue

		if path_free(spot, num, hall):
			move_cost, new_hall, new_rooms = move_to_room(c, spot, num, rooms, hall)

			if cost + move_cost > curr_best:
				continue # if path about to be gone done is worse than current best

			new_path = path + [f'{c} h{spot} --{move_cost}-> r{num}']
			subcost, subpath = solve(new_rooms, new_hall, cost + move_cost, new_path)

			if subcost < best:
				best = subcost
				bestpath = subpath

	return best, bestpath

# # # # # # #
# Demo from website
# rooms_1 = ("BA", "CD", "BC", "DA")
# final = ("AA", "BB", "CC", "DD")
# curr_best = float("inf")
# max_room = 2
# hallway = "..........."
# ans, path = solve(rooms_1, hallway, 0, [])
# print(ans)
# print(path)

rooms_1 = ("CD", "CA", "BB", "DA")
final = ("AA", "BB", "CC", "DD")
curr_best = float("inf")
max_room = 2
hallway = "..........."
ans, path = solve(rooms_1, hallway, 0, [])
print(ans)
print(path)

rooms_2 = ("CDDD", "CCBA", "BBAB", "DACA")
final = ("AAAA", "BBBB", "CCCC", "DDDD")
curr_best = float("inf")
max_room = 4
hallway = "..........."
ans2, path2 = solve(rooms_2, hallway, 0, [])
print(ans2)
print(path2)

# # # # # # #
# Upping the Ante
# rooms_2 = ("BDDDDA", "CCBCBD", "BBABAC", "DACACA")
# final = ("AAAAAA", "BBBBBB", "CCCCCC", "DDDDDD")
# curr_best = float("inf")
# max_room = 6
# hallway = "............"
# hallway_spots = (0, 1, 3, 5, 7, 9, 10)
# ans2, path2 = solve(rooms_2, hallway, 0, [])
# print(ans2)
# print(path2)

print("--- %s seconds ---" % (time.time() - start_time))