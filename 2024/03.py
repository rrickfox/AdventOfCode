import time, re
start_time = time.time()

with open("03.txt", "r") as file:
    data = "".join([line.strip() for line in file.readlines()])

print(sum(int(x.group(1))*int(x.group(2)) for x in re.finditer(r'mul\((\d*),(\d*)\)', data)))

enabled = True
s = 0
for match in re.finditer(r'(mul\((\d*),(\d*)\)|do\(\)|don\'t\(\))', data):
    if match.group(0) == "do()": enabled = True
    elif match.group(0) == "don't()": enabled = False
    else: s += int(match.group(2))*int(match.group(3)) if enabled else 0

print(s)

print(f"--- {(time.time() - start_time)} seconds ---")