import random
with open("message.txt", "a") as file:
    for _ in range(4999):
        for _ in range(4999):
            file.write(str(random.randint(0,9)))
        file.write("\n")