# First Problem

stops = input()
while True:
    command = input()
    if command == "Travel":
        break
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        stop = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + stop + stops[index:]

    elif action == "Remove Stop":
        start = int(command[1])
        end = int(command[2])
        if 0 <= start < len(stops) and 0 <= end < len(stops):
            stops = stops[:start] + stops[end + 1:]

    elif action == "Switch":
        old = command[1]
        new = command[2]
        stops = stops.replace(old, new)
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")



# Second Problem

import re

locations = input()

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"
valid_destinations = re.findall(pattern, locations)
travel_points = sum(len(dest) for _, dest in valid_destinations)

destinations = [dest for _, dest in valid_destinations]

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")



# Third Problem

number = int(input())
dictionary1 = {}
dictionary2 = {}
dictionary3 = {}
dictionary4 = {}

for i in range(number):
    string = input().split("<->")
    plant = string[0]
    rarity = int(string[1])
    dictionary1[plant] = rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(": ")
    action = command[0]

    if action == "Rate":
        plant_rating = command[1].split(" - ")
        plant = plant_rating[0]
        rating = int(plant_rating[1])

        if plant in dictionary1:
            if plant not in dictionary2:
                dictionary2[plant] = 0
                dictionary3[plant] = 0
            dictionary2[plant] += rating
            dictionary3[plant] += 1
        else:
            print("error")
    elif action == "Update":
        plant_rarity = command[1].split(" - ")
        plant = plant_rarity[0]
        rarity = int(plant_rarity[1])

        if plant in dictionary1:
            dictionary1[plant] = rarity
        else:
            print("error")
    elif action == "Reset":
        plant = command[1]
        if plant in dictionary1:
            dictionary2[plant] = 0
            dictionary3[plant] = 0
        else:
            print("error")

print("Plants for the exhibition:")
for key in dictionary1:
    if key in dictionary2 and dictionary3[key] != 0:
        average_rating = dictionary2[key] / dictionary3[key]
    else:
        average_rating = 0.00
    print(f"- {key}; Rarity: {dictionary1[key]}; Rating: {average_rating:.2f}")