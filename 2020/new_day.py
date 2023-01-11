with open("src/BlankDay.cs", "r") as file:
    data = file.read()

day = int(input("What day to generate?\n> "))

day = f"{day:02d}"

data = data.replace("BlankDay", f"Day{day}")

with open(f"src/Day{day}.cs", "w") as file:
    file.write(data)

with open(f"Data/{day}.txt", "w") as file:
    file.write("")