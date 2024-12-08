import time
start_time = time.time()

with open("07.txt", "r") as file:
    lines = [line.strip().split(": ") for line in file.readlines()]
    data = [(int(line[0]), [int(x) for x in line[1].split(" ")]) for line in lines]

def recurse_options(needed, val, l, i, part2 = False, op = ""):
    if (i == len(l)):
        # print(op, val == needed)
        return val == needed
    n = recurse_options(needed, val + l[i], l, i+1, part2, op + "+")
    n += recurse_options(needed, val * l[i], l, i+1, part2, op + "*")
    if part2: n += recurse_options(needed, int(str(val) + str(l[i])), l, i+1, part2, op + "||")
    return n

print(sum(line[0] for line in data if recurse_options(line[0], line[1][0], line[1], 1) > 0))
print(sum(line[0] for line in data if recurse_options(line[0], line[1][0], line[1], 1, True) > 0))

print(f"--- {(time.time() - start_time)} seconds ---")