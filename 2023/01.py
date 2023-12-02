import time, re
start_time = time.time()

with open("01.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [int(v[0]+v[-1]) for line in lines if (v := re.sub("\D", "", line))]

print(sum(data))

def get_numbers(s: str) -> str:
    ret = ""
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    didSomething = False

    while(len(s) > 0):
        didSomething = False
        if s[0].isdigit():
            ret += s[0]
            s = s[1:]
            continue
        for i, num in enumerate(nums):
            if s.startswith(num):
                ret += str(i+1)
                s = s[1:]
                didSomething = True
                break
        if not didSomething:
            s = s[1:]

    return ret

data = [int(v[0]+v[-1]) for line in lines if (v := get_numbers(line))]
for line in lines:
    v = get_numbers(line)
    print(line, v)
print(sum(data))

print(f"--- {(time.time() - start_time)} seconds ---")