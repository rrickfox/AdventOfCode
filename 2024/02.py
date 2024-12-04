import time
start_time = time.time()

with open("02.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [[int(x) for x in line.split()] for line in lines]

diff_data = [[x - y for x, y, in zip(a, a[1:])] for a in data]
print(sum([1 if (all(x > 0 for x in line) or all(x < 0 for x in line)) and all(abs(x) >= 1 and abs(x) <= 3 for x in line) else 0 for line in diff_data]))

data_part_2 = [[line] + [line[:i]+line[i+1:] for i in range(len(line))] for line in data]
diff_data_part_2 = [[[x - y for x, y, in zip(a, a[1:])] for a in line] for line in data_part_2]
print(sum([1 if any((all(x > 0 for x in report) or all(x < 0 for x in report)) and all(abs(x) >= 1 and abs(x) <= 3 for x in report) for report in line) else 0 for line in diff_data_part_2]))

print(f"--- {(time.time() - start_time)} seconds ---")