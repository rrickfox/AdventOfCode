with open("1.txt") as file:
    data = file.readline()

s = 0

prev = data[len(data)-1]
for digit in data:
    if digit == prev:
        s += int(digit)
    prev = digit

print(s)