import time
start_time = time.time()

with open("1.txt", "r") as file:
    lines = file.readlines()
    data = [line for line in lines]



print()

print("--- %s seconds ---" % (time.time() - start_time))