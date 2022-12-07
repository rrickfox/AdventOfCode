import time, json
start_time = time.time()

with open("7.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def addToPath(tree, path, val):
    if len(path) == 1:
        if path[0] in tree:
            print("===== path already existed =====")
        else:
            tree[path[0]] = val
    else:
        addToPath(tree[path[0]], path[1:], val)

value1 = 0
directories = []
def calculateFilesize(tree):
    global value1
    if isinstance(tree, dict):
        s = 0
        for item in tree.values():
            temp = calculateFilesize(item)
            s += temp
        if s <= 100000:
            value1 += s
        directories.append(s)
        return s
    elif isinstance(tree, int):
        return tree
    else:
        print("Neither dict nor int:")
        print(tree)

root = {}
path = []

for line in lines:
    if line[0] == "$":
        command = line.split(" ")
        if command[1] == "cd":
            target = command[2]
            # print(f"$ cd {target}")
            if target == "/":
                path = []
            elif target == "..":
                path.pop()
            else:
                path.append(target)
        else:
            # can only be ls
            pass
    else:
        # describing file or directory
        size, name = line.split(" ")
        # print(f"adding {size}, {name}")
        addToPath(root, path + [name], {} if size == "dir" else int(size))

# print(json.dumps(root, indent=4))
sizeRoot = calculateFilesize(root)
print(value1)
sizeNeeded = sizeRoot - 40000000
directories.sort()
print([i for i in directories if i > sizeNeeded][0])

print("--- %s seconds ---" % (time.time() - start_time))