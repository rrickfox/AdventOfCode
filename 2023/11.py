import time
start_time = time.time()

with open("11.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    ly = len(lines)
    lx = len(lines[0])
    galaxies = [(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "#"]
    empty_rows = {y for y, line in enumerate(lines) if line == "."*lx}
    empty_cols = {x for x, col in enumerate(zip(*lines)) if "".join(col) == "."*ly}


s = s2 = 0
galaxy_pairs = set()
for a in galaxies:
    for b in galaxies:
        if a != b and (b,a) not in galaxy_pairs: galaxy_pairs.add((a,b))
for (x1,y1), (x2,y2) in galaxy_pairs:
    c = len(empty_cols.intersection(set(range(min(x1, x2)+1, max(x1, x2)+1))))
    r = len(empty_rows.intersection(set(range(min(y1, y2)+1, max(y1, y2)+1))))
    s += abs(x1-x2) + abs(y1-y2) + c + r
    s2 += abs(x1-x2) + abs(y1-y2) + c*999999 + r*999999

print(s)
print(s2)

print(f"--- {(time.time() - start_time)} seconds ---")