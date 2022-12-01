import time, math
start_time = time.time()

with open("18.txt") as file:
	lines = file.readlines()
	lines = [eval(line.strip()) for line in lines]

# print(lines)

def find(pair, path):
	# print(pair)
	# print(path)
	if len(path):
		return find(pair[path.pop(0)], path)
	return pair

def find_most_right(pair):
	# print("in find_most_right")
	# print(pair)
	if isinstance(pair, int):
		return pair, []
	ret = find_most_right(pair[1])
	return ret[0], [1] + ret[1]

def find_most_left(pair):
	# print("in find_most_left")
	# print(pair)
	if isinstance(pair, int):
		return pair, []
	ret = find_most_left(pair[0])
	return ret[0], [0] + ret[1]

def replace(pair, path_to_replace, val):
	if path_to_replace == []:
		return val
	next_step = path_to_replace.pop(0)
	if next_step == 0:
		return [replace(pair[0], path_to_replace, val), pair[1]]
	else:
		return [pair[0], replace(pair[1], path_to_replace, val)]

def expl_left(pair, path):
	# print("in expl_left")
	# print("path: " + str(path))
	val_to_explode = find(pair, path+[0])
	last_right_turn = "".join([str(x) for x in path]).rindex("1")
	most_right_val, most_right_rel = find_most_right(find(pair, path[:last_right_turn])[0])
	path_to_most_right = path[:last_right_turn] + [0] + most_right_rel
	replace_val = most_right_val + val_to_explode

	# print("path_to_replace: " + str(path_to_most_right))
	# print("val to replace: " + str(replace_val))
	pair = replace(pair, path_to_most_right, replace_val)
	# print("after replace left: " + str(pair))
	return pair

def expl_right(pair, path):
	# print("in expl_right")
	# print("path: " + str(path))
	val_to_explode = find(pair, path+[1])
	# print(val_to_explode)
	last_left_turn = "".join([str(x) for x in path]).rindex("0")
	most_left_val, most_left_rel = find_most_left(find(pair, path[:last_left_turn])[1])
	path_to_most_left = path[:last_left_turn] + [1] + most_left_rel
	replace_val = most_left_val + val_to_explode

	# print("path_to_replace: " + str(path_to_most_left))
	# print("val to replace: " + str(replace_val))
	pair = replace(pair, path_to_most_left, replace_val)
	# print("after replace right: " + str(pair))
	return pair

def explode(pair, path):
	# print("in explode")
	path = path[:-2]
	if 1 in path: # able to explode left
		pair = expl_left(pair, path)
	if 0 in path:
		pair = expl_right(pair, path)
	pair = replace(pair, path, 0)
	# print("!!!!!")
	# print("after explode: " + str(pair))
	return pair

def split(pair, path):
	# print("in split")
	# print("path: " + str(path))
	val_to_split = path[-1]
	# print("val to split: " + str(val_to_split))
	pair = replace(pair, path[:-1], [math.floor(val_to_split/2), math.ceil(val_to_split/2)])
	# print("after split: " + str(pair))
	return pair

def check_if_pair(pair, path):
	# print(path)
	# print(pair)
	if len(path) == 1:
		if isinstance(pair[path[0]], int) and isinstance(pair[path[0]+1%2], int):
			# print(True)
			return True
		else: return False
	return check_if_pair(pair[path.pop(0)], path)

def check(pair):
	# print("------ Check --------")
	paths = get_path(pair)
	for path in paths:
		if len(path) > 5 and check_if_pair(pair, path[:-1]): # explode
			return check(explode(pair, path))
	for path in paths:
		if path[-1] >= 10:
			return check(split(pair, path))
	return pair

def get_path(elem, curr_path = []):
	if isinstance(elem, int):
		return [curr_path + [elem]]
	return get_path(elem[0], curr_path+[0]) + get_path(elem[1], curr_path+[1])

sum = lines[0]
for elem in lines[1:]:
	# print("================================================")
	sum = check([sum, elem])
	# print(sum)

print()
print("result: " + str(sum))

def magnitude(pair):
	if isinstance(pair, int):
		return pair
	else:
		return 3*magnitude(pair[0]) + 2*magnitude(pair[1])

print("magnitude: " + str(magnitude(sum)))

print("--- %s seconds ---" % (time.time() - start_time))