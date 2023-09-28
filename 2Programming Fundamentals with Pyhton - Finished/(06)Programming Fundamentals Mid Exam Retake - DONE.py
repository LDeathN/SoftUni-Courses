# First Problem

days = int(input())
plunder = int(input())
expected = float(input())
total = 0
for i in range(1, days + 1):
    total += plunder
    if i % 3 == 0:
        total += plunder / 2
    if i % 5 == 0:
        total = total * 0.70
if total >= expected:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = total / expected * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")



# Second Problem

items = input().split("|")
while True:
    command = input()
    if command == "Yohoho!":
        break
    command = command.split(" ")
    name = command[0]
    if name == "Loot":
        for i in range(1, len(command)):
            if command[i] not in items:
                items.insert(0, command[i])
    elif name == "Drop":
        index = int(command[1])
        if 0 <= index <= len(items):
            temp = items[index]
            items.pop(index)
            items.append(temp)
    elif name == "Steal":
        stolen = []
        count = int(command[1])
        if count < len(items):
            for i in range(count):
                stolen.insert(0, items[len(items) - 1])
                items.pop(len(items) - 1)
            for i in range(0, len(stolen)):
                if i != len(stolen) - 1:
                    print(stolen[i], end=", ")
                else:
                    print(stolen[i])
        else:
            for i in range(0, len(items)):
                if i != len(items) - 1:
                    print(f"{items[i]}", end=", ")
                else:
                    print(f"{items[i]}")
            items = []

total = 0
if items != []:
    for item in items:
        total += len(item)
    average = total / len(items)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")



# Third Problem

pirate_ship = input().split(">")
warship = input().split(">")
max_health = int(input())
pirates = 0
warships = 0
flag = True
while True:
    command = input()
    if command == "Retire":
        break
    command = command.split(" ")
    name = command[0]
    if name == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship):
            warship[index] = int(warship[index]) - damage
            if int(warship[index]) <= 0:
                print(f"You won! The enemy ship has sunken.")
                flag = False
                break
    elif name == "Defend":
        start = int(command[1])
        end = int(command[2])
        damage = int(command[3])
        if 0 <= start < len(pirate_ship) and 0 <= end < len(pirate_ship):
            for i in range(start, end + 1):
                pirate_ship[i] = int(pirate_ship[i]) - damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    flag = False
                    break
    elif name == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] = int(pirate_ship[index]) + health
            if int(pirate_ship[index]) > max_health:
                pirate_ship[index] = max_health
    elif name == "Status":
        count = 0
        for i in range(0, len(pirate_ship)):
            if int(pirate_ship[i]) < max_health / 5:
                count += 1
        print(f"{count} sections need repair.")
if flag:
    for i in range(0, len(pirate_ship)):
        pirates += int(pirate_ship[i])
    for i in range(0, len(warship)):
        warships += int(warship[i])
    print(f"Pirate ship status: {pirates}")
    print(f"Warship status: {warships}")
