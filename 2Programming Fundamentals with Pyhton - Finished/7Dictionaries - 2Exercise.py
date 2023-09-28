# First Problem

texts = input().split(" ")
dictionary = {}
for text in texts:
    for i in text:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
for j in dictionary:
    print(f"{j} -> {dictionary[j]}")



# Second Problem

dictionary = {}
while True:
    material = input()
    if material == "stop":
        break
    quantity = int(input())
    if material not in dictionary:
        dictionary[material] = quantity
    else:
        dictionary[material] += quantity
for j in dictionary:
    print(f"{j} -> {dictionary[j]}")



# Third Problem

country = input().split(", ")
capital = input().split(", ")
dictionary = list(zip(country, capital))
for i in dictionary:
    print(f"{i[0]} -> {i[1]}")



# Fourth Problem

dictionary = {}
while True:
    number = input()
    if number.isdigit():
        break
    number = number.split("-")
    name = number[0]
    num = number[1]
    dictionary[name] = num

for i in range(int(number)):
    search = input()
    if search in dictionary:
        print(f"{search} -> {dictionary[search]}")
    else:
        print(f"Contact {search} does not exist.")



# Fifth Problem

dictionary = {}
junk = {}
flag = False
while True and flag == False:
    materials = input().lower().split(" ")
    for i in range(0, len(materials), 2):
        quantity = materials[i]
        material = materials[i + 1]
        if material == "shards" or material == "fragments" or material == "motes":
            if material not in dictionary:
                dictionary[material] = quantity
            elif material in dictionary:
                dictionary[material] = int(dictionary[material]) + int(quantity)
            if int(dictionary[material]) >= 250:
                dictionary[material] = int(dictionary[material]) - 250
                if material == "shards":
                    print(f"Shadowmourne obtained!")
                    flag = True
                elif material == "fragments":
                    print(f"Valanyr obtained!")
                    flag = True
                elif material == "motes":
                    print(f"Dragonwrath obtained!")
                    flag = True
        if flag:
            break
        if material != "shards" and material != "fragments" and material != "motes":
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] = int(junk[material]) + int(quantity)
if "shards" not in dictionary:
    print(f"shards: 0")
elif "shards" in dictionary:
    print(f"shards: {dictionary['shards']}")
if "fragments" not in dictionary:
    print(f"fragments: 0")
elif "fragments" in dictionary:
    print(f"fragments: {dictionary['fragments']}")
if "motes" not in dictionary:
    print(f"motes: 0")
elif "motes" in dictionary:
    print(f"motes: {dictionary['motes']}")
for i in junk:
    print(f"{i}: {junk[i]}")



# Sixth Problem

dictionary = {}
quantities = {}
while True:
    order = input().split(" ")
    if order[0] == "buy":
        break
    drink = order[0]
    price = float(order[1])
    quantity = int(order[2])
    if drink not in dictionary:
        quantities[drink] = quantity
        dictionary[drink] = price * quantities[drink]
    elif drink in dictionary:
        quantities[drink] += quantity
        dictionary[drink] = price * quantities[drink]
for i in dictionary:
    print(f"{i} -> {dictionary[i]:.2f}")



# Seventh Problem

dictionary = {}
n = int(input())
for i in range(n):
    line = input().split(" ")
    command = line[0]
    name = line[1]
    if command == "register":
        plate = line[2]
        if name not in dictionary:
            dictionary[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command == "unregister":
        if name not in dictionary:
            print(f"ERROR: user {name} not found")
        elif name in dictionary:
            print(f"{name} unregistered successfully")
            dictionary.pop(name)
for j in dictionary:
    print(f"{j} => {dictionary[j]}")



# Eight Problem

dictionary = {}
count = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course = command[0]
    name = command[1]
    if course not in dictionary:
        dictionary[course] = name
        count[course] = 1
    elif course in dictionary:
        dictionary[course] += ", " + name
        count[course] += 1
for j in dictionary:
    print(f"{j}: {count[j]}")
    for element in dictionary[j].split(", "):
        print(f"-- {element}")



# Ninth Problem

n = int(input())
dictionary = {}
count = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in dictionary:
        dictionary[name] = grade
        count[name] = 1
    elif name in dictionary:
        dictionary[name] += grade
        count[name] += 1
for name in dictionary:
    if dictionary[name] / count[name] >= 4.50:
        print(f"{name} -> {dictionary[name] / count[name]:.2f}")



# Tenth Problem

dictionary = {}
while True:
    command = input()
    if command == "End":
        break
    info = command.split(" -> ")
    company = info[0]
    id = info[1]
    if company not in dictionary:
        dictionary[company] = id
    if company in dictionary:
        if id not in dictionary[company]:
            dictionary[company] += ", " + id
for j in dictionary:
    print(j)
    for id in dictionary[j].split(", "):
        print(f"-- {id}")



# Eleventh Problem

users_to_sides = {}
sides_to_users = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        side, user = line.split(" | ")

        if side not in sides_to_users:
            sides_to_users[side] = []

        if user not in users_to_sides:
            users_to_sides[user] = side
            sides_to_users[side].append(user)

    elif " -> " in line:
        user, side = line.split(" -> ")

        if user in users_to_sides:
            previous_side = users_to_sides[user]
            sides_to_users[previous_side].remove(user)

        if side not in sides_to_users:
            sides_to_users[side] = []
        sides_to_users[side].append(user)
        users_to_sides[user] = side

        print(f"{user} joins the {side} side!")


for side, members in sides_to_users.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")



# Twelfth Problem

dictionary = {}
count = {}
while True:
    command = input()
    if command == "exam finished":
        break
    info = command.split("-")
    if info[1] != "banned":
        name = info[0]
        course = info[1]
        points = int(info[2])
        if name not in dictionary:
            dictionary[name] = points
        elif name in dictionary:
            if dictionary[name] <= points:
                dictionary[name] = points
        if course not in count:
            count[course] = 1
        elif course in count:
            count[course] += 1
    elif info[1] == "banned":
        name = info[0]
        dictionary.pop(name)

print("Results:")
for j in dictionary:
    print(f"{j} | {dictionary[j]}")
print(f"Submissions:")
for j in count:
    print(f"{j} - {count[j]}")
