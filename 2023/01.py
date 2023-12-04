import time, re
start_time = time.time()

with open("01.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [int(v[0]+v[-1]) for line in lines if (v := re.sub("\D", "", line))]

print(sum(data))
print(sum([int(v[0]+v[-1]) for line in open("01.txt", "r").readlines() if (v := re.sub("\D", "", line.strip()))]))

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
print(sum(data))
n = ["one","two","three","four","five","six","seven","eight","nine"];print(sum([int(v[0]+v[-1]) for line in open("01.txt", "r").readlines() if (v := "".join([s if s.isnumeric() else str(t[0]) if t[0]>0 else "" for i, s in enumerate(line.strip()) if (t := [j+1 for j in range(9) if line[i:].startswith(n[j])]+[-1])]))]))

print(f"--- {(time.time() - start_time)} seconds ---")