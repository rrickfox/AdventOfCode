import time
start_time = time.time()

with open("01.txt", "r") as file:
    lines = [line.strip().split() for line in file.readlines()]
    data = [[int(x) for x in line] for line in lines]

list1, list2 = zip(*data)

list1 = sorted(list(list1))
list2 = sorted(list(list2))

print(sum(abs(x - y) for x, y in zip(list1, list2)))

print(sum(x * list2.count(x) for x in list1))

print(f"--- {(time.time() - start_time)} seconds ---")