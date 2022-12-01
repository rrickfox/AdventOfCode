with open("2.txt") as file:
    data = file.readlines()
    data = [[int(x) for x in line.split("\t")] for line in data]

s = 0

for line in data:
    a = 0
    for x in line:
        for y in line:
            if x != y and x % y == 0:
                a = x / y
                break
        if a != 0:
            break
    s += a

print(s)