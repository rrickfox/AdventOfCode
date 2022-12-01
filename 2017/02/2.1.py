with open("2.txt") as file:
    data = file.readlines()
    data = [[int(x) for x in line.split("\t")] for line in data]

s = 0

for line in data:
    m = max(line)
    n = min(line)
    s += m - n

print(s)