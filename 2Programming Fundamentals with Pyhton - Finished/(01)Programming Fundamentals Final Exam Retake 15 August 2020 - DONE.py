# First Problem

code = input()
while True:
    command = input()
    if command == "Decode":
        break
    command = command.split("|")
    if command[0] == "Move":
        num_letters = int(command[1])
        code = code[num_letters:] + code[:num_letters]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        code = code[:index] + value + code[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        code = code.replace(substring, replacement)
print(f"The decrypted message is:", end=" ")
for symbol in code:
    print(symbol, end="")



# Second Problem

import re
input_string = input()
food_pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,4})\1"
food_items = re.findall(food_pattern, input_string)

total_calories = 0
for item in food_items:
    calories = int(item[3])
    total_calories += calories
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for item in food_items:
    item_name = item[1]
    expiration_date = item[2]
    calories = int(item[3])

    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")



# Third Problem

n = int(input())
collection = {}

for _ in range(n):
    piece_data = input().split("|")
    piece = piece_data[0]
    composer = piece_data[1]
    key = piece_data[2]
    collection[piece] = {'composer': composer, 'key': key}

while True:
    command = input().split("|")
    action = command[0]

    if action == "Stop":
        break

    piece = command[1]

    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece not in collection:
            collection[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in collection:
            collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

# Print the collection
for piece, info in collection.items():
    composer = info['composer']
    key = info['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")


