import time
start_time = time.time()

with open("09.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [[int(x) for x in line.split()] for line in lines]

def predict_next(line: list[int]) -> tuple[int, int]:
    if all(x == 0 for x in line): return 0, 0
    new = [a-b for a, b in zip(line[1:], line[:-1])]
    start, end = predict_next(new)
    return (line[0] - start, line[-1] + end)

part1 = part2 = 0
for line in data:
    a, b = predict_next(line)
    part1 += b
    part2 += a

print(part1)
print(part2)

print(f"--- {(time.time() - start_time)} seconds ---")