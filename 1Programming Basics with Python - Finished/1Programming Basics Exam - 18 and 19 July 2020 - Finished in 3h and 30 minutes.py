# First Problem
company = str(input())
adult_tickets = int(input())
kid_tickets = int(input())
price_of_ticket_for_adult = float(input())
tax_service = float(input())

price_for_kid_ticket = price_of_ticket_for_adult - price_of_ticket_for_adult * 0.7
money_per_adult = price_of_ticket_for_adult + tax_service
money_per_kid = price_for_kid_ticket + tax_service

total = money_per_kid * kid_tickets + money_per_adult * adult_tickets
final_profit = total * 0.2

print(f"The profit of your agency from {company} tickets is {final_profit:.2f} lv.")

# Second Problem
price = float(input())
weight = float(input())
days = int(input())
number_of_sacks = int(input())

if weight < 10:
    money = price * 0.2
elif 10 <= weight <= 20:
    money = price * 0.5
else:
    money = price

if days > 30:
    money = money + money * 0.10
elif 30 >= days >= 7:
    money = money + money * 0.15
else:
    money = money + money * 0.40

total = money * number_of_sacks
print(f"The total price of bags is: {total:.2f} lv. ")

# Third Problem
number = int(input())
types = str(input())
delivery = str(input())

if number < 10 or number > 1000:
    print("Invalid order")
else:
    if types == "90X130":
        price = 110
        if 30 <= number <= 60:
            money = number * price
            money = money - money * 0.05
        elif number > 60:
            money = number * price
            money = money - money * 0.08
        else:
            money = number * price
    elif types == "100X150":
        price = 140
        if 40 <= number <= 80:
            money = number * price
            money = money - money * 0.06
        elif number > 80:
            money = number * price
            money = money - money * 0.10
        else:
            money = number * price
    elif types == "130X180":
        price = 190
        if 20 <= number <= 50:
            money = number * price
            money = money - money * 0.07
        elif number > 50:
            money = number * price
            money = money - money * 0.12
        else:
            money = number * price
    elif types == "200X300":
        price = 250
        if 25 <= number <= 50:
            money = number * price
            money = money - money * 0.09
        elif number > 60:
            money = number * price
            money = money - money * 0.14
        else:
            money = number * price

    if delivery == "With delivery":
        money = money + 60
    elif delivery == "Without delivery":
        money = money


    if number > 99:
        money = money - money * 0.04

    print(f"{money:.2f} BGN")

# Fourth Problem
balls = int(input())
points = 0
count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_other = 0
count_black = 0

for i in range(1, balls + 1):
    color = str(input())
    if color == "red":
        points += 5
        count_red += 1
    elif color == "orange":
        points += 10
        count_orange += 1
    elif color == "yellow":
        points += 15
        count_yellow += 1
    elif color == "white":
        points += 20
        count_white += 1
    elif color == "black":
        points = points // 2
        count_black += 1
    else:
        points = points
        count_other += 1

print(f"Total points: {points}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_other}")
print(f"Divides from black balls: {count_black}")

# Fifth Problem
name = str(input())
goals = int(input())
best_player = ""
best = 0
condition = True
while condition:
    if goals > best:
        best_player = name
        best = goals
    if best >= 10:
        break

    name = str(input())
    if name == "END":
        condition = False
        continue
    goals = int(input())

print(f"{best_player} is the best player!")
if best >= 3:
    print(f"He has scored {best} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best} goals.")

# Sixth Problem
num1 = int(input())
num2 = int(input())
digit1 = num1 // 1000
digit2 = num2 // 1000
digit3 = (num1 % 1000) // 100
digit4 = (num2 % 1000) // 100
digit5 = ((num1 % 1000) % 100) // 10
digit6 = ((num2 % 1000) % 100) // 10
digit7 = ((num1 % 1000) % 100) % 10
digit8 = ((num2 % 1000) % 100) % 10
for i1 in range(digit1, digit2 + 1):
    if i1 % 2 == 0:
        continue
    else:
        position1 = i1
    for i2 in range(digit3, digit4 + 1):
        if i2 % 2 == 0:
            continue
        else:
            position2 = i2
        for i3 in range(digit5, digit6 + 1):
            if i3 % 2 == 0:
                continue
            else:
                position3 = i3
            for i4 in range(digit7, digit8 + 1):
                if i4 % 2 == 0:
                    continue
                else:
                    position4 = i4
                    print(f"{position1}{position2}{position3}{position4}" + " ", end="")