import time
start_time = time.time()

with open("09.txt", "r") as file:
    line = file.readline().strip()

holes = []
data = []
pos = 0
for i, elem in enumerate(line):
    if i % 2 == 0:
        if int(elem) != 0: data.append([pos, pos + int(elem), len(data)])
    else:
        if int(elem) != 0: holes.append([pos, pos + int(elem)])
    pos += int(elem)

orig_holes = [list(elem) for elem in holes]
orig_data = [list(elem) for elem in data]

while len(holes):
    # print("".join(str(i)*(e-s) for s, e, i in data))
    if len(holes) % 100 == 0: print(len(holes))
    start, end, i = data[-1]
    hole_start, hole_end = holes[0]
    index_hole = [i+1 for i in range(len(data)-1) if data[i][1] != data[i+1][0]] + [len(data)]
    index_hole = index_hole[0]
    # print("indices", index_hole)
    if data[index_hole - 1][2] == i:
        data[index_hole - 1][1] += 1
    else:
        data.insert(index_hole, [hole_start, hole_start + 1, i])

    if hole_end - hole_start == 1:
        holes.pop(0)
    else:
        holes[0][0] += 1

    if end - start == 1:
        data.pop()
        if holes[-1][1] == start: holes.pop()
    else:
        data[-1][1] -= 1
    # print("holes", holes)
    # print("data", data)

print(sum(sum(i * x for x in range(s, e)) for s, e, i in data))

holes = [list(elem) for elem in orig_holes]
data = [list(elem) for elem in orig_data]
moved_data = []

for i in range(len(data)-1, -1, -1):
    if i%100 == 0: print(i)
    start, end, i = data[i]
    fitting_holes = [i for i, hole in enumerate(holes) if hole[1]-hole[0] >= end-start]
    if len(fitting_holes) > 0 and holes[fitting_holes[0]][0] < start:
        hole = holes[fitting_holes[0]]
        moved_data.append([hole[0], hole[0] + end-start, i])
        del data[i]
        if end-start == hole[1]-hole[0]:
            # delete hole because it is filled completely
            del holes[fitting_holes[0]]
        else:
            # shrink hole by length of element
            holes[fitting_holes[0]][0] += end-start

# print(data)
moved_data.sort()
# print(moved_data)
combined = []
while True:
    if len(data) == 0:
        combined += moved_data
        break
    if len(moved_data) == 0:
        combined += data
        break
    if data[0][0] < moved_data[0][0]:
        combined.append(data.pop(0))
    else:
        combined.append(moved_data.pop(0))

# print(combined)
print(sum(sum(i * x for x in range(s, e)) for s, e, i in combined))

print(f"--- {(time.time() - start_time)} seconds ---")