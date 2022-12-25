import time
start_time = time.time()

with open("25.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def convert2Number(num):
    ret = 0
    for index, val in enumerate(reversed(num)):
        if val.isdigit():
            val = int(val)
        elif val == "-":
            val = -1
        elif val == "=":
            val = -2
        else:
            print(f"shouldn't happen: {val}")

        ret += 5**index * val
    return ret

def convert2snafu(num):
    ret = []
    while num > 0:
        digit = num % 5
        num = (num - digit) // 5
        if digit > 2:
            digit -= 5
            num += 1
        ret.append(["0", "1", "2", "=", "-"][digit])
    return "".join(reversed(ret))

s = sum(map(convert2Number, lines))
# print(s)
print(convert2snafu(s))

print("--- %s seconds ---" % (time.time() - start_time))