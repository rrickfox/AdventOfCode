import time
start_time = time.time()

# with open("06.txt", "r") as file:
#     lines = [line.strip() for line in file.readlines()]
#     data = list(zip(*[[int(x) for x in line.split()[1:]] for line in lines]))

# res = 1
# for t, record in data:
#     res *= sum(1 for i in range(1, t) if i * (t-i) > record)

# print(res)


# t, record = (int(lines[0].replace(" ", "").split(":")[1]), int(lines[1].replace(" ", "").split(":")[1]))
# print(sum(1 for i in range(1, t) if i * (t-i) > record))

m=open("06.txt").read().split("\n")
import math
print(math.prod(sum(1 for i in range(1,t) if i*(t-i)>r) for t,r in zip(*[[int(x) for x in l.split()[1:]] for l in m])))
t,r=(int(m[i].replace(" ","").split(":")[1]) for i in [0,1])
print(sum(1 for i in range(1,t) if i*(t-i)>r))

# from math import*
# print(prod(ceil(t/2+sqrt(t*t/4-d))-floor(t/2-sqrt(t*t/4-d))-1 for (t,d) in zip(*[map(int,l[l.find(':')+1:].split()) for l in open("06.data").read().split('\n')])))
# [t,d]=[int(l[l.find(':')+1:].replace(' ','')) for l in open("06.data").read().split('\n')]
# print(ceil(t/2+sqrt(t*t/4-d))-floor(t/2-sqrt(t*t/4-d))-1)


print(f"--- {(time.time() - start_time)} seconds ---")