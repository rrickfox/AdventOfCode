import time
start_time = time.time()

with open("13.txt", "r") as file:
    data = [block.split("\n") for block in file.read().split("\n\n")]

def reflects(block):
    ret = set()
    # print(block)
    found = False
    for i1, (r1, r2) in enumerate(zip(block[:-1], block[1:])):
        mirror = True
        if r1 == r2:
            # print("same horiz", i1)
            j = 1
            while True:
                if i1-j < 0 or i1+j+1 >= len(block): break
                if block[i1-j] != block[i1+j+1]:
                    mirror = False
                    break
                j += 1
            if mirror:
                # print("Mirror horiz:", i1)
                ret.add((100, i1+1))
    column_block = ["".join(col) for col in zip(*block)]
    for i1, (r1, r2) in enumerate(zip(column_block[:-1], column_block[1:])):
        mirror = True
        if r1 == r2:
            # print("same vert", i1)
            j = 1
            while True:
                if i1-j < 0 or i1+j+1 >= len(column_block): break
                if column_block[i1-j] != column_block[i1+j+1]:
                    mirror = False
                    break
                j += 1
            if mirror:
                # print("Mirror vert:", i1)
                ret.add((1, i1+1))
    return ret

symbol = ".#"
ret = 0
ret2 = 0
for block in data:
    r = reflects(block)
    r_elem = list(r)[0]
    ret += r_elem[0]*r_elem[1]
    found = False
    for y in range(len(block)):
        for x in range(len(block[0])):
            r_new = reflects(block[:y] + [block[y][:x] + symbol[block[y][x] == "."] + block[y][x+1:]] + block[y+1:])
            if r_new.difference(r) != set():
                found = True
                r_elem2 = list(r_new.difference(r))[0]
                # print(x, y, r_elem2)
                ret2 += r_elem2[0]*r_elem2[1]
            if found: break
        if found: break

print(ret)
print(ret2)

print(f"--- {(time.time() - start_time)} seconds ---")