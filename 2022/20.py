import time
start_time = time.time()

with open("20.txt", "r") as file:
    data = [int(line.strip()) for line in file.readlines()]

class Node:
    def __init__(self, ident, data):
        self.id = ident
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Function to print linked list
    def print_list(self, separator = " "):
        temp = self.head
        s = ""
        if temp:
            # print(temp.data, end=" ")
            s += str(temp.data) + separator
            temp = temp.next
        while temp != self.head:
            # print(temp.data, end=" ")
            s += str(temp.data) + separator
            temp = temp.next
        # print()
        return s

    # Function to push a node in DLL
    def push(self, ident, num):
        self.length += 1
        # DLL is empty
        if self.tail == None:
            temp = Node(ident, num)
            self.tail = temp
            self.head = temp
            return temp
        # DLL is not empty
        else:
            temp = Node(ident, num)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
            return temp

    def advance(self, item, times):
        if times == 0:
            return item
        if times > 0:
            i = 0
            temp = item
            while temp and i < times:
                temp = temp.next
                i += 1
            if i == times:
                return temp
            else:
                return False

    def move(self, item, times):
        if times == 0: return
        elif times > 0:
            times = times % (self.length-1)
            for _ in range(times):
                self.moveRight(item)
        else:
            times = (-times) % (self.length-1)
            for _ in range(times):
                self.moveLeft(item)

    def moveLeft(self, item):
        self.swap(item, item.prev)

    def moveRight(self, item):
        self.swap(item, item.next)

    def swap(self, x, y):
        if self.head == None or self.head.next == None or x == y:
            return

        if x == self.head:
            self.head = y
        elif y == self.head:
            self.head = x
        if x == self.tail:
            self.tail = y
        elif y == self.tail:
            self.tail = x

        # Swapping Node1 and Node2
        temp = None
        temp = x.next
        x.next = y.next
        y.next = temp

        if x.next != None:
            x.next.prev = x
        if y.next != None:
            y.next.prev = y

        temp = x.prev
        x.prev = y.prev
        y.prev = temp

        if x.prev != None:
            x.prev.next = x
        if y.prev != None:
            y.prev.next = y

# === Part 1 ===

# push nodes into doubly linked list and regular list
dll = DLL()
l = []

for i, num in enumerate(data):
    n = dll.push(i, num)
    l.append(n)

dll.head.prev = dll.tail
dll.tail.next = dll.head

# mix
for item in l:
    dll.move(item, item.data)

# find element with value 0
zero = None
for item in l:
    if item.data == 0:
        zero = item
        break

# find elements 1000, 2000 and 3000 after zero
temp = zero
res = 0
for _ in range(3):
    n = dll.advance(temp, 1000)
    res += n.data
    temp = n
print(res)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# === Part 2 ===
# reset
del l
del dll

# push into lists
dll = DLL()
l = []
for i, num in enumerate(data):
    n = dll.push(i, num * 811589153)
    l.append(n)

dll.head.prev = dll.tail
dll.tail.next = dll.head

# mix 10 times
for _ in range(10):
    for item in l:
        dll.move(item, item.data)
        print(dll.print_list())

# find zero
zero = None
for item in l:
    if item.data == 0:
        zero = item
        break

temp = zero
res = 0
for _ in range(3):
    n = dll.advance(temp, 1000)
    res += n.data
    temp = n
print(res)

print("--- %s seconds ---" % (time.time() - start_time))