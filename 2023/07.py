import time, collections
from functools import cmp_to_key
start_time = time.time()

with open("07.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [tuple(line.split()) for line in lines]

order = "AKQJT98765432"
order2 = "AKQT98765432J"

def rank(s: str) -> int:
    num = collections.Counter(s)
    if len(num) == 1: return 0
    elif len(num) == 2:
        if 4 in num.values(): return 1
        else: return 2
    elif len(num) == 3:
        if 3 in num.values(): return 3
        else: return 4
    elif len(num) == 4: return 5
    else: return 6

def rank2(s: str) -> int:
    num = collections.Counter(s)
    cop = dict(num)
    if "J" in num and len(num) > 1:
        c = num["J"]
        del num["J"]
        m = sorted(num.items(), reverse=True, key=lambda x: x[1])[0][0]
        num[m] += c
        # print(cop, num)
    if len(num) == 1: return 0
    elif len(num) == 2:
        if 4 in num.values(): return 1
        else: return 2
    elif len(num) == 3:
        if 3 in num.values(): return 3
        else: return 4
    elif len(num) == 4: return 5
    else: return 6

def compare(a, b):
    x, _ = a
    y, _ = b
    num_x = rank(x)
    num_y = rank(y)
    if num_x != num_y:
        return num_y - num_x
    
    for char_x, char_y in zip(x, y):
        if (n := order.index(char_x)) != (m := order.index(char_y)):
            return m - n

def compare2(a, b):
    x, _ = a
    y, _ = b
    num_x = rank2(x)
    num_y = rank2(y)
    if num_x != num_y:
        return num_y - num_x
    
    for char_x, char_y in zip(x, y):
        if (n := order2.index(char_x)) != (m := order2.index(char_y)):
            return m - n

# for s, _ in data:
#     rank2(s)

data.sort(key=cmp_to_key(compare))
print(sum(int(x[1]) * (i+1) for i, x in enumerate(data)))

data.sort(key=cmp_to_key(compare2))
print(sum(int(x[1]) * (i+1) for i, x in enumerate(data)))

print(f"--- {(time.time() - start_time)} seconds ---")