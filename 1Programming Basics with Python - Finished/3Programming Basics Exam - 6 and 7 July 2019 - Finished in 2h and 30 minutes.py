# First Problem

from math import ceil
people = int(input())
goin = float(input())
bed = float(input())
umbrella = float(input())

tax = people * goin

umbrellas = ceil(people / 2)
money = (umbrella * umbrellas)

beds = ceil(people * 0.75)
moneys = (beds * bed)

total = moneys + money + tax
print(f"{total:.2f} lv.")



# Second Problem

budget = float(input())
nights = int(input())
price = float(input())
percentage = int(input())

if nights > 7:
    price = price - (price * 0.05)
elif nights <= 7:
    price = price

money = nights * price
bonus = budget * percentage / 100
total = money + bonus

if total <= budget:
    left = budget - total
    print(f"Ivanovi will be left with {left:.2f} leva after vacation.")
elif total > budget:
    more = total - budget
    print(f"{more:.2f} leva needed.")



# Third Problem (a)

types = str(input())
sugar = str(input())
number = int(input())
total = 0

if types == "Espresso" and sugar == "Without":
    price = 0.90
    total += price
elif types == "Espresso" and sugar == "Normal":
    price = 1.00
    total += price
elif types == "Espresso" and sugar == "Extra":
    price = 1.20
    total += price
elif types == "Cappuccino" and sugar == "Without":
    price = 1.00
    total += price
elif types == "Cappuccino" and sugar == "Normal":
    price = 1.20
    total += price
elif types == "Cappuccino" and sugar == "Extra":
    price = 1.60
    total += price
elif types == "Tea" and sugar == "Without":
    price = 0.50
    total += price
elif types == "Tea" and sugar == "Normal":
    price = 0.60
    total += price
elif types == "Tea" and sugar == "Extra":
    price = 0.70
    total += price

money = total * number
if sugar == "Without":
    money = money * 0.65
if types == "Espresso" and number >= 5:
    money = money * 0.75
if money > 15:
    money = money * 0.80

print(f"You bought {number} cups of {types} for {money:.2f} lv.")



# Third Problem (b)

city = str(input())
types = str(input())
vip = str(input())
staying = int(input())
if staying > 7:
    staying = staying - 1

if city == "Bansko" or city == "Borovets":
    if types == "withEquipment":
        price = 100
        if vip == "yes":
            price = price - (price * 10 / 100)

    elif types == "noEquipment":
        price = 80
        if vip == "yes":
            price = price - (price * 5 / 100)

if city == "Varna" or city == "Burgas":
    if types == "withBreakfast":
        price = 130
        if vip == "yes":
            price = price - (price * 12 / 100)

    elif types == "noBreakfast":
        price = 100
        if vip == "yes":
            price = price - (price * 7 / 100)



if staying < 1:
    print(f"Days must be positive number!")
elif city != "Bansko" and city != "Borovets" and city != "Burgas" and city != "Varna":
    print("Invalid input!")
elif types != "noEquipment" and types != "withEquipment" and types != "noBreakfast" and types != "withBreakfast":
    print("Invalid input!")
else:
    total = price * staying
    print(f"The price is {total:.2f}lv! Have a nice time!")



# Fourth Problem (a)

wanted = float(input())
cocktail = ""
total = 0
cocktails = 0
flag = False
while cocktail != "Party!" or flag:
    if total >= wanted:
        print("Target acquired.")
        print(f"Club income - {total:.2f} leva.")
        flag = True
        break
    cocktail = str(input())
    if cocktail == "Party!":
        continue
    price = len(cocktail)
    number = int(input())
    money = price * number
    if money % 2 != 0:
        money = money * 0.75
    total += money

if cocktail == "Party!":
    more = wanted - total
    print(f"We need {more:.2f} leva more.")
    print(f"Club income - {total:.2f} leva.")



# Fourth Problem (b)

height = int(input())
width = int(input())
percentage = int(input())
liters = input()
painted = 0
area = height * width * 4
empty = area * percentage / 100
need_paint = round(area - empty)

while liters != "Tired!":
    liter = int(liters)
    painted += liter
    if painted > need_paint:
        left = painted - need_paint
        print(f"All walls are painted and you have {left} l paint left!")
        break
    elif painted == need_paint:
        print(f"All walls are painted! Great job, Pesho!")
        break
    liters = input()
    if liters == "Tired!":
        left = need_paint - painted
        print(f"{left} quadratic m left.")
        continue



# Fifth Problem (a)

n = int(input())
hearthstone = 0
fortnite = 0
overwatch = 0
others = 0
for i in range(1, n + 1):
    name = str(input())
    if name == "Hearthstone":
        hearthstone += 1
    elif name == "Fornite":
        fortnite += 1
    elif name == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {hearthstone / n * 100:.2f}%")
print(f"Fornite - {fortnite / n * 100:.2f}%")
print(f"Overwatch - {overwatch / n * 100:.2f}%")
print(f"Others - {others / n * 100:.2f}%")



# Fifth Problem (b)

name = str(input())
matches = int(input())
wins = 0
loses = 0
draws = 0
points = 0
for i in range(1, matches + 1):
    result = str(input())
    if result == "W":
        wins += 1
        points += 3
    elif result == "L":
        loses += 1
    elif result == "D":
        draws += 1
        points += 1

if matches == 0:
    print(f"{name} hasn't played any games during this season.")
elif matches >= 1:
    print(f"{name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {wins / matches * 100:.2f}%")



# Sixth Problem (a)

name = ""
maximum = 0
while name != "Stop":
    points = 0
    name = str(input())
    if name == "Stop":
        continue
    for i in range(0, len(name)):
        letter = ord(name[i])
        number = int(input())
        if letter == number:
            points += 10
        elif letter != number:
            points += 2
    total = points
    if total > maximum:
        maximum = total
        winner = name
    elif total == maximum:
        maximum = total
        winner = name

print(f"The winner is {winner} with {maximum} points!")



# Sixth Problem (b)

word = str(input())
maximum = 0
winner = ""
while word != "End of words":
    multiply = False
    division = False
    total = 0
    for i in range(0, len(word)):
        if i == 0:
            letter = ord(word[i])
            if letter == 65 or letter == 97:
                multiply = True
            elif letter == 69 or letter == 101:
                multiply = True
            elif letter == 73 or letter == 105:
                multiply = True
            elif letter == 79 or letter == 111:
                multiply = True
            elif letter == 85 or letter == 117:
                multiply = True
            elif letter == 89 or letter == 121:
                multiply = True
            else:
                division = True
        letter = ord(word[i])
        if multiply:
            total += letter * len(word)
        elif division:
            total += letter / len(word)

        if total > maximum:
            maximum = total
            winner = word
    word = str(input())

print(f"The most powerful word is {winner} - {round(maximum)}")