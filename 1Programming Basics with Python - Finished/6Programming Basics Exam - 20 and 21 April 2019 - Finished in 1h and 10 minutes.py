# First Problem (a)

food1 = int(input())
food2 = int(input())
food3 = int(input())

money1 = food1 * 3.20
money2 = food2 * 4.35
money3 = food3 * 5.40
bonus = food2 * 12 * 0.15
total = money3 + money2 + money1 + bonus

print(f"{total:.2f}")



# First Problem (b)

price = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
pack = int(input())
money = 0
money += price * flour
money += sugar * (price * 0.75)
money += eggs * (price * 1.10)
money += pack * ((price * 0.75) * 0.20)
print(f"{money:.2f}")



# Second Problem (a)

people = int(input())
price = float(input())
budget = float(input())

if 10 <= people <= 15:
    price = price - (price * 0.15)
elif 15 < people <= 20:
    price = price - (price * 0.20)
elif 20 < people:
    price = price - (price * 0.25)

cake = budget * 0.10
total = cake + (price * people)
if total <= budget:
    print(f"It is party time! {budget - total:.2f} leva left.")
elif total > budget:
    print(f"No party! {total - budget:.2f} leva needed.")



# Second Problem (b)

from math import ceil

people = int(input())
budget = float(input())

food1 = ceil(people / 3)
food2 = people * 2
money1 = food1 * 4.00
money2 = food2 * 0.45

total = money2 + money1
if total <= budget:
    print(f"Lyubo bought {food1} Easter bread and {food2} eggs.")
    print(f"He has {budget - total:.2f} lv. left.")
elif total > budget:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total - budget:.2f} lv. more.")



# Third Problem (a)

country = str(input())
date = str(input())
days = int(input())

if country == "France":
    if date == "21-23":
        price = 30
    elif date == "24-27":
        price = 35
    elif date == "28-31":
        price = 40
elif country == "Italy":
    if date == "21-23":
        price = 28
    elif date == "24-27":
        price = 32
    elif date == "28-31":
        price = 39
elif country == "Germany":
    if date == "21-23":
        price = 32
    elif date == "24-27":
        price = 37
    elif date == "28-31":
        price = 43

money = days * price
print(f"Easter trip to {country} : {money:.2f} leva.")



# Third Problem (b)

types = str(input())
color = str(input())
packs = int(input())

if types == "Large":
    if color == "Red":
        price = 16
    elif color == "Green":
        price = 12
    elif color == "Yellow":
        price = 9
elif types == "Medium":
    if color == "Red":
        price = 13
    elif color == "Green":
        price = 9
    elif color == "Yellow":
        price = 7
elif types == "Small":
    if color == "Red":
        price = 9
    elif color == "Green":
        price = 8
    elif color == "Yellow":
        price = 5

money = packs * price
tax = money * 0.35
total = money - tax

print(f"{total:.2f} leva.")



# Fourth Problem (a)

eggs1 = int(input())
eggs2 = int(input())
flag = True
win = 0
result = str(input())
while result != "End" and flag == True:
    if result == "one":
        eggs2 -= 1
        if eggs2 == 0:
            flag = False
            win = 1
    elif result == "two":
        eggs1 -= 1
        if eggs1 == 0:
            flag = False
            win = 2
    if flag == True:
        result = str(input())

if result == "End":
    print(f"Player one has {eggs1} eggs left.")
    print(f"Player two has {eggs2} eggs left.")

if flag == False and win == 2:
    print(f"Player one is out of eggs. Player two has {eggs2} eggs left.")
elif flag == False and win == 1:
    print(f"Player two is out of eggs. Player one has {eggs1} eggs left.")



# Fourth Problem (b)

eggs = int(input())
decision = ""
sold = 0
flag = False
while decision != "Close" and flag == False:
    left = eggs
    decision = str(input())
    if decision == "Close":
        continue
    egg = int(input())
    if decision == "Fill":
        eggs += egg
    elif decision == "Buy":
        eggs -= egg
        sold += egg
        if eggs < 0:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {left}.")
            flag = True
            continue

if decision == "Close":
    print(f"Store is closed!")
    print(f"{sold} eggs sold.")



# Fifth Problem (a)

colored = int(input())
red = 0
orange = 0
blue = 0
green = 0
for i in range(1, colored + 1):
    color = str(input())
    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1


print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
if red > orange and red > blue and red > green:
    print(f"Max eggs: {red} -> red")
elif blue > red and blue > orange and blue > green:
    print(f"Max eggs: {blue} -> blue")
elif orange > red and orange > blue and orange > green:
    print(f"Max eggs: {orange} -> orange")
elif green > red and green > blue and green > orange:
    print(f"Max eggs: {green} -> green")



# Fifth Problem (b)

from math import ceil
number = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0
for i in range(1, number + 1):
    sugar = int(input())
    flour = int(input())
    total_sugar += sugar
    total_flour += flour
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

print(f"Sugar: {ceil(total_sugar / 950)}")
print(f"Flour: {ceil(total_flour / 750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")



# Sixth Problem (a)

number = int(input())
winner = ""
total = 0
max = 0
for i in range(1, number + 1):
    total = 0
    name = str(input())
    grade = ""
    while grade != "Stop":
        grade = input()
        if grade == "Stop":
            continue
        real = int(grade)
        total += real
    print(f"{name} has {total} points.")
    if total > max:
        print(f"{name} is the new number 1!")
        max = total
        winner = name

print(f"{winner} won competition with {max} points!")



# Sixth Problem (b)

customers = int(input())
total = 0
count = 0
finish = 0
for i in range(1, customers + 1):
    total = 0
    count = 0
    bought = ""
    while bought != "Finish":
        bought = str(input())
        if bought == "Finish":
            continue
        if bought == "basket":
            price = 1.50
            total += price
            count += 1
        elif bought == "wreath":
            price = 3.80
            total += price
            count += 1
        elif bought == "chocolate bunny":
            price = 7
            total += price
            count += 1

    if count % 2 == 0:
        total = total - (total * 0.20)
    finish += total
    print(f"You purchased {count} items for {total:.2f} leva.")

print(f"Average bill per client is: {finish / customers:.2f} leva.")