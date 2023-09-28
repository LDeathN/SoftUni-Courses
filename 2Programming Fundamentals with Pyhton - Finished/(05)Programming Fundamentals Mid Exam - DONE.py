# First Problem

best = 0
attendances = 0
students = int(input())
lectures = int(input())
bonus = int(input())
for i in range(students):
    attendance = int(input())
    total = round(attendance / lectures * (5 + bonus))
    if total > best:
        best = total
        attendances = attendance
print(f"Max Bonus: {best}.")
print(f"The student has attended {attendances} lectures.")



# Second Problem

health = 100
bitcoins = 0
room = 0
flag = True
rooms = input().split("|")
for i in range(0, len(rooms)):
    name, number = rooms[i].split(" ")
    number = int(number)
    room += 1
    if name == "potion":
        if health + number <= 100:
            print(f"You healed for {number} hp.")
            health += number
            print(f"Current health: {health} hp.")
        else:
            healed = 100 - health
            health = 100
            print(f"You healed for {healed} hp.")
            print(f"Current health: {health} hp.")
    elif name == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        if health - number > 0:
            print(f"You slayed {name}.")
            health -= number
        elif health - number <= 0:
            print(f"You died! Killed by {name}.")
            print(f"Best room: {room}")
            flag = False
            break
if flag:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")



# Third Problem

items = input().split(", ")
while True:
    command = input()
    if command == "Craft!":
        break
    name, item = command.split(" - ")
    if name == "Collect":
        if item not in items:
            items.append(item)
    elif name == "Drop":
        if item in items:
            items.remove(item)
    elif name == "Combine Items":
        old, new = item.split(":")
        if old in items:
            for i in range(0, len(items)):
                if items[i] == old:
                    items.insert(i + 1, new)
    elif name == "Renew":
        if item in items:
            for i in range(0, len(items)):
                if items[i] == item:
                    items.pop(i)
                    items.append(item)
for i in range(0, len(items)):
    if i != len(items) - 1:
        print(items[i], end=", ")
    else:
        print(items[i])
