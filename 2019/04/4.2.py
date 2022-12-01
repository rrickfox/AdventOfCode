from collections import Counter
import time
start_time = time.time()

data = (353096, 843212)

def twoingroup(s):
    l = [(s[0], 1)]
    for x in s[1:]:
        if x == l[-1][0]:
            l[-1] = (x, l[-1][1] + 1)
        else: l.append((x, 1))
    return any([True if x[1] == 2 else False for x in l])

s = 0

for x in range(data[0], data[1] + 1):
    if twoingroup(str(x)):
        a = 1
        last = int(str(x)[0])
        for n in str(x):
            if int(n) < last:
                a = 0
            last = int(n)
        s += a

print(s)

print("--- %s seconds ---" % (time.time() - start_time))