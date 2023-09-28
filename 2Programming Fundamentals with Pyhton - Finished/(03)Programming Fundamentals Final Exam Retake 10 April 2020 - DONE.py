# First Problem

string = input()

while True:
    command = input()
    if command == "Reveal":
        break
    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        string = string[:index] + " " + string[index:]
        print(string)
    elif action == "Reverse":
        substring = command[1]
        if substring in string:
            reversed_substring = substring[::-1]  # Reverse the substring
            string = string.replace(substring, "", 1)  # Remove the first occurrence
            string += reversed_substring  # Add the reversed substring at the end
            print(string)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        string = string.replace(substring, replacement)
        print(string)
print(f"You have a new text message: {string}")



# Second Problem

import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
word_pairs = re.findall(pattern, text)

mirror_words = [pair for pair in word_pairs if pair[1] == pair[2][::-1]]

if not word_pairs:
    print("No word pairs found!")
else:
    print(f"{len(word_pairs)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join([f"{pair[1]} <=> {pair[2]}" for pair in mirror_words]))



# Third Problem

cars = int(input())
cars_specifications = {}
for i in range(cars):
    car = input().split("|")
    mileage = int(car[1])
    fuel = int(car[2])
    car = car[0]
    cars_specifications[car] = {"mileage": mileage, "fuel": fuel}
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars_specifications[car]["fuel"] - fuel < 0:
            print(f"Not enough fuel to make that ride")
        elif cars_specifications[car]["fuel"] - fuel >= 0:
            cars_specifications[car]["mileage"] = cars_specifications[car]["mileage"] + distance
            cars_specifications[car]["fuel"] = cars_specifications[car]["fuel"] - fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_specifications[car]["mileage"] >= 100000:
            del cars_specifications[car]
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars_specifications[car]["fuel"] + fuel > 75:
            fuel = 75 - cars_specifications[car]["fuel"]
            cars_specifications[car]["fuel"] = 75
        else:
            cars_specifications[car]["fuel"] = cars_specifications[car]["fuel"] + fuel
        print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        car = command[1]
        kilometers = int(command[2])
        cars_specifications[car]["mileage"] = cars_specifications[car]["mileage"] - kilometers
        if cars_specifications[car]["mileage"] < 10000:
            cars_specifications[car]["mileage"] = 10000
        elif cars_specifications[car]["mileage"] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, info in cars_specifications.items():
    mileage = info["mileage"]
    fuel = info["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

