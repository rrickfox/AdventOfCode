import time, math
start_time = time.time()

with open("05.txt", "r") as file:
    inp = file.read()
    rules_lines = [tuple(map(int, line.strip().split("|"))) for line in inp.split("\n\n")[0].split("\n")]
    data = [tuple(map(int, line.strip().split(","))) for line in inp.split("\n\n")[1].split("\n")]

rules = {}
for line in rules_lines:
    rules[line[0]] = rules.get(line[0], set()).union(set([line[1]]))

def bubble_up_key(d, key, depth = 0):
    all_keys_where_key_is_member = [k for k in d if key in d[k]]
    for k in all_keys_where_key_is_member:
        d[k] = d.get(k, set()).union(d[key])
    for k in all_keys_where_key_is_member:
        bubble_up_key(d, k, depth+1)

s = 0
s2 = 0
for index, line in enumerate(data):
    valid = True
    for currentIndex in range(len(line)-1):
        if any(line[currentIndex] not in rules or val not in rules[line[currentIndex]] for val in line[currentIndex+1:]):
            valid = False
            break
    if valid:
        s += line[math.floor(len(line) / 2.0)]
    else:
        transitive_dict = {key:rules[key] if key in rules else set() for key in line}
        for key in line:
            bubble_up_key(transitive_dict, key)
        print("index", index, "of", len(data))
        copy_line = list(line)
        reordered = []
        while (len(copy_line)):
            first = [val for val in copy_line if all(other == val or other in transitive_dict[val] for other in copy_line)][0]
            copy_line.remove(first)
            reordered.append(first)
        s2 += reordered[math.floor(len(reordered) / 2.0)]

print(s)
print(s2)

print(f"--- {(time.time() - start_time)} seconds ---")