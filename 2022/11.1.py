import time, math
start_time = time.time()

class Monkey:
    def __init__(self, i: int, items: list[int], op: str, testNum: int, testTrueI: int, testFalseI: int):
        self.i = i
        self.items = items
        self.testTrueI = testTrueI
        self.testFalseI = testFalseI
        self.timesInspected = 0
        op = op.split("= ")[1].split(" ")
        self.op = op[1]
        self.op2 = op[2] if op[2] == "old" else int(op[2])
        self.testNum = testNum

    def inspect(self):
        self.timesInspected += 1
        worry = self.items.pop(0)

        if self.op == "+":
            if isinstance(self.op2, int):
                worry += self.op2
            else:
                worry *= 2
        elif self.op == "*":
            if isinstance(self.op2, int):
                worry *= self.op2
            else:
                worry *= worry

        worry = math.floor(worry / 3)
        return worry, self.testTrueI if worry % self.testNum == 0 else self.testFalseI

with open("11.txt", "r") as file:
    lines = file.read().split("\n\n")

monkeys: dict[int, Monkey] = {}
for monkey in lines:
    i, items, op, test, testTrue, testFalse = monkey.split("\n")
    i = int(i[7])
    items = list(map(int, items.split(": ")[1].split(", ")))
    testNum = int(test.split("by ")[1])
    testTrue = int(testTrue.split("monkey ")[1])
    testFalse = int(testFalse.split("monkey ")[1])
    monkeys[i] = Monkey(i, items, op, testNum, testTrue, testFalse)

for i in range(20):
    for m in range(len(monkeys)):
        while(len(monkeys[m].items) > 0):
            worry, n = monkeys[m].inspect()
            monkeys[n].items.append(worry)

timesInspected = sorted((monkeys[i].timesInspected for i in range(len(monkeys))), reverse=True)
print(timesInspected[0] * timesInspected[1])

print("--- %s seconds ---" % (time.time() - start_time))