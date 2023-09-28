# First Problem

food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
for i in range(1, 31):
    food -= 300
    if i % 2 == 0:
        hay -= food * 0.05
    if i % 3 == 0:
        cover -= weight / 3
    if food < 0 or hay < 0 or cover < 0:
        break
if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
else:
    print(f"Merry must go to the pet store!")



# Second Problem

groceries = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split(" ")
    name = command[0]
    if name == "Urgent":
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif name == "Unnecessary":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif name == "Correct":
        old = command[1]
        new = command[2]
        if old in groceries:
            for i in range(0, len(groceries)):
                if groceries[i] == old:
                    groceries[i] = new
    elif name == "Rearrange":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
for i in range(0, len(groceries)):
    if i != len(groceries) - 1:
        print(groceries[i], end=", ")
    else:
        print(groceries[i])



# Third Problem

numbers = input().split("@")
check = 0
while True:
    command = input()
    if command == "Love!":
        break
    jump, distance = command.split(" ")
    check += int(distance)
    if 0 <= check < len(numbers):
        if numbers[check] != 0:
            numbers[check] = int(numbers[check]) - 2
        else:
            print(f"Place {check} already had Valentine's day.")
            continue
        if numbers[check] == 0:
            print(f"Place {check} has Valentine's day.")
    else:
        check = 0
        if numbers[check] != 0:
            numbers[check] = int(numbers[check]) - 2
        else:
            print(f"Place {check} already had Valentine's day.")
            continue
        if numbers[check] == 0:
            print(f"Place {check} has Valentine's day.")
failed = 0
print(f"Cupid's last position was {check}.")
if numbers == [0] * len(numbers):
    print(f"Mission was successful.")
else:
    for i in range(0, len(numbers)):
        if numbers[i] != 0:
            failed += 1
    print(f"Cupid has failed {failed} places.")
