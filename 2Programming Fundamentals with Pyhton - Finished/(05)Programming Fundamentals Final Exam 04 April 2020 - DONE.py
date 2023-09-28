# First Problem

code = input()
while True:
    command = input()
    if command == "Generate":
        break
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in code:
            print(f"{code} contains {substring}")
        else:
            print(f"Substring not found!")
    elif action == "Flip":
        case = command[1]
        start = int(command[2])
        end = int(command[3])
        if case == "Upper":
            code = code[:start] + code[start:end].upper() + code[end:]
        elif case == "Lower":
            code = code[:start] + code[start:end].lower() + code[end:]
        print(code)
    elif action == "Slice":
        start = int(command[1])
        end = int(command[2])
        code = code[:start] + code[end:]
        print(code)
print(f"Your activation key is: {code}")



# Second Problem

import re

text = input()
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
matches = re.findall(pattern, text)

threshold = 1
for char in text:
    if char.isdigit():
        threshold *= int(char)

cool_emojis = []
for emoji in matches:
    coolnes = 0
    for char in emoji[1]:
        coolnes += ord(char)

    if coolnes > threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(''.join(emoji))



# Third Problem

cities = {}
while True:
    command = input()
    if command == "Sail":
        break
    command = command.split("||")
    population = int(command[1])
    gold = int(command[2])
    city = command[0]
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    elif city in cities:
        cities[city]["population"] = cities[city]["population"] + population
        cities[city]["gold"] = cities[city]["gold"] + gold
while True:
    command = input()
    if command == "End":
        break
    command = command.split("=>")
    action = command[0]
    if action == "Plunder":
        city = command[1]
        people = int(command[2])
        gold = int(command[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[city]["population"] = cities[city]["population"] - people
        cities[city]["gold"] = cities[city]["gold"] - gold
        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif action == "Prosper":
        city = command[1]
        gold = int(command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        elif gold > 0:
            cities[city]["gold"] = cities[city]["gold"] + gold
            total_gold = cities[city]["gold"]
            print(f"{gold} gold added to the city treasury. {city} now has {total_gold} gold.")
if cities != {}:
    print(f"Ahoy, Captain! There are {len(cities.items())} wealthy settlements to go to:")
    for city, wealth in cities.items():
        people = wealth["population"]
        gold = wealth["gold"]
        print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

