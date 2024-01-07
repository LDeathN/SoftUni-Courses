# First Problem (a)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

input_string = input()
reversed_result = reverse_string(input_string)
print(reversed_result)

# First Problem (b)

stack = []
sentence = input()
for letter in sentence:
    stack.append(letter)
reversed_string = ""
while stack:
    reversed_string += stack.pop()
print(reversed_string)



# Second Problem

stack = []
equation = input()
for i in range(0, len(equation)):
    if equation[i] == "(":
        stack.append(i)
    if equation[i] == ")":
        opening = int(stack.pop())
        print(f"{equation[opening:i + 1]}")



# Third Problem

queue = []
while True:
    name = input()
    if name == "End":
        break
    if name == "Paid":
        while queue:
            print(queue.pop(0))
        continue
    queue.append(name)
print(f"{len(queue)} people remaining.")



# Fourth Problem

queue = []
quantity_of_water = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input().split(" ")
    if command[0] == "End":
        break
    elif command[0] == "refill":
        liters = int(command[1])
        quantity_of_water += liters
    else:
        liters = int(command[0])
        if quantity_of_water - liters >= 0:
            quantity_of_water -= liters
            print(f"{queue.pop(0)} got water")
        elif quantity_of_water - liters <= 0:
            print(f"{queue.pop(0)} must wait")

print(f"{quantity_of_water} liters left")



# Fifth Problem (a)

names = input().split(" ")
toss = int(input())
count = 0
while len(names) != 1 and toss != 1:
    for i in range(len(names)):

        if len(names) == 1:
            break
        count += 1

        if toss == count:
            print(f"Removed {names.pop(i)}")
            count = 0

if toss == 1:
    for i in range(len(names)):
        if len(names) != 1:
            print(f"Removed {names.pop(0)}")
        else:
            print(f"Last is {names.pop(0)}")
else:
    print(f"Last is {names.pop(0)}")

# Fifth Problem (b)

from collections import deque

people = input().split(' ')
toss = int(input())
players = deque(people)
i = 1

while len(players) > 1:
    person = players.popleft()

    if i == toss:
        print(f'Removed {person}')
        i = 0
    else:
        players.append(person)
    i += 1

print(f'Last is {players.pop()}')
