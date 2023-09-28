# First Problem

from math import floor
string = str(input())
new = string.split(" ")
result = []
real = 0
for i in range(0, len(new)):
    if float(new[i]) > 0:
        real = -float(new[i])
    elif float(new[i]) < 0:
        real = abs(float(new[i]))
    else:
        real = int(new[i])
    result.append(floor(real))
print(result)



# Second Problem

factor = int(input())
count = int(input())
result = []
number = factor
for i in range(1, count + 1):
    result.append(number)
    number += factor
print(result)



# Third Problem

string = str(input())
check = string.split(" ")
team_a = 11
team_b = 11
count_a = 0
count_b = 0
stop = False
for i in range(1, 12):
    for j in range(0, len(check)):
        if check[j] == f"A-{i}":
            count_a += 1
            if count_a == 1:
                team_a -= 1
        if check[j] == f"B-{i}":
            count_b += 1
            if count_b == 1:
                team_b -= 1
        if team_a < 7 or team_b < 7:
            print(f"Team A - {team_a}; Team B - {team_b}")
            print("Game was terminated")
            stop = True
            break
        if stop:
            break
    if stop:
        break
    count_a = 0
    count_b = 0

if not stop:
    print(f"Team A - {team_a}; Team B - {team_b}")



# Fourth Problem

string = str(input())
list = string.split(", ")
result = []
beggars = int(input())
beggar = 0
for i in range(1, beggars + 1):
    for j in range(i-1, len(list), beggars):
        beggar += int(list[j])
    result.append(beggar)
    beggar = 0
print(result)



# Fifth Problem

string = str(input())
list = string.split(" ")
result = []
result1 = []
result2 = []
shuffles = int(input())
for i in range(1, shuffles + 1):
    for j in range(0, len(list) // 2):
        result.append(list[j])
        result.append(list[j + len(list) // 2])
    list = result
    result = []

print(list)



# Sixth Problem

sequence = str(input())
number = int(input())
smallest = 1000000
start = sequence.split(" ")
result = ""
end = []
position = 0
for i in range(1, number + 1):
    for j in range(0, len(start)):
        if int(start[j]) < smallest:
            smallest = int(start[j])
            position = j
    start.remove(start[position])
    smallest = 1000000
for h in range(0, len(start)):
    end.append(int(start[h]))

print(*end, sep=", ")



# Seventh Problem

gift = str(input())
gifts = gift.split(" ")
command = ""
count = 0
while command != "No Money":
    command = str(input())
    if command == "No Money":
        continue
    check = command.split(" ")
    if check[0] == "OutOfStock":
        for i in range(0, len(gifts)):
            if check[1] == gifts[i]:
                count += 1
                gifts[i] = "None"
    elif check[0] == "Required":
        gift = check[1]
        index = int(check[2])
        if 0 <= index < len(gifts):
            if gifts[index] == "None":
                count -= 1
            gifts[index] = gift
    elif check[0] == "JustInCase":
        gift = check[1]
        if gifts[len(gifts) - 1] == "None":
            count -= 1
        gifts[len(gifts) - 1] = gift

for i in range(1, count + 1):
    gifts.remove("None")
print(*gifts, sep=" ")



# Eighth Problem

fire = str(input())
water = int(input())
fires = fire.split("#")
total = 0
cells = []

for i in range(0, len(fires)):
    check = fires[i].split("=")
    if check[0] == "High " and 81 <= int(check[1]) <= 125:
        water -= int(check[1])
        if water >= 0:
            total += int(check[1])
            cells.append(int(check[1]))
        elif water < 0:
            water += int(check[1])
    elif check[0] == "Medium " and 51 <= int(check[1]) <= 80:
        water -= int(check[1])
        if water >= 0:
            total += int(check[1])
            cells.append(int(check[1]))
        elif water < 0:
            water += int(check[1])
    elif check[0] == "Low " and 1 <= int(check[1]) <= 50:
        water -= int(check[1])
        if water >= 0:
            total += int(check[1])
            cells.append(int(check[1]))
        elif water < 0:
            water += int(check[1])

print("Cells:")
for i in range(0, len(cells)):
    print(f" - {cells[i]}")
print(f"Effort: {total / 4:.2f}")
print(f"Total Fire: {total}")



# Ninth Problem

item = str(input())
items = item.split("|")
budget = float(input())
spent = budget
profit = 0
prices = []
for i in range(0, len(items)):
    check = items[i].split("->")
    if check[0] == "Clothes" and float(check[1]) <= 50.00:
        spent -= float(check[1])
        if spent >= 0:
            price = float(check[1]) * 1.40
            prices.append(price)
            profit += float(check[1]) * 1.40 - float(check[1])
        elif spent < 0:
            spent += float(check[1])
    if check[0] == "Shoes" and float(check[1]) <= 35.00:
        spent -= float(check[1])
        if spent >= 0:
            price = float(check[1]) * 1.40
            prices.append(price)
            profit += float(check[1]) * 1.40 - float(check[1])
        elif spent < 0:
            spent += float(check[1])
    if check[0] == "Accessories" and float(check[1]) <= 20.50:
        spent -= float(check[1])
        if spent >= 0:
            price = float(check[1]) * 1.40
            prices.append(price)
            profit += float(check[1]) * 1.40 - float(check[1])
        elif spent < 0:
            spent += float(check[1])

for i in range(0, len(prices)):
    print(f"{prices[i]:.2f} ", end="")
print()
print(f"Profit: {profit:.2f}")
budget = budget + profit
if budget >= 150:
    print("Hello, France!")
elif budget < 150:
    print("Not enough money.")



# Tenth Problem

event = str(input())
events = event.split("|")
energy = 100
coins = 100
flag = False
for i in range(0, len(events)):
    check = events[i].split("-")
    if check[0] == "rest":
        current = energy
        energy += int(check[1])
        if energy > 100:
            energy = 100
        gained = energy - current
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")
    elif check[0] == "order":
        energy -= 30
        if energy < 0:
            energy += 80
            print("You had to rest!")
            continue
        elif energy >= 0:
            coins += int(check[1])
            earned = int(check[1])
            print(f"You earned {earned} coins.")
    else:
        coins -= int(check[1])
        if coins < 0:
            print(f"Closed! Cannot afford {check[0]}.")
            flag = True
            break
        elif coins >= 0:
            print(f"You bought {check[0]}.")
    if flag:
        break

if not flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")