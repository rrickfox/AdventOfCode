from collections import Counter
import time
start_time = time.time()

data = (353096, 843212)

s = 0

for x in range(data[0], data[1] + 1):
    if any([True if n > 1 else False for n in Counter(list(str(x))).values()]):
        a = 1
        last = int(str(x)[0])
        for n in str(x):
            if int(n) < last:
                a = 0
            last = int(n)
        s += a

print(s)

print("--- %s seconds ---" % (time.time() - start_time))